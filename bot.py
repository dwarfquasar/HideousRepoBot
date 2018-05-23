import discord #Here's the help dumbo: https://python.org/pypi/discord
#This is a discord bot. It Repos obscene texts and can do cool things. Have fun

TOKEN = 'NDQ4MTM3NDA2NDYyNTU4MjE4.DeRxpg.9rw0SCmsCq07eA7sK0cxs4951SI'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('/help')
        msg = "Thanks for requesting help, here are the avalible commands: /help : invokes this dialogue. /chat : WIP conversation. /play[url] : plays the url".format(message)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Awaiting instructions, master')

client.run(TOKEN)
