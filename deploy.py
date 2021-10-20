#!/usr/bin/python3

from os import environ, system
Port = int(environ.get("PORT", 5000))

system("docker-compose up")
