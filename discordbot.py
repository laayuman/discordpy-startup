import discord
import asyncio

client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_ready():
    message.channnel.send('ﾎﾟｯﾎﾟ！デンショバトが巣に帰って来たよ！')

@client.event
async def on_message(message):
	if message.content.isdecimal():
			text = ("$natural " + message.content + "m send 時間になりました、お疲れさまでした！ to " + message.author.mention)
			await message.channel.send("リマインダーを設定しました\n" + text)

client.run('token')
