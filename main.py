import discord

async def resendMessage(message, userMessage):
    webhook = await message.channel.create_webhook(name=message.author.name)
    await webhook.send(userMessage, username=message.author.name, avatar_url=message.author.avatar_url)
    await webhook.delete()

TOKEN = 'DISCORD_BOT_TOKEN'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        userMessage = '{0.content}'.format(message).lower()
        messageChecking = True
        botused = 0
        while messageChecking == True:
            if "wordToBeFiltered" in userMessage:
                userMessage = userMessage.replace("wordToBeFiltered", "filteredWord")
                botused = 1
                continue
            if botused == 1:
                await resendMessage(message, userMessage)
                await message.delete()
            messageChecking = False

client.run(TOKEN)
