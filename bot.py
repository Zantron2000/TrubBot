import os
import dotenv 
import discord

from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print("Current bot running:\n" + str(client.user) + "\n" + str(client.user.id))

"""
*Saves the image locally within the directory called "images\[given name]"
*if the attachment is a file rather than an image
*Syntex for the commands is .save_img [image name]
"""
@client.command()
async def save_img(ctx, image_Name):
    try:
        url = ctx.message.attachments[0].url
        await ctx.message.attachments[0].save("./images/" + image_Name + ".png")
    except:
        await ctx.channel.send("No attachments detected")

"""
*Gets an image based on the file name of the image within the database
*.get_img [name of file]
"""
@client.command()
async def get_img(ctx, image_Name):
    try:
        await ctx.channel.send(file=discord.File('./images/' + image_Name + '.png'))
    except:
        await ctx.channel.send("Incorrect usage of command: .getImg [image_Name]")


"""
*On the command given ping, returns the latency of the bot
*in the given channel the command was ran from
"""
@client.command()
async def ping(ctx):
    await ctx.channel.send("It took {0}s to respond.".format(round(client.latency, 3)))


def main():
    dotenv.load_dotenv()
    client.run(os.getenv("AUTH_KEY"))

if __name__ == '__main__':
    main()
