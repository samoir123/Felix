"""
Python 2.7.15 |Anaconda, Inc.| (default, May  1 2018, 18:37:09) [MSC v.1500 64 bit (AMD64)]
Python 2.7.15 |Anaconda, Inc.| (default, May  1 2018, 18:37:09) [MSC v.1500 64 bit (AMD64)] on win32

Tasks: List Zip Files and extract them into Same Folder (GammaGUI needs *.SAFE Structure)
"""

# Import Libs
# import os, zipfile

def unzip_files ():
    """
    Extract all *.zip Files in current Working Directory
    """
    try:
        import os, zipfile
    except ImportError:
        # Try to install it automatically
        # https://stackoverflow.com/questions/46419607/how-to-automatically-install-required-packages-from-a-python-script-as-necessary
        # Mayve solved with package
        print('Please install {} and {} via pip install').format('os','zipfile')

    # Set wdir and extension
    wdir = os.getcwd() # String CWD # Take Care with Path under Windows max. 250 (?)
    extension = ".zip" # String Extension

    print('-- Start unzipping --')
    # TODO implemend count for extracting / length(list) print i


    for i in os.listdir(wdir):  # loop through items in dir
        if i.endswith(extension):  # check for ".zip" extension
            file_name = os.path.abspath(i)  # get full path of files
            zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
            zip_ref.extractall(wdir)  # extract file to dir
            zip_ref.close()  # close file
            print('File: {} -- successfully extracted --').format(i)

    print('-- Unzipping finished --')

unzip_files()
