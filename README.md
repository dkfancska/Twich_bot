
# My Twitch Bot

This is a Python Twitch bot that responds to user requests in chat. To use this bot, you'll need to obtain a Twitch API token.

## Getting a Twitch API Token

1. Go to the [Twitch Developer Console](https://dev.twitch.tv/console/apps/create) and create a new application.
2. Enter a name for your application and select "Chat Bot" as the category.
3. Enter `http://localhost` as the "OAuth Redirect URLs" (this can be changed later).
4. Click "Create" to create your application.
5. On the next screen, copy the "Client ID" and store it somewhere safe.
6. Click the "New Secret" button to generate a new client secret. Copy the client secret and store it somewhere safe.
7. In the `my_bot.py` file, replace the `TOKEN` variable with your Twitch API token (i.e. the client secret). 

## Cooldown Feature

This bot also includes a cooldown feature to prevent users from spamming certain commands. By default, the cooldown time for each command is set to 30 seconds.

### Setting Cooldowns

Only bot admins are able to set cooldowns for specific users. To add a new admin to the bot, simply add their username to the `BOT_ADMINS` list in the `my_bot.py` file.

To set a cooldown for a specific user on a specific command, use the `set_cooldown` function in the `my_bot.py` file. For example:

```python
set_cooldown('!hello', 'user123', 60)
```
This sets a cooldown of 60 seconds for the user with the username "user123" on the "!hello" command.

### Checking Cooldowns
The get_cooldown function can be used to check the remaining cooldown time for a specific user on a specific command. For example:

```python
remaining_time = get_cooldown('!hello', 'user123')
if remaining_time > 0:
    print(f"{remaining_time} seconds remaining until the cooldown expires.")
else:
    print("The cooldown has expired.")
This prints the remaining time (in seconds) until the cooldown for user "user123" on the "!hello" command expires.
```
### Note
Please note that the cooldown feature only works if the bot is running continuously. If the bot is restarted or shut down, the cooldowns will be reset.

## Running the Bot
* Install the required dependencies by running pip install -r requirements.txt in your terminal.
* Run the bot by running python my_bot.py in your terminal.
* Visit your Twitch channel and type !hello in the chat to test the bot. The bot should respond with "Hello, [your username]!".
