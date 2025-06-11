use tauri::{
  plugin::{Builder, TauriPlugin},
  Manager, Runtime,
};

pub use models::*;

#[cfg(desktop)]
mod desktop;
#[cfg(mobile)]
mod mobile;

mod commands;
mod error;
mod models;

pub use error::{Error, Result};

#[cfg(desktop)]
use desktop::RustyAiSdk;
#[cfg(mobile)]
use mobile::RustyAiSdk;

/// Extensions to [`tauri::App`], [`tauri::AppHandle`] and [`tauri::Window`] to access the rusty-ai-sdk APIs.
pub trait RustyAiSdkExt<R: Runtime> {
  fn rusty_ai_sdk(&self) -> &RustyAiSdk<R>;
}

impl<R: Runtime, T: Manager<R>> crate::RustyAiSdkExt<R> for T {
  fn rusty_ai_sdk(&self) -> &RustyAiSdk<R> {
    self.state::<RustyAiSdk<R>>().inner()
  }
}

/// Initializes the plugin.
pub fn init<R: Runtime>() -> TauriPlugin<R> {
  Builder::new("rusty-ai-sdk")
    .invoke_handler(tauri::generate_handler![commands::ping])
    .setup(|app, api| {
      #[cfg(mobile)]
      let rusty_ai_sdk = mobile::init(app, api)?;
      #[cfg(desktop)]
      let rusty_ai_sdk = desktop::init(app, api)?;
      app.manage(rusty_ai_sdk);
      Ok(())
    })
    .build()
}
