from redbot.core import commands
from redbot.core import Config
import discord
import asyncio

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

BaseCog = getattr(commands, "Cog", object)

class Welcomer(BaseCog):
    def __init__(self, bot):
        #start config section
        self.bot = bot
        self._config = None
        #end config

    def get_config(self,ctx):
        if self._config is None:
            self._config = ctx.bot.get_cog("Session").config
        return self._config

    async def on_member_join(self, member):
        server = member.guild
        channel = self.bot.get_channel(481390232521015296)
        role = discord.utils.get(server.roles, id=455061046390947840)
        await channel.send(f"Welcome {member.mention} to {server.name}. Please read pinned message and head over to <#481295578530185226> for help getting your roles and access to channels. Thank you enjoy.")
        await member.add_roles(role)
        channel = self.bot.get_channel(481295578530185226)
        #await channel.send(f"{member.mention} please pick your timezone from the list below")
        await channel.send(f"{member.mention} please tell me what you are here for? say 1 for monster hunter world \n or 2 for destiny")
        def mhwordestiny(m):
            return m.content == "1" and  m.channel == channel and m.author == member or m.content == "2" and  m.channel == channel and m.author == member
        msg = await self.bot.wait_for('message', check=mhwordestiny)
        if msg.content.startswith("1"):
            await channel.send(f"{member} what is your current hr. for 1-100 please say 1. \n for 101-300 please say 2 \n and for hr 301-999 please say 3")
            def mhwhr(m):
                return m.content == "1" and  m.channel == channel and m.author == member or m.content == "2" and  m.channel == channel and m.author == member or m.content == "3" and  m.channel == channel and m.author == member
            msg = await self.bot.wait_for('message', check=mhwhr)
            #mhw section
            if msg.content.startswith("1"):#hr 1-100
                role = discord.utils.get(server.roles, id=455061046390947840)
                await member.remove_roles(role)
                role = discord.utils.get(server.roles, id=455081655141400576)
                await member.add_roles(role)
                channel = self.bot.get_channel(481710416766959616)
                await channel.send("please say !timezone to set your timezone if you wish to set one")

            elif msg.content.startswith("2"):#hr 101-300
                role = discord.utils.get(server.roles, id=455061046390947840)
                await member.remove_roles(role)
                role = discord.utils.get(server.roles, id=455082122487660564)
                await member.add_roles(role)
                channel = self.bot.get_channel(481710416766959616)
                await channel.send("please say !timezone to set your timezone if you wish to set one")

            elif msg.content.startswith("3"):#hr 301-999
                role = discord.utils.get(server.roles, id=455061046390947840)
                await member.remove_roles(role)
                role = discord.utils.get(server.roles, id=494081715372032000)
                await member.add_roles(role)
                #add temporary role
                role = discord.utils.get(server.roles, id=455082122487660564)
                await member.add_roles(role)
                await channel.send("<@&455081061504778261> this person needs verification for the role hr 301-999")
                channel = self.bot.get_channel(481710416766959616)
                await channel.send("please say !timezone to set your timezone if you wish to set one")

        #destiny section
        elif msg.content.startswith("2"):
            role = discord.utils.get(server.roles, id=455061046390947840)
            await member.remove_roles(role)
            role = discord.utils.get(server.roles, id=494081715372032000)
            await member.add_roles(role)
            await channel.send("<@&481270841326436414> this person needs verification for the destiny clan")
            memtomessage = self.bot.get_user(300869396329660416)
            await memtomessage.send("someone needs verification for the destiny clan")
            channel = self.bot.get_channel(353648357845106699)
            await channel.send("please say !timezone to set your timezone if you wish to set one")


    async def on_message(self,message):
        channel = self.bot.get_channel(478891177232564225)
        member = message.author
        m = message


    async  def on_member_remove(self, member):
        channel = self.bot.get_channel(481390232521015296)
        await channel.send(f"Sorry to see you go {member}")

    
