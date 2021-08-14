"""Class file for News."""

from discord.ext import commands
from discord.ext import tasks
import requests
import datetime as dt
import html
import re
import dotenv

# Load .env variable
dotenv.load_dotenv()
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

def clean_text(text):
    cleaned_text = html.unescape(re.sub(re.compile('<.*?>'), '', text))

    if len(cleaned_text) > 280:
        cleaned_text = f"{cleaned_text[:277]}..."

    return cleaned_text


class News(commands.Cog):
    """News class."""

    def __init__(self, client):
        """Initialize."""
        self.client = client
        self.WEBHOOK_URL = WEBHOOK_URL
        self.MAX_POSTS = 5
        self.TOP_POSTS_URL = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        self.GET_ITEM_URL = 'https://hacker-news.firebaseio.com/v0/item/{}.json'
        self.REQUEST_HEADER = {"User-Agent": "Hacker News Top 5 Bot v1.0"}

    def fetch_top_posts(self, max_posts):
        """
        Fetches post IDs of top posts via the API
        Parameters
        ----------
        max_posts : int
          Number of post IDs to be returned.
        """
        with requests.get(self.TOP_POSTS_URL, headers=self.REQUEST_HEADER) as response:
            item_ids = response.json()
            item_ids = item_ids[:max_posts]
            posts = [self.get_item(item_id) for item_id in item_ids]

            return posts

    def get_item(self, item_id):
        with requests.get(self.GET_ITEM_URL.format(item_id), headers=self.REQUEST_HEADER) as response:
            data = response.json()

            item = {}
            item['id'] = data.get('id')
            item['timestamp'] = f"{dt.datetime.fromtimestamp(data.get('time')).strftime('%Y-%m-%dT%H:%M:%S')}.000Z"
            item['by'] = data.get('by')
            item['title'] = data.get('title')
            item['comments'] = data.get('descendants')
            item['score'] = data.get('score')
            item['permalink'] = f'https://news.ycombinator.com/item?id={item["id"]}'
            item['url'] = data.get('url')
            item['text'] = data.get('text')

            if item['url'] is None:
                item['url'] = item['permalink']

            if item['text'] is None:
                item['text'] = ""

            else:
                item['text'] = clean_text(item['text'])

            return item

    def send_to_webhook(self, posts):
        """
        Sends the JSON payload to a Discord Webhook URL
        Parameters
        ----------
        posts : list
          A list of posts.
        """
        current_date = dt.date.today().strftime('%B %d, %Y')

        payload = {
            'username': 'Hacker News',
            'avatar_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Y_Combinator_logo.svg/240px-Y_Combinator_logo.svg.png',
            'content': f"**Top {self.MAX_POSTS} Posts from Hacker News ({current_date})**",
            'embeds': [
                {
                    'color': '16737792',
                    'author': {
                        'name': post['by']
                    },
                    'title': f"{post['title']}",
                    'url': f"{post['url']}",
                    'description': "" if post['text'] is None else f"{post['text']}",
                    'timestamp': post['timestamp'],
                    'fields': [
                        {
                            'name': 'Post ID',
                            'value': f"[{post['id']}]({post['permalink']})",
                            'inline': True
                        },
                        {
                            'name': 'Score',
                            'value': f"{post['score']} points",
                            'inline': True
                        },
                        {
                            'name': 'Comments',
                            'value': f"{post['comments']}",
                            'inline': True
                        }
                    ],
                    'footer': {
                        'text': 'Hacker News',
                        'icon_url': 'https://news.ycombinator.com/y18.gif'
                    }
                } for post in posts
            ]
        }

        for url in self.WEBHOOK_URL:
            requests.post(url, json=payload)

    # News command
    @tasks.loop(hours=24)
    async def news(self):
        """
        :type self: News
        :rtype News:
        """
        posts = self.fetch_top_posts(self.MAX_POSTS)
        self.send_to_webhook(posts)


def setup(client):
    """Load cog."""
    client.add_cog(News(client))
