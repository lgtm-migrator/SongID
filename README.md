# SongID
[![License](https://img.shields.io/github/license/smcclennon/SongID)](LICENSE)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fsmcclennon%2FSongID.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fsmcclennon%2FSongID?ref=badge_shield)
[![GitHub last commit](https://img.shields.io/github/last-commit/smcclennon/SongID)](https://github.com/smcclennon/SongID/commits)
[![HitCount](https://hits.dwyl.com/smcclennon/SongID.svg)](https://hits.dwyl.com/smcclennon/SongID)

SongID is a Telegram bot that can identify music in audio/video files you send it. These files can be screen recordings of an instagram post, or a telegram audio message taken by holding down the microphone icon in the bottom right.

The bot downloads audio and video files it get sent on telegram via the [Telegram Bot API](https://core.telegram.org/api), and sends the file to [ACRCloud](https://www.acrcloud.com) for audio recognition processing.

Working with the [Telegram Bot API](https://core.telegram.org/api) is made significantly easier by using the [python-telegram-bot](https://python-telegram-bot.org/) wrapper which simplifies every aspect of the API

## Features
- Identify music within files
- Supports video files
- Supports Telegram audio messages
- Find the name, artist, album, duration and release date of an identified song
- Provide direct links to the song on YouTube, Spotify and Deezer
- Deletes downloaded files as soon as they've been processed

## Blog Post
Read the blog post on how I created SongID on the [ACRCloud blog](https://blog.acrcloud.com/how-a-15-year-old-created-a-music-recognition-service-in-less-than-a-day-with-acrcloud)

Also featured on [Telegram Channels](https://telegramchannels.me/bots/songidbot) and [BotoStore](https://botostore.com/c/songidbot/)

# Set up SongID
1. Clone this repo: `git clone https://github.com/smcclennon/songid.git`
2. Install requirements: `python3 -m pip install --upgrade -r requirements.txt`
3. Create a Telegram bot via @botfather, and retrieve your bot token
4. Create 3 projects at ACRCloud (clear, noisy, hum) and retrieve your access keys and secrets
5. Create environment variables:
```
export songid_tg_token="123:ABC-DEF"
export songid_tg_devid="000000000"
export songid_tg_devusername="@username"

# Don't uncomment/run this if you're not using Heroku
#export songid_heroku_webhook="https://yourherokuappname.herokuapp.com/"
#export songid_heroku_listen="0.0.0.0"
#export songid_heroku_port="5000"

export songid_sentry_dsn="https://examplePublicKey@o0.ingest.sentry.io/0"

export songid_acr_clear_key="Insert ACRCloud Project access key"
export songid_acr_clear_secret="Insert ACRCloud Project access secret"

export songid_acr_noisy_key="Insert ACRCloud Project access key"
export songid_acr_noisy_secret="Insert ACRCloud Project access secret"

export songid_acr_hum_key="Insert ACRCloud Project access key"
export songid_acr_hum_secret="Insert ACRCloud Project access secret"
```
6. Run SongID: `python3 SongID.py` 
## Screenshots
<img src="https://smcclennon.github.io/assets/images/screenshots/SongID/voice.png" alt="Send Voice Message" width="100%"></img><img src="https://smcclennon.github.io/assets/images/screenshots/SongID/video.png" alt="Send Video" width="100%"></img>

*Written in Python 3.8 on Windows 10*
