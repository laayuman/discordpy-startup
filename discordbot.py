from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


client = discord.Client()

@client.event
async def on_ready():
    message.channnel.send('ﾎﾟｯﾎﾟ！デンショバトが巣に帰って来たよ！')

@client.event
async def on_message(message):
	if message.content.isdecimal():
			text = ("$natural " + message.content + "m send 時間になりました、お疲れさまでした！ to " + message.author.mention)
			await message.channel.send("リマインダーを設定しました\n" + text)

bot.run(token)
