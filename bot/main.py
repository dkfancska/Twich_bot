import twitchio
import random

# Replace with your own values
BOT_USERNAME = 'your_bot_username'
CHANNEL_NAME = 'your_channel_name'
TOKEN = 'your_bot_token'
admin_list = ['admin1', 'admin2']  # list of bot admin usernames

# Set up the bot
bot = twitchio.Client(token=TOKEN, nick=BOT_USERNAME, prefix='!', initial_channels=[CHANNEL_NAME])
channel = CHANNEL_NAME.lower()


# Command to get list of active users in chat
async def get_active_users():
    try:
        users = await bot.get_chatters(channel)
        active_users = users.all
        return active_users
    except:
        return None


# Command to set a cooldown for a function (admin only)
cooldowns = {}


async def set_cooldown(ctx):
    if ctx.author.name in admin_list:
        cooldown_list = ctx.content.split()[1:]
        for cooldown in cooldown_list:
            try:
                function_name, cooldown_time = cooldown.split(':')
                cooldowns[function_name] = int(cooldown_time)
                message = f"Cooldown for '{function_name}' set to {cooldown_time} seconds."
            except:
                message = f"Invalid input: '{cooldown}'. Cooldown format is 'function_name:cooldown_time'."
            await ctx.send(message)
    else:
        message = f"{ctx.author.name}, you don't have permission to use that command."
        await ctx.send(message)


# Command to get a random active user and "kiss" them (admin only)
async def kiss_user(ctx):
    if ctx.author.name in admin_list:
        if ctx.channel.name == channel:
            active_users = await get_active_users()
            if active_users:
                target_user = random.choice(active_users)
                message = f"{ctx.author.name} kissed {target_user}!"
            else:
                message = "No active users in chat."
        else:
            message = f"{ctx.author.name}, you can't use that command here."
    else:
        message = f"{ctx.author.name}, you don't have permission to use that command."
    await ctx.send(message)


# Command to call the "kiss" function with a cooldown
async def kiss_command(ctx):
    if 'kiss' in cooldowns:
        if ctx.author.name in admin_list:
            cooldown_time = cooldowns['kiss']
        else:
            cooldown_time = cooldowns['kiss'] * 2
        if ctx.author.name not in cooldowns or (ctx.message.timestamp - cooldowns[ctx.author.name]) > cooldown_time:
            cooldowns[ctx.author.name] = ctx.message.timestamp
            await kiss_user(ctx)
        else:
            remaining_time = cooldown_time - int(ctx.message.timestamp - cooldowns[ctx.author.name])
            message = f"{ctx.author.name}, please wait {remaining_time} seconds before using this command again."
            await ctx.send(message)
    else:
        await kiss_user(ctx)


# Run the bot
@bot.event
async def event_ready():
    print(f'Logged in as: {bot.nick}')


@bot.command(name='get_active_users')
async def get_active_users_command(ctx):
    active_users = await get_active_users()
    if active_users:
        message = "Active users: " + ', '.join(active_users)
    else:
        message = "No active users in chat."
    await ctx.send(message)


@bot.command(name='set_cooldown')
async def set_cooldown_command(ctx):
    await set_cooldown(ctx)


@bot.command(name='kiss')
async def kiss_command(ctx):
    await kiss_command(ctx)

def main():
    bot.run()
if '__name__' == '__main__':
    main()

