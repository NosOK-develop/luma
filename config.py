# config.py
import os

# Пытаемся взять ключ из переменной окружения хостинга.
# Если её там нет, берется дефолтная строка (для локального ПК).
FLASK_SECRET_KEY = os.environ.get(
    'FLASK_SECRET_KEY', 
    'super_cool_mega_kruti_nerealno_prekrasni_messenger_for_obmen_messages_and_have_fun_Luma_is_so_cool) 12345678909876532147321546545776289216543628791826754683792183657'
)
