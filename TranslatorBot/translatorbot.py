### TranslatorBot - A discord.py bot made to translate phrases between languages ###
### Made by Tymoteusz Niewodniczański // tymekn#3761 ###

import discord
from discord.ext import commands
from googletrans import Translator

client = commands.Bot(command_prefix = "-- ")           #"Creates" the bot with a set prefix
translator = Translator()                               #Initializes the translator

@client.event                                           #On inititation of bot, change status and print a message to console
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name = "for -- translate"))
    print("Bot is ready")

@client.command()                           #Translate function
async def translate(ctx, message):          
    lang1,lang2,word = message[0:2],message[3:5],message[6:]        #Gathers all required data regarding the translation
    word = word.replace("/"," ")                                    #Removes "word joiners" from the translating phrase   
    try:
        new_word = translator.translate(word, src=lang1, dest=lang2)#Does the translation
        embed = discord.Embed(title = new_word.text)                #Tries to send the message unless the language is not accepted
        await ctx.send(embed=embed)                                 
    except ValueError:
        embed = discord.Embed(title = "Sorry, that language is not recognised/accepted.\nEither you may have misspelled something, or the module cannot output the language.")
        await ctx.send(embed=embed)
    
@client.command()                           #Tells the user how to operate the Translate function
async def syntax(ctx):
    embed = discord.Embed(                  #Embeds the message
    title = """The syntax goes as follows:
    ```-- translate xx-yy-words/to/translate```""")
    await ctx.send(embed=embed)
    
@client.command()                           #Easter egg joke function
async def mlmc(ctx,message):
    word = "ME LLAMO MI CASA"
    lang = message
    try:                                    #If a recognised "language tag" is input, send the translation
        new_word = translator.translate(word,dest=lang)
        embed=discord.Embed(title=new_word.text)
        await ctx.send(embed=embed)
    except ValueError:                      #Otherwise...
        embed=discord.Embed(title="ME LLAMO ME CASA")
        await ctx.send(embed=embed)

def main():                                 #Main function
    with open("token.txt") as f:
        token = f.read()
        client.run(token)

if __name__ == "__main__":main()            #Runs the program 