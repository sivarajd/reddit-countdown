from __future__ import division, print_function
from configparser import ConfigParser
from datetime import datetime
from praw import Reddit
import re

def compute_time_ago_params(target):
    countdown_delta = target - datetime.now()
    days = countdown_delta.days
    hours = countdown_delta.seconds // 3600
    minutes = (countdown_delta.seconds - (hours * 3600)) // 60
    seconds = (countdown_delta.seconds - (hours * 3600) - (minutes * 60))

    return {
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }

if __name__ == '__main__':
    config_parser = ConfigParser()
    config_parser.read('countdown.ini')
    
    reddit = Reddit(config_parser.get('reddit', 'botname'))
    subreddit = reddit.subreddit(config_parser.get('reddit', 'subreddit'))
    sidebar_name = config_parser.get('reddit', 'sidebarname')
    target = config_parser.get('reddit', 'target')
    target_datetime = datetime.strptime(target, '%B %d %Y %H:%M:%S')

    for widget in subreddit.widgets.sidebar:
      if (widget.shortName == sidebar_name):
        countdownWidget = widget
        exit

    countdownText = countdownWidget.text

    for key, value in compute_time_ago_params(target_datetime).items():
        pattern = "\\[[^\\]]*\\]\\(#{0}\\)".format(key) # replace [<anything>](#<key>)
        repl = "[{0}](#{1})".format(value, key) # with [<value>](#<key>)
        countdownText = re.sub(pattern, repl, countdownText)
      
    countdownWidget.mod.update(text=countdownText)

