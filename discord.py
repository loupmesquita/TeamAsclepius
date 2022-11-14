import json
import requests

# This script is used to send a message on a discord channel
# by using discord webhook. It is configurable by setting up
# the "discord_webhook" value in conf.json
def send_discord_message(message: str) -> None:
    f = open("conf.json", "r")
    conf = json.load(f)
    data = {}

    data["content"] = message
    data["username"] = "Asclepius"
    r = requests.post(conf["discord_webhook"], json=data)
    print(r.text)


if __name__ == "__main__":
    send_discord_message("Hey")
