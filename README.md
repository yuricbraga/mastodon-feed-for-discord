# Mastodon feed for Discord

I've made this little Python script to quickly deploy Mastodon feeds into your Discord server, by using Discord Webhooks!

You can self-host this and add a cron job that will handle posting for you. I will teach you how to use this tool in the following sections.

## Requirements

1. A Linux machine
2. Python 3.9
   - probably won't need such a high version as this doesn't use any of the newest features, but the code was written with the interpreter on version 3.9

## How to use this?

0. Install the python requirements of the project with:
   - `pip install -r requirements.txt`
   - Highly recommend you to use [venv](https://docs.python.org/3/library/venv.html) so you won't mess up with dependencies on your system!
1. Create a [webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) in your Discord server. Give it a name and point it to the channel you want your Mastodon feed to appear.
2. After creating the webhook, you need to create a `params.json` file at the root of the project. Start copying the template below:

```javascript
{
  "rssUrl": "https://vt.social/@architectus.rss", // the profile you wanna follow. Make sure to add ".rss" at the end, like the example
  "webhookUrl": "your generated webhook URL here", // self explanatory :P
  "botUsername": "Architectus@vt.social", // The name of your bot. Doesn't need to be the same as the webhook
  "messageNickname": "Archi" // The name that will be used in the message when a new toot comes out
}
```

```json
{
  "rssUrl": "",
  "webhookUrl": "",
  "botUsername": "",
  "messageNickname": ""
}
```

3. Create a [cron job](https://linuxhint.com/execute-crontab-every-5-minutes/) to your liking! The linked article will teach you how to set updates for each 5 minutes.
   - If you decide to go through the venv way, you will need to specify the path for the python binary. [This StackOverflow question covers it.](https://stackoverflow.com/questions/3287038/cron-and-virtualenv)

## Words from the author

This mess of a code was made in a rush because I have very little time being a streamer and a full time developer, so it's likely I won't have time to improve it. If you think there are ways to improve it, feel free to open an issue or fork it for yourself.
