import discord
from discord.ext import commands
from geopy.geocoders import Nominatim
from config import bot_channel, token

bot = commands.Bot(command_prefix='.')

@bot.command(pass_context=True)
async def coords(ctx, *, message:str):
    jwa_geo = Nominatim()
    coord = jwa_geo.geocode(str(message))
    if ctx.message.channel.id == str(bot_channel):
        try:
            await bot.say(str(coord.latitude) + ', ' + str(coord.longitude))
        except:
            tb = traceback.print_exc(file=sys.stdout)
            print(tb)
            await bot.say('An error has occurred processing your request. The bot owner can check the logs.')
    else:
        await bot.say('ERR: Incorrect channel. Please use the command in the correct channel.')

bot.run(token)
