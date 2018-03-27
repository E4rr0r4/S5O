
import requests
import sys
import os

def     block_cutter (string, int_start, int_end):
        ndata = ""
        while (int_start <= int_end):
            ndata += string[int_start]
            int_start += 1
        return ndata


argc = len(sys.argv)
if (argc != 2):
    exit()
else:

    ca = 0
    cb = 0
    i = 0

    nurl = "http://www.nitrxgen.net/md5db/"+str(sys.argv[1])
    r = requests.get(nurl)
    hash_value = r.text.encode('utf-8')
    if (hash_value == ''):
        nurl = "https://www.google.com/search?q="+str(sys.argv[1])+" plain:"
        r = requests.get(nurl)
        data = r.text.encode('utf-8')
        nurl = "https://www.google.com/search?q=list intext:Hash:"+str(sys.argv[1])+" & intext:Plain:"
        r = requests.get(nurl)
        data += r.text.encode('utf-8')
        while (i < len(data)-1):
                if (data[i] == 'H'):
                    ca = i
                    while (i < len(data)-1 and data[i] != ':'):
                        i += 1
                    cb = i
                    tmp = block_cutter(data, ca, cb)
                    if (tmp == 'Hash:'):
                        while (i < len(data)-1 and data[i] != 'A'):
                            i += 1
                        cb = i
                        found = block_cutter(data, ca, cb)
                        hash_view = block_cutter(found, found.find('<b>')+3, found.find('</b>')-1)
                        if (hash_view == sys.argv[1]):
                            hash_value = block_cutter(found, found.find('<b>Plain</b>:')+14, found.find('. A')-1)
                            if (hash_value != ''):
                                print (hash_value)
                        
                i += 1
    else:
        print (hash_value)
