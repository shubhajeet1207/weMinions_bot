import discord
import os
import requests
import json

client = discord.Client()

def get_news():
  response = requests.get\
  ("https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=adb3aa9959564110862634aa0b8ae6ba")
  json_data = json.loads(response.text)
  news = json_data[0]['content']
  return(news)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$news'):
      news = get_news()
      await message.channel.send(news)


client.run(os.getenv('TOKEN'))
