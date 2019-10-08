# ModBot

ModBot is a Discord bot programmed in python for the Sheridan CS Class of 2023 Discord server.

Any member of the server is welcome to message me on Discord to request membership to the
[CS 2023 GitHub Organization](https://github.com/sheridan-cs-2023/), which will allow them to
contribute code!

This server, which starts off in `bot.py`, is designed to be easy for newcomers to programming,
with plenty of explanatory comments.

[Docker Image](https://hub.docker.com/r/mctague/modbot) (Used for deployments)

## Making a Feature

To add a feature, make a python file in the `mods` folder. In this file, import the
`core.bot_module` module and make a class that subclasses BotModule, like so:

```python
from core.bot_module import *


class ExampleModule(BotModule):
    """An explanation of what the module does."""
    pass
```

Within this class, you can implement various methods in order to handle certain types of events.
See `core/bot_module.py` for all possible events.

Here's an example of a module that responds to "!ping" with "Pong!":


```python
from core.bot_module import *


class PingModule(BotModule):
    """An explanation of what the module does."""
    async def on_message(self, message):
        if message.content.startswith("!ping"):
            await message.channel.send("Pong!")
```

After developing your module, edit `bot.py`, the main source file of the bot.
You'll see an import statement like this, with a list of modules:

```python
from mods import aaa, bbb, ccc
```

Add your module's name (NOT the class name!) to the list!
Further down, you'll see something like this:

```python
client = BotClient([
    aaa.AAAModule(),
    bbb.BBBModule(),
    ccc.CCCModule(),
])
```

Add your module's class to the list, and that's it! Your module is good to go!
