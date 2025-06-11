# API Reference for `async-openai`

## Enum: `AllowedTools`

Allowed tools configuration for MCP.

### Variants

- **`List`** - A flat list of allowed tool names.
- **`Filter`** - A filter object specifying allowed tools.
---

## Enum: `Annotation`

### Variants

- **`FileCitation`** - A citation to a file.
- **`UrlCitation`** - A citation for a web resource used to generate a model response.
- **`FilePath`** - A path to a file.
---

## Enum: `AssistantStreamEvent`

Represents an event emitted when streaming a Run.  Each event in a server-sent events stream has an `event` and `data` property:  event: thread.created data: {"id": "thread_123", "object": "thread", ...}  We emit events whenever a new object is created, transitions to a new state, or is being streamed in parts (deltas). For example, we emit `thread.run.created` when a new run is created, `thread.run.completed` when a run completes, and so on. When an Assistant chooses to create a message during a run, we emit a `thread.message.created event`, a `thread.message.in_progress` event, many `thread.message.delta` events, and finally a `thread.message.completed` event.  We may add additional events over time, so we recommend handling unknown events gracefully in your code. See the [Assistants API quickstart](https://platform.openai.com/docs/assistants/overview) to learn how to integrate the Assistants API with streaming.

### Variants

- **`TreadCreated`** - Occurs when a new [thread](https://platform.openai.com/docs/api-reference/threads/object) is created.
- **`ThreadRunCreated`** - Occurs when a new [run](https://platform.openai.com/docs/api-reference/runs/object) is created.
- **`ThreadRunQueued`** - Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `queued` status.
- **`ThreadRunInProgress`** - Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to an `in_progress` status.
- **`ThreadRunRequiresAction`** - Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `requires_action` status.
- **`ThreadRunCompleted`** - Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is completed.
- **`ThreadRunIncomplete`** - Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) ends with status `incomplete`.
- **`ThreadRunFailed`** - Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) fails.
- **`ThreadRunCancelling`** - Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) moves to a `cancelling` status.
- **`ThreadRunCancelled`** - Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) is cancelled.
- **`ThreadRunExpired`** - Occurs when a [run](https://platform.openai.com/docs/api-reference/runs/object) expires.
- **`ThreadRunStepCreated`** - Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is created.
- **`ThreadRunStepInProgress`** - Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) moves to an `in_progress` state.
- **`ThreadRunStepDelta`** - Occurs when parts of a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) are being streamed.
- **`ThreadRunStepCompleted`** - Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is completed.
- **`ThreadRunStepFailed`** - Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) fails.
- **`ThreadRunStepCancelled`** - Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) is cancelled.
- **`ThreadRunStepExpired`** - Occurs when a [run step](https://platform.openai.com/docs/api-reference/run-steps/step-object) expires.
- **`ThreadMessageCreated`** - Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is created.
- **`ThreadMessageInProgress`** - Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) moves to an `in_progress` state.
- **`ThreadMessageDelta`** - Occurs when parts of a [Message](https://platform.openai.com/docs/api-reference/messages/object) are being streamed.
- **`ThreadMessageCompleted`** - Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) is completed.
- **`ThreadMessageIncomplete`** - Occurs when a [message](https://platform.openai.com/docs/api-reference/messages/object) ends before it is completed.
- **`ErrorEvent`** - Occurs when an [error](https://platform.openai.com/docs/guides/error-codes/api-errors) occurs. This can happen due to an internal server error or a timeout.
- **`Done`** - Occurs when a stream ends.
---

## Enum: `AssistantToolType`

### Variants

- **`Function`** - 
- **`CodeInterpreter`** - 
- **`FileSearch`** - 
---

## Enum: `AssistantTools`

### Variants

- **`CodeInterpreter`** - 
- **`FileSearch`** - 
- **`Function`** - 
---

## Enum: `AssistantVectorStoreChunkingStrategy`

### Variants

- **`Auto`** - The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.
- **`Static`** - 
---

## Enum: `AssistantsApiResponseFormatOption`

Specifies the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models/gpt-4o), [GPT-4 Turbo](https://platform.openai.com/docs/models/gpt-4-turbo-and-gpt-4), and all GPT-3.5 Turbo models since `gpt-3.5-turbo-1106`.  Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which guarantees the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).  Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.  **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

### Variants

- **`Auto`** - 
- **`Format`** - 
---

## Enum: `AssistantsApiToolChoiceOption`

Controls which (if any) tool is called by the model. `none` means the model will not call any tools and instead generates a message. `auto` is the default value and means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools before responding to the user. Specifying a particular tool like `{"type": "file_search"}` or `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.

### Variants

- **`None`** - 
- **`Auto`** - 
- **`Required`** - 
- **`Named`** - 
---

## Enum: `AttributeValue`

The value to compare against the attribute key; supports string, number, or boolean types.

### Variants

- **`String`** - 
- **`Number`** - 
- **`Boolean`** - 
---

## Enum: `AudioResponseFormat`

### Variants

- **`Json`** - 
- **`Text`** - 
- **`Srt`** - 
- **`VerboseJson`** - 
- **`Vtt`** - 
---

## Enum: `AuditLogActorApiKeyType`

### Variants

- **`User`** - 
- **`ServiceAccount`** - 
---

## Enum: `AuditLogEventType`

The event type.

### Variants

- **`ApiKeyCreated`** - 
- **`ApiKeyUpdated`** - 
- **`ApiKeyDeleted`** - 
- **`InviteSent`** - 
- **`InviteAccepted`** - 
- **`InviteDeleted`** - 
- **`LoginSucceeded`** - 
- **`LoginFailed`** - 
- **`LogoutSucceeded`** - 
- **`LogoutFailed`** - 
- **`OrganizationUpdated`** - 
- **`ProjectCreated`** - 
- **`ProjectUpdated`** - 
- **`ProjectArchived`** - 
- **`ServiceAccountCreated`** - 
- **`ServiceAccountUpdated`** - 
- **`ServiceAccountDeleted`** - 
- **`UserAdded`** - 
- **`UserUpdated`** - 
- **`UserDeleted`** - 
---

## Enum: `BatchCompletionWindow`

### Variants

- **`W24H`** - 
---

## Enum: `BatchEndpoint`

### Variants

- **`V1ChatCompletions`** - 
- **`V1Embeddings`** - 
- **`V1Completions`** - 
---

## Enum: `BatchRequestInputMethod`

### Variants

- **`POST`** - 
---

## Enum: `BatchSize`

### Variants

- **`BatchSize`** - 
- **`Auto`** - 
---

## Enum: `BatchStatus`

### Variants

- **`Validating`** - 
- **`Failed`** - 
- **`InProgress`** - 
- **`Finalizing`** - 
- **`Completed`** - 
- **`Expired`** - 
- **`Cancelling`** - 
- **`Cancelled`** - 
---

## Enum: `Beta`

### Variants

- **`Beta`** - 
- **`Auto`** - 
---

## Enum: `ButtonPress`

### Variants

- **`Left`** - 
- **`Right`** - 
- **`Wheel`** - 
- **`Back`** - 
- **`Forward`** - 
---

## Enum: `ChatCompletionAudioFormat`

### Variants

- **`Wav`** - 
- **`Mp3`** - 
- **`Flac`** - 
- **`Opus`** - 
- **`Pcm16`** - 
---

## Enum: `ChatCompletionAudioVoice`

### Variants

- **`Alloy`** - 
- **`Ash`** - 
- **`Ballad`** - 
- **`Coral`** - 
- **`Echo`** - 
- **`Sage`** - 
- **`Shimmer`** - 
- **`Verse`** - 
---

## Enum: `ChatCompletionFunctionCall`

### Variants

- **`None`** - The model does not call a function, and responds to the end-user.
- **`Auto`** - The model can pick between an end-user or calling a function.
- **`Function`** - Forces the model to call the specified function.
---

## Enum: `ChatCompletionModalities`

Output types that you would like the model to generate for this request.  Most models are capable of generating text, which is the default: `["text"]`  The `gpt-4o-audio-preview` model can also be used to [generate audio](https://platform.openai.com/docs/guides/audio). To request that this model generate both text and audio responses, you can use: `["text", "audio"]`

### Variants

- **`Text`** - 
- **`Audio`** - 
---

## Enum: `ChatCompletionRequestAssistantMessageContentPart`

### Variants

- **`Text`** - 
- **`Refusal`** - 
---

## Enum: `ChatCompletionRequestAssistantMessageContent`

### Variants

- **`Text`** - The text contents of the message.
- **`Array`** - An array of content parts with a defined type. Can be one or more of type `text`, or exactly one of type `refusal`.
---

## Enum: `ChatCompletionRequestDeveloperMessageContent`

### Variants

- **`Text`** - 
- **`Array`** - 
---

## Enum: `ChatCompletionRequestMessageContentPartRefusalBuilderError`

Error type for ChatCompletionRequestMessageContentPartRefusalBuilder

### Variants

- **`UninitializedField`** - Uninitialized field
- **`ValidationError`** - Custom validation error
---

## Enum: `ChatCompletionRequestMessage`

### Variants

- **`Developer`** - 
- **`System`** - 
- **`User`** - 
- **`Assistant`** - 
- **`Tool`** - 
- **`Function`** - 
---

## Enum: `ChatCompletionRequestSystemMessageContentPart`

### Variants

- **`Text`** - 
---

## Enum: `ChatCompletionRequestSystemMessageContent`

### Variants

- **`Text`** - The text contents of the system message.
- **`Array`** - An array of content parts with a defined type. For system messages, only type `text` is supported.
---

## Enum: `ChatCompletionRequestToolMessageContentPart`

### Variants

- **`Text`** - 
---

## Enum: `ChatCompletionRequestToolMessageContent`

### Variants

- **`Text`** - The text contents of the tool message.
- **`Array`** - An array of content parts with a defined type. For tool messages, only type `text` is supported.
---

## Enum: `ChatCompletionRequestUserMessageContentPart`

### Variants

- **`Text`** - 
- **`ImageUrl`** - 
- **`InputAudio`** - 
---

## Enum: `ChatCompletionRequestUserMessageContent`

### Variants

- **`Text`** - The text contents of the message.
- **`Array`** - An array of content parts with a defined type. Supported options differ based on the [model](https://platform.openai.com/docs/models) being used to generate the response. Can contain text, image, or audio inputs.
---

## Enum: `ChatCompletionToolChoiceOption`

Controls which (if any) tool is called by the model. `none` means the model will not call any tool and instead generates a message. `auto` means the model can pick between generating a message or calling one or more tools. `required` means the model must call one or more tools. Specifying a particular tool via `{"type": "function", "function": {"name": "my_function"}}` forces the model to call that tool.  `none` is the default when no tools are present. `auto` is the default if tools are present.present.

### Variants

- **`None`** - 
- **`Auto`** - 
- **`Required`** - 
- **`Named`** - 
---

## Enum: `ChatCompletionToolType`

### Variants

- **`Function`** - 
---

## Enum: `CodeInterpreterContainerKind`

Auto configuration for code interpreter container.

### Variants

- **`Auto`** - 
---

## Enum: `CodeInterpreterContainer`

Container configuration for a code interpreter.

### Variants

- **`Id`** - A simple container ID.
- **`Container`** - Auto-configured container with optional files.
---

## Enum: `CodeInterpreterOutput`

### Variants

- **`Logs`** - Code interpreter log output
- **`Image`** - Code interpreter image output
---

## Enum: `CodeInterpreterResult`

Individual result from a code interpreter: either logs or files.

### Variants

- **`Logs`** - Text logs from the execution.
- **`Files`** - File outputs from the execution.
---

## Enum: `ComparisonType`

### Variants

- **`Equals`** - 
- **`NotEquals`** - 
- **`GreaterThan`** - 
- **`GreaterThanOrEqualTo`** - 
- **`LessThan`** - 
- **`LessThanOrEqualTo`** - 
---

## Enum: `ComparisonType`

Specifies the comparison operator: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`.

### Variants

- **`Eq`** - 
- **`Ne`** - 
- **`Gt`** - 
- **`Gte`** - 
- **`Lt`** - 
- **`Lte`** - 
---

## Enum: `CompletionFinishReason`

### Variants

- **`Stop`** - 
- **`Length`** - 
- **`ContentFilter`** - 
---

## Enum: `CompoundFilterType`

Type of operation: `and` or `or`.

### Variants

- **`And`** - 
- **`Or`** - 
---

## Enum: `CompoundType`

### Variants

- **`And`** - 
- **`Or`** - 
---

## Enum: `ComputerCallAction`

Represents all user‐triggered actions.

### Variants

- **`Click`** - A click action.
- **`DoubleClick`** - A double-click action.
- **`Drag`** - A drag action.
- **`KeyPress`** - A keypress action.
- **`Move`** - A mouse move action.
- **`Screenshot`** - A screenshot action.
- **`Scroll`** - A scroll action.
- **`Type`** - A type (text entry) action.
- **`Wait`** - A wait (no-op) action.
---

## Enum: `ComputerUsePreviewArgsError`

Error type for ComputerUsePreviewArgs

### Variants

- **`UninitializedField`** - Uninitialized field
- **`ValidationError`** - Custom validation error
---

## Enum: `ContentType`

Parts of a message: text, image, file, or audio.

### Variants

- **`InputText`** - A text input to the model.
- **`InputImage`** - An image input to the model.
- **`InputFile`** - A file input to the model.
---

## Enum: `Content`

### Variants

- **`OutputText`** - A text output from the model.
- **`Refusal`** - A refusal from the model.
---

## Enum: `CreateMessageRequestContent`

### Variants

- **`Content`** - The text contents of the message.
- **`ContentArray`** - An array of content parts with a defined type, each can be of type `text` or images can be passed with `image_url` or `image_file`. Image types are only supported on [Vision-compatible models](https://platform.openai.com/docs/models/overview).
---

## Enum: `DallE2ImageSize`

### Variants

- **`S256x256`** - 
- **`S512x512`** - 
- **`S1024x1024`** - 
---

## Enum: `DeltaCodeInterpreterOutput`

### Variants

- **`Logs`** - 
- **`Image`** - 
---

## Enum: `DeltaStepDetails`

### Variants

- **`MessageCreation`** - 
- **`ToolCalls`** - 
---

## Enum: `EmbeddingInput`

### Variants

- **`String`** - 
- **`StringArray`** - 
- **`IntegerArray`** - 
- **`ArrayOfIntegerArray`** - 
---

## Enum: `EncodingFormat`

### Variants

- **`Float`** - 
- **`Base64`** - 
---

## Enum: `FilePurpose`

### Variants

- **`Assistants`** - 
- **`Batch`** - 
- **`FineTune`** - 
- **`Vision`** - 
---

## Enum: `FileSearchCallOutputStatus`

### Variants

- **`InProgress`** - 
- **`Searching`** - 
- **`Incomplete`** - 
- **`Failed`** - 
- **`Completed`** - 
---

## Enum: `FileSearchRanker`

### Variants

- **`Auto`** - 
- **`Default2024_08_21`** - 
---

## Enum: `Filter`

Filters for file search.

### Variants

- **`Comparison`** - A filter used to compare a specified attribute key to a given value using a defined comparison operation.
- **`Compound`** - Combine multiple filters using and or or.
---

## Enum: `FineTuneMethod`

The method used for fine-tuning.

### Variants

- **`Supervised`** - 
- **`DPO`** - 
---

## Enum: `FineTuningJobEventType`

### Variants

- **`Message`** - 
- **`Metrics`** - 
---

## Enum: `FineTuningJobIntegrationType`

### Variants

- **`Wandb`** - 
---

## Enum: `FineTuningJobStatus`

### Variants

- **`ValidatingFiles`** - 
- **`Queued`** - 
- **`Running`** - 
- **`Succeeded`** - 
- **`Failed`** - 
- **`Cancelled`** - 
---

## Enum: `FinishReason`

### Variants

- **`Stop`** - 
- **`Length`** - 
- **`ToolCalls`** - 
- **`ContentFilter`** - 
- **`FunctionCall`** - 
---

## Enum: `FunctionArgsError`

Error type for FunctionArgs

### Variants

- **`UninitializedField`** - Uninitialized field
- **`ValidationError`** - Custom validation error
---

## Enum: `HostedToolType`

Hosted tool type identifiers.

### Variants

- **`FileSearch`** - 
- **`WebSearchPreview`** - 
- **`ComputerUsePreview`** - 
---

## Enum: `ImageDetail`

### Variants

- **`Auto`** - 
- **`Low`** - 
- **`High`** - 
---

## Enum: `ImageGenerationBackground`

### Variants

- **`Transparent`** - 
- **`Opaque`** - 
- **`Auto`** - 
---

## Enum: `ImageGenerationOutputFormat`

### Variants

- **`Png`** - 
- **`Webp`** - 
- **`Jpeg`** - 
---

## Enum: `ImageGenerationQuality`

### Variants

- **`Low`** - 
- **`Medium`** - 
- **`High`** - 
- **`Auto`** - 
---

## Enum: `ImageGenerationSize`

### Variants

- **`Auto`** - 
- **`Size1024x1024`** - 
- **`Size1024x1536`** - 
- **`Size1536x1024`** - 
---

## Enum: `ImageModel`

### Variants

- **`DallE2`** - 
- **`DallE3`** - 
- **`Other`** - 
---

## Enum: `ImageQuality`

### Variants

- **`Standard`** - 
- **`HD`** - 
---

## Enum: `ImageResponseFormat`

### Variants

- **`Url`** - 
- **`B64Json`** - 
---

## Enum: `ImageSize`

### Variants

- **`S256x256`** - 
- **`S512x512`** - 
- **`S1024x1024`** - 
- **`S1792x1024`** - 
- **`S1024x1792`** - 
---

## Enum: `ImageStyle`

### Variants

- **`Vivid`** - 
- **`Natural`** - 
---

## Enum: `Image`

### Variants

- **`Url`** - The URL of the generated image, if `response_format` is `url` (default).
- **`B64Json`** - The base64-encoded JSON of the generated image, if `response_format` is `b64_json`.
---

## Enum: `InputAudioFormat`

### Variants

- **`Wav`** - 
- **`Mp3`** - 
---

## Enum: `InputContent`

### Variants

- **`TextInput`** - A text input to the model.
- **`InputItemContentList`** - A list of one or many input items to the model, containing different content types.
---

## Enum: `InputItem`

A context item: currently only messages.

### Variants

- **`Message`** - 
- **`Custom`** - 
---

## Enum: `InputMessageType`

### Variants

- **`Message`** - 
---

## Enum: `InputSource`

### Variants

- **`Path`** - 
- **`Bytes`** - 
- **`VecU8`** - 
---

## Enum: `Input`

Input payload: raw text or structured context items.

### Variants

- **`Text`** - A text input to the model, equivalent to a text input with the user role.
- **`Items`** - A list of one or many input items to the model, containing different content types.
---

## Enum: `InviteStatus`

### Variants

- **`Accepted`** - 
- **`Expired`** - 
- **`Pending`** - 
---

## Enum: `LastErrorCode`

### Variants

- **`ServerError`** - 
- **`RateLimitExceeded`** - 
- **`InvalidPrompt`** - 
---

## Enum: `LearningRateMultiplier`

### Variants

- **`LearningRateMultiplier`** - 
- **`Auto`** - 
---

## Enum: `Level`

### Variants

- **`Info`** - 
- **`Warn`** - 
- **`Error`** - 
---

## Enum: `MessageAttachmentTool`

### Variants

- **`CodeInterpreter`** - 
- **`FileSearch`** - 
---

## Enum: `MessageContentInput`

### Variants

- **`Text`** - 
- **`ImageFile`** - 
- **`ImageUrl`** - 
---

## Enum: `MessageContentTextAnnotations`

### Variants

- **`FileCitation`** - A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "retrieval" tool to search files.
- **`FilePath`** - A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.
---

## Enum: `MessageContent`

### Variants

- **`Text`** - 
- **`ImageFile`** - 
- **`ImageUrl`** - 
- **`Refusal`** - 
---

## Enum: `MessageDeltaContentTextAnnotations`

### Variants

- **`FileCitation`** - 
- **`FilePath`** - 
---

## Enum: `MessageDeltaContent`

### Variants

- **`ImageFile`** - 
- **`ImageUrl`** - 
- **`Text`** - 
- **`Refusal`** - 
---

## Enum: `MessageIncompleteDetailsType`

### Variants

- **`ContentFilter`** - 
- **`MaxTokens`** - 
- **`RunCancelled`** - 
- **`RunExpired`** - 
- **`RunFailed`** - 
---

## Enum: `MessageRole`

### Variants

- **`User`** - 
- **`Assistant`** - 
---

## Enum: `MessageStatus`

### Variants

- **`InProgress`** - 
- **`Incomplete`** - 
- **`Completed`** - 
---

## Enum: `ModInputType`

The type of input that was moderated

### Variants

- **`Text`** - Text content that was moderated
- **`Image`** - Image content that was moderated
---

## Enum: `ModerationContentPart`

Content part for multi-modal moderation input

### Variants

- **`Text`** - An object describing text to classify
- **`ImageUrl`** - An object describing an image to classify
---

## Enum: `ModerationInput`

### Variants

- **`String`** - A single string of text to classify for moderation
- **`StringArray`** - An array of strings to classify for moderation
- **`MultiModal`** - An array of multi-modal inputs to the moderation model
---

## Enum: `NEpochs`

### Variants

- **`NEpochs`** - 
- **`Auto`** - 
---

## Enum: `OpenAIError`

### Variants

- **`Reqwest`** - Underlying error from reqwest library after an API call was made
- **`ApiError`** - OpenAI returns error object with details of API call failure
- **`JSONDeserialize`** - Error when a response cannot be deserialized into a Rust type
- **`FileSaveError`** - Error on the client side when saving file to file system
- **`FileReadError`** - Error on the client side when reading file from file system
- **`StreamError`** - Error on SSE streaming
- **`InvalidArgument`** - Error from client side validation or when builder fails to build request before making API call
---

## Enum: `OpenAIFilePurpose`

### Variants

- **`Assistants`** - 
- **`AssistantsOutput`** - 
- **`Batch`** - 
- **`BatchOutput`** - 
- **`FineTune`** - 
- **`FineTuneResults`** - 
- **`Vision`** - 
---

## Enum: `OrganizationRole`

### Variants

- **`Owner`** - 
- **`Reader`** - 
---

## Enum: `OutputContent`

Nested content within an output message.

### Variants

- **`Message`** - An output message from the model.
- **`FileSearchCall`** - The results of a file search tool call.
- **`FunctionCall`** - A tool call to run a function.
- **`WebSearchCall`** - The results of a web search tool call.
- **`ComputerCall`** - A tool call to a computer use tool.
- **`Reasoning`** - A description of the chain of thought used by a reasoning model while generating a response. Be sure to include these items in your input to the Responses API for subsequent turns of a conversation if you are manually managing context.
- **`ImageGenerationCall`** - Image generation tool call output.
- **`CodeInterpreterCall`** - Code interpreter tool call output.
- **`LocalShellCall`** - Local shell tool call output.
- **`McpCall`** - MCP tool invocation output.
- **`McpListTools`** - MCP list-tools output.
- **`McpApprovalRequest`** - MCP approval request output.
---

## Enum: `OutputStatus`

Status of input/output items.

### Variants

- **`InProgress`** - 
- **`Completed`** - 
- **`Incomplete`** - 
---

## Enum: `PredictionContentContent`

The content that should be matched when generating a model response. If generated tokens would match this content, the entire model response can be returned much more quickly.

### Variants

- **`Text`** - The content used for a Predicted Output. This is often the text of a file you are regenerating with minor changes.
- **`Array`** - An array of content parts with a defined type. Supported options differ based on the [model](https://platform.openai.com/docs/models) being used to generate the response. Can contain text inputs.
---

## Enum: `PredictionContent`

Static predicted output content, such as the content of a text file that is being regenerated.

### Variants

- **`Content`** - The type of the predicted content you want to provide. This type is currently always `content`.
---

## Enum: `ProjectApiKeyOwnerType`

### Variants

- **`User`** - 
- **`ServiceAccount`** - 
---

## Enum: `ProjectStatus`

`active` or `archived`

### Variants

- **`Active`** - 
- **`Archived`** - 
---

## Enum: `ProjectUserRole`

`owner` or `member`

### Variants

- **`Owner`** - 
- **`Member`** - 
---

## Enum: `Prompt`

### Variants

- **`String`** - 
- **`StringArray`** - 
- **`IntegerArray`** - 
- **`ArrayOfIntegerArray`** - 
---

## Enum: `Ranker`

### Variants

- **`Auto`** - 
- **`Default20241115`** - 
---

## Enum: `ReasoningEffort`

### Variants

- **`Low`** - 
- **`Medium`** - 
- **`High`** - 
---

## Enum: `ReasoningSummary`

### Variants

- **`Auto`** - 
- **`Concise`** - 
- **`Detailed`** - 
---

## Enum: `RequireApprovalPolicy`

### Variants

- **`Always`** - 
- **`Never`** - 
---

## Enum: `RequireApproval`

Approval policy or filter for MCP tools.

### Variants

- **`Policy`** - A blanket policy: "always" or "never".
- **`Filter`** - A filter object specifying which tools require approval.
---

## Enum: `ResponseFormat`

### Variants

- **`Text`** - The type of response format being defined: `text`
- **`JsonObject`** - The type of response format being defined: `json_object`
- **`JsonSchema`** - The type of response format being defined: `json_schema`
---

## Enum: `Role`

### Variants

- **`System`** - 
- **`User`** - 
- **`Assistant`** - 
- **`Tool`** - 
- **`Function`** - 
---

## Enum: `Role`

Role of messages in the API.

### Variants

- **`User`** - 
- **`Assistant`** - 
- **`System`** - 
- **`Developer`** - 
---

## Enum: `RunObjectIncompleteDetailsReason`

### Variants

- **`MaxCompletionTokens`** - 
- **`MaxPromptTokens`** - 
---

## Enum: `RunStatus`

### Variants

- **`Queued`** - 
- **`InProgress`** - 
- **`RequiresAction`** - 
- **`Cancelling`** - 
- **`Cancelled`** - 
- **`Failed`** - 
- **`Completed`** - 
- **`Incomplete`** - 
- **`Expired`** - 
---

## Enum: `RunStepDeltaStepDetailsToolCalls`

### Variants

- **`CodeInterpreter`** - 
- **`FileSearch`** - 
- **`Function`** - 
---

## Enum: `RunStepDetailsToolCalls`

### Variants

- **`CodeInterpreter`** - Details of the Code Interpreter tool call the run step was involved in.
- **`FileSearch`** - 
- **`Function`** - 
---

## Enum: `RunStepType`

### Variants

- **`MessageCreation`** - 
- **`ToolCalls`** - 
---

## Enum: `ServiceTierResponse`

### Variants

- **`Scale`** - 
- **`Default`** - 
- **`Flex`** - 
---

## Enum: `ServiceTier`

### Variants

- **`Auto`** - 
- **`Default`** - 
- **`Flex`** - 
---

## Enum: `ServiceTier`

Service tier request options.

### Variants

- **`Auto`** - 
- **`Default`** - 
- **`Flex`** - 
---

## Enum: `SpeechModel`

### Variants

- **`Tts1`** - 
- **`Tts1Hd`** - 
- **`Other`** - 
---

## Enum: `SpeechResponseFormat`

### Variants

- **`Mp3`** - 
- **`Opus`** - 
- **`Aac`** - 
- **`Flac`** - 
- **`Pcm`** - 
- **`Wav`** - 
---

## Enum: `Status`

### Variants

- **`Completed`** - 
- **`Failed`** - 
- **`InProgress`** - 
- **`Incomplete`** - 
---

## Enum: `StepDetails`

### Variants

- **`MessageCreation`** - 
- **`ToolCalls`** - 
---

## Enum: `Stop`

### Variants

- **`String`** - 
- **`StringArray`** - 
---

## Enum: `TextResponseFormat`

### Variants

- **`Text`** - The type of response format being defined: `text`
- **`JsonObject`** - The type of response format being defined: `json_object`
- **`JsonSchema`** - The type of response format being defined: `json_schema`
---

## Enum: `TimestampGranularity`

### Variants

- **`Word`** - 
- **`Segment`** - 
---

## Enum: `ToolChoiceMode`

Simple tool-choice modes.

### Variants

- **`None`** - The model will not call any tool and instead generates a message.
- **`Auto`** - The model can pick between generating a message or calling one or more tools.
- **`Required`** - The model must call one or more tools.
---

## Enum: `ToolChoice`

Control how the model picks or is forced to pick a tool.

### Variants

- **`Mode`** - Controls which (if any) tool is called by the model.
- **`Hosted`** - Indicates that the model should use a built-in tool to generate a response.
- **`Function`** - Use this option to force the model to call a specific function.
---

## Enum: `ToolDefinition`

Definitions for model-callable tools.

### Variants

- **`FileSearch`** - File search tool.
- **`Function`** - Custom function call.
- **`WebSearchPreview`** - Web search preview tool.
- **`ComputerUsePreview`** - Virtual computer control tool.
- **`Mcp`** - Remote Model Context Protocol server.
- **`CodeInterpreter`** - Python code interpreter tool.
- **`ImageGeneration`** - Image generation tool.
- **`LocalShell`** - Local shell command execution tool.
---

## Enum: `TruncationObjectType`

### Variants

- **`Auto`** - 
- **`LastMessages`** - 
---

## Enum: `Truncation`

Truncation strategies.

### Variants

- **`Auto`** - 
- **`Disabled`** - 
---

## Enum: `UploadPurpose`

The intended purpose of the uploaded file.

### Variants

- **`Assistants`** - For use with Assistants and Message files
- **`Vision`** - For Assistants image file inputs
- **`Batch`** - For use with the Batch API
- **`FineTune`** - For use with Fine-tuning
---

## Enum: `UploadStatus`

The status of an upload

### Variants

- **`Pending`** - Upload is pending
- **`Completed`** - Upload has completed successfully
- **`Cancelled`** - Upload was cancelled
- **`Expired`** - Upload has expired
---

## Enum: `VectorStoreChunkingStrategy`

### Variants

- **`Auto`** - The default strategy. This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.
- **`Static`** - 
---

## Enum: `VectorStoreFileBatchStatus`

### Variants

- **`InProgress`** - 
- **`Completed`** - 
- **`Cancelled`** - 
- **`Failed`** - 
---

## Enum: `VectorStoreFileErrorCode`

### Variants

- **`ServerError`** - 
- **`UnsupportedFile`** - 
- **`InvalidFile`** - 
---

## Enum: `VectorStoreFileObjectChunkingStrategy`

### Variants

- **`Other`** - This is returned when the chunking strategy is unknown. Typically, this is because the file was indexed before the `chunking_strategy` concept was introduced in the API.
- **`Static`** - 
---

## Enum: `VectorStoreFileStatus`

### Variants

- **`InProgress`** - 
- **`Completed`** - 
- **`Cancelled`** - 
- **`Failed`** - 
---

## Enum: `VectorStoreSearchFilter`

### Variants

- **`Comparison`** - 
- **`Compound`** - 
---

## Enum: `VectorStoreSearchQuery`

### Variants

- **`Text`** - A single query to search for.
- **`Array`** - A list of queries to search for.
---

## Enum: `VectorStoreStatus`

### Variants

- **`Expired`** - 
- **`InProgress`** - 
- **`Completed`** - 
---

## Enum: `Voice`

### Variants

- **`Alloy`** - 
- **`Ash`** - 
- **`Coral`** - 
- **`Echo`** - 
- **`Fable`** - 
- **`Onyx`** - 
- **`Nova`** - 
- **`Sage`** - 
- **`Shimmer`** - 
---

## Enum: `WebSearchContextSize`

### Variants

- **`Low`** - 
- **`Medium`** - 
- **`High`** - 
---

## Enum: `WebSearchContextSize`

The amount of context window space to use for the search.

### Variants

- **`Low`** - 
- **`Medium`** - 
- **`High`** - 
---

## Enum: `WebSearchPreviewArgsError`

Error type for WebSearchPreviewArgs

### Variants

- **`UninitializedField`** - Uninitialized field
- **`ValidationError`** - Custom validation error
---

## Enum: `WebSearchUserLocationType`

### Variants

- **`Approximate`** - 
---

## Function: `add_part`

**Signature:** `fn add_part()`

**Description:** Adds a [Part](https://platform.openai.com/docs/api-reference/uploads/part-object) to an [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object. A Part represents a chunk of bytes from the file you are trying to upload.  Each Part can be at most 64 MB, and you can add Parts until you hit the Upload maximum of 8 GB.  It is possible to add multiple Parts in parallel. You can decide the intended order of the Parts when you [complete the Upload](https://platform.openai.com/docs/api-reference/uploads/complete).

---

## Function: `additional_instructions`

**Signature:** `fn additional_instructions()`

**Description:** Appends additional instructions at the end of the instructions for the run. This is useful for modifying the behavior on a per-run basis without overriding other instructions.

---

## Function: `additional_messages`

**Signature:** `fn additional_messages()`

**Description:** Adds additional messages to the thread before creating the run.

---

## Function: `allowed_tools`

**Signature:** `fn allowed_tools()`

**Description:** List of allowed tool names or filter object.

---

## Function: `api_keys`

**Signature:** `fn api_keys()`

---

## Function: `archive`

**Signature:** `fn archive()`

**Description:** Archives a project in the organization. Archived projects cannot be used or updated.

---

## Function: `assistant_id`

**Signature:** `fn assistant_id()`

**Description:** The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) to use to execute this run.

---

## Function: `assistant_id`

**Signature:** `fn assistant_id()`

**Description:** The ID of the [assistant](https://platform.openai.com/docs/api-reference/assistants) to use to execute this run.

---

## Function: `assistants`

**Signature:** `fn assistants()`

**Description:** To call [Assistants] group related APIs using this client.

---

## Function: `attachments`

**Signature:** `fn attachments()`

**Description:** A list of files attached to the message, and the tools they should be added to.

---

## Function: `attributes`

**Signature:** `fn attributes()`

---

## Function: `audio`

**Signature:** `fn audio()`

**Description:** Data about a previous audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).

---

## Function: `audio`

**Signature:** `fn audio()`

**Description:** Parameters for audio output. Required when audio output is requested with `modalities: ["audio"]`. [Learn more](https://platform.openai.com/docs/guides/audio).

---

## Function: `audio`

**Signature:** `fn audio()`

**Description:** To call [Audio] group related APIs using this client.

---

## Function: `audit_logs`

**Signature:** `fn audit_logs()`

**Description:** To call [AuditLogs] group related APIs using this client.

---

## Function: `background`

**Signature:** `fn background()`

**Description:** Background type: transparent, opaque, or auto.

---

## Function: `batches`

**Signature:** `fn batches()`

**Description:** To call [Batches] group related APIs using this client.

---

## Function: `best_of`

**Signature:** `fn best_of()`

**Description:** Generates `best_of` completions server-side and returns the "best" (the one with the highest log probability per token). Results cannot be streamed.  When used with `n`, `best_of` controls the number of candidate completions and `n` specifies how many to return – `best_of` must be greater than `n`.  **Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `BatchRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionFunctions`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionRequestAssistantMessage`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionRequestDeveloperMessage`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionRequestFunctionMessage`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionRequestMessageContentPartAudio`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionRequestMessageContentPartImage`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionRequestMessageContentPartRefusal`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionRequestMessageContentPartText`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionRequestSystemMessage`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionRequestToolMessage`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionRequestUserMessage`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ChatCompletionTool`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CodeInterpreter`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ComputerUsePreview`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateAssistantRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateChatCompletionRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateCompletionRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateEmbeddingRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateFileRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateFineTuningJobRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateImageEditRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateImageRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateImageVariationRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateMessageRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateModerationRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateResponse`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateRunRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateSpeechRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateThreadAndRunRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateThreadRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateTranscriptionRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateTranslationRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateUploadRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateVectorStoreFileBatchRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateVectorStoreFileRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `CreateVectorStoreRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `FileSearch`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `FunctionObject`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `Function`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ImageGeneration`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ImageUrl`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `InputFile`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `InputImage`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `InputMessage`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `InviteRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `Location`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `Mcp`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ModifyAssistantRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ProjectCreateRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ProjectUpdateRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ProjectUserCreateRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ProjectUserUpdateRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ReasoningConfig`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `ToolsOutputs`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `UpdateVectorStoreRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `UserRoleUpdateRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `VectorStoreSearchRequest`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Builds a new `WebSearchPreview`.   If a required field has not been initialized.

---

## Function: `build`

**Signature:** `fn build()`

**Description:** Create client with a custom HTTP client, OpenAI config, and backoff.

---

## Function: `bytes`

**Signature:** `fn bytes()`

**Description:** The number of bytes in the file you are uploading.

---

## Function: `cancel`

**Signature:** `fn cancel()`

**Description:** Cancel a vector store file batch. This attempts to cancel the processing of files in this batch as soon as possible.

---

## Function: `cancel`

**Signature:** `fn cancel()`

**Description:** Cancels a run that is `in_progress`

---

## Function: `cancel`

**Signature:** `fn cancel()`

**Description:** Cancels an in-progress batch. The batch will be in status `cancelling` for up to 10 minutes, before changing to `cancelled`, where it will have partial results (if any) available in the output file.

---

## Function: `cancel`

**Signature:** `fn cancel()`

**Description:** Cancels the Upload. No Parts may be added after an Upload is cancelled.

---

## Function: `cancel`

**Signature:** `fn cancel()`

**Description:** Immediately cancel a fine-tune job.

---

## Function: `chat`

**Signature:** `fn chat()`

**Description:** To call [Chat] group related APIs using this client.

---

## Function: `chunking_strategy`

**Signature:** `fn chunking_strategy()`

**Description:** The chunking strategy used to chunk the file(s). If not set, will use the `auto` strategy. Only applicable if `file_ids` is non-empty.

---

## Function: `chunking_strategy`

**Signature:** `fn chunking_strategy()`

---

## Function: `chunking_strategy`

**Signature:** `fn chunking_strategy()`

---

## Function: `city`

**Signature:** `fn city()`

**Description:** Free text input for the city of the user, e.g. San Francisco.

---

## Function: `complete`

**Signature:** `fn complete()`

**Description:** Completes the [Upload](https://platform.openai.com/docs/api-reference/uploads/object).  Within the returned Upload object, there is a nested [File](https://platform.openai.com/docs/api-reference/files/object) object that is ready to use in the rest of the platform.  You can specify the order of the Parts by passing in an ordered list of the Part IDs.  The number of bytes uploaded upon completion must match the number of bytes initially specified when creating the Upload object. No Parts may be added after an Upload is completed.

---

## Function: `completion_window`

**Signature:** `fn completion_window()`

**Description:** The time frame within which the batch should be processed. Currently only `24h` is supported.

---

## Function: `completions`

**Signature:** `fn completions()`

**Description:** To call [Completions] group related APIs using this client.

---

## Function: `config`

**Signature:** `fn config()`

---

## Function: `container`

**Signature:** `fn container()`

**Description:** Container configuration for running code.

---

## Function: `content`

**Signature:** `fn content()`

**Description:** Returns the contents of the specified file

---

## Function: `content`

**Signature:** `fn content()`

**Description:** Text, image, or audio input to the model, used to generate a response. Can also contain previous assistant responses.

---

## Function: `content`

**Signature:** `fn content()`

**Description:** The content of the message.

---

## Function: `content`

**Signature:** `fn content()`

**Description:** The contents of the assistant message. Required unless `tool_calls` or `function_call` is specified.

---

## Function: `content`

**Signature:** `fn content()`

**Description:** The contents of the developer message.

---

## Function: `content`

**Signature:** `fn content()`

**Description:** The contents of the system message.

---

## Function: `content`

**Signature:** `fn content()`

**Description:** The contents of the tool message.

---

## Function: `content`

**Signature:** `fn content()`

**Description:** The contents of the user message.

---

## Function: `content`

**Signature:** `fn content()`

**Description:** The return value from the function call, to return to the model.

---

## Function: `country`

**Signature:** `fn country()`

**Description:** The two-letter ISO country code of the user, e.g. US.

---

## Function: `create_and_run_stream`

**Signature:** `fn create_and_run_stream()`

**Description:** Create a thread and run it in one request (streaming).  byot: You must ensure "stream: true" in serialized `request`

---

## Function: `create_and_run`

**Signature:** `fn create_and_run()`

**Description:** Create a thread and run it in one request.

---

## Function: `create_base64`

**Signature:** `fn create_base64()`

**Description:** Creates an embedding vector representing the input text.  The response will contain the embedding in base64 format.  byot: In serialized `request` you must ensure "encoding_format" is "base64"

---

## Function: `create_edit`

**Signature:** `fn create_edit()`

**Description:** Creates an edited or extended image given an original image and a prompt.

---

## Function: `create_stream`

**Signature:** `fn create_stream()`

**Description:** Create a run.  byot: You must ensure "stream: true" in serialized `request`

---

## Function: `create_stream`

**Signature:** `fn create_stream()`

**Description:** Creates a completion for the chat message  partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message.  [ChatCompletionResponseStream] is a parsed SSE stream until a \[DONE\] is received from server.  byot: You must ensure "stream: true" in serialized `request`

---

## Function: `create_stream`

**Signature:** `fn create_stream()`

**Description:** Creates a completion request for the provided prompt and parameters  Stream back partial progress. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#event_stream_format) as they become available, with the stream terminated by a data: \[DONE\] message.  [CompletionResponseStream] is a parsed SSE stream until a \[DONE\] is received from server.  You must ensure that "stream: true" in serialized `request`

---

## Function: `create_variation`

**Signature:** `fn create_variation()`

**Description:** Creates a variation of a given image.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Adds a user to the project. Users must already be members of the organization to be added to a project.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Classifies if text and/or image inputs are potentially harmful. Learn more in the [moderation guide](https://platform.openai.com/docs/guides/moderation).

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Create a message.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Create a new project in the organization. Projects can be created and archived, but cannot be deleted.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Create a run.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Create a thread.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Create a vector store file by attaching a [File](https://platform.openai.com/docs/api-reference/files) to a [vector store](https://platform.openai.com/docs/api-reference/vector-stores/object).

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Create a vector store.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Create an assistant with a model and instructions.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Create an invite for a user to the organization. The invite must be accepted by the user before they have access to the organization.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Create vector store file batch

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Creates a completion for the provided prompt and parameters  You must ensure that "stream: false" in serialized `request`

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Creates a job that fine-tunes a specified model from a given dataset.  Response includes details of the enqueued job including job status and the name of the fine-tuned models once complete.  [Learn more about Fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Creates a model response for the given chat conversation. Learn more in the  [text generation](https://platform.openai.com/docs/guides/text-generation), [vision](https://platform.openai.com/docs/guides/vision),  and [audio](https://platform.openai.com/docs/guides/audio) guides.   Parameter support can differ depending on the model used to generate the response, particularly for newer reasoning models. Parameters that are only supported for reasoning models are noted below. For the current state of unsupported parameters in reasoning models,  [refer to the reasoning guide](https://platform.openai.com/docs/guides/reasoning).  byot: You must ensure "stream: false" in serialized `request`

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Creates a model response for the given input.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Creates a new service account in the project. This also returns an unredacted API key for the service account.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Creates an embedding vector representing the input text.  byot: In serialized `request` you must ensure "encoding_format" is not "base64"

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Creates an image given a prompt.

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Creates an intermediate [Upload](https://platform.openai.com/docs/api-reference/uploads/object) object that you can add [Parts](https://platform.openai.com/docs/api-reference/uploads/part-object) to. Currently, an Upload can accept at most 8 GB in total and expires after an hour after you create it.  Once you complete the Upload, we will create a [File](https://platform.openai.com/docs/api-reference/files/object) object that contains all the parts you uploaded. This File is usable in the rest of our platform as a regular File object.  For certain `purpose`s, the correct `mime_type` must be specified. Please refer to documentation for the supported MIME types for your use case: - [Assistants](https://platform.openai.com/docs/assistants/tools/file-search/supported-files)  For guidance on the proper filename extensions for each purpose, please follow the documentation on [creating a File](https://platform.openai.com/docs/api-reference/files/create).

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Creates and executes a batch from an uploaded file of requests

---

## Function: `create`

**Signature:** `fn create()`

**Description:** Upload a file that can be used across various endpoints. Individual files can be up to 512 MB, and the size of all files uploaded by one organization can be up to 100 GB.  The Assistants API supports files up to 2 million tokens and of specific file types. See the [Assistants Tools guide](https://platform.openai.com/docs/assistants/tools) for details.  The Fine-tuning API only supports `.jsonl` files. The input also has certain required formats for fine-tuning [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input) or [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input) models.  The Batch API only supports `.jsonl` files up to 100 MB in size. The input also has a specific required [format](https://platform.openai.com/docs/api-reference/batch/request-input).  Please [contact us](https://help.openai.com/) if you need to increase these storage limits.

---

## Function: `delete`

**Signature:** `fn delete()`

**Description:** Delete a file.

---

## Function: `delete`

**Signature:** `fn delete()`

**Description:** Delete a fine-tuned model. You must have the Owner role in your organization.

---

## Function: `delete`

**Signature:** `fn delete()`

**Description:** Delete a thread.

---

## Function: `delete`

**Signature:** `fn delete()`

**Description:** Delete a vector store file. This will remove the file from the vector store but the file itself will not be deleted. To delete the file, use the [delete file](https://platform.openai.com/docs/api-reference/files/delete) endpoint.

---

## Function: `delete`

**Signature:** `fn delete()`

**Description:** Delete a vector store.

---

## Function: `delete`

**Signature:** `fn delete()`

**Description:** Delete an assistant.

---

## Function: `delete`

**Signature:** `fn delete()`

**Description:** Delete an invite. If the invite has already been accepted, it cannot be deleted.

---

## Function: `delete`

**Signature:** `fn delete()`

**Description:** Deletes a service account from the project.

---

## Function: `delete`

**Signature:** `fn delete()`

**Description:** Deletes a user from the organization.

---

## Function: `delete`

**Signature:** `fn delete()`

**Description:** Deletes a user from the project.

---

## Function: `delete`

**Signature:** `fn delete()`

**Description:** Deletes an API key from the project.

---

## Function: `delete`

**Signature:** `fn delete()`

---

## Function: `description`

**Signature:** `fn description()`

**Description:** A description of the function. Used by the model to determine whether or not to call the function.

---

## Function: `description`

**Signature:** `fn description()`

**Description:** A description of what the function does, used by the model to choose when and how to call the function.

---

## Function: `description`

**Signature:** `fn description()`

**Description:** A description of what the function does, used by the model to choose when and how to call the function.

---

## Function: `description`

**Signature:** `fn description()`

**Description:** The description of the assistant. The maximum length is 512 characters.

---

## Function: `description`

**Signature:** `fn description()`

**Description:** The description of the assistant. The maximum length is 512 characters.

---

## Function: `detail`

**Signature:** `fn detail()`

**Description:** Specifies the detail level of the image. Learn more in the [Vision guide](https://platform.openai.com/docs/guides/vision/low-or-high-fidelity-image-understanding).

---

## Function: `detail`

**Signature:** `fn detail()`

**Description:** The detail level of the image to be sent to the model.

---

## Function: `dimensions`

**Signature:** `fn dimensions()`

**Description:** The number of dimensions the resulting output embeddings should have. Only supported in `text-embedding-3` and later models.

---

## Function: `display_height`

**Signature:** `fn display_height()`

**Description:** The height of the computer display.

---

## Function: `display_width`

**Signature:** `fn display_width()`

**Description:** The width of the computer display.

---

## Function: `echo`

**Signature:** `fn echo()`

**Description:** Echo back the prompt in addition to the completion

---

## Function: `effort`

**Signature:** `fn effort()`

**Description:** Constrain effort on reasoning.

---

## Function: `email`

**Signature:** `fn email()`

---

## Function: `embeddings`

**Signature:** `fn embeddings()`

**Description:** To call [Embeddings] group related APIs using this client.

---

## Function: `encoding_format`

**Signature:** `fn encoding_format()`

**Description:** The format to return the embeddings in. Can be either `float` or [`base64`](https://pypi.org/project/pybase64/). Defaults to float

---

## Function: `endpoint`

**Signature:** `fn endpoint()`

**Description:** The endpoint to be used for all requests in the batch. Currently `/v1/chat/completions`, `/v1/embeddings`, and `/v1/completions` are supported. Note that `/v1/embeddings` batches are also restricted to a maximum of 50,000 embedding inputs across all requests in the batch.

---

## Function: `environment`

**Signature:** `fn environment()`

**Description:** The type of computer environment to control.

---

## Function: `expires_after`

**Signature:** `fn expires_after()`

**Description:** The expiration policy for a vector store.

---

## Function: `expires_after`

**Signature:** `fn expires_after()`

---

## Function: `file_batches`

**Signature:** `fn file_batches()`

**Description:** [VectorStoreFileBatches] API group

---

## Function: `file_data`

**Signature:** `fn file_data()`

**Description:** The content of the file to be sent to the model.

---

## Function: `file_id`

**Signature:** `fn file_id()`

**Description:** A [File](https://platform.openai.com/docs/api-reference/files) ID that the vector store should use. Useful for tools like `file_search` that can access files.

---

## Function: `file_id`

**Signature:** `fn file_id()`

**Description:** The ID of the file to be sent to the model.

---

## Function: `file_id`

**Signature:** `fn file_id()`

**Description:** The ID of the file to be sent to the model.

---

## Function: `file_ids`

**Signature:** `fn file_ids()`

**Description:** A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.

---

## Function: `file_ids`

**Signature:** `fn file_ids()`

**Description:** A list of [File](https://platform.openai.com/docs/api-reference/files) IDs that the vector store should use. Useful for tools like `file_search` that can access files.

---

## Function: `file`

**Signature:** `fn file()`

**Description:** The File object (not file name) to be uploaded.

---

## Function: `file`

**Signature:** `fn file()`

**Description:** The audio file object (not file name) translate, in one of these formats: flac, mp3, mp4, mpeg, mpga, m4a, ogg, wav, or webm.

---

## Function: `file`

**Signature:** `fn file()`

**Description:** The audio file to transcribe, in one of these formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm.

---

## Function: `filename`

**Signature:** `fn filename()`

**Description:** The name of the file to be sent to the model.

---

## Function: `filename`

**Signature:** `fn filename()`

**Description:** The name of the file to upload.

---

## Function: `files`

**Signature:** `fn files()`

**Description:** To call [Files] group related APIs using this client.

---

## Function: `files`

**Signature:** `fn files()`

**Description:** [VectorStoreFiles] API group

---

## Function: `filters`

**Signature:** `fn filters()`

**Description:** A filter to apply based on file attributes.

---

## Function: `filters`

**Signature:** `fn filters()`

**Description:** A filter to apply.

---

## Function: `fine_tuning`

**Signature:** `fn fine_tuning()`

**Description:** To call [FineTuning] group related APIs using this client.

---

## Function: `frequency_penalty`

**Signature:** `fn frequency_penalty()`

**Description:** Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.

---

## Function: `frequency_penalty`

**Signature:** `fn frequency_penalty()`

**Description:** Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim.  [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation/parameter-details)

---

## Function: `from_bytes`

**Signature:** `fn from_bytes()`

---

## Function: `from_bytes`

**Signature:** `fn from_bytes()`

---

## Function: `from_bytes`

**Signature:** `fn from_bytes()`

---

## Function: `from_vec_u8`

**Signature:** `fn from_vec_u8()`

---

## Function: `from_vec_u8`

**Signature:** `fn from_vec_u8()`

---

## Function: `from_vec_u8`

**Signature:** `fn from_vec_u8()`

---

## Function: `function_call`

**Signature:** `fn function_call()`

**Description:** Deprecated and replaced by `tool_calls`. The name and arguments of a function that should be called, as generated by the model.

---

## Function: `function_call`

**Signature:** `fn function_call()`

**Description:** Deprecated in favor of `tool_choice`.  Controls which (if any) function is called by the model. `none` means the model will not call a function and instead generates a message. `auto` means the model can pick between generating a message or calling a function. Specifying a particular function via `{"name": "my_function"}` forces the model to call that function.  `none` is the default when no functions are present. `auto` is the default if functions are present.

---

## Function: `function`

**Signature:** `fn function()`

---

## Function: `functions`

**Signature:** `fn functions()`

**Description:** Deprecated in favor of `tools`.  A list of functions the model may generate JSON inputs for.

---

## Function: `get`

**Signature:** `fn get()`

**Description:** List user actions and configuration changes within this organization.

---

## Function: `headers`

**Signature:** `fn headers()`

**Description:** Optional HTTP headers for the MCP server.

---

## Function: `hyperparameters`

**Signature:** `fn hyperparameters()`

**Description:** The hyperparameters used for the fine-tuning job. This value is now deprecated in favor of `method`, and should be passed in under the `method` parameter.

---

## Function: `image_url`

**Signature:** `fn image_url()`

**Description:** The URL of the image to be sent to the model. A fully qualified URL or base64 encoded image in a data URL.

---

## Function: `image_url`

**Signature:** `fn image_url()`

---

## Function: `image`

**Signature:** `fn image()`

**Description:** The image to edit. Must be a valid PNG file, less than 4MB, and square. If mask is not provided, image must have transparency, which will be used as the mask.

---

## Function: `image`

**Signature:** `fn image()`

**Description:** The image to use as the basis for the variation(s). Must be a valid PNG file, less than 4MB, and square.

---

## Function: `images`

**Signature:** `fn images()`

**Description:** To call [Images] group related APIs using this client.

---

## Function: `include`

**Signature:** `fn include()`

**Description:** Specify additional output data to include in the model response.  Supported values: - `file_search_call.results` Include the search results of the file search tool call. - `message.input_image.image_url` Include image URLs from the input message. - `computer_call_output.output.image_url` Include image URLs from the computer call output. - `reasoning.encrypted_content` Include an encrypted version of reasoning tokens in reasoning item outputs. This enables reasoning items to be used in multi-turn conversations when using the Responses API statelessly (for example, when the `store` parameter is set to `false`, or when an organization is enrolled in the zero-data- retention program).  If `None`, no additional data is returned.

---

## Function: `input_audio`

**Signature:** `fn input_audio()`

---

## Function: `input_file_id`

**Signature:** `fn input_file_id()`

**Description:** The ID of an uploaded file that contains requests for the new batch.  See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.  Your input file must be formatted as a [JSONL file](https://platform.openai.com/docs/api-reference/batch/request-input), and must be uploaded with the purpose `batch`. The file can contain up to 50,000 requests, and can be up to 100 MB in size.

---

## Function: `input_image_mask`

**Signature:** `fn input_image_mask()`

**Description:** Optional mask for inpainting.

---

## Function: `input`

**Signature:** `fn input()`

**Description:** Input (or inputs) to classify. Can be a single string, an array of strings, or an array of multi-modal input objects similar to other models.

---

## Function: `input`

**Signature:** `fn input()`

**Description:** Input text to embed, encoded as a string or array of tokens. To embed multiple inputs in a single request, pass an array of strings or array of token arrays. The input must not exceed the max input tokens for the model (8192 tokens for `text-embedding-ada-002`), cannot be an empty string, and any array must be 2048 dimensions or less. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.

---

## Function: `input`

**Signature:** `fn input()`

**Description:** Text, image, or file inputs to the model, used to generate a response.

---

## Function: `input`

**Signature:** `fn input()`

**Description:** The text to generate audio for. The maximum length is 4096 characters.

---

## Function: `instructions`

**Signature:** `fn instructions()`

**Description:** Control the voice of your generated audio with additional instructions. Does not work with `tts-1` or `tts-1-hd`.

---

## Function: `instructions`

**Signature:** `fn instructions()`

**Description:** Inserts a system (or developer) message as the first item in the model's context.  When using along with previous_response_id, the instructions from a previous response will not be carried over to the next response. This makes it simple to swap out system (or developer) messages in new responses.

---

## Function: `instructions`

**Signature:** `fn instructions()`

**Description:** Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis.

---

## Function: `instructions`

**Signature:** `fn instructions()`

**Description:** Overrides the [instructions](https://platform.openai.com/docs/api-reference/assistants/createAssistant) of the assistant. This is useful for modifying the behavior on a per-run basis.

---

## Function: `instructions`

**Signature:** `fn instructions()`

**Description:** The system instructions that the assistant uses. The maximum length is 256,000 characters.

---

## Function: `instructions`

**Signature:** `fn instructions()`

**Description:** The system instructions that the assistant uses. The maximum length is 256,000 characters.

---

## Function: `integrations`

**Signature:** `fn integrations()`

**Description:** A list of integrations to enable for your fine-tuning job.

---

## Function: `invites`

**Signature:** `fn invites()`

**Description:** To call [Invites] group related APIs using this client.

---

## Function: `kind`

**Signature:** `fn kind()`

**Description:** The type of location approximation. Always approximate.

---

## Function: `kind`

**Signature:** `fn kind()`

---

## Function: `language`

**Signature:** `fn language()`

**Description:** The language of the input audio. Supplying the input language in [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) format will improve accuracy and latency.

---

## Function: `list_checkpoints`

**Signature:** `fn list_checkpoints()`

---

## Function: `list_events`

**Signature:** `fn list_events()`

**Description:** Get fine-grained status updates for a fine-tune job.

---

## Function: `list_paginated`

**Signature:** `fn list_paginated()`

**Description:** List your organization's fine-tuning jobs

---

## Function: `list`

**Signature:** `fn list()`

**Description:** List your organization's batches.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Lists all of the users in the organization.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Lists the currently available models, and provides basic information about each one such as the owner and availability.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of API keys in the project.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of assistants.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of files that belong to the user's organization.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of invites in the organization.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of messages for a given thread.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of projects.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of run steps belonging to a run.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of runs belonging to a thread.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of service accounts in the project.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of users in the project.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of vector store files in a batch.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of vector store files.

---

## Function: `list`

**Signature:** `fn list()`

**Description:** Returns a list of vector stores.

---

## Function: `logit_bias`

**Signature:** `fn logit_bias()`

**Description:** Modify the likelihood of specified tokens appearing in the completion.  Accepts a json object that maps tokens (specified by their token ID in the GPT tokenizer) to an associated bias value from -100 to 100. You can use this [tokenizer tool](/tokenizer?view=bpe) (which works for both GPT-2 and GPT-3) to convert text to token IDs. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.  As an example, you can pass `{"50256": -100}` to prevent the <|endoftext|> token from being generated.

---

## Function: `logit_bias`

**Signature:** `fn logit_bias()`

**Description:** Modify the likelihood of specified tokens appearing in the completion.  Accepts a json object that maps tokens (specified by their token ID in the tokenizer) to an associated bias value from -100 to 100. Mathematically, the bias is added to the logits generated by the model prior to sampling. The exact effect will vary per model, but values between -1 and 1 should decrease or increase likelihood of selection; values like -100 or 100 should result in a ban or exclusive selection of the relevant token.

---

## Function: `logprobs`

**Signature:** `fn logprobs()`

**Description:** Include the log probabilities on the `logprobs` most likely output tokens, as well the chosen tokens. For example, if `logprobs` is 5, the API will return a list of the 5 most likely tokens. The API will always return the `logprob` of the sampled token, so there may be up to `logprobs+1` elements in the response.  The maximum value for `logprobs` is 5.

---

## Function: `logprobs`

**Signature:** `fn logprobs()`

**Description:** Whether to return log probabilities of the output tokens or not. If true, returns the log probabilities of each output token returned in the `content` of `message`.

---

## Function: `mask`

**Signature:** `fn mask()`

**Description:** An additional image whose fully transparent areas (e.g. where alpha is zero) indicate where `image` should be edited. Must be a valid PNG file, less than 4MB, and have the same dimensions as `image`.

---

## Function: `max_completion_tokens`

**Signature:** `fn max_completion_tokens()`

**Description:** An upper bound for the number of tokens that can be generated for a completion, including visible output tokens and [reasoning tokens](https://platform.openai.com/docs/guides/reasoning).

---

## Function: `max_completion_tokens`

**Signature:** `fn max_completion_tokens()`

**Description:** The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

---

## Function: `max_completion_tokens`

**Signature:** `fn max_completion_tokens()`

**Description:** The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

---

## Function: `max_num_results`

**Signature:** `fn max_num_results()`

**Description:** The maximum number of results to return. This number should be between 1 and 50 inclusive.

---

## Function: `max_num_results`

**Signature:** `fn max_num_results()`

**Description:** The maximum number of results to return. This number should be between 1 and 50 inclusive.

---

## Function: `max_output_tokens`

**Signature:** `fn max_output_tokens()`

**Description:** An upper bound for the number of tokens that can be generated for a response, including visible output tokens and reasoning tokens.

---

## Function: `max_prompt_tokens`

**Signature:** `fn max_prompt_tokens()`

**Description:** The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

---

## Function: `max_prompt_tokens`

**Signature:** `fn max_prompt_tokens()`

**Description:** The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

---

## Function: `max_tokens`

**Signature:** `fn max_tokens()`

**Description:** The maximum number of [tokens](https://platform.openai.com/tokenizer) that can be generated in the chat completion.  This value can be used to control [costs](https://openai.com/api/pricing/) for text generated via API. This value is now deprecated in favor of `max_completion_tokens`, and is not compatible with [o1 series models](https://platform.openai.com/docs/guides/reasoning).

---

## Function: `max_tokens`

**Signature:** `fn max_tokens()`

**Description:** The maximum number of [tokens](https://platform.openai.com/tokenizer) that can be generated in the completion.  The token count of your prompt plus `max_tokens` cannot exceed the model's context length. [Example Python code](https://cookbook.openai.com/examples/how_to_count_tokens_with_tiktoken) for counting tokens.

---

## Function: `messages`

**Signature:** `fn messages()`

**Description:** A list of [messages](https://platform.openai.com/docs/api-reference/messages) to start the thread with.

---

## Function: `messages`

**Signature:** `fn messages()`

**Description:** A list of messages comprising the conversation so far. Depending on the [model](https://platform.openai.com/docs/models) you use, different message types (modalities) are supported, like [text](https://platform.openai.com/docs/guides/text-generation), [images](https://platform.openai.com/docs/guides/vision), and [audio](https://platform.openai.com/docs/guides/audio).

---

## Function: `messages`

**Signature:** `fn messages()`

**Description:** Call [Messages] group API to manage message in [thread_id] thread.

---

## Function: `metadata`

**Signature:** `fn metadata()`

**Description:** Developer-defined tags and values used for filtering completions in the [dashboard](https://platform.openai.com/chat-completions).

---

## Function: `metadata`

**Signature:** `fn metadata()`

**Description:** Optional custom metadata for the batch.

---

## Function: `metadata`

**Signature:** `fn metadata()`

**Description:** Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format, and querying for objects via API or the dashboard.  Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of 512 characters.

---

## Function: `metadata`

**Signature:** `fn metadata()`

**Description:** Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long.

---

## Function: `metadata`

**Signature:** `fn metadata()`

**Description:** Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maximum of 512 characters long.

---

## Function: `metadata`

**Signature:** `fn metadata()`

**Description:** Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

---

## Function: `metadata`

**Signature:** `fn metadata()`

---

## Function: `metadata`

**Signature:** `fn metadata()`

---

## Function: `metadata`

**Signature:** `fn metadata()`

---

## Function: `metadata`

**Signature:** `fn metadata()`

---

## Function: `metadata`

**Signature:** `fn metadata()`

---

## Function: `method`

**Signature:** `fn method()`

---

## Function: `mime_type`

**Signature:** `fn mime_type()`

**Description:** The MIME type of the file.  This must fall within the supported MIME types for your file purpose. See the supported MIME types for assistants and vision.

---

## Function: `modalities`

**Signature:** `fn modalities()`

---

## Function: `model`

**Signature:** `fn model()`

**Description:** ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** ID of the model to use. Only `whisper-1` (which is powered by our open source Whisper V2 model) is currently available.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** ID of the model to use. See the [model endpoint compatibility](https://platform.openai.com/docs/models#model-endpoint-compatibility) table for details on which models work with the Chat API.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models/overview) for descriptions of them.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models/overview) for descriptions of them.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models/overview) for descriptions of them.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models/overview) for descriptions of them.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** Model ID used to generate the response, like `gpt-4o`. OpenAI offers a wide range of models with different capabilities, performance characteristics, and price points.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** Model to use (default: gpt-image-1).

---

## Function: `model`

**Signature:** `fn model()`

**Description:** One of the available [TTS models](https://platform.openai.com/docs/models/tts): `tts-1` or `tts-1-hd`

---

## Function: `model`

**Signature:** `fn model()`

**Description:** The ID of the [Model](https://platform.openai.com/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** The ID of the [Model](https://platform.openai.com/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** The content moderation model you would like to use. Learn more in the [moderation guide](https://platform.openai.com/docs/guides/moderation), and learn about available models [here](https://platform.openai.com/docs/models/moderation).

---

## Function: `model`

**Signature:** `fn model()`

**Description:** The model to use for image generation.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** The model to use for image generation. Only `dall-e-2` is supported at this time.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** The model to use for image generation. Only `dall-e-2` is supported at this time.

---

## Function: `model`

**Signature:** `fn model()`

**Description:** The name of the model to fine-tune. You can select one of the [supported models](https://platform.openai.com/docs/guides/fine-tuning#which-models-can-be-fine-tuned).

---

## Function: `models`

**Signature:** `fn models()`

**Description:** To call [Models] group related APIs using this client.

---

## Function: `moderation`

**Signature:** `fn moderation()`

**Description:** Moderation level (default: auto).

---

## Function: `moderations`

**Signature:** `fn moderations()`

**Description:** To call [Moderations] group related APIs using this client.

---

## Function: `modify`

**Signature:** `fn modify()`

**Description:** Modifies a project in the organization.

---

## Function: `modify`

**Signature:** `fn modify()`

**Description:** Modifies a user's role in the organization.

---

## Function: `modify`

**Signature:** `fn modify()`

**Description:** Modifies a user's role in the project.

---

## Function: `n`

**Signature:** `fn n()`

**Description:** How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep `n` as `1` to minimize costs.

---

## Function: `n`

**Signature:** `fn n()`

**Description:** How many completions to generate for each prompt. **Note:** Because this parameter generates many completions, it can quickly consume your token quota. Use carefully and ensure that you have reasonable settings for `max_tokens` and `stop`.

---

## Function: `n`

**Signature:** `fn n()`

**Description:** The number of images to generate. Must be between 1 and 10.

---

## Function: `n`

**Signature:** `fn n()`

**Description:** The number of images to generate. Must be between 1 and 10.

---

## Function: `n`

**Signature:** `fn n()`

**Description:** The number of images to generate. Must be between 1 and 10. For `dall-e-3`, only `n=1` is supported.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** An optional name for the participant. Provides the model information to differentiate between participants of the same role.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** An optional name for the participant. Provides the model information to differentiate between participants of the same role.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** An optional name for the participant. Provides the model information to differentiate between participants of the same role.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** An optional name for the participant. Provides the model information to differentiate between participants of the same role.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** The friendly name of the project, this name appears in reports.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** The name of the assistant. The maximum length is 256 characters.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** The name of the assistant. The maximum length is 256 characters.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** The name of the function to be called. Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length of 64.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** The name of the function to call.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** The name of the function to call.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** The name of the vector store.

---

## Function: `name`

**Signature:** `fn name()`

**Description:** The updated name of the project, this name appears in reports.

---

## Function: `name`

**Signature:** `fn name()`

---

## Function: `new`

**Signature:** `fn new()`

**Description:** Client with default [OpenAIConfig]

---

## Function: `new`

**Signature:** `fn new()`

**Description:** Constructs a new Responses client.

---

## Function: `new`

**Signature:** `fn new()`

**Description:** Create client with default [OPENAI_API_BASE] url and default API key from OPENAI_API_KEY env var

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `new`

**Signature:** `fn new()`

---

## Function: `org_id`

**Signature:** `fn org_id()`

---

## Function: `output_compression`

**Signature:** `fn output_compression()`

**Description:** Compression level (0-100).

---

## Function: `output_format`

**Signature:** `fn output_format()`

**Description:** Output format: png, webp, or jpeg.

---

## Function: `output`

**Signature:** `fn output()`

**Description:** The output of the tool call to be submitted to continue the run.

---

## Function: `parallel_tool_calls`

**Signature:** `fn parallel_tool_calls()`

**Description:** Whether to allow the model to run tool calls in parallel.

---

## Function: `parallel_tool_calls`

**Signature:** `fn parallel_tool_calls()`

**Description:** Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling/parallel-function-calling) during tool use.

---

## Function: `parallel_tool_calls`

**Signature:** `fn parallel_tool_calls()`

**Description:** Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling/parallel-function-calling) during tool use.

---

## Function: `parallel_tool_calls`

**Signature:** `fn parallel_tool_calls()`

**Description:** Whether to enable [parallel function calling](https://platform.openai.com/docs/guides/function-calling/parallel-function-calling) during tool use.

---

## Function: `parameters`

**Signature:** `fn parameters()`

**Description:** A JSON schema object describing the parameters of the function.

---

## Function: `parameters`

**Signature:** `fn parameters()`

**Description:** The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/text-generation/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.  Omitting `parameters` defines a function with an empty parameter list.

---

## Function: `parameters`

**Signature:** `fn parameters()`

**Description:** The parameters the functions accepts, described as a JSON Schema object. See the [guide](https://platform.openai.com/docs/guides/text-generation/function-calling) for examples, and the [JSON Schema reference](https://json-schema.org/understanding-json-schema/) for documentation about the format.  Omitting `parameters` defines a function with an empty parameter list.

---

## Function: `partial_images`

**Signature:** `fn partial_images()`

**Description:** Number of partial images (0-3).

---

## Function: `prediction`

**Signature:** `fn prediction()`

**Description:** Configuration for a [Predicted Output](https://platform.openai.com/docs/guides/predicted-outputs),which can greatly improve response times when large parts of the model response are known ahead of time. This is most common when you are regenerating a file with only minor changes to most of the content.

---

## Function: `presence_penalty`

**Signature:** `fn presence_penalty()`

**Description:** Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.

---

## Function: `presence_penalty`

**Signature:** `fn presence_penalty()`

**Description:** Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics.  [See more information about frequency and presence penalties.](https://platform.openai.com/docs/guides/text-generation/parameter-details)

---

## Function: `previous_response_id`

**Signature:** `fn previous_response_id()`

**Description:** The unique ID of the previous response to the model. Use this to create multi-turn conversations.

---

## Function: `projects`

**Signature:** `fn projects()`

**Description:** To call [Projects] group related APIs using this client.

---

## Function: `prompt`

**Signature:** `fn prompt()`

**Description:** A text description of the desired image(s). The maximum length is 1000 characters for `dall-e-2` and 4000 characters for `dall-e-3`.

---

## Function: `prompt`

**Signature:** `fn prompt()`

**Description:** A text description of the desired image(s). The maximum length is 1000 characters.

---

## Function: `prompt`

**Signature:** `fn prompt()`

**Description:** An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should be in English.

---

## Function: `prompt`

**Signature:** `fn prompt()`

**Description:** An optional text to guide the model's style or continue a previous audio segment. The [prompt](https://platform.openai.com/docs/guides/speech-to-text#prompting) should match the audio language.

---

## Function: `prompt`

**Signature:** `fn prompt()`

**Description:** The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.  Note that <|endoftext|> is the document separator that the model sees during training, so if a prompt is not specified the model will generate as if from the beginning of a new document.

---

## Function: `purpose`

**Signature:** `fn purpose()`

**Description:** The intended purpose of the uploaded file.  See the [documentation on File purposes](https://platform.openai.com/docs/api-reference/files/create#files-create-purpose).

---

## Function: `purpose`

**Signature:** `fn purpose()`

**Description:** The intended purpose of the uploaded file.  Use "assistants" for [Assistants](https://platform.openai.com/docs/api-reference/assistants) and [Message](https://platform.openai.com/docs/api-reference/messages) files, "vision" for Assistants image file inputs, "batch" for [Batch API](https://platform.openai.com/docs/guides/batch), and "fine-tune" for [Fine-tuning](https://platform.openai.com/docs/api-reference/fine-tuning).

---

## Function: `quality`

**Signature:** `fn quality()`

**Description:** Quality: low, medium, high, or auto.

---

## Function: `quality`

**Signature:** `fn quality()`

**Description:** The quality of the image that will be generated. `hd` creates images with finer details and greater consistency across the image. This param is only supported for `dall-e-3`.

---

## Function: `query`

**Signature:** `fn query()`

**Description:** A query string for a search.

---

## Function: `ranking_options`

**Signature:** `fn ranking_options()`

**Description:** Ranking options for search.

---

## Function: `ranking_options`

**Signature:** `fn ranking_options()`

**Description:** Ranking options for search.

---

## Function: `reasoning_effort`

**Signature:** `fn reasoning_effort()`

**Description:** **o1 models only**  Constrains effort on reasoning for [reasoning models](https://platform.openai.com/docs/guides/reasoning).  Currently supported values are `low`, `medium`, and `high`. Reducing  reasoning effort can result in faster responses and fewer tokens used on reasoning in a response.

---

## Function: `reasoning`

**Signature:** `fn reasoning()`

**Description:** **o-series models only**: Configuration options for reasoning models.

---

## Function: `refusal`

**Signature:** `fn refusal()`

**Description:** The refusal message by the assistant.

---

## Function: `refusal`

**Signature:** `fn refusal()`

**Description:** The refusal message generated by the model.

---

## Function: `region`

**Signature:** `fn region()`

**Description:** Free text input for the region of the user, e.g. California.

---

## Function: `require_approval`

**Signature:** `fn require_approval()`

**Description:** Approval policy or filter for tools.

---

## Function: `response_format`

**Signature:** `fn response_format()`

**Description:** An object specifying the format that the model must output. Compatible with [GPT-4o](https://platform.openai.com/docs/models/gpt-4o), [GPT-4o mini](https://platform.openai.com/docs/models/gpt-4o-mini), [GPT-4 Turbo](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo) and all GPT-3.5 Turbo models newer than `gpt-3.5-turbo-1106`.  Setting to `{ "type": "json_schema", "json_schema": {...} }` enables Structured Outputs which guarantees the model will match your supplied JSON schema. Learn more in the [Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs).  Setting to `{ "type": "json_object" }` enables JSON mode, which guarantees the message the model generates is valid JSON.  **Important:** when using JSON mode, you **must** also instruct the model to produce JSON yourself via a system or user message. Without this, the model may generate an unending stream of whitespace until the generation reaches the token limit, resulting in a long-running and seemingly "stuck" request. Also note that the message content may be partially cut off if `finish_reason="length"`, which indicates the generation exceeded `max_tokens` or the conversation exceeded the max context length.

---

## Function: `response_format`

**Signature:** `fn response_format()`

**Description:** The format in which the generated images are returned. Must be one of `url` or `b64_json`.

---

## Function: `response_format`

**Signature:** `fn response_format()`

**Description:** The format in which the generated images are returned. Must be one of `url` or `b64_json`.

---

## Function: `response_format`

**Signature:** `fn response_format()`

**Description:** The format in which the generated images are returned. Must be one of `url` or `b64_json`. URLs are only valid for 60 minutes after the image has been generated.

---

## Function: `response_format`

**Signature:** `fn response_format()`

**Description:** The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt.

---

## Function: `response_format`

**Signature:** `fn response_format()`

**Description:** The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt.

---

## Function: `response_format`

**Signature:** `fn response_format()`

**Description:** The format to audio in. Supported formats are `mp3`, `opus`, `aac`, `flac`, `wav`, and `pcm`.

---

## Function: `response_format`

**Signature:** `fn response_format()`

---

## Function: `response_format`

**Signature:** `fn response_format()`

---

## Function: `response_format`

**Signature:** `fn response_format()`

---

## Function: `response_format`

**Signature:** `fn response_format()`

---

## Function: `responses`

**Signature:** `fn responses()`

**Description:** To call [Responses] group related APIs using this client.

---

## Function: `retrieve_file_content`

**Signature:** `fn retrieve_file_content()`

**Description:** Retrieve the parsed contents of a vector store file.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Gets info about the fine-tune job.  [Learn more about Fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieve a message.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieve a user by their identifier

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves a batch.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves a model instance, providing basic information about the model such as the owner and permissioning.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves a project.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves a run step.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves a run.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves a service account in the project.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves a thread.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves a user in the project.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves a vector store file batch.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves a vector store file.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves a vector store.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves an API key in the project.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves an assistant.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Retrieves an invite.

---

## Function: `retrieve`

**Signature:** `fn retrieve()`

**Description:** Returns information about a specific file.

---

## Function: `rewrite_query`

**Signature:** `fn rewrite_query()`

**Description:** Whether to rewrite the natural language query for vector search.

---

## Function: `role`

**Signature:** `fn role()`

**Description:** The role of the entity that is creating the message. Allowed values include: - `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages. - `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

---

## Function: `role`

**Signature:** `fn role()`

**Description:** The role of the message input.

---

## Function: `role`

**Signature:** `fn role()`

**Description:** `owner` or `member`

---

## Function: `role`

**Signature:** `fn role()`

**Description:** `owner` or `member`

---

## Function: `role`

**Signature:** `fn role()`

**Description:** `owner` or `reader`

---

## Function: `role`

**Signature:** `fn role()`

---

## Function: `runs`

**Signature:** `fn runs()`

**Description:** Call [Runs] group API to manage runs in [thread_id] thread.

---

## Function: `save`

**Signature:** `fn save()`

**Description:** Save each image in a dedicated Tokio task and return paths to saved files. For [ResponseFormat::Url] each file is downloaded in dedicated Tokio task.

---

## Function: `save`

**Signature:** `fn save()`

---

## Function: `search_context_size`

**Signature:** `fn search_context_size()`

**Description:** High level guidance for the amount of context window space to use for the search.

---

## Function: `search`

**Signature:** `fn search()`

**Description:** Searches a vector store.

---

## Function: `seed`

**Signature:** `fn seed()`

**Description:** If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result.  Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

---

## Function: `seed`

**Signature:** `fn seed()`

**Description:** The seed controls the reproducibility of the job. Passing in the same seed and job parameters should produce the same results, but may differ in rare cases. If a seed is not specified, one will be generated for you.

---

## Function: `seed`

**Signature:** `fn seed()`

**Description:** This feature is in Beta. If specified, our system will make a best effort to sample deterministically, such that repeated requests with the same `seed` and parameters should return the same result. Determinism is not guaranteed, and you should refer to the `system_fingerprint` response parameter to monitor changes in the backend.

---

## Function: `server_label`

**Signature:** `fn server_label()`

**Description:** A label for this MCP server.

---

## Function: `server_url`

**Signature:** `fn server_url()`

**Description:** The URL for the MCP server.

---

## Function: `service_accounts`

**Signature:** `fn service_accounts()`

---

## Function: `service_tier`

**Signature:** `fn service_tier()`

**Description:** Specifies the latency tier to use for processing the request.  This parameter is relevant for customers subscribed to the Scale tier service.  Supported values: - `auto` - If the Project is Scale tier enabled, the system will utilize Scale tier credits until they are exhausted. - If the Project is not Scale tier enabled, the request will be processed using the default service tier with a lower uptime SLA and no latency guarantee. - `default` The request will be processed using the default service tier with a lower uptime SLA and no latency guarantee. - `flex` The request will be processed with the Flex Processing service tier. Learn more.  When not set, the default behavior is `auto`.  When this parameter is set, the response body will include the `service_tier` utilized.

---

## Function: `service_tier`

**Signature:** `fn service_tier()`

**Description:** Specifies the latency tier to use for processing the request. This parameter is relevant for customers subscribed to the scale tier service: - If set to 'auto', the system will utilize scale tier credits until they are exhausted. - If set to 'default', the request will be processed using the default service tier with a lower uptime SLA and no latency guarentee. - When not set, the default behavior is 'auto'.  When this parameter is set, the response body will include the `service_tier` utilized.

---

## Function: `size`

**Signature:** `fn size()`

**Description:** Size: e.g. "1024x1024" or auto.

---

## Function: `size`

**Signature:** `fn size()`

**Description:** The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024` for `dall-e-2`. Must be one of `1024x1024`, `1792x1024`, or `1024x1792` for `dall-e-3` models.

---

## Function: `size`

**Signature:** `fn size()`

**Description:** The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

---

## Function: `size`

**Signature:** `fn size()`

**Description:** The size of the generated images. Must be one of `256x256`, `512x512`, or `1024x1024`.

---

## Function: `speech`

**Signature:** `fn speech()`

**Description:** Generates audio from the input text.

---

## Function: `speed`

**Signature:** `fn speed()`

**Description:** The speed of the generated audio. Select a value from 0.25 to 4.0. 1.0 is the default.

---

## Function: `steps`

**Signature:** `fn steps()`

**Description:** [Steps] API group

---

## Function: `stop`

**Signature:** `fn stop()`

**Description:** Up to 4 sequences where the API will stop generating further tokens.

---

## Function: `stop`

**Signature:** `fn stop()`

**Description:** Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.

---

## Function: `store`

**Signature:** `fn store()`

**Description:** Whether or not to store the output of this chat completion request  for use in our [model distillation](https://platform.openai.com/docs/guides/distillation) or [evals](https://platform.openai.com/docs/guides/evals) products.

---

## Function: `store`

**Signature:** `fn store()`

**Description:** Whether to store the generated model response for later retrieval via API.

---

## Function: `stream_options`

**Signature:** `fn stream_options()`

---

## Function: `stream_options`

**Signature:** `fn stream_options()`

---

## Function: `stream`

**Signature:** `fn stream()`

**Description:** If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

---

## Function: `stream`

**Signature:** `fn stream()`

**Description:** If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

---

## Function: `stream`

**Signature:** `fn stream()`

**Description:** If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message. [Example Python code](https://cookbook.openai.com/examples/how_to_stream_completions).

---

## Function: `stream`

**Signature:** `fn stream()`

**Description:** Whether to stream back partial progress. If set, tokens will be sent as data-only [server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) as they become available, with the stream terminated by a `data: [DONE]` message.

---

## Function: `strict`

**Signature:** `fn strict()`

**Description:** Whether to enable strict schema adherence when generating the function call. If set to true, the model will follow the exact schema defined in the `parameters` field. Only a subset of JSON Schema is supported when `strict` is `true`. Learn more about Structured Outputs in the [function calling guide](https://platform.openai.com/docs/guides/function-calling).

---

## Function: `strict`

**Signature:** `fn strict()`

**Description:** Whether to enforce strict parameter validation.

---

## Function: `style`

**Signature:** `fn style()`

**Description:** The style of the generated images. Must be one of `vivid` or `natural`. Vivid causes the model to lean towards generating hyper-real and dramatic images. Natural causes the model to produce more natural, less hyper-real looking images. This param is only supported for `dall-e-3`.

---

## Function: `submit_tool_outputs_stream`

**Signature:** `fn submit_tool_outputs_stream()`

**Description:** byot: You must ensure "stream: true" in serialized `request`

---

## Function: `submit_tool_outputs`

**Signature:** `fn submit_tool_outputs()`

**Description:** When a run has the status: "requires_action" and required_action.type is submit_tool_outputs, this endpoint can be used to submit the outputs from the tool calls once they're all completed. All outputs must be submitted in a single request.

---

## Function: `suffix`

**Signature:** `fn suffix()`

**Description:** A string of up to 64 characters that will be added to your fine-tuned model name.  For example, a `suffix` of "custom-model-name" would produce a model name like `ft:gpt-4o-mini:openai:custom-model-name:7p4lURel`.

---

## Function: `suffix`

**Signature:** `fn suffix()`

**Description:** The suffix that comes after a completion of inserted text.  This parameter is only supported for `gpt-3.5-turbo-instruct`.

---

## Function: `summary`

**Signature:** `fn summary()`

**Description:** Summary mode for reasoning.

---

## Function: `temperature`

**Signature:** `fn temperature()`

**Description:** The sampling temperature used for this run. If not set, defaults to 1.

---

## Function: `temperature`

**Signature:** `fn temperature()`

**Description:** The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

---

## Function: `temperature`

**Signature:** `fn temperature()`

**Description:** The sampling temperature, between 0 and 1. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. If set to 0, the model will use [log probability](https://en.wikipedia.org/wiki/Log_probability) to automatically increase the temperature until certain thresholds are hit.

---

## Function: `temperature`

**Signature:** `fn temperature()`

**Description:** What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

---

## Function: `temperature`

**Signature:** `fn temperature()`

**Description:** What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

---

## Function: `temperature`

**Signature:** `fn temperature()`

**Description:** What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

---

## Function: `temperature`

**Signature:** `fn temperature()`

**Description:** What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.  We generally recommend altering this or `top_p` but not both.

---

## Function: `temperature`

**Signature:** `fn temperature()`

**Description:** What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.  We generally recommend altering this or `top_p` but not both.

---

## Function: `temperature`

**Signature:** `fn temperature()`

**Description:** What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or `top_p` but not both.

---

## Function: `text`

**Signature:** `fn text()`

**Description:** Configuration options for a text response from the model. Can be plain text or structured JSON data.

---

## Function: `text`

**Signature:** `fn text()`

---

## Function: `thread`

**Signature:** `fn thread()`

**Description:** If no thread is provided, an empty thread will be created.

---

## Function: `threads`

**Signature:** `fn threads()`

**Description:** To call [Threads] group related APIs using this client.

---

## Function: `timestamp_granularities`

**Signature:** `fn timestamp_granularities()`

**Description:** The timestamp granularities to populate for this transcription. `response_format` must be set `verbose_json` to use timestamp granularities. Either or both of these options are supported: `word`, or `segment`. Note: There is no additional latency for segment timestamps, but generating word timestamps incurs additional latency.

---

## Function: `timezone`

**Signature:** `fn timezone()`

**Description:** The IANA timezone of the user, e.g. America/Los_Angeles.

---

## Function: `tool_call_id`

**Signature:** `fn tool_call_id()`

**Description:** The ID of the tool call in the `required_action` object within the run object the output is being submitted for.

---

## Function: `tool_call_id`

**Signature:** `fn tool_call_id()`

---

## Function: `tool_calls`

**Signature:** `fn tool_calls()`

---

## Function: `tool_choice`

**Signature:** `fn tool_choice()`

**Description:** How the model should select which tool (or tools) to use when generating a response.

---

## Function: `tool_choice`

**Signature:** `fn tool_choice()`

---

## Function: `tool_choice`

**Signature:** `fn tool_choice()`

---

## Function: `tool_choice`

**Signature:** `fn tool_choice()`

---

## Function: `tool_resources`

**Signature:** `fn tool_resources()`

**Description:** A set of resources that are made available to the assistant's tools in this thread. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

---

## Function: `tool_resources`

**Signature:** `fn tool_resources()`

**Description:** A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

---

## Function: `tool_resources`

**Signature:** `fn tool_resources()`

**Description:** A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

---

## Function: `tool_resources`

**Signature:** `fn tool_resources()`

**Description:** A set of resources that are used by the assistant's tools. The resources are specific to the type of tool. For example, the `code_interpreter` tool requires a list of file IDs, while the `file_search` tool requires a list of vector store IDs.

---

## Function: `tools`

**Signature:** `fn tools()`

**Description:** A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

---

## Function: `tools`

**Signature:** `fn tools()`

**Description:** A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `file_search`, or `function`.

---

## Function: `tools`

**Signature:** `fn tools()`

**Description:** A list of tools the model may call. Currently, only functions are supported as a tool. Use this to provide a list of functions the model may generate JSON inputs for. A max of 128 functions are supported.

---

## Function: `tools`

**Signature:** `fn tools()`

**Description:** An array of tools the model may call while generating a response. Can include built-in tools (file_search, web_search_preview, computer_use_preview) or custom function definitions.

---

## Function: `tools`

**Signature:** `fn tools()`

**Description:** Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

---

## Function: `tools`

**Signature:** `fn tools()`

**Description:** Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

---

## Function: `top_logprobs`

**Signature:** `fn top_logprobs()`

**Description:** An integer between 0 and 20 specifying the number of most likely tokens to return at each token position, each with an associated log probability. `logprobs` must be set to `true` if this parameter is used.

---

## Function: `top_p`

**Signature:** `fn top_p()`

**Description:** An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or `temperature` but not both.

---

## Function: `top_p`

**Signature:** `fn top_p()`

**Description:** An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or `temperature` but not both.

---

## Function: `top_p`

**Signature:** `fn top_p()`

**Description:** An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or temperature but not both.

---

## Function: `top_p`

**Signature:** `fn top_p()`

**Description:** An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or temperature but not both.

---

## Function: `top_p`

**Signature:** `fn top_p()`

**Description:** An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or temperature but not both.

---

## Function: `top_p`

**Signature:** `fn top_p()`

**Description:** An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.  We generally recommend altering this or temperature but not both.

---

## Function: `top_p`

**Signature:** `fn top_p()`

**Description:** An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or `temperature` but not both.

---

## Function: `training_file`

**Signature:** `fn training_file()`

**Description:** The ID of an uploaded file that contains training data.  See [upload file](https://platform.openai.com/docs/api-reference/files/create) for how to upload a file.  Your dataset must be formatted as a JSONL file. Additionally, you must upload your file with the purpose `fine-tune`.  The contents of the file should differ depending on if the model uses the [chat](https://platform.openai.com/docs/api-reference/fine-tuning/chat-input), [completions](https://platform.openai.com/docs/api-reference/fine-tuning/completions-input) format, or if the fine-tuning method uses the [preference](https://platform.openai.com/docs/api-reference/fine-tuning/preference-input) format.  See the [fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning) for more details.

---

## Function: `transcribe_raw`

**Signature:** `fn transcribe_raw()`

**Description:** Transcribes audio into the input language.

---

## Function: `transcribe_verbose_json`

**Signature:** `fn transcribe_verbose_json()`

**Description:** Transcribes audio into the input language.

---

## Function: `transcribe`

**Signature:** `fn transcribe()`

**Description:** Transcribes audio into the input language.

---

## Function: `translate_raw`

**Signature:** `fn translate_raw()`

**Description:** Transcribes audio into the input language.

---

## Function: `translate_verbose_json`

**Signature:** `fn translate_verbose_json()`

**Description:** Translates audio into English.

---

## Function: `translate`

**Signature:** `fn translate()`

**Description:** Translates audio into English.

---

## Function: `truncation_strategy`

**Signature:** `fn truncation_strategy()`

**Description:** Controls for how a thread will be truncated prior to the run. Use this to control the intial context window of the run.

---

## Function: `truncation_strategy`

**Signature:** `fn truncation_strategy()`

**Description:** Controls for how a thread will be truncated prior to the run. Use this to control the intial context window of the run.

---

## Function: `truncation`

**Signature:** `fn truncation()`

**Description:** The truncation strategy to use for the model response: - `auto`: drop items in the middle to fit context window. - `disabled`: error if exceeding context window.

---

## Function: `type`

**Signature:** `fn type()`

---

## Function: `update`

**Signature:** `fn update()`

**Description:** Modifies a message.

---

## Function: `update`

**Signature:** `fn update()`

**Description:** Modifies a run.

---

## Function: `update`

**Signature:** `fn update()`

**Description:** Modifies a thread.

---

## Function: `update`

**Signature:** `fn update()`

**Description:** Modifies a vector store.

---

## Function: `update`

**Signature:** `fn update()`

**Description:** Modifies an assistant.

---

## Function: `uploads`

**Signature:** `fn uploads()`

**Description:** To call [Uploads] group related APIs using this client.

---

## Function: `url`

**Signature:** `fn url()`

**Description:** Either a URL of the image or the base64 encoded image data.

---

## Function: `user_id`

**Signature:** `fn user_id()`

**Description:** The ID of the user.

---

## Function: `user_location`

**Signature:** `fn user_location()`

**Description:** The user's location.

---

## Function: `user`

**Signature:** `fn user()`

**Description:** A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse.

---

## Function: `user`

**Signature:** `fn user()`

**Description:** A unique identifier representing your end-user, which can help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/guides/safety-best-practices#end-user-ids).

---

## Function: `user`

**Signature:** `fn user()`

**Description:** A unique identifier representing your end-user, which will help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/usage-policies/end-user-ids).

---

## Function: `user`

**Signature:** `fn user()`

**Description:** A unique identifier representing your end-user, which will help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/usage-policies/end-user-ids).

---

## Function: `user`

**Signature:** `fn user()`

**Description:** A unique identifier representing your end-user, which will help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/usage-policies/end-user-ids).

---

## Function: `user`

**Signature:** `fn user()`

**Description:** A unique identifier representing your end-user, which will help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/usage-policies/end-user-ids).

---

## Function: `user`

**Signature:** `fn user()`

**Description:** A unique identifier representing your end-user, which will help OpenAI to monitor and detect abuse. [Learn more](https://platform.openai.com/docs/usage-policies/end-user-ids).

---

## Function: `users`

**Signature:** `fn users()`

**Description:** To call [Users] group related APIs using this client.

---

## Function: `users`

**Signature:** `fn users()`

---

## Function: `validation_file`

**Signature:** `fn validation_file()`

**Description:** The ID of an uploaded file that contains validation data.  If you provide this file, the data is used to generate validation metrics periodically during fine-tuning. These metrics can be viewed in the fine-tuning results file. The same data should not be present in both train and validation files.  Your dataset must be formatted as a JSONL file. You must upload your file with the purpose `fine-tune`.  See the [fine-tuning guide](https://platform.openai.com/docs/guides/fine-tuning) for more details.

---

## Function: `vector_store_ids`

**Signature:** `fn vector_store_ids()`

**Description:** The IDs of the vector stores to search.

---

## Function: `vector_stores`

**Signature:** `fn vector_stores()`

**Description:** To call [VectorStores] group related APIs using this client.

---

## Function: `voice`

**Signature:** `fn voice()`

**Description:** The voice to use when generating the audio. Supported voices are `alloy`, `ash`, `coral`, `echo`, `fable`, `onyx`, `nova`, `sage`, `shimmer` and `verse`. Previews of the voices are available in the [Text to speech guide](https://platform.openai.com/docs/guides/text-to-speech#voice-options).

---

## Function: `web_search_options`

**Signature:** `fn web_search_options()`

**Description:** This tool searches the web for relevant results to use in a response. Learn more about the [web search tool](https://platform.openai.com/docs/guides/tools-web-search?api-mode=chat).

---

## Function: `with_api_base`

**Signature:** `fn with_api_base()`

**Description:** API base url in form of <https://your-resource-name.openai.azure.com>

---

## Function: `with_api_base`

**Signature:** `fn with_api_base()`

**Description:** To use a API base url different from default [OPENAI_API_BASE]

---

## Function: `with_api_key`

**Signature:** `fn with_api_key()`

**Description:** To use a different API key different from default OPENAI_API_KEY env var

---

## Function: `with_api_key`

**Signature:** `fn with_api_key()`

**Description:** To use a different API key different from default OPENAI_API_KEY env var

---

## Function: `with_api_version`

**Signature:** `fn with_api_version()`

---

## Function: `with_backoff`

**Signature:** `fn with_backoff()`

**Description:** Exponential backoff for retrying [rate limited](https://platform.openai.com/docs/guides/rate-limits) requests.

---

## Function: `with_config`

**Signature:** `fn with_config()`

**Description:** Create client with [OpenAIConfig] or [crate::config::AzureConfig]

---

## Function: `with_deployment_id`

**Signature:** `fn with_deployment_id()`

---

## Function: `with_http_client`

**Signature:** `fn with_http_client()`

**Description:** Provide your own [client] to make HTTP requests with.  [client]: reqwest::Client

---

## Function: `with_org_id`

**Signature:** `fn with_org_id()`

**Description:** To use a different organization id other than default

---

## Function: `with_project_id`

**Signature:** `fn with_project_id()`

**Description:** Non default project id

---

## Struct: `AddUploadPartRequest`

Request parameters for adding a part to an Upload

---

## Struct: `ApiError`

OpenAI API returns error object on failure

---

## Struct: `AssistantObject`

Represents an `assistant` that can call the model and use tools.

---

## Struct: `AssistantToolsFileSearch`

Retrieval tool

---

## Struct: `AssistantToolsFunction`

Function tool

---

## Struct: `AssistantsNamedToolChoice`

Specifies a tool the model should use. Use to force the model to call a specific tool.

---

## Struct: `Assistants`

Build assistants that can call models and use tools to perform tasks.  [Get started with the Assistants API](https://platform.openai.com/docs/assistants)

---

## Struct: `Audio`

Turn audio into text or text into audio. Related guide: [Speech to text](https://platform.openai.com/docs/guides/speech-to-text)

---

## Struct: `AuditLogActorApiKey`

The API Key used to perform the audit logged action.

---

## Struct: `AuditLogActorServiceAccount`

The service account that performed the audit logged action.

---

## Struct: `AuditLogActorSession`

The session in which the audit logged action was performed.

---

## Struct: `AuditLogActorUser`

The user who performed the audit logged action.

---

## Struct: `AuditLogActor`

The actor who performed the audit logged action.

---

## Struct: `AuditLogApiKeyCreatedData`

The payload used to create the API key.

---

## Struct: `AuditLogApiKeyCreated`

The details for events with the type `api_key.created`.

---

## Struct: `AuditLogApiKeyDeleted`

The details for events with the type `api_key.deleted`.

---

## Struct: `AuditLogApiKeyUpdatedChangesRequested`

The payload used to update the API key.

---

## Struct: `AuditLogApiKeyUpdated`

The details for events with the type `api_key.updated`.

---

## Struct: `AuditLogInviteAccepted`

The details for events with the type `invite.accepted`.

---

## Struct: `AuditLogInviteDeleted`

The details for events with the type `invite.deleted`.

---

## Struct: `AuditLogInviteSentData`

The payload used to create the invite.

---

## Struct: `AuditLogInviteSent`

The details for events with the type `invite.sent`.

---

## Struct: `AuditLogLoginFailed`

The details for events with the type `login.failed`.

---

## Struct: `AuditLogLogoutFailed`

The details for events with the type `logout.failed`.

---

## Struct: `AuditLogOrganizationUpdatedChangesRequestedSettings`

The organization settings.

---

## Struct: `AuditLogOrganizationUpdatedChangesRequested`

The payload used to update the organization settings.

---

## Struct: `AuditLogOrganizationUpdated`

The details for events with the type `organization.updated`.

---

## Struct: `AuditLogProjectArchived`

The details for events with the type `project.archived`.

---

## Struct: `AuditLogProjectCreatedData`

The payload used to create the project.

---

## Struct: `AuditLogProjectCreated`

The details for events with the type `project.created`.

---

## Struct: `AuditLogProjectUpdatedChangesRequested`

The payload used to update the project.

---

## Struct: `AuditLogProjectUpdated`

The details for events with the type `project.updated`.

---

## Struct: `AuditLogProject`

The project that the action was scoped to. Absent for actions not scoped to projects.

---

## Struct: `AuditLogServiceAccountCreatedData`

The payload used to create the service account.

---

## Struct: `AuditLogServiceAccountCreated`

The details for events with the type `service_account.created`.

---

## Struct: `AuditLogServiceAccountDeleted`

The details for events with the type `service_account.deleted`.

---

## Struct: `AuditLogServiceAccountUpdatedChangesRequested`

The payload used to updated the service account.

---

## Struct: `AuditLogServiceAccountUpdated`

The details for events with the type `service_account.updated`.

---

## Struct: `AuditLogUserAddedData`

The payload used to add the user to the project.

---

## Struct: `AuditLogUserAdded`

The details for events with the type `user.added`.

---

## Struct: `AuditLogUserDeleted`

The details for events with the type `user.deleted`.

---

## Struct: `AuditLogUserUpdatedChangesRequested`

The payload used to update the user.

---

## Struct: `AuditLogUserUpdated`

The details for events with the type `user.updated`.

---

## Struct: `AuditLog`

A log of a user action or configuration change within this organization.

---

## Struct: `AuditLogs`

Logs of user actions and configuration changes within this organization. To log events, you must activate logging in the [Organization Settings](https://platform.openai.com/settings/organization/general). Once activated, for security reasons, logging cannot be deactivated.

---

## Struct: `AzureConfig`

Configuration for Azure OpenAI Service

---

## Struct: `Base64Embedding`

Represents an base64-encoded embedding vector returned by embedding endpoint.

---

## Struct: `BatchRequestArgs`

Builder for [`BatchRequest`](struct.BatchRequest.html).

---

## Struct: `BatchRequestInput`

The per-line object of the batch input file

---

## Struct: `BatchRequestOutput`

The per-line object of the batch output and error files

---

## Struct: `Batches`

Create large batches of API requests for asynchronous processing. The Batch API returns completions within 24 hours for a 50% discount.  Related guide: [Batch](https://platform.openai.com/docs/guides/batch)

---

## Struct: `CategoryAppliedInputTypes`

A list of the categories along with the input type(s) that the score applies to.

---

## Struct: `CategoryScore`

A list of the categories along with their scores as predicted by model.

---

## Struct: `ChatCompletionFunctionsArgs`

Builder for [`ChatCompletionFunctions`](struct.ChatCompletionFunctions.html).

---

## Struct: `ChatCompletionNamedToolChoice`

Specifies a tool the model should use. Use to force the model to call a specific function.

---

## Struct: `ChatCompletionRequestAssistantMessageArgs`

Builder for [`ChatCompletionRequestAssistantMessage`](struct.ChatCompletionRequestAssistantMessage.html).

---

## Struct: `ChatCompletionRequestDeveloperMessageArgs`

Builder for [`ChatCompletionRequestDeveloperMessage`](struct.ChatCompletionRequestDeveloperMessage.html).

---

## Struct: `ChatCompletionRequestFunctionMessageArgs`

Builder for [`ChatCompletionRequestFunctionMessage`](struct.ChatCompletionRequestFunctionMessage.html).

---

## Struct: `ChatCompletionRequestMessageContentPartAudioArgs`

Builder for [`ChatCompletionRequestMessageContentPartAudio`](struct.ChatCompletionRequestMessageContentPartAudio.html).

---

## Struct: `ChatCompletionRequestMessageContentPartAudio`

Learn about [audio inputs](https://platform.openai.com/docs/guides/audio).

---

## Struct: `ChatCompletionRequestMessageContentPartImageArgs`

Builder for [`ChatCompletionRequestMessageContentPartImage`](struct.ChatCompletionRequestMessageContentPartImage.html).

---

## Struct: `ChatCompletionRequestMessageContentPartRefusalBuilder`

Builder for [`ChatCompletionRequestMessageContentPartRefusal`](struct.ChatCompletionRequestMessageContentPartRefusal.html).

---

## Struct: `ChatCompletionRequestMessageContentPartTextArgs`

Builder for [`ChatCompletionRequestMessageContentPartText`](struct.ChatCompletionRequestMessageContentPartText.html).

---

## Struct: `ChatCompletionRequestSystemMessageArgs`

Builder for [`ChatCompletionRequestSystemMessage`](struct.ChatCompletionRequestSystemMessage.html).

---

## Struct: `ChatCompletionRequestToolMessageArgs`

Builder for [`ChatCompletionRequestToolMessage`](struct.ChatCompletionRequestToolMessage.html).

---

## Struct: `ChatCompletionRequestToolMessage`

Tool message

---

## Struct: `ChatCompletionRequestUserMessageArgs`

Builder for [`ChatCompletionRequestUserMessage`](struct.ChatCompletionRequestUserMessage.html).

---

## Struct: `ChatCompletionResponseMessage`

A chat completion message generated by the model.

---

## Struct: `ChatCompletionStreamOptions`

Options for streaming response. Only set this when you set `stream: true`.

---

## Struct: `ChatCompletionStreamResponseDelta`

A chat completion delta generated by streamed model responses.

---

## Struct: `ChatCompletionToolArgs`

Builder for [`ChatCompletionTool`](struct.ChatCompletionTool.html).

---

## Struct: `Chat`

Given a list of messages comprising a conversation, the model will return a response.  Related guide: [Chat completions](https://platform.openai.com//docs/guides/text-generation)

---

## Struct: `Click`

A click action.

---

## Struct: `Client`

Client is a container for config, backoff and http_client used to make API calls.

---

## Struct: `CodeInterpreterArgs`

Builder for [`CodeInterpreter`](struct.CodeInterpreter.html).

---

## Struct: `CodeInterpreterCallOutput`

Output of a code interpreter request.

---

## Struct: `CodeInterpreterFileOutput`

The output containing file references.

---

## Struct: `CodeInterpreterTextOutput`

The output containing execution logs.

---

## Struct: `CodeInterpreter`

Code interpreter tool definition.

---

## Struct: `ComparisonFilter`

A filter used to compare a specified attribute key to a given value using a defined comparison operation.

---

## Struct: `ComparisonFilter`

Single comparison filter.

---

## Struct: `CompleteUploadRequest`

Request parameters for completing an Upload

---

## Struct: `CompletionTokensDetails`

Breakdown of tokens used in a completion.

---

## Struct: `CompletionUsage`

Usage statistics for the completion request.

---

## Struct: `Completions`

Given a prompt, the model will return one or more predicted completions, and can also return the probabilities of alternative tokens at each position. We recommend most users use our Chat completions API. [Learn more](https://platform.openai.com/docs/deprecations/2023-07-06-gpt-and-embeddings)  Related guide: [Legacy Completions](https://platform.openai.com/docs/guides/gpt/completions-api)

---

## Struct: `CompoundFilter`

Combine multiple filters using `and` or `or`.

---

## Struct: `CompoundFilter`

Combine multiple filters.

---

## Struct: `ComputerCallOutput`

Output from a computer tool call.

---

## Struct: `ComputerUsePreviewArgs`

Builder for [`ComputerUsePreview`](struct.ComputerUsePreview.html).

---

## Struct: `CreateAssistantRequestArgs`

Builder for [`CreateAssistantRequest`](struct.CreateAssistantRequest.html).

---

## Struct: `CreateChatCompletionRequestArgs`

Builder for [`CreateChatCompletionRequest`](struct.CreateChatCompletionRequest.html).

---

## Struct: `CreateChatCompletionResponse`

Represents a chat completion response returned by model, based on the provided input.

---

## Struct: `CreateChatCompletionStreamResponse`

Represents a streamed chunk of a chat completion response returned by model, based on the provided input.

---

## Struct: `CreateCompletionRequestArgs`

Builder for [`CreateCompletionRequest`](struct.CreateCompletionRequest.html).

---

## Struct: `CreateEmbeddingRequestArgs`

Builder for [`CreateEmbeddingRequest`](struct.CreateEmbeddingRequest.html).

---

## Struct: `CreateFileRequestArgs`

Builder for [`CreateFileRequest`](struct.CreateFileRequest.html).

---

## Struct: `CreateFineTuningJobRequestArgs`

Builder for [`CreateFineTuningJobRequest`](struct.CreateFineTuningJobRequest.html).

---

## Struct: `CreateImageEditRequestArgs`

Builder for [`CreateImageEditRequest`](struct.CreateImageEditRequest.html).

---

## Struct: `CreateImageRequestArgs`

Builder for [`CreateImageRequest`](struct.CreateImageRequest.html).

---

## Struct: `CreateImageVariationRequestArgs`

Builder for [`CreateImageVariationRequest`](struct.CreateImageVariationRequest.html).

---

## Struct: `CreateMessageRequestArgs`

Builder for [`CreateMessageRequest`](struct.CreateMessageRequest.html).

---

## Struct: `CreateModerationRequestArgs`

Builder for [`CreateModerationRequest`](struct.CreateModerationRequest.html).

---

## Struct: `CreateModerationResponse`

Represents if a given text input is potentially harmful.

---

## Struct: `CreateResponseArgs`

Builder for [`CreateResponse`](struct.CreateResponse.html).

---

## Struct: `CreateResponse`

Builder for a Responses API request.

---

## Struct: `CreateRunRequestArgs`

Builder for [`CreateRunRequest`](struct.CreateRunRequest.html).

---

## Struct: `CreateSpeechRequestArgs`

Builder for [`CreateSpeechRequest`](struct.CreateSpeechRequest.html).

---

## Struct: `CreateThreadAndRunRequestArgs`

Builder for [`CreateThreadAndRunRequest`](struct.CreateThreadAndRunRequest.html).

---

## Struct: `CreateThreadRequestArgs`

Builder for [`CreateThreadRequest`](struct.CreateThreadRequest.html).

---

## Struct: `CreateTranscriptionRequestArgs`

Builder for [`CreateTranscriptionRequest`](struct.CreateTranscriptionRequest.html).

---

## Struct: `CreateTranscriptionResponseJson`

Represents a transcription response returned by model, based on the provided input.

---

## Struct: `CreateTranscriptionResponseVerboseJson`

Represents a verbose json transcription response returned by model, based on the provided input.

---

## Struct: `CreateTranslationRequestArgs`

Builder for [`CreateTranslationRequest`](struct.CreateTranslationRequest.html).

---

## Struct: `CreateUploadRequestArgs`

Builder for [`CreateUploadRequest`](struct.CreateUploadRequest.html).

---

## Struct: `CreateUploadRequest`

Request to create an upload object that can accept byte chunks in the form of Parts.

---

## Struct: `CreateVectorStoreFileBatchRequestArgs`

Builder for [`CreateVectorStoreFileBatchRequest`](struct.CreateVectorStoreFileBatchRequest.html).

---

## Struct: `CreateVectorStoreFileRequestArgs`

Builder for [`CreateVectorStoreFileRequest`](struct.CreateVectorStoreFileRequest.html).

---

## Struct: `CreateVectorStoreRequestArgs`

Builder for [`CreateVectorStoreRequest`](struct.CreateVectorStoreRequest.html).

---

## Struct: `DoubleClick`

A double click action.

---

## Struct: `Drag`

A drag action.

---

## Struct: `Embedding`

Represents an embedding vector returned by embedding endpoint.

---

## Struct: `Embeddings`

Get a vector representation of a given input that can be easily consumed by machine learning models and algorithms.  Related guide: [Embeddings](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings)

---

## Struct: `ErrorObject`

Error returned by the API when a request fails.

---

## Struct: `FileSearchArgs`

Builder for [`FileSearch`](struct.FileSearch.html).

---

## Struct: `FileSearchCallOutput`

File search tool call output.

---

## Struct: `FileSearchRankingOptions`

The ranking options for the file search. If not specified, the file search tool will use the `auto` ranker and a score_threshold of 0.  See the [file search tool documentation](https://platform.openai.com/docs/assistants/tools/file-search#customizing-file-search-settings) for more information.

---

## Struct: `FileSearchResult`

A single result from a file search.

---

## Struct: `Files`

Files are used to upload documents that can be used with features like Assistants and Fine-tuning.

---

## Struct: `FineTuneJobError`

For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.

---

## Struct: `FineTuningJobCheckpoint`

The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.

---

## Struct: `FineTuningJobEvent`

Fine-tuning job event object

---

## Struct: `FineTuningJob`

The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.

---

## Struct: `FineTuning`

Manage fine-tuning jobs to tailor a model to your specific training data.  Related guide: [Fine-tune models](https://platform.openai.com/docs/guides/fine-tuning)

---

## Struct: `FunctionArgs`

Builder for [`Function`](struct.Function.html).

---

## Struct: `FunctionCall`

Metadata for a function call request.

---

## Struct: `FunctionCall`

The name and arguments of a function that should be called, as generated by the model.

---

## Struct: `FunctionObjectArgs`

Builder for [`FunctionObject`](struct.FunctionObject.html).

---

## Struct: `ImageGenerationArgs`

Builder for [`ImageGeneration`](struct.ImageGeneration.html).

---

## Struct: `ImageGenerationCallOutput`

Output of an image generation request.

---

## Struct: `ImageGeneration`

Image generation tool definition.

---

## Struct: `ImageUrlArgs`

Builder for [`ImageUrl`](struct.ImageUrl.html).

---

## Struct: `Images`

Given a prompt and/or an input image, the model will generate a new image.  Related guide: [Image generation](https://platform.openai.com/docs/guides/images)

---

## Struct: `IncompleteDetails`

Details about an incomplete response.

---

## Struct: `InputFileArgs`

Builder for [`InputFile`](struct.InputFile.html).

---

## Struct: `InputImageArgs`

Builder for [`InputImage`](struct.InputImage.html).

---

## Struct: `InputImageMask`

Mask image input for image generation.

---

## Struct: `InputMessageArgs`

Builder for [`InputMessage`](struct.InputMessage.html).

---

## Struct: `InputMessage`

A message to prime the model.

---

## Struct: `InviteRequestArgs`

Builder for [`InviteRequest`](struct.InviteRequest.html).

---

## Struct: `Invite`

Represents an individual `invite` to the organization.

---

## Struct: `Invites`

Invite and manage invitations for an organization. Invited users are automatically added to the Default project.

---

## Struct: `KeyPress`

A keypress action.

---

## Struct: `ListAuditLogsResponse`

Represents a list of audit logs.

---

## Struct: `LocalShellAction`

Define the shape of a local shell action (exec).

---

## Struct: `LocalShellCallOutput`

Output of a local shell command request.

---

## Struct: `LocationArgs`

Builder for [`Location`](struct.Location.html).

---

## Struct: `Location`

Approximate user location for web search.

---

## Struct: `McpAllowedToolsFilter`

Filter object for MCP allowed tools.

---

## Struct: `McpApprovalFilter`

Filter object for MCP tool approval.

---

## Struct: `McpApprovalRequestOutput`

Output representing a human approval request for an MCP tool.

---

## Struct: `McpArgs`

Builder for [`Mcp`](struct.Mcp.html).

---

## Struct: `McpCallOutput`

Output of an MCP server tool invocation.

---

## Struct: `McpListToolsOutput`

Output listing tools available on an MCP server.

---

## Struct: `McpToolInfo`

Information about a single tool on an MCP server.

---

## Struct: `Mcp`

MCP (Model Context Protocol) tool configuration.

---

## Struct: `MessageContentImageFileObject`

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

---

## Struct: `MessageContentImageUrlObject`

References an image URL in the content of a message.

---

## Struct: `MessageContentTextAnnotationsFileCitationObject`

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

---

## Struct: `MessageContentTextObject`

The text content that is part of a message.

---

## Struct: `MessageDeltaContentImageFileObject`

References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.

---

## Struct: `MessageDeltaContentTextAnnotationsFileCitationObject`

A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.

---

## Struct: `MessageDeltaContentTextAnnotationsFilePathObject`

A URL for the file that's generated when the assistant used the `code_interpreter` tool to generate a file.

---

## Struct: `MessageDeltaContentTextObject`

The text content that is part of a message.

---

## Struct: `MessageDeltaObject`

Represents a message delta i.e. any changed fields on a message during streaming.

---

## Struct: `MessageObject`

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

---

## Struct: `Messages`

Represents a message within a [thread](https://platform.openai.com/docs/api-reference/threads).

---

## Struct: `Model`

Describes an OpenAI model offering that can be used with the API.

---

## Struct: `Models`

List and describe the various models available in the API. You can refer to the [Models](https://platform.openai.com/docs/models) documentation to understand what models are available and the differences between them.

---

## Struct: `ModerationImageUrl`

Image URL configuration for image moderation

---

## Struct: `Moderations`

Given text and/or image inputs, classifies if those inputs are potentially harmful across several categories.  Related guide: [Moderations](https://platform.openai.com/docs/guides/moderation)

---

## Struct: `ModifyAssistantRequestArgs`

Builder for [`ModifyAssistantRequest`](struct.ModifyAssistantRequest.html).

---

## Struct: `MoveAction`

A mouse move action.

---

## Struct: `OpenAIConfig`

Configuration for OpenAI API

---

## Struct: `OpenAIFile`

The `File` object represents a document that has been uploaded to OpenAI.

---

## Struct: `OutputMessage`

A message generated by the model.

---

## Struct: `OutputText`

A simple text output from the model.

---

## Struct: `Point`

A point in 2D space.

---

## Struct: `ProjectAPIKeys`

Manage API keys for a given project. Supports listing and deleting keys for users. This API does not allow issuing keys for users, as users need to authorize themselves to generate keys.

---

## Struct: `ProjectApiKeyDeleteResponse`

Represents the response object for deleting a project API key.

---

## Struct: `ProjectApiKeyListResponse`

Represents the response object for listing project API keys.

---

## Struct: `ProjectApiKeyOwner`

Represents the owner of a project API key.

---

## Struct: `ProjectApiKey`

Represents an individual API key in a project.

---

## Struct: `ProjectCreateRequestArgs`

Builder for [`ProjectCreateRequest`](struct.ProjectCreateRequest.html).

---

## Struct: `ProjectCreateRequest`

The project create request payload.

---

## Struct: `ProjectListResponse`

A list of Project objects.

---

## Struct: `ProjectServiceAccountApiKey`

Represents the API key associated with a project service account.

---

## Struct: `ProjectServiceAccountCreateRequest`

Represents the request object for creating a project service account.

---

## Struct: `ProjectServiceAccountCreateResponse`

Represents the response object for creating a project service account.

---

## Struct: `ProjectServiceAccountDeleteResponse`

Represents the response object for deleting a project service account.

---

## Struct: `ProjectServiceAccountListResponse`

Represents the response object for listing project service accounts.

---

## Struct: `ProjectServiceAccount`

Represents an individual service account in a project.

---

## Struct: `ProjectServiceAccounts`

Manage service accounts within a project. A service account is a bot user that is not associated with a user. If a user leaves an organization, their keys and membership in projects will no longer work. Service accounts do not have this limitation. However, service accounts can also be deleted from a project.

---

## Struct: `ProjectUpdateRequestArgs`

Builder for [`ProjectUpdateRequest`](struct.ProjectUpdateRequest.html).

---

## Struct: `ProjectUpdateRequest`

The project update request payload.

---

## Struct: `ProjectUserCreateRequestArgs`

Builder for [`ProjectUserCreateRequest`](struct.ProjectUserCreateRequest.html).

---

## Struct: `ProjectUserCreateRequest`

The project user create request payload.

---

## Struct: `ProjectUserUpdateRequestArgs`

Builder for [`ProjectUserUpdateRequest`](struct.ProjectUserUpdateRequest.html).

---

## Struct: `ProjectUser`

Represents an individual user in a project.

---

## Struct: `ProjectUsers`

Manage users within a project, including adding, updating roles, and removing users. Users cannot be removed from the Default project, unless they are being removed from the organization.

---

## Struct: `Project`

Represents an individual project.

---

## Struct: `Projects`

Manage the projects within an organization includes creation, updating, and archiving or projects. The Default project cannot be modified or archived.

---

## Struct: `PromptTokensDetails`

Breakdown of tokens used in a completion.

---

## Struct: `RankingOptions`

Options for search result ranking.

---

## Struct: `RankingOptions`

Ranking options for search.

---

## Struct: `ReasoningConfigArgs`

Builder for [`ReasoningConfig`](struct.ReasoningConfig.html).

---

## Struct: `ReasoningConfig`

o-series reasoning settings.

---

## Struct: `ReasoningItem`

A reasoning item representing the model's chain of thought, including summary paragraphs.

---

## Struct: `Refusal`

A refusal explanation from the model.

---

## Struct: `Response`

The complete response returned by the Responses API.

---

## Struct: `Responses`

Given text input or a list of context items, the model will generate a response.  Related guide: [Responses API](https://platform.openai.com/docs/guides/responses)

---

## Struct: `RunObject`

Represents an execution run on a [thread](https://platform.openai.com/docs/api-reference/threads).

---

## Struct: `RunStepDeltaObject`

Represents a run step delta i.e. any changed fields on a run step during streaming.

---

## Struct: `RunStepDeltaStepDetailsMessageCreationObject`

Details of the message creation by the run step.

---

## Struct: `RunStepDeltaStepDetailsToolCallsCodeObject`

Details of the Code Interpreter tool call the run step was involved in.

---

## Struct: `RunStepDeltaStepDetailsToolCallsCodeOutputImageObject`

Code interpreter image output

---

## Struct: `RunStepDeltaStepDetailsToolCallsCodeOutputLogsObject`

Text output from the Code Interpreter tool call as part of a run step.

---

## Struct: `RunStepDeltaStepDetailsToolCallsFunctionObject`

Function tool call

---

## Struct: `RunStepDeltaStepDetailsToolCallsObject`

Details of the tool call.

---

## Struct: `RunStepDetailsMessageCreationObject`

Details of the message creation by the run step.

---

## Struct: `RunStepDetailsToolCallsCodeObject`

Code interpreter tool call

---

## Struct: `RunStepDetailsToolCallsCodeOutputLogsObject`

Text output from the Code Interpreter tool call as part of a run step.

---

## Struct: `RunStepDetailsToolCallsFileSearchObject`

File search tool call

---

## Struct: `RunStepDetailsToolCallsFileSearchResultObject`

A result instance of the file search.

---

## Struct: `RunStepDetailsToolCallsObject`

Details of the tool call.

---

## Struct: `RunStepObject`

Represents a step in execution of a run.

---

## Struct: `Runs`

Represents an execution run on a thread.  Related guide: [Assistants](https://platform.openai.com/docs/assistants/overview)

---

## Struct: `Scroll`

A scroll action.

---

## Struct: `StaticChunkingStrategy`

Static Chunking Strategy

---

## Struct: `Steps`

Represents a step in execution of a run.

---

## Struct: `SummaryText`

A single summary text fragment from reasoning.

---

## Struct: `TextConfig`

Configuration for text response format.

---

## Struct: `ThreadObject`

Represents a thread that contains [messages](https://platform.openai.com/docs/api-reference/messages).

---

## Struct: `Threads`

Create threads that assistants can interact with.  Related guide: [Assistants](https://platform.openai.com/docs/assistants/overview)

---

## Struct: `ToolsOutputsArgs`

Builder for [`ToolsOutputs`](struct.ToolsOutputs.html).

---

## Struct: `TruncationObject`

Thread Truncation Controls

---

## Struct: `TypeAction`

A typing (text entry) action.

---

## Struct: `UpdateVectorStoreRequestArgs`

Builder for [`UpdateVectorStoreRequest`](struct.UpdateVectorStoreRequest.html).

---

## Struct: `UploadPart`

The upload Part represents a chunk of bytes we can add to an Upload object.

---

## Struct: `Upload`

The Upload object can accept byte chunks in the form of Parts.

---

## Struct: `Uploads`

Allows you to upload large files in multiple parts.

---

## Struct: `Usage`

Usage statistics for a response.

---

## Struct: `UserDeleteResponse`

Confirmation of the deleted user

---

## Struct: `UserListResponse`

A list of `User` objects.

---

## Struct: `UserRoleUpdateRequestArgs`

Builder for [`UserRoleUpdateRequest`](struct.UserRoleUpdateRequest.html).

---

## Struct: `User`

Represents an individual `user` within an organization.

---

## Struct: `Users`

Manage users and their role in an organization. Users will be automatically added to the Default project.

---

## Struct: `VectorStoreExpirationAfter`

Vector store expiration policy

---

## Struct: `VectorStoreFileBatchObject`

A batch of files attached to a vector store.

---

## Struct: `VectorStoreFileBatches`

Vector store file batches represent operations to add multiple files to a vector store.  Related guide: [File Search](https://platform.openai.com/docs/assistants/tools/file-search)

---

## Struct: `VectorStoreFileContentObject`

Represents the parsed content of a vector store file.

---

## Struct: `VectorStoreFileContentResponse`

Represents the parsed content of a vector store file.

---

## Struct: `VectorStoreFiles`

Vector store files represent files inside a vector store.  Related guide: [File Search](https://platform.openai.com/docs/assistants/tools/file-search)

---

## Struct: `VectorStoreObject`

A vector store is a collection of processed files can be used by the `file_search` tool.

---

## Struct: `VectorStoreSearchRequestArgs`

Builder for [`VectorStoreSearchRequest`](struct.VectorStoreSearchRequest.html).

---

## Struct: `WebSearchCallOutput`

Web search tool call output.

---

## Struct: `WebSearchLocation`

Approximate location parameters for the search.

---

## Struct: `WebSearchOptions`

Options for the web search tool.

---

## Struct: `WebSearchPreviewArgs`

Builder for [`WebSearchPreview`](struct.WebSearchPreview.html).

---
