param([string]$Mode)

if ($Mode -eq "off") {
    powercfg /change standby-timeout-ac 0 | Out-Null
    powercfg /change monitor-timeout-ac 0 | Out-Null
    Write-Host "절전 모드 비활성화"
} elseif ($Mode -eq "on") {
    powercfg /change standby-timeout-ac 30 | Out-Null
    powercfg /change monitor-timeout-ac 15 | Out-Null
    Write-Host "절전 모드 활성화"
} else {
    Write-Host "사용법: .\sleep.ps1 on  또는  .\sleep.ps1 off"
}
