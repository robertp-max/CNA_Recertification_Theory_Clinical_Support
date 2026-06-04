param(
  [int]$MaxAttempts = 12,
  [int]$RestartDelaySeconds = 30
)

$ErrorActionPreference = "Continue"
$Repo = "C:\AI\Git\CNA_Recertification_Theory_Clinical_Support"
$Python = "C:\AI\qwen3-tts-env\Scripts\python.exe"
$Script = Join-Path $Repo "Module_Dry_Run\_module13_dryrun_outputs\audio\qwen_tts_batch_generate.py"
$Manifest = Join-Path $Repo "Module_Dry_Run\_module13_dryrun_outputs\audio\audio_manifest.json"
$LogDir = Join-Path $Repo "Module_Dry_Run\_module13_dryrun_outputs\audio\logs"
$RunLog = Join-Path $LogDir "qwen_tts_resume_runner.log"

New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"
Set-Location $Repo

function Read-ManifestStatus {
  if (-not (Test-Path $Manifest)) {
    return [pscustomobject]@{ status = "manifest_missing"; generated_count = 0; failed_count = 0 }
  }
  try {
    $m = Get-Content $Manifest -Raw -Encoding UTF8 | ConvertFrom-Json
    return [pscustomobject]@{
      status = [string]$m.status
      generated_count = [int]($m.generated_count ?? 0)
      failed_count = [int]($m.failed_count ?? 0)
    }
  } catch {
    return [pscustomobject]@{ status = "manifest_read_error: $($_.Exception.Message)"; generated_count = 0; failed_count = 0 }
  }
}

"[$(Get-Date -Format s)] Qwen TTS resume runner start. MaxAttempts=$MaxAttempts RestartDelaySeconds=$RestartDelaySeconds" | Add-Content -Path $RunLog -Encoding UTF8

for ($attempt = 1; $attempt -le $MaxAttempts; $attempt++) {
  $before = Read-ManifestStatus
  "[$(Get-Date -Format s)] Attempt $attempt starting. Before status=$($before.status) generated=$($before.generated_count) failed=$($before.failed_count)" | Add-Content -Path $RunLog -Encoding UTF8

  & $Python $Script 2>&1 | Tee-Object -FilePath $RunLog -Append
  $exitCode = $LASTEXITCODE

  $after = Read-ManifestStatus
  "[$(Get-Date -Format s)] Attempt $attempt finished. PythonExit=$exitCode After status=$($after.status) generated=$($after.generated_count) failed=$($after.failed_count)" | Add-Content -Path $RunLog -Encoding UTF8

  if ($after.status -eq "qwen_tts_generated") {
    "[$(Get-Date -Format s)] DONE: all Qwen TTS clips generated." | Add-Content -Path $RunLog -Encoding UTF8
    exit 0
  }

  if ($attempt -lt $MaxAttempts) {
    "[$(Get-Date -Format s)] Not complete yet; sleeping $RestartDelaySeconds seconds before restart. Completed WAVs will be skipped on next attempt." | Add-Content -Path $RunLog -Encoding UTF8
    Start-Sleep -Seconds $RestartDelaySeconds
  }
}

$final = Read-ManifestStatus
"[$(Get-Date -Format s)] STOP: max attempts reached. Final status=$($final.status) generated=$($final.generated_count) failed=$($final.failed_count)" | Add-Content -Path $RunLog -Encoding UTF8
exit 1
