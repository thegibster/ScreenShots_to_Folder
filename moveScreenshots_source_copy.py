import os, re, shutil

print(os.getcwd())
print("parent directory is", os.path.exists("parent_dir"))


file_path = "parent_dir/tmp_file_to_be_deleted.txt"
user_dir = "~/Desktop/"
screenshotRegex = re.compile (r'Screen Shot+')
# try:
#     f = open(file_path, 'w')
#     f.close()
#     print()
#     print('Content of "parent_dir" after creating the file:')
#     print(os.listdir("parent_dir"))
# except FileNotFoundError as exception_object:
#     print("Cannot file file:", exception_object)
# except PermissionError as exception_object:
#     # this is for if we wanted to delete a file
#     print("Cannot delete a directory:", exception_object)
# except Exception as exception_object:
#     print("Unexpected exception:,", exception_object)

try:
    homedir = os.environ['HOME']
    homedir = os.path.join(homedir, 'Desktop')
    print(homedir)
    files_to_move = list(filter(screenshotRegex.match, os.listdir(homedir)))
    # print(os.listdir(homedir))
    print(files_to_move)
    # to move these Screen Shot files , the next line is used

    def move_the_files():
        for x in list(files_to_move):
            move_file = ('{}{}{}'.format(homedir,"/",x))
            print(move_file)
        
            if os.path.isfile(move_file):
                try:
                    shutil.move(move_file, '{}{}'.format(homedir,"/ScreenShots"))
                    print("File moved successfully")
                except Exception as exception_object:
                    print("Unexpected exception:,", exception_object)

    if not os.path.exists('{}{}'.format(homedir,"/ScreenShots")):
        print("path does not exist")
        os.mkdir('{}{}'.format(homedir,"/ScreenShots"))
        move_the_files()
        
    else:
        print("path exists", '{}{}'.format(homedir,"/ScreenShots"))
        move_the_files()


    
except Exception as exception_object:
    print("Unexpected exception:,", exception_object)
# os.path.isdir  to check if the directory exists
# with open(file_path, mode) as file -- safe way to open files so they auto close on failure