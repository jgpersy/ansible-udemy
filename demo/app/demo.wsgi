#!/usr/bin/python3
activate_this = '/var/www/demo/.venv/bin/activate_this.py'
exec(open(activate_this, dict(__file__=activate_this)).read())

import os
os.environ['DATABASE_URI'] = 'mysql://demo:demo@db01/demo'

import sys
sys.path.insert(0, '/var/www/demo')

from demo import app as application
