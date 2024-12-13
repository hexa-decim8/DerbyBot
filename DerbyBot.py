import discord
from discord.ext import commands

# Initialize derbybot
def create_derbybot():
    intents = discord.Intents.default()
    intents.message_content = True  # To read messages
    return commands.Bot(command_prefix="!", intents=intents)

derbybot = create_derbybot()

# Load extensions (modules)
if __name__ == "__main__":
    derbybot.load_extension("modules.lesson_suggestions")  # Add more extensions as needed
    derbybot.run("your_discord_api_key")
import discord
from discord.ext import commands

# Initialize derbybot
def create_derbybot():
    intents = discord.Intents.default()
    intents.message_content = True  # To read messages
    return commands.Bot(command_prefix="!", intents=intents)

derbybot = create_derbybot()

# Load extensions (modules)
if __name__ == "__main__":
    derbybot.load_extension("modules.lesson_suggestions")  # Add more extensions as needed
    derbybot.run("your_discord_api_key")
