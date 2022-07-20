import urllib.request, urllib.parse, urllib.error

f_handle = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in f_handle:
    print(line.decode().strip())