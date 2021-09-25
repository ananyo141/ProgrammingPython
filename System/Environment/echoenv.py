#!/usr/bin/env python
# print the username from the 'USER' environment variable
import os

print("Hello there", os.environ.get('USER'), '!')
