from configparser import ConfigParser
from functools import cache

CONFIG_FILE_PATH_FOR_LOCAL = "config/application_conf.ini"

"amqp://admin:admin@localhost:7010"


@cache
class AppSettings:
    def __init__(self):
        self.settings = None
        self.setup()
        self.API_PORT = self.settings.get("app", "api_port")

        self.REDIS_HOST = self.settings.get("messaging", "redis_host")
        self.REDIS_PORT = self.settings.get("messaging", "redis_port")
        self.RABBITMQ_HOST = self.settings.get("messaging", "rabbitmq_host")
        self.RABBITMQ_PORT = self.settings.get("messaging", "rabbitmq_port")
        self.RABBITMQ_USER = self.settings.get("messaging", "rabbitmq_user")
        self.RABBITMQ_PASSWORD = self.settings.get("messaging", "rabbitmq_password")
        self.BACKEND_URL = f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"
        self.BROKER_URL = f"amqp://{self.RABBITMQ_USER}:{self.RABBITMQ_PASSWORD}@{self.RABBITMQ_HOST}:{self.RABBITMQ_PORT}"
        self.DEFAULT_QUEUE = "celery_queue"

    def setup(self):
        config_file_to_use = CONFIG_FILE_PATH_FOR_LOCAL
        self.settings = ConfigParser()
        self.settings.read(config_file_to_use)


APP_SETTINGS = AppSettings()
