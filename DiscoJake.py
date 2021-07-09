import discord
from urllib.request import Request, urlopen
import random
import os
import json

TOKEN = "ENTER TOKEN HERE"
keyword = "jake"
  
client = discord.Client()
embed = discord.Embed()

#file dir
jake_quotes_path = os.path.join(os.path.dirname(__file__), f'jakequotes.json')



@client.event
async def on_ready():
  print("Bot is ready to party, logged in as {0.user}.".format(client))
 
@client.event
async def on_message(message):
  global keyword
  if message.author == client.user:
    return
  elif keyword.lower() in message.content.lower():
    try:
      with open(jake_quotes_path, "r") as jake_quotes_file:
        jake_quotes_read = json.load(jake_quotes_file)
    except:
        print(f"jakequotes.json cannot be found, make sure it is in main directory with DiscoJake.py")
    image_num = random.randint(1,5)
    quote_num = random.randint(1,(int(list(jake_quotes_read.keys())[-1])))
    for x in list(jake_quotes_read.keys()):
      if int(x) == quote_num:
        jake_quote = jake_quotes_read[x].strip()
    if image_num == 1:
          embed.set_image(url="https://i.imgur.com/BkTYpZi.gif")
    elif image_num == 2:
          embed.set_image(url="https://i.imgur.com/nWEFAga.gif")
    elif image_num == 3:
          embed.set_image(url="https://i.imgur.com/uhyP2rH.gif")
    elif image_num == 4:
          embed.set_image(url="https://i.imgur.com/sZrgTyE.gif")
    elif image_num == 5:
          embed.set_image(url="https://i.imgur.com/mEXOHp7.gif")
    await message.channel.send(embed=embed) 
    await message.channel.send(f'"{jake_quote}" - Jake the Dog')
  elif message.content.startswith("!set keyword"):
    keyword = message.content.strip()[13:]
    await message.channel.send(f"You can now call jake with '{keyword}'.")
  elif message.content.startswith("!add quote"):
    with open(jake_quotes_path, "r") as jake_quotes_file:
      jake_quotes_read = json.load(jake_quotes_file)
      jake_quotes_newind = int(list(jake_quotes_read.keys())[-1])
    jake_quotes_read[jake_quotes_newind + 1] = message.content[10:].strip()
    await message.channel.send(f"'{message.content[10:].strip()}' has been added under dict id: {jake_quotes_newind + 1}.")
    with open(jake_quotes_path, "w") as jake_quotes_file_w:
      json.dump(jake_quotes_read, jake_quotes_file_w)
  else:
    return

client.run(TOKEN)