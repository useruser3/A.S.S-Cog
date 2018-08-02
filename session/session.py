from discord.ext import commands
from redbot.core import Config
class Session:
    def __init__(self):
        #start config section
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {
            "sessions": {
                "main": "There is no session set. Please set one using session set followed by the session ID",
                "red": "There is no session set. Please set one using session set followed by the session ID",
                "green": "There is no session set. Please set one using session set followed by the session ID",
                "amber": "There is no session set. Please set one using session set followed by the session ID"         
            }
        }
        self.config.register_global(**default_global)
        #end config

    @commands.group(pass_context=True)
    async def session(self,ctx):
        """type ```session``` followed by team to see the current session. leave team blank to see a general session"""
        if ctx.invoked_subcommand is None:
            await ctx.send("The current session is " + "```" + await self.config.sessions.main() + "```")

    @session.command(name="set", pass_context=True)
    async def set_session(self,ctx,stype,*,text):
        """Type set and the team you want to update followed by the new session ID (stype is the name of the team colour and text is the session ID)""" 
        if stype == "main":
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.main.set(text)
        elif stype == "red":
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.red.set(text)
        elif stype == "amber":
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.amber.set(text)
        elif stype == "green":
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.green.set(text)
        else:
            await ctx.send("invalid team")

    @session.command(name="red", pass_context=True)
    async def sred(self,ctx):
        """tells you the session for red"""
        await ctx.send("The current session for red is " + "```" + await self.config.sessions.red() + "```")

    @session.command(name="green", pass_context=True)
    async def sgre(self,ctx):
        """tells you the session for green"""
        await ctx.send("The current session for green is " + "```" + await self.config.sessions.green() + "```")

    @session.command(name="amber", pass_context=True)
    async def samb(self,ctx):
        """tells you the session for amber"""
        await ctx.send("The current session for amber is " + "```" + await self.config.sessions.amber() + "```")









