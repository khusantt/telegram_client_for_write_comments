from telethon import TelegramClient, events, types
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.channels import GetFullChannelRequest
import asyncio
import random
import time
import os


# Ваши данные API ID и API Hash, которые можно получить на https://my.telegram.org
api_id = 'your_id'
api_hash = 'your_hash'

# Ваш номер телефона и сессия
phone_number = 'your_phone'
session_name = '/home/redos/podpiska-otpiska-group/session_name.session'

# 🔹 Файл для хранения кода аутентификации
AUTH_CODE_FILE = "/home/redos/auth_code.txt"

# Создаем клиент
client = TelegramClient(session_name, api_id, api_hash)


async def authenticate():
    """ Функция авторизации с запросом кода """
    while True:
        try:
            while True:
                # 🔹 Ожидаем код из файла
                if os.path.exists(AUTH_CODE_FILE):
                    with open(AUTH_CODE_FILE, "r") as file:
                        auth_code = file.read().strip()

                    if auth_code:
                        print(f"📥 Используем код: {auth_code}")
                        await client.sign_in(phone_number, code=auth_code)
                        print("✅ Успешная аутентификация!")
                        return
                print("⏳ Ожидание кода...")
                time.sleep(5)

        except Exception as e:
            print(f"❌ Ошибка при аутентификации: {e}")

        print("🔄 Повторная попытка через 30 секунд...")
        time.sleep(210)  # Ждем 210 секунд перед новой попыткой

# Функция для чтения каналов из файла
def read_channels_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

# Функция для добавления канала в черный список
def add_to_blacklist(channel, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(channel + '\n')


async def main():
    await client.connect()

    if not await client.is_user_authorized():
        print("🔑 Бот не авторизован, начинаем процесс входа...")
        # 🔹 Отправляем запрос на получение кода
        print("📩 Запрашиваем код подтверждения у Telegram...")
        await client.send_code_request(phone_number)
        print("✅ Код отправлен! Введите его в Telegram и сохраните в auth_code.txt")
        time.sleep(240)
        await authenticate()

    print("✅ Скрипт запущен и подписывается на каналы...")

    i=0
    #Реализация подписки на группы
    channels = read_channels_from_file('/home/redos/podpiska-otpiska-group/sort-tg-food-baza')
    for channel in channels:
        try:
            i+=1
            time.sleep(5)
#начало проверки доступности комментов
            # Получаем полную информацию о группе
            full_chat = await client(GetFullChannelRequest(channel))
#            print(f"Log: {full_chat.full_chat.linked_chat_id}")
            # Проверяем, разрешены ли комментарии
            if full_chat.full_chat.linked_chat_id is not None:
                print(f"{i}) Комментарии разрешены.")
                print(f"ID чата для комментариев: {full_chat.full_chat.linked_chat_id}")
                await client(JoinChannelRequest(channel))
                print(f"Подписался на канал {channel}.")
            else:
                print(f"{i}) Комментарии не разрешены для канала {channel}")
                add_to_blacklist(channel, '/home/redos/podpiska-otpiska-group/blacklist')
                print(f"Канал {channel} добавлен в blacklist.")
#конец проверки доступности комментов
        except Exception as e:
            print(f"Не удалось подписаться на канал {channel}: {e}")

if __name__ == "__main__":
    asyncio.run(main())
