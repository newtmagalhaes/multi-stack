from dataclasses import dataclass
from os import environ


@dataclass
class Config:
    # App
    ENV_NAME: str
    SECRET_KEY: str
    _ALLOWED_HOSTS: str
    _SECRET_KEY_FALLBACKS: str
    # db
    DB_HOST: str
    DB_PORT: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_NAME: str

    @property
    def DEBUG(self) -> bool:
        return self.ENV_NAME == 'dev'

    @property
    def ALLOWED_HOSTS(self) -> list[str]:
        return self._ALLOWED_HOSTS.split()

    @property
    def SECRET_KEY_FALLBACKS(self) -> list[str]:
        return self._SECRET_KEY_FALLBACKS.split('|')

    def get_default_database(self) -> dict:
        return {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': self.DB_NAME,
            'USER': self.DB_USERNAME,
            'PASSWORD': self.DB_PASSWORD,
            'HOST': self.DB_HOST,
            'PORT': self.DB_PORT,
        }


config = Config(
    ENV_NAME=environ['ENV_NAME'],
    SECRET_KEY=environ['SECRET_KEY'],
    _ALLOWED_HOSTS=environ['ALLOWED_HOSTS'],
    _SECRET_KEY_FALLBACKS=environ['SECRET_KEY_FALLBACKS'],
    DB_NAME=environ['DB_NAME'],
    DB_HOST=environ['DB_HOST'],
    DB_PORT=environ['DB_PORT'],
    DB_USERNAME=environ['DB_USERNAME'],
    DB_PASSWORD=environ['DB_PASSWORD'],
)
