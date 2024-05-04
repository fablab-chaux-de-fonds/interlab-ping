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

## CRON
To set up a cron job that runs every 5 minutes between 7:00 AM and 11:59 PM (23:59), you can use the following cron expression:

```bash
*/5 6-1 * * * <python> <app.py>
```

Here's what each part of the cron expression means:

    */5: Run every 5 minutes.
    6-1: Run between the hours of 7 (7:00 AM) and 23 (11:00 PM).
    * * *: Run on every day of the month, every month, and every day of the week.
    <python> <app.py>: Path to your Python interpreter followed by the path to your Python script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.