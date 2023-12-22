$exclude = @("venv", "dio-automation-bot.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "dio-automation-bot.zip" -Force