$ErrorActionPreference = "Stop"
$Repo = "C:\AI\Git\CNA_Recertification_Theory_Clinical_Support"
$Runner = Join-Path $Repo "Module_Dry_Run\_module13_dryrun_outputs\audio\run_qwen_tts_resume_until_done.ps1"
$LogDir = Join-Path $Repo "Module_Dry_Run\_module13_dryrun_outputs\audio\logs"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
$StdOut = Join-Path $LogDir "qwen_tts_background.stdout.log"
$StdErr = Join-Path $LogDir "qwen_tts_background.stderr.log"

$p = Start-Process -FilePath "powershell.exe" `
  -ArgumentList @("-NoProfile", "-ExecutionPolicy", "Bypass", "-File", $Runner, "-MaxAttempts", "12", "-RestartDelaySeconds", "30") `
  -WorkingDirectory $Repo `
  -RedirectStandardOutput $StdOut `
  -RedirectStandardError $StdErr `
  -WindowStyle Hidden `
  -PassThru

"Started Qwen TTS background resume runner. PID=$($p.Id)"
"Stdout: $StdOut"
"Stderr: $StdErr"
