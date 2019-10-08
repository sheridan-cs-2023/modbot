from cowpy import cow
from core.bot_module import *


class MooModule(BotModule):
    """Handles cowsay (!moo) commands."""

    async def on_message(self, message):
        if message.content.startswith("!moo "):
            thing = cow.Cower()
            await message.channel.send(f"```\n{thing.milk(message.content[5:])}\n```")
