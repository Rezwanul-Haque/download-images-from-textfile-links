# Download Images From Text File with links

### Current repo is about a small program which will read a text file and
### read the text file content (which is some image urls) then download those
### images to the local computer.

## Here $ will be  represent commands which will be run on the cmd or git bash.

# You can use virtualenv to create a separate python installation for this project

$ virtualenv venv

## Activate the virtualenv
# For windows

$ cd venv
$ scripts\activate
$ cd ..

# For linux

$ cd venv
$ source bin\activate

# clone repo

$ git clone https://github.com/Rezwanul-Haque/download-images-from-textfile-links.git

# install the requirements

$ cd download-images-from-textfile-links
$ pip install -r requirements.txt

### This program use requests package to download images from links given in the images.txt file.
### Run image_download.py file from cmd or any other python interpreter.

# CMD
$ python image_download.py

### All downloaded images will be downloaded in the images folder in the current directory.  
### If the images folder not created then it will be created.

# Test Cases
### I added a test case using python unittest test built-in package to check links in the text
### file give http success status code (200) or http page not found status code (404) for links.
### test cases can be run using cmd

$ python -m unittest

### Another manual test case was added to the same file (test_image_download.py) to check if the
### links text file (here its called images.txt) file was present on the current directory or not.

$ python test_image_download.py

# Program Details
### image_download has two function
1. image fetch
2. main

# help text doc string can be seen using cmd

$ python
>>> from image_download import image_fetch
>>> help(image_fetch)
