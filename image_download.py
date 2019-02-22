import os
import random
import requests

"""
This is a module which read a .txt file which contain some urls of some images
on the internet and download then to current_folder/images/ directory.

fetched image name always going to be a random number between 1, 10000.

"""

def image_fetch(url, file_path):
    """
    Fetch image from the internet.

    Parameters:
    url (string): A image url

    file_path (string): Directory name where the image will be saved.

    Output:
    url's image will be saved in the file_path directory

    """
    response = requests.get(url)
    image_name = random.randint(1,10000)  ## A random name assign to each image fetched.
    fetched_image_name = file_path + str(image_name) + '.jpg' ## saving the image as jpg

    if response.status_code == 200:
        with open(fetched_image_name, 'wb') as f:
            f.write(response.content)

    return response.status_code



def main():
    """ This is the main function which open a .txt file and read the urls """
    ## Checking if the current directory has the images.txt file on pwd.
    if os.path.isfile('./images.txt'):
        file_name = 'images.txt'
    else:
        raise FileNotFoundError
    ## Directory name where the image file should be saved.
    directory_to_save_the_image = 'images/'

    if os.path.isdir(directory_to_save_the_image):  ## Checking if the directory is present
        print("Please wait downloading images...")
    else:
        os.mkdir(directory_to_save_the_image)

    with open(file_name) as file:
        # lines = [l.strip() for l in file]  ## using list comprehension to remove the "\n"
        lines = file.read().splitlines()  ## using built in function

    for line in lines:  ## going through the url in the file
        image_fetch(line, directory_to_save_the_image)

    print("Download complete.")

if __name__ == "__main__":  ## When this module is run as a script
    main()
