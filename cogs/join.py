import logging
from typing import Any, Dict

from disnake import Member, AllowedMentions
from disnake.ext.commands import Cog

from main import KiltChanBot

from .commandbase import CommandBase

class join(CommandBase):
    @Cog.listener()
    async def on_member_join(self, member: Member):
        guild = member.guild
        channel = guild.system_channel
        message = (
            f"Hey {member.mention}, welcome to **𝐆𝐫𝐞𝐞𝐧𝐰𝐨𝐨𝐝 𝐀𝐧𝐢𝐦𝐞 𝐒𝐨𝐜𝐢𝐞𝐭𝐲**, the UCR Anime Club. いらっしゃいませ! "
            "Be sure to read <#615578637525057549>!\n\n"
            "Let us get to know you better by telling us about yourself in <#634755907695411206>, and by selecting roles in <#1017576019378569277>!\n"
            "⊹₊┈ㆍ┈ㆍ┈ㆍ✿ㆍ┈ㆍ┈ㆍ┈₊⊹\n"
            ":sparkles:**Club Links**:sparkles:\n"
            "> Official Website\n"
            "> <https://greenwoodanimesociety.carrd.co/>\n"
            "> Our Insta\n"
            "> <https://www.instagram.com/greenwoodanimesociety/>\n"
            "> Become An Official Member\n"
            "> <https://highlanderlink.ucr.edu/organization/greenwood>\n"
            "> Our universal Discord Invite\n"
            "> <https://discord.gg/sW8CFRJ>\n"
            "> Help out with the Bot! Contact <@264606033681317888>\n"
            "> <https://github.com/ssumachai/kilt-chan>\n"
            "⊹₊┈ㆍ┈ㆍ┈ㆍ✿ㆍ┈ㆍ┈ㆍ┈₊⊹\n"
            "𝑾𝒆 𝒉𝒐𝒑𝒆 𝒚𝒐𝒖 𝒆𝒏𝒋𝒐𝒚 𝒚𝒐𝒖𝒓 𝒔𝒕𝒂𝒚 𝒂𝒕 𝑮𝑾𝑨𝑺"
        )
        if channel:
            await channel.send(content=message, suppress_embeds=True, allowed_mentions=AllowedMentions(users=False))

    @classmethod
    def is_enabled(cls, configs: Dict[str, Any] = {}):
        return configs.get("ENABLE_JOIN_MESSAGE", False)
    
def setup(bot: KiltChanBot):
    if join.is_enabled(bot.configs):
        bot.add_cog(join(bot))
    else:
        logging.warn("SKIPPING: cogs.join")
