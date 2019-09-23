import discord
import os
import sys


# The BotClient class is a custom class that *extends* the discord.Client class, and
# acts as a client that can send and receive messages under a bot account on Discord.
class BotClient(discord.Client):

    # This method ID represents the message asking users to react to choose their class track
    CLASSTRACK_MESSAGE_ID = 619620774021562380

    # Maps certain reactions (emojis) to certain roles that can be assigned, by name
    CLASSTRACK_REACTIONS_ROLES = {
        "🅰": "Class Track A",
        "🅱": "Class Track B",
        "👦": "H i m ' s t d v e",
        "👧": "H e r ' s t d v e",
        "🤠": "T h e y ' s t d v e"
    }

    # This method is called when the bot is logged in and ready to send messages
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        await super().get_channel(619620234906828830).fetch_message(self.CLASSTRACK_MESSAGE_ID)

    # This method is called whenever a new message is sent in the server
    # The `message` parameter is a discord.Message object with message information.
    async def on_message(self, message: discord.Message):

        # !eval <code> evaluates a python expression and sends the result.
        # Note that this is a fairly unsafe feature to add, and if users attempt to abuse it, it will be removed.
        if message.content.startswith('!eval '):
            try:
                result = eval(message.content[6:])
                await message.channel.send(f"Result: {result}")
            except:
                await message.channel.send(f"Error: {sys.exc_info()[0]}")

    # This method is called whenever a new reaction is created
    async def on_raw_reaction_add(self, event: discord.RawReactionActionEvent):
        await self.handle_raw_reaction(event, True)

    # This method is called whenever a new reaction is removed
    async def on_raw_reaction_remove(self, event: discord.RawReactionActionEvent):
        await self.handle_raw_reaction(event, False)

    # This method is called whenever a reaction is added or removed
    async def handle_raw_reaction(self, event: discord.RawReactionActionEvent, is_add: bool):

        # We need to get some info about the event
        guild: discord.Guild = super().get_guild(event.guild_id)
        member: discord.Member = guild.get_member(event.user_id)
        channel: discord.TextChannel = guild.get_channel(event.channel_id)
        message: discord.Message = await channel.fetch_message(event.message_id)

        # Do class track role enrollment if the reaction is on the enrollment message
        if event.message_id == self.CLASSTRACK_MESSAGE_ID:
            # Make sure the emoji is valid
            if event.emoji.name in self.CLASSTRACK_REACTIONS_ROLES:

                # Add or remove the appropriate role
                if is_add:
                    await member.add_roles(discord.utils.get(guild.roles, name=self.CLASSTRACK_REACTIONS_ROLES[event.emoji.name]))
                else:
                    await member.remove_roles(discord.utils.get(guild.roles, name=self.CLASSTRACK_REACTIONS_ROLES[event.emoji.name]))

            # If this emoji is invalid, remove it!
            else:
                await message.remove_reaction(event.emoji, member)



# The __name__ variable will only be set to '__main__' if we are trying to run this file.
# This makes sure the code in the if statement doesn't run if we `import` this file from another one.
if __name__ == '__main__':
    # Set up an instance of the BotClient and run it
    # The token is a secret code given by Discord that proves the bot is allowed to log in under its account.
    client = BotClient()
    client.run(os.environ['BOT_TOKEN'])
