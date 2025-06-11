use serde::de::DeserializeOwned;
use tauri::{plugin::PluginApi, AppHandle, Runtime};

use crate::models::*;

pub fn init<R: Runtime, C: DeserializeOwned>(
  app: &AppHandle<R>,
  _api: PluginApi<R, C>,
) -> crate::Result<RustyAiSdk<R>> {
  Ok(RustyAiSdk(app.clone()))
}

/// Access to the rusty-ai-sdk APIs.
pub struct RustyAiSdk<R: Runtime>(AppHandle<R>);

impl<R: Runtime> RustyAiSdk<R> {
  pub fn ping(&self, payload: PingRequest) -> crate::Result<PingResponse> {
    Ok(PingResponse {
      value: payload.value,
    })
  }
}
