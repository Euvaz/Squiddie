# Squiddie

Squiddie is a Discord chat bot intended to provide music player functionality, in response to numerous bots deprecating YouTube support. 

## Overview

- [Usage](https://github.com/euvaz/squiddie#usage)
- [Installation](https://github.com/euvaz/squiddie#installation)
  - [Configuration](https://github.com/euvaz/squiddie#configuration)
  - [Docker](https://github.com/euvaz/squiddie#docker)
  - [Manual](https://github.com/euvaz/squiddie#manual)
    - [Setup virtual env](https://github.com/euvaz/squiddie#setup-virtual-env)
    - [Activate virtual env](https://github.com/euvaz/squiddie#activate-virtual-env)
- [License](https://github.com/euvaz/squiddie#license)

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

### Configuration

Firstly, it is necessary to update the environment and application files respectively

```sh
$ cp .env_sample .env && cp application_sample.yaml application.yaml
```

After copying over the sample files, set their values accordingly

### Execution

There are two methods of running the bot, [Docker](https://github.com/euvaz/squiddie#Docker) (Recommended) or [Manual](https://github.com/euvaz/squiddie#manual)

### Docker

Build image and run as daemon

```sh
$ docker compose up -d
```

### Manual

> Poetry is recommended to be used with Python version 3.10

#### Setup virtual env

1. Install Poetry

    ```sh
    $ pip3 install -U poetry
    ```

2. Initialize Poetry
   
    ```sh
    $ poetry init
    ```

#### Activate virtual env

There are two methods for running the project.

1. Inline - Recommended method due to simplicity
    
    ```sh
    $ poetry run python3 -m squiddie
    ```

2. Out-of-line - Useful for debugging

    ```sh
    $ poetry shell
    $ python3 -m squiddie
    ```

## License

As of 21-Oct-2021, Squiddie is no longer private, and is now fully open to the public. Contributions are welcome, and appreciated.
Squiddie is now licensed under GPLv2.
