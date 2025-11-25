# i2pd-multipath-outproxy
Multipath socks5 outproxy for i2p network, for increase bandwidth, speed and stability

Demo video: https://webm.red/view/9A6I.webm

# Начальные требования
- VPS (для запуска outproxy)
- Основной хост с которого вы будете выходить в интернет анонимно

# Минимальная пошаговая установка
## Настройка VPS
- Зайдите на сервер и установите зависимости (`sudo apt install git docker docker-compose`)
- На VPS выполните `git clone https://github.com/f7124has/i2pd-multipath-outproxy.git`
- VPS: `cd i2pd-multipath-outproxy/server/i2pd && ./scripts/build.sh && sudo chown -R 1000:1000 ./data && ./scripts/run.sh`
- Узнайте ваш `.b32.i2p` адрес в сети `lynx http://127.0.0.1:7070/?page=i2p_tunnels`. Сохраните адрес вашего сервера, он понадобится вам позже для запуска клиента (будет выглядеть примерно вот так `tr26d3g4hviaqufmld6r16ikpdvjvd6g5qwdemnbuffck2fh663a.b32.i2p` и называтся `outproxy`)
- VPS: `cd ../multipath && ./scripts/build.sh && ./scripts/run.sh`
- Проверьте что все сервисы запущены и работают нормально `docker ps`

## Настройка вашего компьютера
- Установите `git docker docker-compose`
- ВАЖНО! Убедитесь что docker доступен от обычного пользователя системы без привелегий (non root)! Выполните `docker ps` для проверки
- На выполните `git clone https://github.com/f7124has/i2pd-multipath-outproxy.git`
- `cd i2pd-multipath-outproxy/client/i2pd && ./scripts/build.sh` Соберите образ
- В файле `gen.py` замените `[CENSORED].b32.i2p` на адрес вашего сервера, он должен выглядеть как то так: `tr26d3g4hviaqufmld6r16ikpdvjvd6g5qwdemnbuffck2fh663a.b32.i2p`
- Создайте конфиг для тунелей, выполните `python3 gen.py > data/tunnels.conf`
- Измените привелегии папки на нужные `sudo chown -R 1000:1000 ./data`
- Запустите контейнер `./scripts/run.sh`
- Вернитесь к multipath `cd ../multipath`
- Соберите образ `./scripts/build.sh`
- Запустите `./scripts/run.sh`
- Проверьте что все сервисы работают (`docker ps`)
- Прокси `socks5` должна быть запущена на `0.0.0.0:1081` и `127.0.0.1:1080`
- Проверьте что все работает `curl --socks5-hostname 127.0.0.1:1080 1.1.1.1 -v`

# Отедельное спасибо
- https://github.com/PurpleI2P/i2pd
- https://github.com/surban/aggligator
- А так же ребятам из чата `irc.ilita.i2p`
