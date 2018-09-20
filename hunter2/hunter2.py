from redbot.core import commands
from redbot.core import Config
import discord
acechannel = 474639017422356491

def is_channel(channel_id):
            def predicate(ctx):
                 return ctx.channel.id == channel_id
            return commands.check(predicate)
            return ctx.send("error")
def is_channel_not(channel_id):
            def predicate(ctx):
                 return ctx.channel.id != channel_id
            return commands.check(predicate)
            return ctx.send("error")


class Hunter2:
    def __init__(self):
        #start config section
        self._config = None
        #end config

    def get_config(self,ctx):
        if self._config is None:
            self._config = ctx.bot.get_cog("Session").config
        return self._config

#user commands(guildcard)
    @is_channel(455140064721109002)
    @commands.group(autohelp=False)
    async def hunter2(self,ctx):
        """shows your guild card"""
        self.get_config(ctx)
        user_data = self._config.user(ctx.author)
        duser = await user_data.info.lastupdate2() 
        if ctx.invoked_subcommand is None:

            embed=discord.Embed(title='User Details')
            embed.add_field(name='Name: ', value=await user_data.info.name2(), inline=False)
            embed.add_field(name='HR: ', value=await user_data.info.hr2(), inline=False)
            embed.add_field(name='WEAPON: ', value=await user_data.info.weapon2(), inline=False)
            embed.add_field(name='LAST UPDATED BY: ', value=await user_data.info.lastupdate2(), inline=False)
            await ctx.send(embed=embed)

    @hunter2.command(name="set", autohelp=False)
    async def set(self,ctx,stype,*,text):

        user_data = self._config.user(ctx.author)
        """set the details of your guild card. you can set your name, hr and weapon"""
        if stype == "name":
             await user_data.info.name2.set(text)
             await user_data.info.lastupdate2.set(ctx.author.id)
             await ctx.send("User details updated")
        elif stype == "weapon":
            await user_data.info.weapon2.set(text)
            await user_data.info.lastupdate2.set(ctx.author.id)
            await ctx.send("User details updated")
        elif stype == "hr":
            try: 
                if int(text) > 999 or int(text) < 0:
                    await ctx.send("Error: Please select a value lower than 1000 and greater than -1 :smile:")
                    return
            except:
                await ctx.send("Error: HR must be a number :smile:")
            else:
                    await user_data.info.hr2.set(text)
                    await user_data.info.lastupdate2.set(ctx.author.id)
                    await ctx.send("User details updated")