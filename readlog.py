#!/usr/bin/env python
import re

source = open("/Users/simonvas/sonic.txt", "r")
output = open("/Users/simonvas/output.txt", "w")
bps=0
ln=0
for line in source:
    if re.match ("(.*)(rx-bits-per-second:)(.*)", line) or re.match ("(.*)(tx-bits-per-second:)(.*)", line):
        print >> output, line,
        print line
        bpsgrp = re.search ('([0-9]+.[0-9])([A-Za-z]bps)', line)
        symb = bpsgrp.group(2)
        if symb.lower() == "mbps":
            bps += float(bpsgrp.group(1)) * 1000000
        elif symb.lower() == 'kbps':
            bps += float(bpsgrp.group(1)) * 1000
        elif symb.lower() == 'bps':
            bps += float(bpsgrp.group(1))
        ln += 1
        
average = bps / ln
print bps, ln, average