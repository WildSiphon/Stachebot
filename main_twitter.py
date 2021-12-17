import logging
import sys

from mustachizer.twitter.twitter_bot import BotTwitter

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def main():
    twitter = BotTwitter(debug=False)
    twitter.run()


if __name__ == "__main__":
    main()
