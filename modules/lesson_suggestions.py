from discord.ext import commands
from notion_client import Client

# Initialize Notion API client
notion = Client(auth="your_notion_api_key")
DATABASE_ID = "your_notion_database_ID"

def add_lesson_to_notion(lesson_name, username, description):
    """Add a lesson suggestion to Notion."""
    return notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Name": {"title": [{"text": {"content": lesson_name}}]},
            "Username": {"rich_text": [{"text": {"content": username}}]},
            "Description": {"rich_text": [{"text": {"content": description}}]},
        }
    )

class LessonSuggestions(commands.Cog):
    """Cog for lesson suggestions in derbybot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='suggest_lesson')
    async def suggest_lesson(self, ctx, lesson_name: str, description: str):
        """Command to submit a lesson suggestion."""
        try:
            add_lesson_to_notion(lesson_name, ctx.author.name, description)
            await ctx.send(f"Thank you {ctx.author.name}, your lesson suggestion has been submitted!")
        except Exception as e:
            await ctx.send(f"An error occurred while submitting your lesson: {e}")

# Setup function for the cog
def setup(bot):
    bot.add_cog(LessonSuggestions(bot))
