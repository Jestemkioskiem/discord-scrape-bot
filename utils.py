# utils.py
import discord
import pymongo
import config

# Retrieves all messages and returns them as a dict object.
async def get_all_messages(guild):
    messages = []

    # Load the channels from the guild discord.py object.
    channels = guild.channels

    for channel in channels:
        try:
            # Iterate through all messages on the given channel.
            async for message in channel.history(limit=config.MESSAGE_LIMIT):
                # Skip welcome messages, etc.
                if message.content == "":
                    continue

                # Store relevant information in a dict object.
                final_message = {
                    "channel": message.channel.name,
                    "author": message.author.name,
                    "content": message.content
                }
                messages.append(final_message)

        # Error thrown on Title Channels like "Text Channels"
        except AttributeError:
            pass

    return messages


# Storing retrieved messages in a MongoDB database.
def store_messages(messages):

    myclient = pymongo.MongoClient(config.DB_IP)
    mydb = myclient[config.DB_NAME]
    mycol = mydb["Messages"]
    mycol.insert_many(messages)

    print("Finished inserting messages!")
