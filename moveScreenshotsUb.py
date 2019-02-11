import os, re, shutil

user_dir = "~/Desktop/"
screenshotRegex = re.compile (r'Screen Shot+')
screenshotRegexUb = re.compile (r'Screenshot+')
try:
    homedir = os.path.join(os.environ['HOME'], 'Desktop')
    # print(homedir)
    files_to_move = list(filter(screenshotRegex.match, os.listdir(homedir)))
    files_to_move2 = list(filter(screenshotRegexUb.match, os.listdir(homedir)))
    # print(os.listdir(homedir))
    # print(files_to_move)
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
        for x in list(files_to_move2):
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
        try:
            os.mkdir('{}{}'.format(homedir,"/ScreenShots"))
        except Exception as exception_object:
            print("Unexpected exception:,", exception_object)
        else:
            move_the_files()

    else:
        print("path exists", '{}{}'.format(homedir,"/ScreenShots"))
        try:
           move_the_files()
        except Exception as exception_object:
            print("Unexpected exception:,", exception_object)




except Exception as exception_object:
    print("Unexpected exception:,", exception_object)
# os.path.isdir  to check if the directory exists
# with open(file_path, mode) as file -- safe way to open files so they auto close on failure
