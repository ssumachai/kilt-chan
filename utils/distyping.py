from typing import Any, Callable, Coroutine, Dict

from disnake import Interaction
from disnake.ext import commands

from main import KiltChanBot

# For typing
Context = commands.Context[KiltChanBot]
Config = Dict[str, Any]
Callback = Callable[[Interaction], Coroutine[Any, Any, None]]
