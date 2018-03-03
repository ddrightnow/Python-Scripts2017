import os

#def rename_files():

    

# This would print all the files and directories
dirs = os.listdir(r"C:\Users\Dmob\Desktop\ANDROID DEVELOPMENT\python\work\prank" )

#for file in dirs:
   # path = r"C:\Users\Dmob\Desktop\ANDROID DEVELOPMENT\python\work\prank"
    #print (dirs)
def rename_files():
    filelist = os.listdir(r"C:\Users\Dmob\Desktop\ANDROID DEVELOPMENT\python\work\prank" )
    print (filelist)
    
    savedpath = os.getcwd()
    print(savedpath)
    savedpath = os.chdir(r"C:\Users\Dmob\Desktop\ANDROID DEVELOPMENT\python\work\prank")
    print(savedpath)
    for filename in filelist:
        #os.rename(filename, filename.strip("0123456789"))
        os.rename(str.filename, str.filename.translate(str.maketrans('', '', '1234567890'))
        #break;

rename_files()

#old_file = os.path.join("directory", "a.txt")
#new_file = os.path.join("directory", "b.kml")
#os.rename(old_file, new_file)
#os.rename(filename[], filename[7:])


    
   # a = os.listdir(r"C:\Users\Dmob\Desktop\ANDROID DEVELOPMENT\python\work\prank")
   # print(a)
    #with disable_file_system_redirection():
     #   print(a)
    #print (a)

#(rename_files()) 
