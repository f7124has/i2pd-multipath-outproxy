FROM debian:latest

RUN mkdir -p /multipath
COPY ./agg-tunnel /multipath/agg-tunnel
RUN chmod +x /multipath/agg-tunnel
CMD ["/multipath/agg-tunnel", "--help"]
