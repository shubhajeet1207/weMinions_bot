import discord
import requests
import json


class myClient(discord.Client):
    async def on_ready(self):
        print(f'Howdy 👋 ! Logged in as {client.user}'.format(client))
    async def on_message(self, ctx):
        if ctx.author == client.user:
            return
        elif ctx.content.startswith('hello'):
            await ctx.channel.send('Hello, my friend 👋')
        elif ctx.content.startswith('make me laugh'):
            await ctx.channel.send('Would you like to hear a cliche joke 😛 ?')
            res = await client.wait_for('message', check=lambda message: ctx.author == message.author)
            if res.content.lower() == ('yes'):
                async def get_joke(self):
                    response = requests.get(
                        'https://api.chucknorris.io/jokes/random')
                    joke = json.loads(response.text)
                    # print(joke)
                    return(joke['value'])
                the_joke = await get_joke(self)
                await ctx.channel.send(the_joke)
            else:
                await ctx.channel.send('no problem!')
        elif ctx.content.startswith('tell me a joke'):
            await ctx.channel.send('Would you like to hear a clihe joke 😛 ?')
            res = await client.wait_for('message', check=lambda message: ctx.author == message.author)
            if res.content.lower() == ('yes'):
                async def get_joke(self):
                    response = requests.get(
                        'https://api.chucknorris.io/jokes/random')
                    joke = json.loads(response.text)
                    # print(joke)
                    return(joke['value'])
                the_joke = await get_joke(self)
                await ctx.channel.send(the_joke)
            else:
                await ctx.channel.send('no problem!')
                async def get_joke(self):
                    response = requests.get(
                        'https://api.chucknorris.io/jokes/random')
                    joke = json.loads(response.text)
                    # print(joke)
                    return(joke['value'])
                the_joke = await get_joke(self)
                await ctx.channel.send(the_joke)
        elif ctx.content.startswith('hii'):
            await ctx.channel.send('Hello 👋')
        elif ctx.content.startswith('yo'):
            await ctx.channel.send('Yo Dude 👋')
        elif ctx.content.startswith('who created you?'):
            await ctx.channel.send('Shubhajeet Pradhan 😎')
        elif ctx.content.startswith('do you know me?'):
            await ctx.channel.send('Ya !! since you are in this channel then definately you will be his friend 😏')
        elif ctx.content.startswith('bye'):
            await ctx.channel.send('tata bye bye 👋')

client = myClient()
# Bot login using the token
client.run('OTI0OTQ4NTMwMTk4NjM0NTE2.Ycl_cg.BV-ZYj16yeghZbjxYMwuDyMdt70')

