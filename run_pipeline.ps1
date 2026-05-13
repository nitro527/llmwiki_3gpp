param(
    [string]$Phase = "all",
    [string]$Backend = "gemini"
)

$SleepTimeout = 30
$MonitorTimeout = 15

powercfg /change standby-timeout-ac 0 | Out-Null
powercfg /change monitor-timeout-ac 0 | Out-Null
Write-Host "절전 모드 비활성화"

try {
    py wiki_builder/orchestrate.py --phase $Phase --backend $Backend
} finally {
    powercfg /change standby-timeout-ac $SleepTimeout | Out-Null
    powercfg /change monitor-timeout-ac $MonitorTimeout | Out-Null
    Write-Host "절전 모드 복원 완료"
}
