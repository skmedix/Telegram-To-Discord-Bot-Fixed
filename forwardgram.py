from telethon import TelegramClient, events
from telethon.tl.types import InputChannel
import yaml
import discord
import asyncio

message = None

with open('config.yml', 'rb') as f:
    config = yaml.safe_load(f)



"""
TELEGRAM CLIENT STUFF
"""
client = TelegramClient("forwardgram", config["api_id"], config["api_hash"])
client.start()

#Find input telegram channel
for d in client.iter_dialogs():
    if d.name in config["input_channel_name"] or d.entity.id in config["input_channel_id"]:
        input_channel = InputChannel(d.entity.id, d.entity.access_hash)
        break

#TELEGRAM NEW MESSAGE
@client.on(events.NewMessage())
async def handler(event):
    # If the message contains a URL, parse and send Message + URL
    try:
        parsed_response = (event.message.message + '\n' + event.message.entities[0].url )
        parsed_response = ''.join(parsed_response)
    # Or we only send Message    
    except:
        parsed_response = event.message.message

    globals()['message'] = parsed_response



"""
DISCORD CLIENT STUFF
"""
discord_client = discord.Client()

async def background_task():
    global message
    await discord_client.wait_until_ready()
    discord_channel = discord_client.get_channel(config["discord_channel"])
    while True:
        if message:
            await discord_channel.send(message)
            message = None
        await asyncio.sleep(0.1)

discord_client.loop.create_task(background_task())



"""
RUN EVERYTHING ASYNCHRONOUSLY
"""

print("Listening now")
asyncio.run( discord_client.run(config["discord_bot_token"]) )
asyncio.run( client.run_until_disconnected() )