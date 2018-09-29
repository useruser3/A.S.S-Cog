from redbot.core import commands
from redbot.core import Config
import discord
import random
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


class Monitor:
    def __init__(self, bot):
        #start config section
        self.bot = bot
        self._config = None
        #end config

    def get_config(self,ctx):
        if self._config is None:
            self._config = ctx.bot.get_cog("Session").config
        return self._config

    async  def on_message(self, message):
        channel = self.bot.get_channel(495397972498972682)
        words = ["blah","bloop","rape","anal","anus","arse","ass","bastard","bitch","ass fuck","ass hole","assfucker","asshole","asshole","black cock","bloody hell","boong","cock","cockfucker","cocksuck","cocksucker","coon","coonnass","crap","cunt","cyberfuck","damn","darn","dick","dirty","douche","dummy","erect","erection","erotic","escort","fag","faggot","fuck","Fuck off","fuck you","fuckass","fuckhole","god damn","gook","hard core","hardcore","homoerotic","hore","lesbian","lesbians","mother fucker","motherfuck","motherfucker","negro","nigger","orgasim","orgasm","penis","penisfucker","piss","piss off","porn","porno","pornography","pussy","retard","sadist","sex","sexy","shit","slut","son of a bitch","suck","tits","viagra","whore","xxx"]
        theMessage = message
        theContent = message.content.lower()
        theAuthor = message.author
        theMTime = message.created_at
        theChannel = message.channel.id
        theJump = message.jump_url
        if theAuthor.bot == False:
            if any(string in theContent for string in words):
                await channel.send(f"{theAuthor.display_name} said: **{theContent}** at **{theMTime}** in <#{theChannel}> {theJump}")
            #auto responses
            reactchannel = self.bot.get_channel(theChannel)
            if "night" in theContent:
                choices = [f"goodnight {theAuthor.display_name}",f"dont let the bed bugs bite..... you :fork_and_knife: "]
                await reactchannel.send(random.choice(choices))
            #halloween reacts
            halloweenchannel = self.bot.get_channel(theChannel)
            if "pumpkin" in theContent:
                choices = [":jack_o_lantern: yes please","only in my coffee please"]
                await halloweenchannel.send(random.choice(choices))
            elif "ghost" in theContent:
                choices = [":ghost: Ooooooooooo spooky","mwhahahahahahahaha"]
                await halloweenchannel.send(random.choice(choices))


