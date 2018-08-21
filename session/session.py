from redbot.core import commands
from redbot.core import Config
import discord
acechannel = 474639017422356491

def is_channel(channel_id):
            def predicate(ctx):
                 return ctx.channel.id == channel_id
            return commands.check(predicate)
            return ctx.send("error")


class Session:
    def __init__(self):
        #start config section
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {
            "sessions": {
                "apex": "There is no session set. Please set one using session set followed by the session ID",
                "apex2": "There is no session set. Please set one using session set followed by the session ID",
                "apex3": "There is no session set. Please set one using session set followed by the session ID",
                "apex4": "There is no session set. Please set one using session set followed by the session ID",
                "apex5": "There is no session set. Please set one using session set followed by the session ID",
                "ace": "There is no session set. Please set one using session set followed by the session ID"

        
            }
        }
        default_user = {
            "info": {
                "name": "none",
                "hr": "0",
                "weapon": "none",
                "lastupdate": 0      
            }
        }
        self.config.register_global(**default_global)
        self.config.register_user(**default_user)
        #end config

    #session commands
    @commands.group(autohelp=False)
    async def session(self,ctx):
        """type ```session``` followed by team to see the current session. leave team blank to see a general session"""
        if ctx.invoked_subcommand is None:
            await ctx.send("The current main session is " + "```" + await self.config.sessions.apex() + "```")

    @session.command(name="set")
    async def set_session(self,ctx,stype,*,text):
        """Type set and the team you want to update followed by the new session ID (stype is the name of the team colour and text is the session ID)""" 
        if stype == "apex":
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.apex.set(text)
        elif stype == "apex2":
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.apex2.set(text)
        elif stype == "apex3":
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.apex3.set(text)
        elif stype == "apex4":
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.apex4.set(text)
        elif stype == "apex5":
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.apex5.set(text)
        elif stype == "ace" and ctx.channel.id == acechannel:
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.ace.set(text)
        else:
            await ctx.send("invalid team")


    @session.command(name="list")
    async def slist(self,ctx):
        """lists all sessions"""
        embed=discord.Embed(title='Session List')
        if self.config.sessions.apex() != "none":
            embed.add_field(name='APEX: ', value=await self.config.sessions.apex(), inline=False)
        if self.config.sessions.apex2() != "none":   
            embed.add_field(name='APEX2: ', value=await self.config.sessions.apex2(), inline=False)
        if self.config.sessions.apex3() != "none":
            embed.add_field(name='APEX3: ', value=await self.config.sessions.apex3(), inline=False)
        if self.config.sessions.apex4() != "none":
            embed.add_field(name='APEX4: ', value=await self.config.sessions.apex4(), inline=False)
        if self.config.sessions.apex5() != "none":
            embed.add_field(name='APEX5: ', value=await self.config.sessions.apex5(), inline=False)
        if ctx.channel.id == acechannel:
                embed.add_field(name='ACE: ', value=await self.config.sessions.ace(), inline=False)
        await ctx.send(embed=embed)

    @session.command(name="main")
    async def sapx(self,ctx):
        """tells you the session for apex"""
        await ctx.send("The current session for apex is " + "```" + await self.config.sessions.apex() + "```")

    @session.command(name="apex2")
    async def sapx2(self,ctx):
        """tells you the session for apex2"""
        await ctx.send("The current session for apex2 is " + "```" + await self.config.sessions.apex2() + "```")

    @session.command(name="apex3")
    async def sapx3(self,ctx):
        """tells you the session for apex3"""
        await ctx.send("The current session for apex3 is " + "```" + await self.config.sessions.apex3() + "```")

    @session.command(name="apex4")
    async def sapx4(self,ctx):
        """tells you the session for apex4"""
        await ctx.send("The current session for apex4 is " + "```" + await self.config.sessions.apex4() + "```")

    @session.command(name="apex5")
    async def sapx5(self,ctx):
        """tells you the session for apex5"""
        await ctx.send("The current session for apex5 is " + "```" + await self.config.sessions.apex5() + "```")

    @session.command(name="ace")
    async def sace(self,ctx):
        """tells you the session for ace"""

        if ctx.channel.id == acechannel:
            await ctx.send("The current session for ace is " + "```" + await self.config.sessions.ace() + "```")
        else:
            return


#user commands(guildcard)
    @is_channel(455140064721109002)
    @commands.group(autohelp=False)
    async def hunter(self,ctx):
        """shows your guild card"""
        duser = await self.config.user(ctx.author).info.lastupdate() 
        if ctx.invoked_subcommand is None:
            embed=discord.Embed(title='User Details')
            embed.add_field(name='Name: ', value=await self.config.user(ctx.author).info.name(), inline=False)
            embed.add_field(name='HR: ', value=await self.config.user(ctx.author).info.hr(), inline=False)
            embed.add_field(name='WEAPON: ', value=await self.config.user(ctx.author).info.weapon(), inline=False)
            embed.add_field(name='LAST UPDATED BY: ', value=await self.config.user(ctx.author).info.lastupdate(), inline=False)
            await ctx.send(embed=embed)

    @hunter.command(name="set", autohelp=False)
    async def set(self,ctx,stype,*,text):
        """set the details of your guild card. you can set your name, hr and weapon"""
        if stype == "name":
             await self.config.user(ctx.author).info.name.set(text)
             await self.config.user(ctx.author).info.lastupdate.set(ctx.author.id)
             await ctx.send("User details updated")
        elif stype == "weapon":
            await self.config.user(ctx.author).info.weapon.set(text)
            await ctx.send("User details updated")
        elif stype == "hr":
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