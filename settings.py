"""Модуль с конфигурационными классами."""
from environs import Env
from dataclasses import dataclass

# Исправить доку!!!
@dataclass
class Bots:
    """
    Датакласс.

    Содержит в себе параметры по подключению токена бота,
    а так же параметров подключения к базе данных
    (в данном случае PostgreSQL).
    """

    bot_token: str
    admin_id: int


@dataclass
class Settings:
    """
    Датакласс.

    Содержит в себе параметр бота.
    """

    bots: Bots


def get_settings(path: str):
    """Функция получения параметров из файла input."""
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("TOKEN"),
            admin_id=env.int('ADMIN_ID'),
        ),
    )


settings = get_settings('input')
