import os
import shutil
import time
def 
path = input('enter path name')
path = path+'/'
time = input('enter todays date')
time.time()
if os.path.exists(path):
    os.walk(path)
elif:
    print('please enter correct path')
joinfiles = os.path.join
dt = time.ctime()
stats = os.stat(path)
file = os.listdir(path)
for i in file:
    shutil.rmtree()