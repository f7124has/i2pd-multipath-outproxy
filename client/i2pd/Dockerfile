FROM alpine:3 AS builder

RUN apk --no-cache --virtual build-dependendencies add \
  cmake \
  make \
  gcc \
  g++ \
  binutils \
  libtool \
  libev-dev \
  check-dev \
  zlib-dev \
  boost-dev \
  build-base \
  openssl-dev \
  openssl \
  git \
  sed \
  autoconf \
  automake \
  miniupnpc \
  miniupnpc-dev

# COPY conf/ /i2pd/conf/
# COPY network/ /i2pd/network/

# install deps && build i2p binary
RUN mkdir -p /i2pd/data/addressbook \
  && mkdir /i2pd/tunnels.null \
  && mkdir /i2pd/tunnels.source.conf.d \
  && mkdir /i2pd/tunnels.conf.d \
  && mkdir /i2pd/bin

RUN cd /tmp \
  && git clone --depth 1 --branch 2.58.0 https://github.com/PurpleI2P/i2pd.git

COPY ./my.patch /tmp/i2pd/my.patch
RUN cd /tmp/i2pd && git apply my.patch

RUN cd /tmp/i2pd/build \
  && cmake -DWITH_AESNI=ON -DWITH_UPNP=ON . \
  && make -j $(nproc) \
  && strip i2pd

FROM alpine:3

RUN apk --no-cache add \
  boost-system \
  boost-filesystem \
  boost-program_options \
  openssl \
  musl-utils \
  libstdc++ \
  sed \
  miniupnpc

RUN mkdir -p /i2pd/data/addressbook \
  && mkdir /i2pd/tunnels.null \
  && mkdir /i2pd/tunnels.source.conf.d \
  && mkdir /i2pd/tunnels.conf.d \
  && mkdir /i2pd/bin

COPY --from=builder /tmp/i2pd/build/i2pd /i2pd/bin/i2pd
#COPY --from=builder /tmp/i2pd/LICENSE /i2pd/LICENSE
#COPY --from=builder /tmp/i2pd/ChangeLog /i2pd/ChangeLog
COPY --from=builder /tmp/i2pd/contrib/certificates /i2pd/data/certificates

#COPY conf/ /i2pd/conf/
#COPY network/ /i2pd/network/
#COPY htdocs/ /i2pd/htdocs/
#COPY entrypoint.sh /
# cp /i2pd/conf/addresses-initial.org.csv /i2pd/data/addressbook/addresses.csv \
#   && chmod +x /entrypoint.sh \


RUN addgroup -g 1000 i2pd \
  && adduser -u 1000 -G i2pd -s /bin/sh -h "/i2pd" -D i2pd \
  && chown -R i2pd:i2pd /i2pd \
  && chmod 0700 /i2pd/bin/i2pd \
  && mkdir -p /home/i2pd/

USER i2pd

WORKDIR "/home/i2pd/"

CMD ["/i2pd/bin/i2pd", "--datadir=/home/i2pd/data"]
