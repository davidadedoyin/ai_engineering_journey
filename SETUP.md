# Setup guide

## Install Python

1. Download Python from python.org.
2. On Windows, tick "Add Python to PATH".
3. Open a terminal and run:

```bash
python --version
```

## Install VS Code and Python extension

1. Install VS Code.
2. Open the Extensions panel.
3. Install the Python extension.
4. For later data work, also install Jupyter.

## Create the GitHub repo

1. Create a GitHub account.
2. Create a public or private repo named `ai-engineering-journey`.
3. From the terminal in this project:

```bash
git init
git add .
git commit -m "Initialize AI engineering journey"
```

## Local app testing

To launch the FastAPI apps in this repo on localhost, use the included PowerShell helper:

```powershell
cd ai-engineering-journey
.\scripts\run_local_services.ps1
```

This starts the local services and waits for each `/health` endpoint to respond.

You can also stop them with:

```powershell
.\scripts\run_local_services.ps1 -Stop
```

Example health check:

```powershell
Invoke-WebRequest http://127.0.0.1:8000/health
```

Example secure-chat request:

```powershell
curl.exe http://127.0.0.1:8010/chat -H "X-API-Key: demo-secret" -H "Content-Type: application/json" -d '{"message":"hello"}'
```

## Human tasks

- Create the GitHub repo and connect it.
- Create a Kaggle account when the roadmap reaches Titanic.
- Add your Anthropic API key to `.env` later.
