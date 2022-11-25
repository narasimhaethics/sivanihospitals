import os
import sys
import subprocess
import json
from subprocess import Popen, PIPE, STDOUT

#pp = os.system("python po.py")
#dd = sys.stdout.write('ai')
def ab(abc):

     c=''
     process = os.popen('cd ..')
     process = os.popen('echo '+abc+' | python3 po.py')


     preprocessed = process.read()



     pp = list(preprocessed.split(' '))
     #cc = pp[29:]



     stra = ' '.join(pp)

     print (stra)

     with open('data.json', 'a') as outfile:
          json.dump(abc, outfile)
          json.dump(stra, outfile)


     process.close()




     return stra



     #subprocess.call(['python' '/home/office/lop.py'])
