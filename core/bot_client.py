import discord


# The BotClient class is a custom class that *extends* the discord.Client class, and
# acts as a client that can send and receive messages under a bot account on Discord.
class BotClient(discord.Client):
    """Provides the discord bot client behavior"""

    def __init__(self, modules, **options):
        super().__init__(**options)
        self._modules = modules

        for module in self._modules:
            module.client = self

    # This method is called when the bot is logged in and ready to send messages
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        for module in self._modules:
            await module.on_ready()

    # This method is called whenever a new message is sent in the server
    # The `message` parameter is a discord.Message object with message information.
    async def on_message(self, message: discord.Message):
        for module in self._modules:
            await module.on_message(message)

    # This method is called whenever a new reaction is created
    async def on_raw_reaction_add(self, event: discord.RawReactionActionEvent):
        await self.handle_raw_reaction(event, True)

    # This method is called whenever a new reaction is removed
    async def on_raw_reaction_remove(self, event: discord.RawReactionActionEvent):
        await self.handle_raw_reaction(event, False)

    # This method is called whenever a reaction is added or removed
    async def handle_raw_reaction(self, event: discord.RawReactionActionEvent, is_add: bool):
        for module in self._modules:
            await module.on_reaction(event, is_add)
