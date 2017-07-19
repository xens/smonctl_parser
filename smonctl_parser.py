#!/usr/bin/python

import os
import re
import json
import subprocess

proc = subprocess.Popen(['/usr/sbin/smonctl', '-j'], stdout=subprocess.PIPE)
smonctl_output = json.loads(proc.stdout.read())

for i in smonctl_output:
   name = i['name'].lower()
   descr = i['description']
   state = i['state']
   type = i['type']

   if i['state'] == "OK":
      value = 1
   elif i['state'] == "ABSENT":
      value == -1
   elif i['state'] == "BAD":
      value == 0

   print("# HELP smon_%s %s" % (type, descr))
   print("# TYPE smon_%s gauge" % type)
   print("smon_%s{name='%s'} %s" % (type,name,value))
