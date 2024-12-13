import discord
from notion_client import Client
from discord.ext import commands

# Initialize Notion API client
notion = Client(auth="your_notion_api_key")

# Define your Notion database ID
DATABASE_ID = "your_notion_database_ID"

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True  # To read messages

bot = commands.Bot(command_prefix="!", intents=intents)

# Helper function to add lesson suggestion to Notion
def add_lesson_to_notion(lesson_name, username, description):
    new_page = notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Name": {"title": [{"text": {"content": lesson_name}}]},
            "Username": {"rich_text": [{"text": {"content": username}}]},
            "Description": {"rich_text": [{"text": {"content": description}}]},
        }
    )
    return new_page

# Command to submit lesson suggestions
@bot.command(name='suggest_lesson')
async def suggest_lesson(ctx, lesson_name: str, description: str):
    username = ctx.author.name  # Capture the Discord username
    try:
        # Add lesson to Notion
        add_lesson_to_notion(lesson_name, username, description)
        await ctx.send(f"Thank you {username}, your lesson suggestion has been submitted!")
    except Exception as e:
        await ctx.send(f"An error occurred while submitting your lesson: {e}")

# Run the bot
bot.run("your_discord_api_key")
