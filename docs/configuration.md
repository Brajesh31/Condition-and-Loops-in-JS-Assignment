# ⚙️ Configuration

## Current configuration
The exercise values are declared directly in each page's JavaScript. The pages do not read environment variables, configuration files, or server settings.

## Browser
A modern browser is sufficient. Use Developer Tools → Console to observe messages.

## Optional local server
From the repository root:
```bash
python -m http.server 8000
```
This serves static files only. It does not add backend behavior.

## Environment file
The root `.env.example` records that there are currently no runtime environment variables. Do not add secret values to this repository.
