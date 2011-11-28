#!/usr/bin/python

import sys
import os
import datetime

ENV_VAR = 'PROJECT_ENV_TYPE'
if ENV_VAR == 'PROJECT_ENV_TYPE':
    raise Exception, 'please define your environment variable'

ENVIRONMENT_TYPE = os.environ.get(ENV_VAR)
if not ENVIRONMENT_TYPE:
    raise Exception, 'Must set ENVIRONMENT_TYPE via environment variable (%s)' % ENV_VAR

# Import shared settings across all environment types
from configurations.settings_global import *

try:
    settings_module = __import__('configurations.settings_%s' % ENVIRONMENT_TYPE, globals(), locals(),  ['*'])
except ImportError:
    raise Exception("Invalid environment type: " + ENVIRONMENT_TYPE)
try:
    attributes = settings_module.__all__
except AttributeError:
    attributes = dir(settings_module)
for attr in attributes:
    if not attr.startswith('__'):
        globals()[attr] = getattr(settings_module, attr)

if __name__ == '__main__':
    print ENVIRONMENT_TYPE
