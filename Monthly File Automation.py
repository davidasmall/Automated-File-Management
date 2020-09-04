import os
import shutil

# Have a pre made year folder first
# My raw files are formatted like this (default on phone): VID_yyyymmdd_nnnnnn - n can be any number (represents video no.)

print('--------------------------------')
print('os walk part (grabbing all the files from folders)')
print()
#from the phone to the ext hardrive 

old_dir = '/Users/David/phone/huawei p20 pro'          
new_dir = '/Users/David/Toshiba/2020'           
        
for root, subdirs, files in os.walk(old_dir):
    for f in files:
        if (f.strip()[0:3]) == "VID" in f:  
            path = os.path.join(root , f)  
            shutil.move(path, new_dir) 

'''
#for new phone samsung
for root, subdirs, files in os.walk(old_dir):
    for f in files:
        file_name, file_ext = os.path.splitext(f)
        if file_ext == ".mp4" in f:
            path = os.path.join(root , f)  
            shutil.move(path, new_dir)
'''

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('--------------------------------')
print('renaming part')
print()
# files now in ext hardrive and renaming

os.chdir('/Users/David/Toshiba/2020')  

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f) 
    f_title, ddate, v_num = file_name.split('_')
    
    date = (ddate + v_num)  

    "yyyymmdd"
    y_date = date.strip()[0:4]
    m_date = date.strip()[4:6]
    d_date = date.strip()[6:8]
    v_num = date.strip()[8:14]

    new_name = '{}-{}-{}-{}'.format(y_date, m_date, d_date, v_num)

    os.rename(f , new_name + file_ext) 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

print('--------------------------------')
print('Moving files to correct places part')
print()

from os.path import join

# 1. List out all the files inside folder
# 2. create new folders
# 3. Move the files into the newly created folders based on filename.

#1
directory = '/Users/David/Toshiba/2020'  #insert location of all vid files.

names = os.listdir(directory)  #this will list out all the files and save it in a list.

#2
folder_name = ['jan' , 'feb', 'march' , 'april' , 'may' , 'june' , 'july' , 'august' , 'sept' , 'octo' , 'nov', 'dec']

# As an error handling technique we need the following.
for x in range(0 , 12):
    if not os.path.exists(folder_name[x]):  #if this folder does not exist we go ahead and make the folder. But if this path and folder already exist then it won't.
        os.makedirs(folder_name[x])         


jan = '/Users/David/Toshiba/2020/jan'
feb = '/Users/David/Toshiba/2020/feb'
march = '/Users/David/Toshiba/2020/march'
april = '/Users/David/Toshiba/2020/april'
may = '/Users/David/Toshiba/2020/may'
june = '/Users/David/Toshiba/2020/june'
july = '/Users/David/Toshiba/2020/july'
aug = '/Users/David/Toshiba/2020/aug'
sept = '/Users/David/Toshiba/2020/sept'
octo = '/Users/David/Toshiba/2020/octo'
nov = '/Users/David/Toshiba/2020/nov'
dec = '/Users/David/Toshiba/2020/dec'

#3
for root, subdirs, vfiles in os.walk(directory):
    for f in vfiles:
        weekday = int(f.strip()[8:10])
        if ((f.strip()[5:7]) == "01" in f):
            path = os.path.join(root , f) 
            shutil.move(path, jan)
        elif (f.strip()[5:7]) == "02" in f:
            path = os.path.join(root , f) 
            shutil.move(path, feb)
        elif (f.strip()[5:7]) == "03" in f:
            path = os.path.join(root , f) 
            shutil.move(path, march)
        elif (f.strip()[5:7]) == "04" in f:
            path = os.path.join(root , f) 
            shutil.move(path, april)
        elif (f.strip()[5:7]) == "05" in f:
            path = os.path.join(root , f) 
            shutil.move(path, may)
        elif (f.strip()[5:7]) == "06" in f:
            path = os.path.join(root , f) 
            shutil.move(path, june)
        elif (f.strip()[5:7]) == "07" in f:
            path = os.path.join(root , f) 
            shutil.move(path, july)
        elif (f.strip()[5:7]) == "08" in f:
            path = os.path.join(root , f) 
            shutil.move(path, aug)
        elif (f.strip()[5:7]) == "09" in f:
            path = os.path.join(root , f) 
            shutil.move(path, sept)
        elif (f.strip()[5:7]) == "10" in f:
            path = os.path.join(root , f) 
            shutil.move(path, octo)
        elif (f.strip()[5:7]) == "11" in f:
            path = os.path.join(root , f) 
            shutil.move(path, nov)
        elif (f.strip()[5:7]) == "12" in f:
            path = os.path.join(root , f) 
            shutil.move(path, dec)