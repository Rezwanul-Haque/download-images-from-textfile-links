import os, urllib3
import unittest

from image_download import image_fetch


class TestImageFetch(unittest.TestCase):
    """Unittesting for TestImageFetch."""
    def setUp(self):
        # set test data
        self.success_status = 200 ## http success status code
        self.page_not_found = 404 ## http page not found status code
        self.url1 = 'https://images.unsplash.com/photo-1504610926078-a1611febcad3' # link 1
        self.url2 = 'https://images.unsplash.com/photo-1465765639406-044153778532' # link 4
        self.url3 = 'https://images.unsplash.com/photo-1495954484750-af469f2f9b'   # link 5 modified so that it gives 404
        self.file_path = 'images/'  ## downloaded images will be on that folder

    def test_image_fetch(self):
        self.assertEqual(image_fetch(self.url1, self.file_path), self.success_status)
        self.assertEqual(image_fetch(self.url2, self.file_path), self.success_status)
        self.assertEqual(image_fetch(self.url3, self.file_path), self.page_not_found)

def test_is_file_exists():
    """ manually unittesting for checking images.txt files exists in the current folder"""
    if os.path.isfile('./images.txt'):  ## should be exists
        print('Files exists')
    else:
        raise FileNotFoundError


if __name__ == "__main__":  ## When this module is run as a script
    test_is_file_exists()
    unittest.main()
