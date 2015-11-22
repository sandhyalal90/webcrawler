import urllib
import re

htmlfile = urllib.urlopen("https://in.finance.yahoo.com/q?s=gcz15.cmx")

htmltext = htmlfile.read()

regex = '<span id="yfs_h00_gcz15.cmx">(.+?)</span>'

pattern = re.compile(regex)

price = re.findall(pattern, htmltext)

print price 