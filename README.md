<img src="resources/new_logo.gif">

* JOIN Support & FAQ Discord 👉 <a href="https://discord.gg/UcxcyxS5X8"><img src="https://discord.com/assets/f9bb9c4af2b9c32a2c5ee0014661546d.png" width="18" height="18"></img></a>

```
As always, I took bits from an open source repo and rebranded it into a useful bot with detailed instructions.
Please star my repo if this contribution helped you ! Its FREEE !

Please Join Support & FAQ Discord if you have questions.

```
# Telegram to Discord Message Bot — Forward Telegram Messages to Discord 

<img src="https://img.shields.io/badge/Status-works%20after%20little%20debugging-orange"> <img src="https://img.shields.io/badge/Python%20Skill-intermediate%20-brightgreen"> 

* Advanced python users post your debug queries here : <a href="https://discord.gg/wkznBbgBFD"><img src="https://discord.com/assets/f9bb9c4af2b9c32a2c5ee0014661546d.png" width="25" height="25"></img></a>


## Description
Forwardgram is a free and open source, telegram to discord message bot. It enables one to forward messages from Multiple Telegram channels to one (or more) Telegram/Discord channels of your own. This python bot monitors multiple telegram channels. When a new message/entity is sent, it will parse the response and forward it to a discord channel using your own personalized bot. It will also forward the same message to your own Telegram channel.


### Dependencies

1. Python 3.6+ 
3. Create you own discord bot, add it to your server and retrive token. Follow Steps [here](https://www.writebots.com/discord-bot-token/).
4. Have a Telegram account with valid phone number


### Installing and Setup
1. Clone this repository
2. Open your choice of console (or Anaconda console) and navigate to cloned folder 
3. Run Command: `python3 -m pip install -r requirements.txt`.
4. Fill out a configuration file. An exmaple file can be found at `config.yml`. 


#### Filling `config.yml` file

* Add your Telegram `api_id` and `api_hash` to config.yml | Read more [here](https://core.telegram.org/api/obtaining_api_id)

* Add your `discord_bot_token` to config.yml | Read more [here](https://www.writebots.com/discord-bot-token/)

* Add the Discord channel ID you would like to log to at `discord_channel`.

* Locate the Telegram channels you would like to log and set their names at `input_channel_names`

### Running
* Run the command `python3 forwardgram.py`

```
***PLEASE NOTE:  In the first time initializing the script, you will be requried to validate your phone number using telegram API. This happens only at the first time (per session name).
```

## Authors

* Karan Kapuria
* voidbar
* Brent Stanfield (discord bot delay fix & rewrite)

<a href="https://www.buymeacoffee.com/kapuriakaran" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>


## License

This project is licensed under the MIT License - see the LICENSE.md file for details
