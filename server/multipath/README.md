Докер версия для Aggligator(https://github.com/surban/aggligator) и haproxy.

# Первый запуск
- Собираем контейнер `./scripts/build.sh`
- Модифицируем команду в `docker-compose.yml` (опционально)
- Модифицируем конфиг Aggligator `multipath.cfg` (опционально)
- Запускаем `./scripts/run.sh`

# Папка `scripts`
- Старт через `./scripts/run.sh`
- Выключение `./scripts/stop.sh`
- Экспорт docker образа через `./scripts/export.sh`, эта команда создаст файл `multipath_image.tar`
- Импорт образа через `./scripts/import.sh image_name.tar`