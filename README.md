# DerbyBot - A multi-use discord bot for roller derby teams.

This Python script integrates a Discord bot with Notion API to allow users to submit lesson suggestions directly through discord. The bot will capture the name of the lesson, the Discord username of the person submitting it, and a description of the lesson, then store that data in a pre-created Notion database.

## Prereqs
Have the following ready:
- **Python 3.x** installed on your machine.
- **Notion Integration Token** for accessing your Notion database.
- **Notion Database ID** where lesson suggestions will be stored.
- **Discord Bot Token** to run the Discord bot.

## Setup

### Dependencies
Dependencies for this script are minimal, on the system you intend to run the python script on, install the following libraries:

```
pip install discord.py notion-client
```
### Finding your keys

#### 1. **Notion Integration Token**
   - Go to [Notion Developer](https://www.notion.so/my-integrations) and create an integration.
   - After creating your integration, the integration will be prominently displayed in the center of the page after the integration has been created.

#### 2. **Notion Database ID**
   - Open the Notion database where you want to store the lesson suggestions.
   - In the URL, find the database ID (it should look like `https://www.notion.so/yourworkspace/your-database-name-xxxxxxxxxxxxxxxxxxxxxx`).
   - **Copy everything after the last slash**, this is your **Database ID**. It should be a 32 character alphanumeric value.

#### 3. **Discord Bot Token**
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Create a new application, then create a bot within that application.
   - Go to the "Bot" section and copy the **Bot Token**.

## Usage

Once the bot is running, users can submit lesson suggestions in your Discord server using the following command:

```
!suggest <lesson_name> <description>
```
The bot will then store the lesson name, the discord username of the submitter, and the description in your Notion database.

## Example Notion Database Structure

Your Notion database should have the following columns:

- **Name** (Title) - The lesson name.
- **Description** (Text) - The description of the lesson.
