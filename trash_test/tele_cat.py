import time
from telegram import Bot


chat_id = 642411623 #замените на свое значение, подробнее ниже
bot = Bot("5718308924:AAFDDxwBvSoOXZJHOZICW75RZPLD2pSO668")


def send_random_cat():
    url = f'https://yandex.ru/images/search?from=tabbar&text=skyrim{time.time()}'
    bot.send_photo(chat_id, url)


def main() -> None:
    send_random_cat()
    print('Cat has been sent')


if __name__ == "__main__":
    main()