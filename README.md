# interlab-ping - Website Availability Checker with Discord Notification

This Python script checks the availability of a website and sends a notification to a Discord channel if the website status changes.

## Features

- Checks the availability of a website by sending a GET request.
- Sends a notification message to a Discord channel using a bot.
- Maintains the previous state of the website to detect changes.

## Usage

1. Install the required Python packages by running:
    ```bash
    pip install -r requirements.txt
    ```

2. Rename `.env_example` to `.env` and set up environment variables:
    - `WEBSITE_URL`: The URL of the website to monitor.
    - `DISCORD_TOKEN`: The token for your Discord bot.
    - `DISCORD_CHANNEL_ID`: The ID of the Discord channel where notifications will be sent.

3. Run the script:
    ```bash
    python app.py
    ```

## Requirements

- Python 3.x
- `discord.py` library
- `requests` library
- `dotenv` library

## Configuration

- Ensure you have a valid Discord bot token and channel ID.
- Make sure the `WEBSITE_URL` environment variable is set to the website you want to monitor.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.