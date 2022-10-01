import os, dotenv, discord

from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print("HI")

@client.event
async def on_message(message: discord.message.Message):
    print(message.author.roles)

def main():
    dotenv.load_dotenv()
    client.run(os.getenv("AUTH_KEY"))

if __name__ == '__main__':
    main()