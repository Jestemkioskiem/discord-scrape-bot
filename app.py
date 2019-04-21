#app.py
import discord
import utils, config

client = discord.Client()

@client.event
async def on_ready():
  # Retrieve the server based on provided ID
  guild = client.get_guild(config.SERVER_ID)
  if guild == None:
    raise Exception("Incorrect ID")

  # Run all of the scraping & database functions.
  messages = await utils.get_all_messages(guild)
  utils.store_messages(messages)

  # Quit the script.
  await client.logout()

client.run(config.AUTH_TOKEN, bot=config.AUTH_BOOL)