#welcomer commands
    @commands.group(autohelp=False)
    async def timezone(self,ctx):
        self.get_config(ctx)
        user_data = self._config.user(ctx.author)
        if ctx.invoked_subcommand is None:
            channel = ctx.channel
            member = ctx.message.author
            server = ctx.guild
            await channel.send(f"{member.mention} please pick your timezone from the list below")
            await channel.send("```      GMT+                   GMT-  \nGMT    - press 0       GMT-1  -  press 13\nGMT+1  - press 1       GMT-2  -  press 14\nGMT+2  - press 2       GMT-3  -  press 15\nGMT+3  - press 3       GMT-4  -  press 16\nGMT+4  - press 4       GMT-5  -  press 17\nGMT+5  - press 5       GMT-6  -  press 18\nGMT+6  - press 6       GMT-7  -  press 19\nGMT-7  - press 7       GMT-8  -  press 20\nGMT-8  - press 8       GMT-9  -  press 21\nGMT-9  - press 9       GMT-10 -  press 22\nGMT-10 - press 10      GMT-11 -  press 23\nGMT-11 - press 11      GMT-12 -  press 24\nGMT-12 - press 12```")
            def tzset(m):
                return m.content == "1" and  m.channel == channel and m.author == member or m.content == "2" and  m.channel == channel and m.author == member or m.content == "3" and  m.channel == channel and m.author == member or m.content == "4" and  m.channel == channel and m.author == member or m.content == "5" and  m.channel == channel and m.author == member or m.content == "6" and  m.channel == channel and m.author == member or m.content == "7" and  m.channel == channel and m.author == member or m.content == "8" and  m.channel == channel and m.author == member or m.content == "9" and  m.channel == channel and m.author == member or m.content == "10" and  m.channel == channel and m.author == member or m.content == "11" and  m.channel == channel and m.author == member or m.content == "12" and  m.channel == channel and m.author == member or m.content == "13" and  m.channel == channel and m.author == member or m.content == "14" and  m.channel == channel and m.author == member or m.content == "15" and  m.channel == member or m.content == "16" and  m.channel == channel and m.author == member or m.content == "17" and  m.channel == channel and m.author == member or m.content == "18" and  m.channel == channel and m.author == member or m.content == "19" and  m.channel == channel and m.author == member or m.content == "20" and  m.channel == channel and m.author == member or m.content == "21" and  m.channel == channel and m.author == member or m.content == "22" and  m.channel == channel and m.author == member or m.content == "23" and  m.channel == channel and m.author == member or m.content == "24" and  m.channel == channel and m.author == member
            msg = await self.bot.wait_for('message', check=tzset)
            #timezones
            if msg.content.startswith("0"):#gmt
                role = discord.utils.get(server.roles, id=481767933194928130)
                await member.add_roles(role)
                await channel.send("timezone set")

            elif msg.content.startswith("0"):#gmt
                role = discord.utils.get(server.roles, id=481768352155435018)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("1"):#gmt
                role = discord.utils.get(server.roles, id=481768539037106207)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("2"):#gmt
                role = discord.utils.get(server.roles, id=481768968747614233)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("3"):#gmt
                role = discord.utils.get(server.roles, id=481769249199882261)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("4"):#gmt
                role = discord.utils.get(server.roles, id=481769396813955085)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("5"):#gmt
                role = discord.utils.get(server.roles, id=481769623822270471)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("6"):#gmt
                role = discord.utils.get(server.roles, id=481769804206964738)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("7"):#gmt
                role = discord.utils.get(server.roles, id=481769958573998091)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("8"):#gmt
                role = discord.utils.get(server.roles, id=481770677737881610)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("9"):#gmt
                role = discord.utils.get(server.roles, id=481771070131535882)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("10"):#gmt
                role = discord.utils.get(server.roles, id=481771545040257024)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("11"):#gmt
                role = discord.utils.get(server.roles, id=481771769473138689)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("12"):#gmt
                role = discord.utils.get(server.roles, id=481772045621788692)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("13"):#gmt
                role = discord.utils.get(server.roles, id=481772632577146890)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("14"):#gmt
                role = discord.utils.get(server.roles, id=481772842480959488)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("15"):#gmt
                role = discord.utils.get(server.roles, id=481772985066192897)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("16"):#gmt
                role = discord.utils.get(server.roles, id=481773197038190592)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("17"):#gmt
                role = discord.utils.get(server.roles, id=481773594960199680)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("18"):#gmt
                role = discord.utils.get(server.roles, id=481774041355649034)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("19"):#gmt
                role = discord.utils.get(server.roles, id=481774173769826315)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("20"):#gmt
                role = discord.utils.get(server.roles, id=481774490485784578)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("21"):#gmt
                role = discord.utils.get(server.roles, id=481774809290637332)
                await member.add_roles(role)
                await channel.send("timezone set")
            elif msg.content.startswith("22"):#gmt
                role = discord.utils.get(server.roles, id=481774954937843713)
                await member.add_roles(role)
                await channel.send("timezone set")

    @commands.command(hidden=True)
    async def meow(self,ctx,channel:int,*,text):
        """
        some description
        """
        channel = self.bot.get_channel(channel)
        await channel.send(text)