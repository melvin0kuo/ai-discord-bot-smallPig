<a href="https://discord.gg/funzKnyWeG">
    <img src="https://img.shields.io/discord/1212823415204085770?color=7289DA&label=Support&logo=discord&style=for-the-badge" alt="Discord">
</a>

# PigPig (Discord Bot Base on LLM and Vocard bot)
> PigPig is a simple custom Disocrd LLM Bot built with Python & [discord.py](https://discordpy.readthedocs.io/en/stable/) <br>
Demo: [Discord Bot Demo](https://discord.com/api/oauth2/authorize?client_id=890399639008866355&permissions=36708608&scope=bot%20applications.commands),
[Dashboard Demo](https://vocard.xyz)
![alt text](readmeimg/image-4.png)

![alt text](readmeimg/image.png)

![alt text](readmeimg/image-1.png)

![alt text](readmeimg/image-2.png)

![alt text](readmeimg/image-3.png)
## Requirements
* [Python 3.10+](https://www.python.org/downloads/)
* [Modules in requirements](https://github.com/ChocoMeow/Vocard/blob/main/requirements.txt)
* [Lavalink Server (Requires 4.0.0+)](https://github.com/freyacodes/Lavalink)

## Quick Start
```sh
git clone https://github.com/starpig1129/PigPig-discord-LLM-bot.git  #Clone the repository
cd PigPig-discord-LLM-bot                                        #Go to the directory
python -m pip install -r requirements.txt          #Install required packages
```
After installing all packages, you must configure the bot before to start! [How To Configure](https://github.com/ChocoMeow/Vocard#configuration)<br />
Start your bot with `python main.py`

## Configuration
1. **Rename `.env Example` to `.env` and fill all the values**
```sh
TOKEN = XXXXXXXXXXXXXXXXXXXXXXXX.XXXXXX.XXXXXXXXXXXXXXXXXXXXXXXXXXX
CLIENT_ID = 123456789012345678
CLIENT_SECRET_ID = XXXXXXXXXX-XXXXXXXXXXXXXXXXXXXXX
SERCET_KEY = DASHBOARD_SERCET_KEY

BUG_REPORT_CHANNEL_ID = 123456789012345678

SPOTIFY_CLIENT_ID = 0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
SPOTIFY_CLIENT_SECRET = 0XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

GENIUS_TOKEN = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

MONGODB_URL = mongodb+srv://user:password@clusterURL
MONGODB_NAME = Vocard
```
| Values | Description |
| --- | --- |
| TOKEN | Your Discord bot token [(Discord Portal)](https://discord.com/developers/applications) |
| CLIENT_ID | Your Discord bot client id [(Discord Portal)](https://discord.com/developers/applications) |
| CLIENT_SECRET_ID | Your Discord bot client secret id [(Discord Portal)](https://discord.com/developers/applications) ***(optional)*** |
| SERCET_KEY | Secret key for dashboard ***(optional)*** |
| BUG_REPORT_CHANNEL_ID | All the error messages will send to this text channel ***(optional)*** |
| SPOTIFY_CLIENT_ID | Your Spoity client id [(Spotify Portal)](https://developer.spotify.com/dashboard/applications) ***(optional)*** |
| SPOTIFY_CLIENT_SECRET | Your Spoity client sercret id [(Spotify Portal)](https://developer.spotify.com/dashboard/applications) ***(optional)*** |
| GENIUS_TOKEN | Your genius api key [(Genius Lyrics API)](https://genius.com/api-clients) ***(optional)*** |
| MONGODB_URL | Your Mongo datebase url [(Mongodb)](https://www.mongodb.com/) |
| MONGODB_NAME | The datebase name that you created on [Mongodb](https://www.mongodb.com/) |

2. **Rename `settings Example.json` to `settings.json` and customize your settings**
***(Note: Do not change any keys from `settings.json`)***
```json
{
    "nodes": {
        "DEFAULT": {
            "host": "127.0.0.1",
            "port": 2333,
            "password": "password",
            "secure": false,
            "identifier": "DEFAULT"
        }   
    },
    "prefix": "?",
    "activity":[
        {"listen": "/help"}
    ],
    "bot_access_user": [],
    "embed_color":"0xb3b3b3",
    "default_max_queue": 1000,
    "lyrics_platform": "A_ZLyrics",
    "ipc_server": {
        "host": "127.0.0.1",
        "port": 8000,
        "enable": false
    },
    "sources_settings": {
        "youtube": {
            "emoji": "<:youtube:826661982760992778>",
            "color": "0xFF0000"
        },
        "youtube music": {
            "emoji": "<:youtube:826661982760992778>",
            "color": "0xFF0000"
        },
        "spotify": {
            "emoji": "<:spotify:826661996615172146>",
            "color": "0x1DB954"
        },
        "soundcloud": {
            "emoji": "<:soundcloud:852729280027033632>",
            "color": "0xFF7700"
        },
        "twitch": {
            "emoji": "<:twitch:852729278285086741>",
            "color": "0x9B4AFF"
        },
        "bandcamp": {
            "emoji": "<:bandcamp:864694003811221526>",
            "color": "0x6F98A7"
        },
        "vimeo": {
            "emoji": "<:vimeo:864694001919721473>",
            "color": "0x1ABCEA"
        },
        "apple": {
            "emoji": "<:applemusic:994844332374884413>",
            "color": "0xE298C4"
        },
        "reddit": {
            "emoji": "<:reddit:996007566863773717>",
            "color": "0xFF5700"
        },
        "tiktok": {
            "emoji": "<:tiktok:996007689798811698>",
            "color": "0x74ECE9"
        }
    },
    "default_controller": {
        "embeds": {
            "active": {
                "description": "**Now Playing: ```[@@track_name@@]```\nLink: [Click Me](@@track_url@@) | Requester: @@requester@@ | DJ: @@dj@@**",
                "footer": {
                    "text": "Queue Length: @@queue_length@@ | Duration: @@track_duration@@ | Volume: @@volume@@% {{loop_mode != 'Off' ?? | Repeat: @@loop_mode@@}}"
                },
                "image": "@@track_thumbnail@@",
                "author": {
                    "name": "Music Controller | @@channel_name@@",
                    "icon_url": "@@bot_icon@@"
                },
                "color": "@@track_color@@"
            },
            "inactive": {
                "header": {
                    "title": "There are no songs playing right now"
                },
                "description": "[Support](@@server_invite_link@@) | [Invite](@@invite_link@@) | [Questionnaire](https://forms.gle/Qm8vjBfg2kp13YGD7)",
                "image": "https://i.imgur.com/dIFBwU7.png",
                "color": "@@default_embed_color@@"
            }
        },
        "default_buttons": [
            ["back", "resume", "skip", {"stop": "red"}, "add"],
            ["tracks"]
        ],
        "disableButtonText": false
    },
    "cooldowns": {
        "connect": [2, 30],
        "playlist view": [1, 30]
    },
    "aliases": {
        "connect": ["join"],
        "leave": ["stop", "bye"],
        "play": ["p"],
        "view": ["v"]
    }
}
```
* For `nodes` you have to provide host, port, password and identifier of the [Lavalink Server](https://github.com/freyacodes/Lavalink)
* For `prefix` you can set the prefix of the bot. (If you don't provide any prefix, the bot will disable the message command).
* For `activity` you can set the activity of the bot. [Example Here](https://github.com/ChocoMeow/Vocard/blob/main/PLACEHOLDERS.md#bot-activity-activity-are-updated-every-10-minutes)
* For `bot_access_user` you can pass the [discord user id](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-). Example: `[123456789012345678]`
* For `embed_color` you must pass a [Hexadecimal color code](https://htmlcolorcodes.com/) and add `0x` before the color code. Example: `"0xb3b3b3"`
* For `default_max_queue` you can set a default maximum number of tracks that can be added to the queue.
* For `lyrics_platform` you can set lyrics search engine (e.g. `A_ZLyrics`, `Genius`, `lyrist`)<br>**NOTE: If you are using Genius as your lyrics search engine, you must install the lyricsgenius module (`pip install lyricsgenius`)**
* For `ipc_server` you can set the host, password and enable of the ipc server.
* For `emoji_source_raw` you can change the source emoji of the track with discord emoji like `<:EMOJI_NAME:EMOJI_ID>`
* For `cooldowns` you can set a custom cooldown in the command. Example: `"command_name": [The total number of tokens available, The length of the cooldown period in seconds]`
* For `aliases` you can set custom aliases in the command. Example: `"command_name": [alias1, alias2, ...]`
* For `default_controller` you can set custom embeds and buttons in controller, [Example Here](https://github.com/ChocoMeow/Vocard/blob/main/PLACEHOLDERS.md#controller-embeds)

## How to update? (For Windows and Linux)
***Note: Make sure there are no personal files in the directory! Otherwise it will be deleted.***
```sh
# Check the current version
python update.py -c

# Install the latest version
python update.py -l

# Install the specified version
python update.py -v VERSION

# Install the beta version
python update.py -b
```


# Vocard (Discord Music Bot)
> Vocard is a simple custom Disocrd Music Bot built with Python & [discord.py](https://discordpy.readthedocs.io/en/stable/) <br>
Demo: [Discord Bot Demo](https://discord.com/api/oauth2/authorize?client_id=890399639008866355&permissions=36708608&scope=bot%20applications.commands),
[Dashboard Demo](https://vocard.xyz)

# Tutorial
Click on the image below to watch the tutorial on Youtube.

[![Discord Music Bot](https://img.youtube.com/vi/f_Z0RLRZzWw/maxresdefault.jpg)](https://www.youtube.com/watch?v=f_Z0RLRZzWw)
 
## Screenshot
### Discord Bot
<img src="https://user-images.githubusercontent.com/94597336/227766331-dfa7d360-18d7-4014-ac6a-4fca55907d99.png">
<img src="https://user-images.githubusercontent.com/94597336/227766379-c824512e-a6f7-4ca5-9342-cc8e78d52491.png">
<img src="https://user-images.githubusercontent.com/94597336/227766408-37d733f7-c849-4cbd-9e17-0cd5800affb3.png">
<img src="https://user-images.githubusercontent.com/94597336/227766416-22ae3d91-40d9-44c0-bde1-9d40bd54c3af.png">

### Dashboard
<img src="https://github.com/ChocoMeow/Vocard/assets/94597336/53f31f9f-57c5-452c-8317-114125ddbf03">
<img src="https://github.com/ChocoMeow/Vocard/assets/94597336/b2acd87a-e910-4247-8d5a-418f3782f63f">


