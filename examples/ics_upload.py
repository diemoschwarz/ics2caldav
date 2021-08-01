#!/sw/bin/python3

import os
import sys
from ics2caldav import Ical2CalDav

''' patching doesn't work anymore with current ics module as of 07-2021
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

passed = 0
failed = 0
failedlist = []

for ic in ics:
    print('try %d of %d:' % (passed + failed, len(ics)), ic)
    try:
        Ical2CalDav.parse_args(args + ['-i', ic])
    except Exception as e:
        print("can't import %s: %s" % (ic, e))
        failedlist.append(ic)
        failed = failed + 1
    else:  
        passed = passed + 1

print('---------finished %d of %d\n' % (passed + failed, len(ics)))
print('-------- %d of %d failed:\n' % (failed, len(ics)), failedlist)
print('\n-------- %d of %d uploaded\n' % (passed, len(ics)))
