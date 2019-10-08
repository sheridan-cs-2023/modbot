import inspect
import sys
from core.bot_module import *


class EvalModule(BotModule):
    """Handles !eval commands."""

    async def on_message(self, message):
        if message.content.startswith('!eval '):
            try:
                result = eval(message.content[6:])
                if inspect.isawaitable(result):
                    result = await result
                await message.channel.send(f"Result: {result}")
            except:
                await message.channel.send(f"Error: {sys.exc_info()[0]}")
