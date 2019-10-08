from core.bot_module import *


class ReactRolesModule(BotModule):
    """Handles reactions on a specific message and assigns the matching role."""

    # This method ID represents the message asking users to react
    REACT_MESSAGE_ID = 619620774021562380

    # Maps certain reactions (emojis) to certain roles that can be assigned, by name
    REACT_REACTIONS_ROLES = {
        "🅰": "Class Track A",
        "🅱": "Class Track B",
        "👦": "H i m ' s t d v e",
        "👧": "H e r ' s t d v e",
        "🤠": "T h e y ' s t d v e"
    }

    async def on_ready(self):
        # Make sure the class track message is in the cache
        await self.client.get_channel(619620234906828830).fetch_message(self.REACT_MESSAGE_ID)

    async def on_reaction(self, event: discord.RawReactionActionEvent, is_add: bool):
        # We need to get some info about the event
        guild: discord.Guild = self.client.get_guild(event.guild_id)
        member: discord.Member = guild.get_member(event.user_id)
        channel: discord.TextChannel = guild.get_channel(event.channel_id)
        message: discord.Message = await channel.fetch_message(event.message_id)

        # Assign roles if the reaction is on the right message
        if event.message_id == self.REACT_MESSAGE_ID:
            # Make sure the emoji is valid
            if event.emoji.name in self.REACT_REACTIONS_ROLES:

                # Add or remove the appropriate role
                if is_add:
                    await member.add_roles(
                        discord.utils.get(guild.roles, name=self.REACT_REACTIONS_ROLES[event.emoji.name]))
                else:
                    await member.remove_roles(
                        discord.utils.get(guild.roles, name=self.REACT_REACTIONS_ROLES[event.emoji.name]))

            # If this emoji is invalid, remove it!
            else:
                await message.remove_reaction(event.emoji, member)
