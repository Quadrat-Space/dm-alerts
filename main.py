import disnake
from disnake.ext import commands
import os
import shutil
import random
from ratelimit import limits, RateLimitException
import tqdm
import asyncio
from datetime import datetime, timedelta
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

intents = disnake.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=config["prefix"], intents=intents)

def is_allowed(ctx):
    return ctx.author.id == config["allowed_user_id"]

def create_users_file(guild_id):
    with open(f'users_{guild_id}.txt', 'w', encoding='utf-8') as file:
        file.write('')

@limits(calls=config["message_limit"], period=60)
@bot.slash_command()
@commands.check(is_allowed)
async def send_everyone(ctx, message: str, guild_id: str = None):
    if guild_id is None:
        guild_id = config["default_guild_id"]

    guild = bot.get_guild(int(guild_id))

    if guild is None:
        await ctx.send("The server with the specified ID was not found.")
        return

    create_users_file(guild.id)

    async def gather_users():
        with open(f'users_{guild.id}.txt', 'a', encoding='utf-8') as file:
            for member in tqdm.tqdm(guild.members, desc='Gathering users'):
                file.write(f'{member.display_name} | {member.id}\n')

    success = []
    no_success = []

    async def send_message(user_name, user_id):
        try:
            user = await guild.fetch_member(user_id)
            await user.send(f'{message}\nThis bot is created by the <Q/S> team. Link: https://qs-e.space/community')
            success.append(f'{user_name} | {user_id}')
        except Exception as e:
            no_success.append(f'{user_name} | {user_id}')

    await gather_users()

    message_limit = config["message_limit"]
    message_period = timedelta(minutes=config["message_period_minutes"])
    message_count = 0
    message_last_time = datetime.now()

    with tqdm.tqdm(total=len(guild.members), desc='Sending messages') as pbar:
        for member in tqdm.tqdm(guild.members, desc='Sending messages'):
            user_name = member.display_name
            user_id = member.id

            now = datetime.now()
            if now - message_last_time >= message_period:
                message_count = 0
                message_last_time = now

            if message_count >= message_limit:
                wait_time = (message_last_time + message_period) - now
                await asyncio.sleep(wait_time.total_seconds())
                message_count = 0
                message_last_time = datetime.now()

            await send_message(user_name, user_id)
            message_count += 1

    archive_folder = config["archive_folder"]

    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)

    def move_to_archive(file_name):
        base_name, ext = os.path.splitext(file_name)
        new_name = file_name

        while os.path.exists(os.path.join(archive_folder, new_name)):
            random_number = random.randint(1, 999)
            new_name = f"{base_name}_{random_number}{ext}"

        shutil.move(file_name, os.path.join(archive_folder, new_name))

    await ctx.send("Successfully sent:", file=disnake.File(f'users_success_{guild.id}.txt'))

    if no_success:
        with open(f'users_no_success_{guild.id}.txt', 'w', encoding='utf-8') as file:
            file.write('\n'.join(no_success))
        await ctx.send("Failed to send to some users:", file=disnake.File(f'users_no_success_{guild.id}.txt'))

    move_to_archive(f'users_{guild.id}.txt')
    move_to_archive(f'users_success_{guild.id}.txt')
    move_to_archive(f'users_no_success_{guild.id}.txt')

bot.run(config["token"])