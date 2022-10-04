import os
import dotenv 
import discord
import random

from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)


@client.event
async def on_ready():
    print("Current bot running:\n" + str(client.user) + "\n" + str(client.user.id))


@client.command()
async def save_img(ctx, image_Name):
    try:
        if message.attachments[0].content_type.startswith("video"):
            pass
        url = ctx.message.attachments[0].url
    except IndexError:
        await ctx.send("No attachments detected")
    else:
        print(url)
        await ctx.message.attachments[0].save("./images/" + image_Name + ".png")

@client.command()
async def getImg(ctx, image_Name):
    try:
        await ctx.channel.message(ctx.content)
        await ctx.channel.send(file=discord.File('./images/' + image_Name + '.png'))
    except:
        if image_Name == NULL:
            await message.channel.send("Please enter the image's name")
        else:
            await message.channel.send("Please send the command .getImg [image_Name]")


"""
*On the command given ping, returns the latency of the bot
*in the given channel the command was ran from
"""
@client.command()
async def ping(ctx):
    await ctx.channel.send("It took {0}s to respond.".format(round(client.latency, 3)))

"""
*Takes a low value and a high value and returns an integer between the two
*within the channel the command was executed in, if no args are given gives a random number
*between 1 and 5
"""
@client.command()
async def randNum(ctx, start, end):
    try:
        await ctx.channel.send(random.randrange(int(start), int(end+1)))
    except:
        if(int(start) > int(end)):
            await ctx.channel.send("The start must be less than the end")
        else:
            await ctx.channel.send("Please input the right command: .randomNumber [start] [end]")

@client.event
async def on_message_delete(message: discord.message.Message):
    try:
        await message.channel.send("Message by: " + str(message.author) 
                        + "\nThe deleted message: " + str(message.content))
    except:
        print("Message deleted: " + str(message.content))
        pass


def main():
    dotenv.load_dotenv()
    client.run(os.getenv("AUTH_KEY"))

if __name__ == '__main__':
    main()


"""
@client.event
async def on_message(message): #discord.message.Message
    try:
        if message.attachments:
            await message.channel.send(content=message.attachments[0].url)
        #print(client.intents.message_content)
        #print(message.content)
        #print(message.attachments)
        if((client.user != message.author) & (message.content.startswith(client.command_prefix))):
            #await message.channel.send(content=message.attachments[0].url) posts image
            await message.channel.send(message.content.replace(client.command_prefix,''))
            await message.channel.send(message.author.mention)
            print(str(message.content.startswith(client.command_prefix)) + " ... " + message.content)
            
    except:
        #print(message.attachments[0].url)
        pass
       """ 