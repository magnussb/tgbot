from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1746370175  # my telegram ID
    OWNER_USERNAME = "mmagnusb"  # my telegram username
    API_KEY = "1925846421:AAFONrpnhNuT_8SrbLUtxqEAwZACct4Hy4E"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'mongodb+srv://dbUser:<password>@cluster0.4lsq6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'  # sample db credentials
    MESSAGE_DUMP = '-1234567890' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [679686531, 1746370175]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
