import telegram, json, time, os
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, MessageQueue
import sentry_sdk


ver='0.2.3'
botName=f'SongID'
botVer=f'{botName} {ver}'
botAt=f'@SongIDBot'
botUsername='SongIDbot'
downloadDIR='data/downloads'


# Initialise the logger and format it's output
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
)
logger = logging.getLogger(__name__)


# Load environment environment variables
# using .get so KeyError is not raised if env var does not exist
# None is returned instead
token = os.environ.get('songid_tg_token')
devid = os.environ.get('songid_tg_devid')
devusername = os.environ.get('songid_tg_devusername')

heroku_webhook = os.environ.get('songid_heroku_webhook')
heroku_listen = os.environ.get('songid_heroku_listen')
heroku_port = os.environ.get('songid_heroku_port')

sentry_dsn = os.environ.get('songid_sentry_dsn')

# Check all required environment variables are present
for env_var in ['songid_tg_token', 'songid_tg_devid', 'songid_tg_devusername', 'songid_acr_clear_key', 'songid_acr_clear_secret', 'songid_acr_noisy_key', 'songid_acr_noisy_secret', 'songid_acr_hum_key', 'songid_acr_hum_secret']:
    if os.environ.get(env_var) == None:
        raise KeyError(f"Missing environment variable: \"{env_var}\"")

# Check if Sentry is set up
for env_var in ['songid_sentry_dsn']:
    if os.environ.get(env_var) == None:
        sentry_enabled = "False"
        print('Missing environment variable: \"{env_var}\".  Sentry integration disabled.')
    else:
        sentry_enabled = "True"

# Check if Heroku is set up
for env_var in ['songid_heroku_webhook', 'songid_heroku_listen', 'songid_heroku_port']:
    if os.environ.get(env_var) == None:
        heroku_enabled = "False"
        print('Missing environment variable: \"{env_var}\".  Heroku integration disabled.')
        break  # Break out of for loop to prevent multiple messages
    else:
        heroku_enabled = "True"

if sentry_enabled:
sentry_sdk.init(
dsn=sentry_dsn,
sample_rate=1.0,
traces_sample_rate=1.0,
attach_stacktrace=True,
with_locals=True
)


# Load data/userdata.json into the variable 'userdata'
with open('data/userdata.json') as f:
    userdata = json.load(f)




#  Initialise the required telegram bot data
u=Updater(token=token, use_context=True, request_kwargs={'read_timeout': 6, 'connect_timeout': 7})
dp = u.dispatcher



# Log the users previous message (debugging)
def logusr(update):
    if hasattr(update.message, 'text'):
        message = update.message.text
    else:
        message = '[No message]'
    logger.info(f'[@{update.effective_chat.username}][{update.effective_chat.first_name} {update.effective_chat.last_name}][U:{update.effective_chat.id}][M:{update.effective_message.message_id}]: {message}')


# Send a message to the user
def botsend(update, context, msg):
    if hasattr(update.message, 'reply_text'):
        update.message.reply_text(str(msg)+f'\n\n<i>{botAt} <code>{ver}</code></i>', parse_mode=telegram.ParseMode.HTML)

def devsend(update, context, msg):
    if '{update.message.text}' in msg:
        if hasattr(update.message, 'text'):
            msg = update.message.text
        else:
            msg = '[No message]'
    context.bot.send_message(devid, f'User @{update.effective_user.username} ({update.effective_chat.id}): \'{msg}\'')


# Send a message to the user and log the message sent
def logbotsend(update, context, msg):
    update.message.reply_text(str(msg)+f'\n\n<i>{botAt} <code>{ver}</code></i>', parse_mode=telegram.ParseMode.HTML)
    logger.info(f'[@{botUsername}][{botName}][M:{update.effective_message.message_id}]: {msg}')


# Log a message the bot has sent anonymously
def logbot(update, msg):
    logger.info(f'[@{botUsername}][{botName}][M:{update.effective_message.message_id}]: {msg}')




logger.info('Loaded: SongIDFramework')