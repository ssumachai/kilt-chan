from __future__ import annotations

from typing import TYPE_CHECKING

from disnake.ext.commands import Cog

if TYPE_CHECKING:
    from utils.distyping import Config, KiltChanBot


class CommandBase(Cog):
    def __init__(self, bot: KiltChanBot):
        self.bot = bot

    @classmethod
    def is_enabled(cls, configs: Config = {}) -> bool:
        return True

    @property
    def configs(self) -> Config:
        return self.bot.configs

    @property
    def centralized_configs(self) -> Config:
        """Returns related config keys based on Cog. Override in subclasses."""
        return self.configs


def setup(_):
    pass
