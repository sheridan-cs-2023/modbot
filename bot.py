import discord


# The BotClient class is a custom class that *extends* the discord.Client class, and
# acts as a client that can send and receive messages under a bot account on Discord.
class BotClient(discord.Client):
    # This method is called when the bot is logged in and ready to send messages
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    # This method is called whenever a new message is sent in the server
    # The `message` parameter is a discord.Message object with message information.
    async def on_message(self, message: discord.Message):
        print(f'Message from {message.author}: {message.content}')


# The __name__ variable will only be set to '__main__' if we are trying to run this file.
# This makes sure the code in the if statement doesn't run if we `import` this file from another one.
if __name__ == '__main__':
    # Set up an instance of the BotClient and run it
    # The token is a secret code given by Discord that proves the bot is allowed to log in under its account.
    client = BotClient()
    client.run('TODO: Token!')
