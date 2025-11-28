# i2pd-multipath-outproxy
Multipath socks5 outproxy for i2p network, for increase bandwidth, speed and stability

Demo video: https://webm.red/view/9A6I.webm

# Basic requirements
- VPS (for outproxy)
- Computer which you will use for anonymous access to the internet

# Minimal basic setup
## VPS setup (execute it on your VPS)
- `sudo apt install git docker docker-compose` Go to the your VPS and install requirements
- `git clone https://github.com/f7124has/i2pd-multipath-outproxy.git` Clone the repo
- `cd i2pd-multipath-outproxy/server/i2pd && ./scripts/build.sh && sudo chown -R 1000:1000 ./data && ./scripts/run.sh` Build docker image for i2pd and start it
- `lynx 'http://127.0.0.1:7070/?page=i2p_tunnels'` Find your `.b32.i2p` address here. Save it, you will need it later to launch the client (looks like `tr26d3g4hviaqufmld6r16ikpdvjvd6g5qwdemnbuffck2fh663a.b32.i2p` and called `outproxy`)
- `cd ../multipath && ./scripts/build.sh && ./scripts/run.sh` Build aggligator (multipath) docker image and haproxy and start it
- `docker ps` Verify is all containers are started and work normaly

## Your computer setup (client side)
- `sudo apt install git docker docker-compose` Setup requirements
- IMPORTANT! Make sure Docker is accessible from a regular system user without privileges. (non root)! Execute `docker ps` for verify it
- `git clone https://github.com/f7124has/i2pd-multipath-outproxy.git` Clone the repo
- `cd i2pd-multipath-outproxy/client/i2pd && ./scripts/build.sh` Build docker image
- In file `gen.py` change `[CENSORED].b32.i2p` to the your server `.b32.i2p` address, it should looks like that: `tr26d3g4hviaqufmld6r16ikpdvjvd6g5qwdemnbuffck2fh663a.b32.i2p`
- `python3 gen.py > data/tunnels.conf` Generate a i2pd tunnels config file using `gen.py` script
- `sudo chown -R 1000:1000 ./data` Change `data` folder permissions (required for correct docker image working)
- `./scripts/run.sh` Start the i2pd container
- `cd ../multipath && ./scripts/build.sh && ./scripts/run.sh` Go back to multipath, build docker image and start the container
- `docker ps` Verify is the all container are started and works.
- Proxy `socks5` should be started on `0.0.0.0:1081` (haproxy) and `127.0.0.1:1080` (aggligator)
- `curl --socks5-hostname 127.0.0.1:1080 1.1.1.1 -v` Try to use it!

## How it works
A typical outproxy is limited by the throughput of a single tunnel used for data transfer. As a user, you have no influence on the tunnel's throughput because it is built through other nodes in the network, which you have no control over. Consequently, your connection speed is almost always random and often slow.

Aggligator (https://github.com/surban/aggligator) allows you to split your single TCP connection into multiple ones, essentially allowing you to use multiple tunnels for a single outproxy. Their speeds will be combined. The default implementation in this repository uses 32 tunnels for data transfer, which can potentially increase download speeds several times over.

You can easily surf the internet and use popular apps like YouTube while remaining anonymous.

# Thanks so much
- https://github.com/PurpleI2P/i2pd
- https://github.com/surban/aggligator
- Also guys from http://irc.ilita.i2p/
