#app.py
import discord, asyncio

client = discord.Client()


async def get_all_messages():
	messages = []

	guild = client.guilds[0]
	channels = guild.channels

	for channel in channels:
		try:
			async for message in channel.history(limit=10000):
				if message.content == "":
					continue

				final_message = {
					"channel" : message.channel.name,
					"author" : message.author.name,
					"content" : message.content
				}

				messages.append(final_message)
		except AttributeError:
			pass

	return messages


@client.event
async def on_ready():
	print(await get_all_messages())


AUTH = ""

client.run(AUTH, bot=True)