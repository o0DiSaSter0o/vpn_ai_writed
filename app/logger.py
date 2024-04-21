import logging
from logging.handlers import RotatingFileHandler

# Создание логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создание обработчика для записи логов в файл
file_handler = RotatingFileHandler('bot.log', maxBytes=10_000_000, backupCount=5)
file_handler.setLevel(logging.INFO)

# Создание форматтера для логов
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика к логгеру
logger.addHandler(file_handler)

"""
Этот код создает логгер с именем __name__, устанавливает уровень логирования INFO и настраивает обработчик для записи логов в файл bot.log. Файл логов будет ротироваться (создаваться новый файл) при достижении размера 10 МБ, и будет сохранено максимум 5 архивных файлов логов.

Теперь вы можете импортировать этот логгер в другие файлы и использовать его для логирования:

python

Copy code
from logger import logger

# Пример использования логгера
logger.info('Бот запущен')
Вы можете изменить уровень логирования, формат сообщений и другие параметры в соответствии с вашими потребностями.

После добавления логирования рекомендуется использовать его во всех критических местах вашего кода, таких как обработка команд, взаимодействие с базой данных, вызовы API и т.д."""