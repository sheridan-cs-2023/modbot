import discord


class BotModule:
    """A parent class for every bot module! Extend this to create a bot module!"""

    async def on_ready(self):
        pass

    async def on_ready(self):
        pass

    async def on_message(self, message: discord.Message):
        pass

    async def on_reaction(self, event: discord.RawReactionActionEvent, is_add: bool):
        pass
