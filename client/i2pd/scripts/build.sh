#!/bin/sh
docker rmi -f "myi2pd:latest" || true
docker build -t "myi2pd:latest" .
