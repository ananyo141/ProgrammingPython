#!/usr/bin/env python
# show current shell USER variable
# change it to bob, then arthur, then input and show each time

import os

os.chdir('./Environment')
os.system('python echoenv.py')
os.environ['USER'] = 'Bob'
os.system('python echoenv.py')
os.environ['USER'] = 'Arthur'
os.system('python echoenv.py')
os.environ['USER'] = input("? ")
print(os.popen('python echoenv.py').read())
