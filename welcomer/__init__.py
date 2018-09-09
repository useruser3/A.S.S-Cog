from .welcomer import Welcomer

def setup(bot):
    bot.add_cog(Welcomer(bot))
