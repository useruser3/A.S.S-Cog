from redbot.core import commands
from redbot.core import Config
import discord
import random
import re
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
        words = ["coon","cunt","fag","faggot","negro","nigger","nigga","retard","slut"]
        theMessage = message
        theContent = message.content.lower()
        theAuthor = message.author
        theMTime = message.created_at
        theChannel = message.channel.id
        theJump = message.jump_url
        if theAuthor.bot == False:
            brokenStr1 = theContent.split()
            lowerstring = [str(word).lower() for word in brokenStr1]

            badWordMask = '!@#$%!@#$%^~!@%^~@#$%!@#$%^~!'
            new = ''
            for word in lowerstring:
                if word in words:
                    await channel.send(f"{theAuthor.display_name} said: **{theContent}** at **{theMTime}** in <#{theChannel}> the offending word was **{word}** {theJump}")
            #auto responses
            reactchannel = self.bot.get_channel(theChannel)
            if re.match(r"\bgoodnight\b|\bgood night\b",theContent):
                choices = [f"goodnight {theAuthor.display_name}",f"dont let the bed bugs bite..... you :fork_and_knife: "]
                await reactchannel.send(random.choice(choices))
            #halloween reacts
            halloweenchannel = self.bot.get_channel(theChannel)
            if re.match(r"\bpumpkin\b|\b🍴\b",theContent):
                choices = [":jack_o_lantern: yes please","only in my coffee please"]
                await halloweenchannel.send(random.choice(choices))
            elif re.match(r"\bghost\b",theContent):
                choices = [":ghost: Ooooooooooo spooky","mwhahahahahahahaha"]
                await halloweenchannel.send(random.choice(choices))


    @commands.command(name="addword",usage="word or phrase to censor")
    async def test(self,ctx,*,word):
        self.get_config(ctx)
        wordlist = await self._config.wordstofilter()
        if word in wordlist:
            return await ctx.send(f"the word {word} is already in the list")
        else:
            wordlist.append(word)
            await ctx.send (f"{word} added to words")
            await ctx.send (f"{wordlist}")
            await ctx.send(await self._config.wordstofilter())
