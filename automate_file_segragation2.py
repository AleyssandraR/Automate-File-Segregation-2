import os
import shutil

from_dir='C:/Users/user/Downloads'
to_dir='C:/Users/user/Downloads/downloadImages'

listOfFiles=os.listdir(from_dir)

for fileName in listOfFiles:
    name,ext=os.path.splitext(fileName)
    
    if(ext==''):
        continue

    if(ext in ['.txt', '.doc', '.docx', '.pdf']):
        path1=from_dir+'/'+fileName
        path2=to_dir+'/'+'documents_file'
        path3=to_dir+'/'+'documents_file'+'/'+fileName

        if(os.path.exists(path2)):
            print('Moving'+fileName+'...')
            shutil.move(path1,path3)

        else:
            os.makedirs(path2)
            print('Moving'+fileName+'...')
            shutil.move(path1,path3)