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
        default_user = {
            "info": {
                "name": "none",
                "hr": "0",
                "lastupdate": 0      
            }
        }
        self.config.register_global(**default_global)
        self.config.register_user(**default_user)
        #end config

    @commands.group(invoke_without_subcommand=True)
    async def session(self,ctx):
        """type ```session``` followed by team to see the current session. leave team blank to see a general session"""
        if ctx.invoked_subcommand is None:
            await ctx.send("The current main session is " + "```" + await self.config.sessions.main() + "```")
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


    @session.command(name="list", pass_context=True)
    async def list(self,ctx):
        await ctx.send("The current sessions are: " + "\n")
        await ctx.send("```" + "MAIN: " + await self.config.sessions.main() + "\n" +  "RED: " + await self.config.sessions.red() +"\n" + "GREEN: " + await self.config.sessions.green() + "\n" + "AMBER: " + await self.config.sessions.amber() + "```")


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

    @commands.group()
    async def user(self,ctx):
        duser = await self.config.user(ctx.author).info.lastupdate()
        if ctx.invoked_subcommand is None:
                await ctx.send("```" + "User Info:" + "\n\n" + "NAME: " + await self.config.user(ctx.author).info.name() + "\n" + "HR: " + await self.config.user(ctx.author).info.hr() + "\n" + "LAST UPDATED BY: " + str(duser) + "```")
    @user.command(name="info", pass_context=True)
    async def list(self,ctx):
        await ctx.send(await self.config.user(ctx.author).info.name())

    @user.command(name="set")
    async def set(self,ctx,stype,*,text):
        if stype == "name":
             await self.config.user(ctx.author).info.name.set(text)
             await self.config.user(ctx.author).info.lastupdate.set(ctx.author.id)
             await ctx.send("User details updated")
        if stype == "hr":
            try: 
                if int(text) > 999 or int(text) < 0:
                    await ctx.send("Error: Please select a value lower than 1000 and greater than -1 :smile:")
                    return
            except:
                await ctx.send("Error: HR must be a number :smile:")
            else:
                    await self.config.user(ctx.author).info.hr.set(text)
                    await self.config.user(ctx.author).info.lastupdate.set(ctx.author.id)
                    await ctx.send("User details updated")