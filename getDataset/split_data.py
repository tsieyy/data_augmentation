
import os, shutil
from sklearn.model_selection import train_test_split

#val_size = 0.1
#test_size = 0.2
postfix = 'jpg'
imgpath = 'VOCdevkit/JPEGImages'
txtpath = 'VOCdevkit/txt'


os.makedirs('images/train', exist_ok=True)
os.makedirs('images/val', exist_ok=True)
os.makedirs('images/test', exist_ok=True)
os.makedirs('labels/train', exist_ok=True)
os.makedirs('labels/val', exist_ok=True)
os.makedirs('labels/test', exist_ok=True)

#listdir = os.listdir(txtpath)
#train, test = train_test_split(listdir, test_size=test_size, shuffle=True, random_state=0)
#train, val = train_test_split(train, test_size=val_size, shuffle=True, random_state=0)
with open('Main/train.txt','r') as f:
    for i in f.readlines():
        i=i.strip('\n')
        shutil.copy('{}/{}.{}'.format(imgpath, i, postfix), 'images/train/{}.{}'.format(i, postfix))
        shutil.copy('{}/{}.{}'.format(txtpath, i,'txt'), 'labels/train/{}.{}'.format(i,'txt'))

with open('Main/test.txt','r') as g:
    for i in g.readlines():
        i=i.strip('\n')
        shutil.copy('{}/{}.{}'.format(imgpath, i, postfix), 'images/test/{}.{}'.format(i, postfix))
        shutil.copy('{}/{}.{}'.format(txtpath, i,'txt'), 'labels/test/{}.{}'.format(i,'txt'))


with open('Main/val.txt','r') as k:
    for i in k.readlines():
        i=i.strip('\n')
        shutil.copy('{}/{}.{}'.format(imgpath, i, postfix), 'images/val/{}.{}'.format(i, postfix))
        shutil.copy('{}/{}.{}'.format(txtpath, i,'txt'), 'labels/val/{}.{}'.format(i,'txt'))
'''

import os, shutil
from sklearn.model_selection import train_test_split

test_size = 0.2
val_size = 0.1

postfix = 'jpg'
imgpath = 'VOCdevkit/JPEGImages'
txtpath = 'VOCdevkit/txt'

os.makedirs('images/train', exist_ok=True)
os.makedirs('images/val', exist_ok=True)
os.makedirs('images/test', exist_ok=True)
os.makedirs('labels/train', exist_ok=True)
os.makedirs('labels/val', exist_ok=True)
os.makedirs('labels/test', exist_ok=True)

listdir = os.listdir(txtpath)
train, test = train_test_split(listdir, test_size=test_size, shuffle=True, random_state=0)
train, val = train_test_split(train, test_size=val_size, shuffle=True, random_state=0)

for i in train:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'images/train/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), 'labels/train/{}'.format(i))

for i in val:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'images/val/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), 'labels/val/{}'.format(i))

for i in test:
    shutil.copy('{}/{}.{}'.format(imgpath, i[:-4], postfix), 'images/test/{}.{}'.format(i[:-4], postfix))
    shutil.copy('{}/{}'.format(txtpath, i), 'labels/test/{}'.format(i))
     
'''