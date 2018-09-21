'''
In a large collection of MP3 files, there may be more than one copy of
the same song, stored in different directories or with different file
names. The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories,
recursively, and returns a list of complete paths for all files with a
given suffix (like .mp3). Hint: os.path provides several useful
functions for manipulating file and path names.

To recognize duplicates, you can use md5sum to compute a “checksum” for
each file. If two files have the same checksum, they probably have the
same contents. To double-check, you can use the Unix command diff.
Solution: http://thinkpython2.com/code/find_duplicates.py.

Go and tackle your duplicate files! :)

Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

Ideas for ways to actually make a usable mp3 de-duper:
For each file
- Filter files to compare with by filesize to to create candidate pool
- Split() the file name by " ", ", " ".", "_"
- remove chunks smaller than 4 characters
- Compare chunks wiht filenames of candidate group
- Use mp3 tags to score likelines of a match
-

'''
import os, glob

###############
### Classes ###
###############

class Search():

    def __init__(self, path, term):
        self.path = path
        self.term = term

    def get(self):
        return(self.path, self.term)


    def set(self, path, term):
        self.path = path
        self.term = term

    # Check i path exists
    def check_path(self):
        return(os.path.isdir(self.path))

    # Recursively search for files with self.term in self.path using regex
    def search(self):
        self.result = glob.glob(self.path + '/**/*.' + self.term, recursive=True)
        return(self.result)

    def compare(self, tracks):
        for track in tracks:
            pass
        pass

class Tracks(Search):


    # def __str__(self):
    #     return(len(self.tracks))

    # def set(self, tracks):
    #     self.tracks = tracks
    pass


# class Track():
#
#     def __init__(self, path):
#         self.path = path
#
#     def extract_name():
#         pass # extraxt filename from path
#
#     def checksum(self):
#         pass
#
#     def delete(self):
#         pass






#################
### Functions ###
#################




###############
### Execute ###
###############

if __name__ == '__main__':

    cwd = "/Users/vkng/Dropbox/99_code/Python/CodingNomads/python_core/week_03/labs/12_files"

    # Get [path] from user
    path = "/Users/vkng/Dropbox/99_code/Python/CodingNomads/python_core/week_03/labs/12_files/mp3"
    #path = input("Please enter the filepath to the folder you want to search: ")

    # Get [term] from user
    term = "mp3"
    #term = input("Please enter the term (filetype) you are looking for. For example - if you want to find x.mp3 files enter 'mp3': ")

    my_search = Search(path, term)
    # print("Searchpath:", my_search.get()[0])
    # print("Search term:", my_search.get()[1])
    # print("Path exists:", my_search.check_path())
    result = my_search.search()
    #print(result)
    my_tracks = Tracks(my_search.path, my_search.term)
    for each in
    print(my_tracks.path)

    # my_tracks = Tracks(my_search)
    # print(tracks)
    # for track in tracks:
    #     print(track)
