# Classplus Mock Extractor Bot

Telegram bot to extract Classplus mock tests and generate offline HTML mocks.

## Features

- Login via Organisation Code + credentials or Authorization Token.
- Fetch and list available mock tests.
- Extract mock questions, options, images, and explanations.
- Generate offline HTML mock with timer, navigation, submit, and analysis.
- Upload HTML file to Telegram.
- Auto-delete temporary files.
- Error handling for invalid inputs.
- Deployable on Render/Heroku/Docker.

## Tech Stack

- Python 3
- Pyrogram (Telegram Bot)
- HTTPX (API calls)
- Jinja2 (HTML templating)
- Flask (for deployment on Render)

## Setup

1. Clone repo:

```bash
git clone https://github.com/yourusername/classplus-mock-extractor-bot.git
cd classplus-mock-extractor-bot
