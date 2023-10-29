from InflexMusic.core.bot import Inflex
from InflexMusic.core.dir import dirr
from InflexMusic.core.git import git
from InflexMusic.core.userbot import Userbot
from InflexMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Inflex()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
