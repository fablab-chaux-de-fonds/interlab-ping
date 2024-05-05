import os
import requests

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
def send_discord_webhook(webhook_url, message):
    """
    Sends a message to a Discord webhook.

    Parameters:
        webhook_url (str): The URL of the Discord webhook.
        message (str): The content of the message to send.

    Returns:
        bool: True if the message was sent successfully, False otherwise.
    """
    try:
        response = requests.post(webhook_url, json={"content": message})
        if response.status_code == 204:
            print("Message sent successfully!")
            return True
        else:
            print("Failed to send message:", response.text)
            return False
    except Exception as e:
        print("An error occurred:", e)
        return False

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
def main():
    """
    The main function of the program.

    This function checks the availability of a website and sends a notification to a Discord channel if the website status changes.

    Parameters:
        None

    Returns:
        None

    Side Effects:
        - Sends a notification message to a Discord channel if the website status changes.
        - Writes the current state of the website to a file.

    Environment Variables:
        - WEBSITE_URL: The URL of the website to monitor.
        - DISCORD_WEBHOOK: The webhook URL for the Discord channel where notifications will be sent.

    File I/O:
        - Reads the previous state of the website from a file.
        - Writes the current state of the website to a file.

    Exceptions:
        - FileNotFoundError: If the file containing the previous state does not exist.
    """
    website_url = os.getenv('WEBSITE_URL')
    discord_webhook = os.getenv('DISCORD_WEBHOOK')
    offline_message = f"The website {website_url} is currently offline!"
    online_message = f"The website {website_url} is now online."

    current_state = "online" if check_website(website_url) else "offline"
    previous_state = read_previous_state()

    # Check if state has changed
    if current_state != previous_state:
        if current_state == "offline":
            send_discord_webhook(discord_webhook, offline_message)
            print("Sent offline message to Discord server")
        else:
            send_discord_webhook(discord_webhook, online_message)
            print("Sent online message to Discord server")
        
        write_current_state(current_state)

# Run the main function
if __name__ == "__main__":
    main()