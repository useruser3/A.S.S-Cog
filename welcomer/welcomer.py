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
                await channel.send(f"welcome {member}")
                role = discord.utils.get(server.roles, id=455061046390947840)
                await member.remove_roles(role)
                role = discord.utils.get(server.roles, id=455081655141400576)
                await member.add_roles(role)

            elif msg.content.startswith("2"):#hr 101-300
                await channel.send(f"welcome {member}")
                role = discord.utils.get(server.roles, id=455061046390947840)
                await member.remove_roles(role)
                role = discord.utils.get(server.roles, id=455082122487660564)
                await member.add_roles(role)

            elif msg.content.startswith("3"):#hr 301-999
                await channel.send(f"welcome {member}")
                role = discord.utils.get(server.roles, id=455061046390947840)
                await member.remove_roles(role)
                role = discord.utils.get(server.roles, id=494081715372032000)
                await member.add_roles(role)
                await channel.send("<@&455081061504778261> this person needs verification for the role hr 301-999")

        #destiny section
        elif msg.content.startswith("2"):
            await channel.send(f"{member} you are here for destiny")
            role = discord.utils.get(server.roles, id=455061046390947840)
            await member.remove_roles(role)
            role = discord.utils.get(server.roles, id=494081715372032000)
            await member.add_roles(role)
            await channel.send("<@&455081061504778261> this person needs verification for the destiny clan")
            memtomessage = self.bot.get_user(300869396329660416)
            await memtomessage.send("someone needs verification for the destiny clan")


    async def on_message(self,message):
        channel = self.bot.get_channel(478891177232564225)
        member = message.author
        m = message


    async  def on_member_remove(self, member):
        channel = self.bot.get_channel(481390232521015296)
        await channel.send(f"Sorry to see you go {member}")

    
#welcomer commands
    @commands.group(autohelp=False)
    async def welcomer(self,ctx):
    
        self.get_config(ctx)
        user_data = self._config.user(ctx.author)
        if ctx.invoked_subcommand is None:
            return

    @commands.command(hidden=True)
    async def meow(self,ctx,channel:int,*,text):
        """
        some description
        """
        channel = self.bot.get_channel(channel)
        await channel.send(text)