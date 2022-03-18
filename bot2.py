import nextcord
from nextcord.ext import commands
import random

bot = commands.Bot(command_prefix="유미야 ")
bot_token = "OTUzMjMyMTkyOTYyNzAzMzYw.YjBkqQ.VCLGjVsv5Xb_jFT0ESmhLenI0Dg"

learn = {}

@bot.event
async def on_ready():
    print(f"{bot.user.name} start")
    game = nextcord.Game("\"유미야\"라고 말해보세요!")
    await bot.change_presence(status=nextcord.Status.online, activity=game)

@bot.command(aliases=["안녕", "반가워"])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}님 안녕하세요!')

@bot.command(aliases=["도움말"])
async def helpp(ctx):
    embed = nextcord.Embed(title="유미", description="made by 후루룹추루룹 and 소라다", color=0x4432a8)
    embed.add_field(name="유미봇은 대화를 할 수 있습니다!", value= "sans", inline=False)
    await ctx.send(embed=embed)

@bot.command(aliases=["주사위", "주사위 굴려줘"])
async def dice(ctx):
    await ctx.send(f"{random.randint(1, 6)}이 나왔습니다! ({ctx.author.mention}님의 주사위)")

@bot.command(aliases=["배워"])
async def teaching(ctx, arg1, arg2):
    learn[arg1] = arg2
    await ctx.send("배우기 성공!")

@bot.command(aliases=list(learn.keys()))
async def learn(ctx):
    await ctx.send()

bot.run(bot_token)
