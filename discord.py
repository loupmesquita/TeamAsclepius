import json
import requests

# This script is used to send a message on a discord channel
# by using discord webhook. It is configurable by setting up
# the "discord_webhook" value in conf.json


# Sends a notification to the webhook
def send_discord_message(message: str) -> None:
    f = open("conf.json", "r")
    conf = json.load(f)
    data = {}

    data["content"] = message
    data["username"] = "Asclepius"
    r = requests.post(conf["discord_webhook"], json=data)
    print(r.text)


# Sends a notification only once to the webhook
def send_discord_message_once(message: str) -> None:
    global notification_sent
    if notification_sent is False:
        notification_sent = True
        send_discord_message(message)


notification_sent = False


if __name__ == "__main__":
    send_discord_message("Hey")
