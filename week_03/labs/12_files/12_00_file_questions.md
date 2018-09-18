# Files

Read through chapter ["Case Study: Word Play"](http://greenteapress.com/thinkpython2/html/thinkpython2010.html) as well as chapter ["Files"](http://greenteapress.com/thinkpython2/html/thinkpython2015.html) from
Allen B. Downey's Think Python 2e book.

- How do you open a file in read mode and print the first line?

    ```py
    fin = open("words.txt", "r")
    print(fin.readline())
    ```

- How can you use a for loop to iterate through the words of a file?

    ```py
    fin = open("words.txt", "r")
    for line in fin:
        word = line.strip()
        print(word)
    ```

- What does it mean when a program is persistent?

    Persistent programs run for a long time (or all the time); they keep at least some of their data in permanent storage (a hard drive, for example); and if they shut down and restart, they pick up where they left off.

- How do you open a file in write mode?

    ```py
    fin = open("words.txt", "w")
    ```

- Practice using f-strings as a replacement for the .format() method

    ```py
    name = "Rasmus"
    birth_year = 1975
    print(f"Hello {name}, you are from {birth_year}")
    ```

- What is the difference between a relative path and an absolute path?

    An absolute path begins with / and does not depend on the current directory but to the root of the filesystem
    A relative path relates to the current directory.


- What are some IOExceptions that you might encounter? How are they generated?

    IOError: [Errno 2] No such file or directory: 'bad_file'
    PermissionError: [Errno 13] Permission denied: '/etc/passwd'

    by the exceptions class built into Python

- What is a try statement used for?

    To try executing a set of statements

- What is an except statement used for?

    To catch exceptions and enable the developer to handle them without stopping the script.

- Can you have a try without an except? Can you have an except without a try?

    No

- What is the variable `__name__` used for?

    To test which environment you are running your module in - ie is it an import or run directly

    if __name__ == '__main__':
        print 'This program is being run by itself'
    else:
        print 'I am being imported from another module'

