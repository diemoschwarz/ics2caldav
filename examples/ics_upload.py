#!/sw/bin/python3

import os
import sys
from ics2caldav import Ical2CalDav

''' patching doesn't work anymore with current ics module
print(sys.path)
sys.path.append(os.path.abspath('../ics2caldav'))
print(sys.path)

from patches import patch_module_caldav, patch_module_ics

# fix needed for redmine Redmics plugin
patch_module_caldav()
patch_module_ics()
'''

Ical2CalDav.config_logger()

args = []
ics  = []

# split out ics args
for arg in sys.argv[1:]:
    (_, ext) = os.path.splitext(arg)
    if ext == '.ics':
        ics.append(arg)
    else:
        args.append(arg)
    
#print(args)
#print(ics)

for ic in ics:
    print('try', ic)
    try:
        Ical2CalDav.parse_args(args + ['-i', ic])
    except Exception as e:
        print("can't import %s: %s" % (ic, e))
        
