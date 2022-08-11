"""Main bot code for Squiddie."""

import os
import miru
import aiohttp
import lightbulb
import concurrent.futures
from lightbulb.ext import tasks
from hikari import Intents, StartingEvent, StoppingEvent, Status, Activity, ActivityType


# Initialize bot
bot = lightbulb.BotApp (
        os.environ["DISCORD_TOKEN"],
        default_enabled_guilds=int(os.environ["DEFAULT_GUILD_ID"]),
        intents=Intents.ALL,
        help_slash_command=True,
        ignore_bots=True,
        case_insensitive_prefix_commands=True,
        #logs= {
        #    "version": 0,
        #    "incremental": True,
        #    "loggers": {
        #        "hikari": {"level": "INFO"},
        #        "lightbulb": {"level": "INFO"},
        #        },
        #},
)

miru.load(bot)
tasks.load(bot)


@bot.listen()
async def on_starting(event: StartingEvent) -> None:
    bot.d.aio_session = aiohttp.ClientSession()
    bot.d.process_pool = concurrent.futures.ProcessPoolExecutor()


@bot.listen()
async def on_stopping(event: StoppingEvent) -> None:
    await bot.d.aio_session.close()
    bot.d.process_pool.shutdown(wait=True)


bot.load_extensions_from("./extensions/", must_exist=True, recursive=True)
#bot.load_extensions("lightbulb.ext.filament.exts.superuser")


def run() -> None:
    if os.name != "nt":
        import uvloop
        uvloop.install()

    bot.run(
            status=Status.ONLINE,
            activity=Activity(
                name="Squid in development",
                type=ActivityType.WATCHING
                )
            )
