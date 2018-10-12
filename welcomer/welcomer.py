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
        asyncio.sleep(10)
        await channel.send(f"{member.mention} please tell me what you are here for? say 1 for monster hunter world \n or 2 for destiny")
        def mhwordestiny(m):
            return m.content == "1" and  m.channel == channel or m.content == "2" and  m.channel == channel
        msg = await self.bot.wait_for('message', check=mhwordestiny)
        if m.content.startswith("1"):
            await channel.send(f"{member} you are here for monster hunter world")
        elif m.content.startswith("2"):
            await channel.send(f"{member} you are here for destiny")


    # async def on_message(self,message):
    #     channel = self.bot.get_channel(478891177232564225)
    #     member = message.author
    #     def mhwordestiny(m):
    #         return m.content == "1" and  m.channel == channel or m.content == "2" and  m.channel == channel
    #     msg = await self.bot.wait_for('message', check=mhwordestiny)
    #     if message.content.startswith("1"):
    #         await channel.send(f"{member} you are here for monster hunter world")
    #     elif m.content.startswith("2"):
    #         await channel.send(f"{member} you are here for monster hunter world")

    async  def on_member_remove(self, member):
        channel = self.bot.get_channel(481390232521015296)
        await channel.send(f"Sorry to see you go {member}")

    # async def on_member_update(self, before,member):
    #         channel = self.bot.get_channel(478891177232564225)
    #         server=member.guild
    #         role = discord.utils.get(server.roles, id=455061046390947840)
    #         if member.id == 141908685738737664:
    #             await channel.send(role)
    #             await member.add_roles(role)
    #             await channel.send("role added")
    
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