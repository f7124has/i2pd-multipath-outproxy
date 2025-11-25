#!/bin/sh
docker rmi -f "mymultipath:latest" || true
docker build -t "mymultipath:latest" .
