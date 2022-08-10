# Squiddie

Squiddie is a small Discord chat bot created to serve the needs of it's authors' by providing them with several features that they would prefer to have more control over.

These features include displaying exchange rates for several cryptocurrencies, generating a feed of the most recent Hacker News posts, or giving general information relating to a provided IP address.

## How to use Squiddie?

The prefix for commands is `!sq `. For example, if you want to display the current Monero exchange rate, you can type `!sq xmr`.

Full set of commands and their descriptions can be seen by typing `!sq help`:

```
IPLookup:
  iplookup    Display general IP information.
Infract:
  infract     
Invite:
  invite      Generate a temporary (1-hour) single use invite link.
Misc:
  chicken     Think fast chucklenuts.
Music:
  connect     Connect to voice.
  now_playing Display information about the currently playing song.
  pause       Pause the currently playing song.
  play        Request a song and add it to the queue.
  queue       Retrieve a basic queue of upcoming songs.
  resume      Resume the currently paused song.
  skip        Skip the song.
  stop        Stop the currently playing song and destroy the player.
  volume      Change the player volume.
Wiki:
  wiki        Provide Wikipedia information given user input.
XMR:
  xmr         Display XMR exchange rate.
No Category:
  help        Shows this message
  load        Load cogs.
  unload      Unload cogs.

Type !sq help command for more info on a command.
You can also type !sq help category for more info on a category.
```

## Install

Pipenv is required with Python 3.9

### Setup virtual env

1. Install pipenv

   `pip install -U pipenv`

2. Setup pipenv env
   
   `pipenv --python 3.9`

3. Install the requirements
   
   `pipenv install`

### Activating the virtual env

You need to activate the virtual env before running the code
`pipenv shell`

You could also run the activation inline using the following method
`pipenv run python <path to script>`

## LICENSE

As of 21-Oct-2021, Squiddie is no longer private, and is now fully open to the public. Contributions are welcome, and appreciated.
Squiddie is now licensed under GPLv2.
