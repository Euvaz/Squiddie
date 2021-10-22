# Squiddie

Squiddie is a small Discord chat bot created to serve the needs of it's authors' by providing them with several features that they would prefer to have more control over.

These features include displaying exchange rates for several cryptocurrencies, generating a feed of the most recent Hacker News posts, or giving general information relating to a provided IP address.

## How to use Squiddie?

The prefix for commands is `!sq `. For example, if you want to display the current Monero exchange rate, you can type `!sq xmr`.

Full set of commands and their descriptions can be seen by typing `!sq help`:

```
No Category:
  btc
  eth
  help     Shows this message
  iplookup
  news
  xmr

Type !sq help command for more info on a command.
You can also type !sq help category for more info on a category.
```

## Install

Pipenv is required with Python 3.9

### Setup virtual env

1. Install pipenv

   `pip install -U pipenv`

2. Setup pienv env
   
   `pipenv --python 3.9`

3. Install the requirements
   
   `pipenv install`

### Activating the virtual env

You need to activate the virtual env before run the code
`pipenv shell`

You could also run the activation inline using the following method
`pipenv run python <path to script>`

## LICENSE

As of 21-Oct-2021, Squiddie is now public, fully open to the public. Contributions are welcome, and appreciated.
Squiddie is now licensed under GPLv2.
