
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


## Running the Bot
* Install the required dependencies by running pip install -r requirements.txt in your terminal.
* Run the bot by running python my_bot.py in your terminal.
* Visit your Twitch channel and type !hello in the chat to test the bot. The bot should respond with "Hello, [your username]!".


## Usage


### Cooldown Feature

This bot also includes a cooldown feature to prevent users from spamming certain commands. By default, the cooldown time for each command is set to 30 seconds.


#### The bot has the following commands:
```css
!get_active_users: Returns a list of active users in the chat.

!set_cooldown function_name:cooldown_time ...: Sets a cooldown time (in seconds) for a bot function. 
The format for adding multiple functions and cooldown times is function_name:cooldown_time function_name2:cooldown_time2 ....                                  
                                  
!kiss: Sends a kiss to a random active user in the chat.
```



Note: the !kiss command has a cooldown time that can be set using !set_cooldown.