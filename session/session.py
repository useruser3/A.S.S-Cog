from redbot.core import checks,commands
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


class Session:
    def __init__(self):
        #start config section
        self.config = Config.get_conf(self, identifier=1234567890)
        default_global = {
            "sessions": {
                "session1":{
                    "defaultname": "session1",
                    "name": "false:",
                    "id": "none"
                },
                "session2":{
                    "defaultname": "session2",
                    "name": "EVENT",
                    "id": "none"
                },
                "session3":{
                    "defaultname": "session3",
                    "name": "none",
                    "id": "none"
                },
                "session4":{
                    "defaultname": "session4",
                    "name": False,
                    "id": "none"
                },
                "session5":{
                    "defaultname": "session5",
                    "name": False,
                    "id": "none"
                },
                "session6":{
                    "defaultname": "session6",
                    "name": False,
                    "id": "noneeeee"
                }
            }
        }

        default_user = {
            "info": {
                "name": "none",
                "hr": "0",
                "weapon": "none",
                "lastupdate": 0,
                "name2": "none",
                "hr2": "0",
                "weapon2": "none",
                "lastupdate2": 0          
            }
        }
        self.config.register_global(**default_global)
        self.config.register_user(**default_user)
        #end config

    #session commands

    @is_channel_not(455080960455868417)
    @commands.group(autohelp=False)
    async def session(self,ctx):        
        """type ```session``` followed by team to see the current session. leave team blank to see a general session"""
        if ctx.invoked_subcommand is None:
            """lists all active sessions"""
            embed=discord.Embed(title='Session List')
            if await self.config.sessions.session1.id() != "none":
                embed.add_field(name=await self.config.sessions.session1.name(), value=await self.config.sessions.session1.id(), inline=False)
            if await self.config.sessions.session2.id() != "none":
                embed.add_field(name=await self.config.sessions.session2.name(), value=await self.config.sessions.session2.id(), inline=False)
            if await self.config.sessions.session3.id() != "none":
               embed.add_field(name=await self.config.sessions.session3.name(), value=await self.config.sessions.session3.id(), inline=False)
            if await self.config.sessions.session4.id() != "none":
                embed.add_field(name=await self.config.sessions.session4.name(), value=await self.config.sessions.session4.id(), inline=False)
            if await self.config.sessions.session5.id() != "none":
               embed.add_field(name=await self.config.sessions.session5.name(), value=await self.config.sessions.session5.id(), inline=False)
            if ctx.channel.id == acechannel and await self.config.sessions.session6.id() != "none":
                embed.add_field(name=await self.config.sessions.session6.name(), value=await self.config.sessions.session6.id(), inline=False)
            await ctx.send(embed=embed)

    @session.command(name="set")
    async def set_session(self,ctx,stype,*,text):
        """Type set and the team you want to update followed by the new session ID (stype is the name of the team colour and text is the session ID)""" 
        newtext = text.replace(" ", "_")
        if stype == await self.config.sessions.session1.name() or stype == await self.config.sessions.session1.defaultname():
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + newtext + "```")
            await self.config.sessions.session1.id.set(newtext)
        elif stype == await self.config.sessions.session2.name() or stype == await self.config.sessions.session2.defaultname():
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + newtext + "```")
            await self.config.sessions.session2.id.set(newtext)
        elif stype == await self.config.sessions.session3.name() or stype == await self.config.sessions.session3.defaultname():
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + newtext + "```")
            await self.config.sessions.session3.id.set(newtext)
        elif stype == await self.config.sessions.session4.name() or stype == await self.config.sessions.session4.defaultname():
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + newtext + "```")
            await self.config.sessions.session4.id.set(newtext)
        elif stype == await self.config.sessions.session5.name() or stype == await self.config.sessions.session5.defaultname():
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + newtext + "```")
            await self.config.sessions.session5.id.set(newtext)
        elif stype == await self.config.sessions.session6.name() or stype == await self.config.sessions.session6.defaultname() and ctx.channel.id == acechannel:
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + newtext + "```")
            await self.config.sessions.session6.id.set(newtext)
        else:
            await ctx.send("invalid team")

    @session.command(name="setname")
    @checks.mod_or_permissions()
    async def set_session_name(self,ctx,*,str):
        """some descriptive text will be here soon-james"""
        stype,text = str.split(",")
        if stype == await self.config.sessions.session1.name() or stype == await self.config.sessions.session1.defaultname():
            await ctx.send("```" + "The session Name for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session1.name.set(text)
        elif stype == await self.config.sessions.session2.name() or stype == await self.config.sessions.session2.defaultname():
            await ctx.send("```" + "The session Name for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session2.name.set(text)
        elif stype == await self.config.sessions.session3.name() or stype == await self.config.sessions.session3.defaultname():
            await ctx.send("```" + "The session Name for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session3.name.set(text)
        elif stype == await self.config.sessions.session4.name() or stype == await self.config.sessions.session4.defaultname():
            await ctx.send("```" + "The session Name for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session4.name.set(text)
        elif stype == await self.config.sessions.session5.name() or stype == await self.config.sessions.session5.defaultname():
            await ctx.send("```" + "The session Name for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session5.name.set(text)
        elif stype == await self.config.sessions.session6.name() or stype == await self.config.sessions.session6.defaultname() and ctx.channel.id == acechannel:
            await ctx.send("```" + "The session Name for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session6.name.set(text)
        else:
            await ctx.send("invalid team")