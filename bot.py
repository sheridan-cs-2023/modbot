import os
from core.bot_client import BotClient
# We need to import each module (feature) from the mods folder
from mods import evil, moo, reactroles, trumpet

# The __name__ variable will only be set to '__main__' if we are trying to run this file.
# This makes sure the code in the if statement doesn't run if we `import` this file from another one.
if __name__ == '__main__':
    # Set up an instance of the BotClient and run it
    # The token is a secret code given by Discord that proves the bot is allowed to log in under its account.
    client = BotClient([
        # We need to do this for each module (feature) we want activated
        evil.EvalModule(),
        moo.MooModule(),
        reactroles.ReactRolesModule(),
        trumpet.TrumpetModule(),
    ])
    client.run(os.environ['BOT_TOKEN'])
