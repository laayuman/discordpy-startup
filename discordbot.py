from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
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
