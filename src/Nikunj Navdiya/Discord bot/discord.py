import discord  # needed for building bot
import os  # for getting the bot token from .env
import re  # for reading particular messages
import google.generativeai as palm

palm.configure(api_key=os.environ['API_KEY'])        # Palm API
TOKEN = os.getenv('TOKEN')                         # Discord bot application token

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

response = ""


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):

  if message.author == client.user:
    return
  if client.user.mentioned_in(message):
    # response = palm.generate_text(prompt=str(message.content))
    # if(len(str(response.result))>2000):
    #   await message.channel.send(str(response.result)[0:1900]+"\nFor more reference do google yourself 🤣")
    # else:
    #   await message.channel.send(response.result)
    global response
    if (response == ""):
      print("If")
      response = palm.chat(messages=[str(message.content)])
      if (len(str(response.last)) > 1900):
        await message.channel.send(
            str(response.last)[0:1900] +
            "\nFor more reference do google yourself 🤣")
      else:
        await message.channel.send(response.last)
    else:
      print("Else")
      response.reply(str(message.content))
      response = palm.chat(messages=[str(message.content)])
      if (len(str(response.last)) > 1900):
        await message.channel.send(
            str(response.last)[0:1900] +
            "\nFor more reference do google yourself 🤣")
      else:
        await message.channel.send(response.last)


client.run(TOKEN)
