import os
import shutil
from os.path import join

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

# BY MONTHLY - DONE - transfer files into bank on 1st of each month, windows task schedule for evening of the 1st every month.

directory = '/Users/David/Toshiba/2020'

os.chdir('/Users/David/Toshiba/2020')

folder_name = ['jan' , 'feb', 'march' , 'april' , 'may' , 'june' , 'july' , 'august' , 'sept' , 'octo' , 'nov', 'dec']

for x in range(0 , 12):
    if not os.path.exists(folder_name[x]):  
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

for root, subdirs, vfiles in os.walk(directory):
    for f in vfiles:
        if (f.strip()[5:7]) == "01" in f:
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



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# BY WEEKLY AND MONTHLY - transfer files into bank monday morning, windows task schedule for monday evening.

directory = '/Users/David/Toshiba/2020' 

os.chdir('/Users/David/Toshiba/2020')

folder_name = ['jan' , 'feb' , 'march' , 'april' , 'may' , 'june' , 'july' , 'aug' , 'sept' , 'octo' , 'nov' , 'dec']

for x in range(0 , 12):                            
    if not os.path.exists(folder_name[x]): 
        os.makedirs(folder_name[x])   

root = '/Users/David/Documents/newfolder'
jan = '/Users/David/Documents/newfolder/jan'
feb = '/Users/David/Documents/newfolder/feb'
march = '/Users/David/Documents/newfolder/march'
april = '/Users/David/Documents/newfolder/april'
may = '/Users/David/Documents/newfolder/may'
june = '/Users/David/Documents/newfolder/june'
july = '/Users/David/Documents/newfolder/july'
aug = '/Users/David/Documents/newfolder/aug'
sept = '/Users/David/Documents/newfolder/sept'
octo = '/Users/David/Documents/newfolder/octo'
nov = '/Users/David/Documents/newfolder/nov'
dec = '/Users/David/Documents/newfolder/dec'



month = [jan , feb , march , april , may , june , july , aug , sept , octo , nov , dec]

for y in month:
    os.chdir(y)
    path = os.path.join(root,y)
    wfolder_name = ['week1' , 'week2', 'week3' , 'week4']
    for z in range(0 , 4):
                if not os.path.exists(wfolder_name[z]):  
                    os.makedirs(wfolder_name[z])