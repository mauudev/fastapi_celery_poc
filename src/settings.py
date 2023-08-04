import os
from configparser import ConfigParser
from functools import cache

CONFIG_FILE_PATH_FOR_LOCAL = "config/application_conf.ini"
CONFIG_FILE_PATH_FOR_DOCKER = "config/docker_application_conf.ini"


@cache
class AppSettings:
    def __init__(self):
        self.settings = None
        self.setup()
        self.API_HOST = self.settings.get("app", "api_host")
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
        config_file = CONFIG_FILE_PATH_FOR_LOCAL
        is_docker_env = os.getenv("DOCKER_ENV")

        if is_docker_env:
            print(f"Using docker config file {CONFIG_FILE_PATH_FOR_DOCKER}")
            config_file = CONFIG_FILE_PATH_FOR_DOCKER
        else:
            print(f"Using local config file {CONFIG_FILE_PATH_FOR_LOCAL}")

        self.settings = ConfigParser()
        self.settings.read(config_file)


APP_SETTINGS = AppSettings()
