import re
from core.bot_module import *
from util.chain import Chain


class TrumpetModule(BotModule):
    """Trump markov chain. Responds to `!trumpet` with a trump speech generated from 'trump-nonsense.txt'"""

    def __init__(self):
        super()
        self._chain = Chain()

        # Load the source file
        with open("data/trump-nonsense.txt") as speeches:
            file = speeches.read()
            # Each speech is separated by "SPEECH <n>", so we split it and take out the number
            parts = file.split("SPEECH ")
            parts = [part[1:].strip() for part in parts]

            # Split each part into tokens (words or punctuation) and feed them to the markov chain
            for part in parts:
                loc = re.findall(r"[\w']+|[.,!?;]", part)
                self._chain.add(loc)

    async def on_message(self, message):
        if message.content.startswith("!trumpet"):
            result = ' '.join(self._chain.generate(max_len=500))
            await message.channel.send(result)

