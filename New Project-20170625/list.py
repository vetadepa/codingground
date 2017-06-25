#

mylist = ["Ramana", 31, 5.7, "Mar30, 1986", "ORACLE"]
wifelist = ["Aruna", 26, 5.0, "Mar10, 1991", "Home Maker"]

print mylist + wifelist
print "Names : " + mylist[0] + " " + wifelist[0]
print mylist[1:] + wifelist[1:]

wifelist[4] = "Housewife"
print wifelist[4]