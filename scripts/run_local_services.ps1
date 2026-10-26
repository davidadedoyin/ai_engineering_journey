param(
    [switch]$Stop
)

$repoRoot = Split-Path -Parent $PSScriptRoot
$venvPython = Join-Path $repoRoot ".venv\Scripts\python.exe"

$appList = @(
    @{ Name = "Titanic API"; Module = "projects.month3_titanic_api.app"; Port = 8000 },
    @{ Name = "Sentiment API"; Module = "projects.month4_sentiment_api.app"; Port = 8002 },
    @{ Name = "Smart Reply Assistant"; Module = "projects.month5_smart_reply_assistant.app"; Port = 8003 },
    @{ Name = "FAQ Bot"; Module = "projects.month6_rag_faq_bot.app"; Port = 8004 },
    @{ Name = "LLM Assistant"; Module = "projects.month7_llm_assistant.app"; Port = 8005 },
    @{ Name = "Agent Tool Use"; Module = "projects.month8_agent_tool_use.app"; Port = 8006 },
    @{ Name = "Memory Planner"; Module = "projects.month9_memory_planner.app"; Port = 8007 },
    @{ Name = "Final Chat App"; Module = "projects.month10_final_chat_app.app"; Port = 8008 },
    @{ Name = "Deployment Service"; Module = "projects.month11_deployment_ready_service.app"; Port = 8009 },
    @{ Name = "Secure Chat"; Module = "projects.month12_secure_chat.app"; Port = 8010 },
    @{ Name = "Flagship Assistant"; Module = "flagship_chat_assistant.app"; Port = 8011 }
)

function Test-Health {
    param(
        [string]$Url
    )

    try {
        $response = Invoke-WebRequest -Uri $Url -Method Get -UseBasicParsing -TimeoutSec 5
        return ($response.StatusCode -eq 200)
    }
    catch {
        return $false
    }
}

if ($Stop) {
    foreach ($app in $appList) {
        $pid = Get-CimInstance Win32_Process |
            Where-Object { $_.CommandLine -match "uvicorn.*$($app.Module):app.*--port $($app.Port)" } |
            Select-Object -ExpandProperty ProcessId -First 1

        if ($pid) {
            Stop-Process -Id $pid -Force
            Write-Host "Stopped $($app.Name) (PID $pid)"
        }
    }
    return
}

if (-not (Test-Path $venvPython)) {
    throw "Python venv not found at $venvPython. Run 'python -m venv .venv' first."
}

foreach ($app in $appList) {
    $args = @(
        '-m', 'uvicorn', "$($app.Module):app", '--host', '127.0.0.1', '--port', [string]$app.Port
    )

    $process = Start-Process -FilePath $venvPython -ArgumentList $args -WorkingDirectory $repoRoot -PassThru -WindowStyle Hidden
    Write-Host "Started $($app.Name) on http://127.0.0.1:$($app.Port)/health (PID $($process.Id))"
}

foreach ($app in $appList) {
    $healthUrl = "http://127.0.0.1:$($app.Port)/health"
    $deadline = (Get-Date).AddSeconds(20)
    $ready = $false

    while ((Get-Date) -lt $deadline) {
        if (Test-Health -Url $healthUrl) {
            $ready = $true
            break
        }
        Start-Sleep -Seconds 1
    }

    if ($ready) {
        Write-Host "OK: $($app.Name) is healthy at $healthUrl"
    }
    else {
        Write-Warning "$($app.Name) did not respond at $healthUrl within 20 seconds."
    }
}

Write-Host ""
Write-Host "Quick examples:"
Write-Host "  Invoke-WebRequest http://127.0.0.1:8000/health"
Write-Host "  curl.exe http://127.0.0.1:8010/chat -H \"X-API-Key: demo-secret\" -H \"Content-Type: application/json\" -d '{\"message\":\"hello\"}'"
Write-Host ""
Write-Host "To stop them later: .\scripts\run_local_services.ps1 -Stop"
