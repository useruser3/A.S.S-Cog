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
def replaceMultiple(mainString, toBeReplaces, newString):
    # Iterate over the strings to be replaced
    for elem in toBeReplaces :
        # Check if string is in the main string
        if elem in mainString :
            # Replace the string
            mainString = mainString.replace(elem, newString)
    
    return  mainString

async def get_names_list(self):
    async with self.config.sessions() as session_dict:
        temp=[]
        namelist=[]
        for session, session_data in session_dict.items():
            if str(session_data['name']) != 'none':
                temp = [session_data['name']]
                namelist.append(temp)
        finaltext = replaceMultiple(str(namelist),['[',']',"'"], "")
        return str(finaltext)




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
        """lists all active sessions"""
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

    @session.command(name="set",usage="<oldname,sessionid>")
    async def set_session_id(self,ctx,*,str):
        """Type enter the name of the session that you want to change the ID for followed by a comma and your new ID for example (+session set main session,g34g2dssfS) make sure there is no space after the comma"""
        stype,text = str.split(",")
        if stype == await self.config.sessions.session1.name() or stype == await self.config.sessions.session1.defaultname():
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session1.id.set(text)
        elif stype == await self.config.sessions.session2.name() or stype == await self.config.sessions.session2.defaultname():
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session2.id.set(text)
        elif stype == await self.config.sessions.session3.name() or stype == await self.config.sessions.session3.defaultname():
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session3.id.set(text)
        elif stype == await self.config.sessions.session4.name() or stype == await self.config.sessions.session4.defaultname():
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session4.id.set(text)
        elif stype == await self.config.sessions.session5.name() or stype == await self.config.sessions.session5.defaultname():
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session5.id.set(text)
        elif stype == await self.config.sessions.session6.name() or stype == await self.config.sessions.session6.defaultname() and ctx.channel.id == acechannel:
            await ctx.send("```" + "The session ID for " + stype + " is now:" + " " + text + "```")
            await self.config.sessions.session6.id.set(text)
        else:
            emessage = await get_names_list(self)
            await ctx.send("Thats not a valid session. \n the current sessions are: " + emessage)

    @session.command(name="setname",usage="<oldname,newname>")
    async def set_session_name(self,ctx,*,str):
        """Type enter the name of the session that you want to change the name for followed by a comma and your new name for example (+session setname main session,awsome event session) make sure there is no space after the comma"""
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
            emessage = await get_names_list(self)
            await ctx.send("Thats not a valid session. \n the current sessions are: " + emessage)