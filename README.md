# Reddit Countdown

Text based countdown timer for a subreddit's sidebar to help Reddit
communities to count down to important events.

Based on the code from [matchu/reddit-countdown](https://github.com/matchu/reddit-countdown)

## Pre-requisites

* Python 3.8 or above 
* [praw (Python Reddit API Wrapper)](https://praw.readthedocs.io/)


## Quick Start

1. Create an app on Reddit (https://www.reddit.com/prefs/apps/).
   You just need to enter `name` & `redirect uri`. Use http://127.0.0.1 as redirect uri.
2. You will get a client id & secret that you will use below.
3. If you are using a separate Bot account (recommended), it should have `Manage Settings` access.
4. In the cloned repository, copy countdown.ini.sample to countdown.ini.
   - Give a name to reference your bot (YourBotName).
   - Specify your subreddit.
   - Name of the sidebar where you want the countdown.
   - Specify a target time. It will be in UTC.
5. Copy praw.ini.sample to praw.ini.
   - Replace the section heading with YourBotName.
   - Enter the client id & secret you received when creating the app
   - Enter your Reddit username and password
   - Specify a meaningful user agent. Check [Reddit API Rules](https://github.com/reddit-archive/reddit/wiki/API) for rules.
6. In the sidebar, create a text widget with the name you mentioned above.
7. Enter the placeholder as below:

    There are [some](#days) days, [some](#hours) hours, [some](#minutes)
    minutes, and [some](#seconds) seconds remaining.
8. Run your script.
   ```python countdown.py```
9. It will update the widget content replacing the placeholders.
10. Setup a job to run the script at regular intervals. 
 

### Note 
* It works with Markup text. Not tested with HTML content.
* Might work in lower Python 3.x versions.

