
# Author: chris guest
# run splat script for QTH files in current dir starting with specified prefix.
import sys
import create_output
import os
import glob, getopt

receive_sensitivity = '-110'
definition='sd'

try:
    opts, args = getopt.getopt(sys.argv[1:],"s:h",["sensitivity="])
except getopt.GetoptError:
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-h"):
        definition="hd"
    elif opt in("-s","--sensitivity"):
        receive_sensitivity = int(arg)

#force sensititive to a negitive, so cli can pass positive numbers
if receive_sensitivity >= 0:
    receive_sensitivity = (0 - (receive_sensitivity))

print 'modelling with a receive sensitivity of: ' + str(receive_sensitivity) + ' dBm'


myglob = '*.qth'
#if len(sys.argv)>1:
#    myglob = sys.argv[1] + myglob

i=0
for filename in glob.glob('*.qth'):
    stub = filename[:-4]
    create_output.create(stub, receive_sensitivity, definition)
    i+=1
    if i>300:
        break

print '%d files generated.' % i

create_output.convert_kml_to_world()

myglob = 'img/*.png'
if len(sys.argv)>1:
    myglob = sys.argv[1] + myglob
i=0
for filename in glob.glob('img/*.png'):
    stub = filename[:-4]
    create_output.convert(stub, receive_sensitivity)
    i+=1
    if i>300:
        break

print '%d files generated.' % i
