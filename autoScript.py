import os
from os import listdir
from os.path import isfile, join
mypath = "."
print "[+] Path Set"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(str(mypath),f)) ]
x = len(onlyfiles)
print "[+] Files Counted: "+str(x)
a=0
print "[+] Starting..."
print "[+] Generating Sums"
os.system("exiftool * > exiftool.output")
os.system("touch ./sums.md5sum")
os.system("touch ./sums.sha1sum")
os.system("md5sum * > sums.md5sum")
os.system("sha1sum * > sums.sha1sum")


while a < x:
	syntax = "hd '"+onlyfiles[a]+"' > '"+onlyfiles[a]+".hex'"
	#print "Hex Completed for file:"+str(a+1)
	os.system(syntax)
	syntax = "strings '"+onlyfiles[a]+"' | grep '|' > '"+onlyfiles[a]+".strings-output'"
	#print "strings completed for file: "+str(a+1)
	os.system(syntax)
	#print "Completed "+str(a+1)+" file(s)"
	a=a+1

print "[+] Completed "+str(a)