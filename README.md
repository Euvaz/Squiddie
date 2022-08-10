# Squiddie

Squiddie is a Discord chat bot intended to provide music player functionality, in response to numerous bots deprecating YouTube support. 

## Overview

- [Usage](https://github.com/euvaz/squiddie#-usage)
- [Installation](https://github.com/euvaz/squiddie#-installation)
  - [Docker](https://github.com/euvaz/squiddie#-docker)
  - [Manual](https://github.com/euvaz/squiddie#-manual)
- [License](https://github.com/euvaz/squiddie/#-license)

## Usage

The prefix for commands is `!sq `. For example, if you want to generate a temporary (1-hour) single use invite link, this can be done via `!sq invite`.

Full set of commands and their descriptions can be seen by typing `!sq help`:

```
Invite:
  invite      Generate a temporary (1-hour) single use invite link.
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
No Category:
  help        Shows this message
  load        Load cogs.
  unload      Unload cogs.

Type !sq help command for more info on a command.
You can also type !sq help category for more info on a category.
```

## Installation

### Docker

TODO: Add support for dockerfiles and docker-compose for quick and scalable deployments

### Manual
> Pipenv is required with Python 3.9

#### Setup virtual env

1. Install pipenv

   `pip install -U pipenv`

2. Setup pipenv env
   
   `pipenv --python 3.9`

3. Install the requirements
   
   `pipenv install`

#### Activating the virtual env

You need to activate the virtual env before running the code
`pipenv shell`

You could also run the activation inline using the following method
`pipenv run python <path to script>`

## License

As of 21-Oct-2021, Squiddie is no longer private, and is now fully open to the public. Contributions are welcome, and appreciated.
Squiddie is now licensed under GPLv2.
