import os
import requests
import discord
from discord import Intents

from dotenv import load_dotenv
load_dotenv()

WEBSITE_STATE_FILENAME = "website_state.txt"

# Function to check if website is available
def check_website(url):
    """
    A fsunction that checks the availability of a website by sending a GET request to the provided URL.

    Parameters:
        url (str): The URL of the website to check.

    Returns:
        bool: True if the website is available (status code 200), False otherwise.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

# Function to send message to Discord server
async def send_discord_message(token, channel_id, message):
    """
    Sends a message to a Discord channel using the provided token, channel ID, and message.

    Parameters:
        token (str): The token used to authenticate with the Discord API.
        channel_id (int): The ID of the Discord channel to send the message to.
        message (str): The content of the message to send.

    Returns:
        None

    Raises:
        None
    """
    intents = Intents.default()
    intents.messages = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        channel = client.get_channel(channel_id)
        if channel:
            await channel.send(message)
        else:
            print("Failed to find channel with ID:", channel_id)
        await client.close()

    await client.start(token)

# Function to read previous state from file
def read_previous_state():
    try:
        with open(WEBSITE_STATE_FILENAME, "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        with open(WEBSITE_STATE_FILENAME, "w") as file:
            file.write("")
        return None

# Function to write current state to file
def write_current_state(current_state):
    with open(WEBSITE_STATE_FILENAME, "w") as file:
        file.write(current_state)

# Main function
async def main():
    website_url = os.getenv('WEBSITE_URL')
    discord_token = os.getenv('DISCORD_TOKEN')
    discord_channel_id = int(os.getenv('DISCORD_CHANNEL_ID'))
    offline_message = f"The website {website_url} is currently offline!"
    online_message = f"The website {website_url} is now online."

    current_state = "online" if check_website(website_url) else "offline"
    previous_state = read_previous_state()

    # Check if state has changed
    if current_state != previous_state:
        if current_state == "offline":
            await send_discord_message(discord_token, discord_channel_id, offline_message)
            print("Sent offline message to Discord server")
        else:
            await send_discord_message(discord_token, discord_channel_id, online_message)
            print("Sent online message to Discord server")
        
        write_current_state(current_state)

# Run the main function
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())