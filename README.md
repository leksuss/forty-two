Forty-two is a Telegram bot that allows you to create your own ChatGPT in Telegram.

## Features

- Easy to use and deploy. You just need to set the Telegram and OpenAI API keys and run the bot.
- GPT Vision. You can send images to the bot and ask questions about them.
- Track your conversation history with GPT.
- Limit users who can interact with the bot.
- Fully asynchronous.
- MIT License.

## Setup

### 1. Create a .env file with the following content:

```
TELEGRAM_TOKEN=your_telegram_api_key
OPENAI_API_KEY=your_openai_api_key
```

### 2. Run the bot

With docker-compose:

```bash
docker-compose up -d
```

Run without Docker: 

```bash
pip install -r requirements.txt
alembic upgrade head
python main.py
```

## Settings

| Variable              | Description                                                                                                                                                                             | Default Value                                   |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| TELEGRAM_TOKEN        | Telegram API key.                                                                                                                                                                       | -                                               |
| OPENAI_API_KEY        | OpenAI API key.                                                                                                                                                                         | -                                               |
| DB_STRING             | Database connection string.                                                                                                                                                             | sqlite+aiosqlite:///db.sqlite3                  |
| MAX_COMPLETION_TOKENS | Maximum tokens for completion.                                                                                                                                                          | 4096                                            |
| MAX_TOTAL_TOKENS      | Maximum tokens for total output. If OpenAI uses more than this amount, the bot will summarize user input.                                                                               | 10000                                           |
| SYSTEM_PROMPT         | System prompt for GPT.                                                                                                                                                                  | You are a friendly assistant, your name is Rick |
| OPENAI_MODEL          | OpenAI model.                                                                                                                                                                           | gpt-4o                                          |
| ALLOWED_USERS         | Comma-separated list of Telegram users who can interact with the bot. You can use both Telegram IDs or Usernames. If None, everyone can interact with the bot. Example: durov,238373289 | None                                            |

## In development

- DALL-E generation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Made with love in Barcelona