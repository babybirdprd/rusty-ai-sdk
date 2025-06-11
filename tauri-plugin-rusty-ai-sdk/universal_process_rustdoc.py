import json
import os
import sys
import argparse
from collections import defaultdict

def clean_doc_string(doc_string: str | None) -> str:
    """Cleans the rustdoc string, removing markdown headers and code fences."""
    if not doc_string:
        return ""
    lines = doc_string.split('\n')
    cleaned_lines = [
        line.strip() for line in lines
        if not line.strip().startswith(('# ', '## ', '### ')) and
           not line.strip().startswith('```') and
           not line.strip().startswith('#[')
    ]
    return ' '.join(cleaned_lines).strip()

def resolve_type(type_info: dict, all_items: dict) -> str:
    """Recursively resolves a type object from the rustdoc JSON into a readable string."""
    if not isinstance(type_info, dict):
        return '?'

    kind = type_info.get("kind")
    if kind == "resolved_path":
        return type_info.get("name", '?')
    elif kind == "generic":
        name = type_info.get("name", "")
        args = ", ".join(
            resolve_type(arg.get("type", {}), all_items)
            for arg in type_info.get("args", {}).get("angle_bracketed", {}).get("args", [])
        )
        return f"{name}<{args}>"
    elif kind == "primitive":
        return type_info.get("name", '?')
    elif kind == "borrow":
        prefix = "&'static " if type_info.get("lifetime") == "'static'" else "&"
        mutability = "mut " if type_info.get("mutable", False) else ""
        inner_type = resolve_type(type_info.get("inner", {}), all_items)
        return f"{prefix}{mutability}{inner_type}"
    elif kind == "tuple":
        if not type_info.get("inner"):
            return "()"
        inner_types = ", ".join(resolve_type(t, all_items) for t in type_info.get("inner", []))
        return f"({inner_types})"
    return '?'


def format_item(item_id: str, all_items: dict, target_crate_id: int) -> str | None:
    """
    Formats a single rustdoc item (struct, enum, or function) into a detailed
    Markdown string, including its members.
    """
    item = all_items.get(item_id)
    if not item:
        return None

    # --- Filtering Logic using the dynamically found crate_id ---
    if item.get("visibility") != "public" or item.get("crate_id") != target_crate_id:
        return None

    name = item.get("name")
    if not name:
        return None

    docs = clean_doc_string(item.get("docs"))
    inner_item = item.get("inner", {})
    kind = next(iter(inner_item.keys()), None)

    if not kind:
        return None

    output = []

    # --- Struct Formatting ---
    if kind == "struct":
        output.append(f"## Struct: `{name}`\n")
        if docs:
            output.append(f"{docs}\n")
        
        fields = item.get("inner", {}).get("struct", {}).get("plain", {}).get("fields", [])
        if fields:
            output.append("### Fields\n")
            for field_id in fields:
                field_item = all_items.get(str(field_id))
                if not field_item: continue
                field_name = field_item.get("name", "?")
                field_docs = clean_doc_string(field_item.get("docs"))
                field_type_info = field_item.get("inner", {}).get("struct_field", {}).get("type", {})
                field_type_str = resolve_type(field_type_info, all_items)
                output.append(f"- **`{field_name}`**: `{field_type_str}` - {field_docs}")
    
    # --- Enum Formatting ---
    elif kind == "enum":
        output.append(f"## Enum: `{name}`\n")
        if docs:
            output.append(f"{docs}\n")

        variants = item.get("inner", {}).get("enum", {}).get("variants", [])
        if variants:
            output.append("### Variants\n")
            for variant_id in variants:
                variant_item = all_items.get(str(variant_id))
                if not variant_item: continue
                variant_name = variant_item.get("name", "?")
                variant_docs = clean_doc_string(variant_item.get("docs"))
                output.append(f"- **`{variant_name}`** - {variant_docs}")

    # --- Function Formatting ---
    elif kind == "function":
        decl = item.get("inner", {}).get("function", {}).get("decl", {})
        inputs = decl.get("inputs", [])
        output_type = decl.get("output")

        param_strs = []
        for param_name, type_info in inputs:
            type_str = resolve_type(type_info, all_items)
            param_strs.append(f"{param_name}: {type_str}")
        
        params = ", ".join(param_strs)
        return_str = ""
        if output_type:
            return_str = f" -> {resolve_type(output_type, all_items)}"

        signature = f"fn {name}({params}){return_str}"

        output.append(f"## Function: `{name}`\n")
        output.append(f"**Signature:** `{signature}`\n")
        if docs:
            output.append(f"**Description:** {docs}\n")

    else:
        return None

    if not output or len(output) <= 1:
        return None
        
    return "\n".join(output) + "\n---\n"


def main():
    """Main function to parse, filter, and format rustdoc JSON for a specific crate."""
    parser = argparse.ArgumentParser(description="Convert rustdoc JSON into a Markdown format suitable for LLMs.")
    parser.add_argument("crate_name", help="The name of the crate to process (e.g., 'async-openai').")
    args = parser.parse_args()
    
    crate_name_hyphen = args.crate_name
    crate_name_underscore = crate_name_hyphen.replace('-', '_')

    # Use the crate name to construct file paths
    json_path = os.path.join("target", "doc", f"{crate_name_underscore}.json")
    output_path = f"llm_context_{crate_name_underscore}.md"
    
    if not os.path.exists(json_path):
        print(f"Error: JSON file not found at {json_path}")
        print(f"Please run: cargo +nightly rustdoc --package {crate_name_hyphen} -- -Z unstable-options --output-format json")
        sys.exit(1)

    print(f"Loading JSON from {json_path}...")
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        sys.exit(1)

    # --- Dynamically find the target crate's ID ---
    target_crate_id = None
    for crate_id, crate_data in data.get("crates", {}).items():
        if crate_data.get("name") in (crate_name_hyphen, crate_name_underscore):
            target_crate_id = int(crate_id)
            print(f"Found crate '{crate_data.get('name')}' with ID: {target_crate_id}")
            break

    if target_crate_id is None:
        print(f"Warning: Could not find crate '{args.crate_name}' in the 'crates' section.")
        print("Falling back to assuming crate_id is 0. This may yield incorrect results.")
        target_crate_id = 0

    all_items = data.get("index", {})
    if not all_items:
        print("Error: The 'index' section of the JSON is empty.")
        sys.exit(1)
        
    output_content = []

    print("Processing and filtering items...")
    for item_id, item_data in all_items.items():
        # Pass the found crate_id to the formatting function
        formatted_str = format_item(item_id, all_items, target_crate_id)
        if formatted_str:
            output_content.append(formatted_str)
            
    final_output = f"# API Reference for `{crate_name_underscore}`\n\n" + "\n".join(sorted(output_content))

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_output)

    print(f"✅ Successfully created distilled documentation at: {output_path}")
    print(f"Original item count: {len(all_items)}. Filtered item count: {len(output_content)}.")

if __name__ == "__main__":
    main()
