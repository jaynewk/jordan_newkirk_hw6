#!/usr/bin/env python3
import sys
import urllib
import urllib.request
"""
Open an Apache server error log file and find the top 25 errors.
"""

url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test"

def get_url(url):
    """
    Gets the url of the server error log and gets the file
    Args:
        url: The url of the Apache error log
    Returns:
        List of errors
    """
    resource = urllib.request.urlopen(url)
    content = resource.read().decode('utf-8')
    data = content.splitlines()
    global dlist 
    dlist =('\n'.join('{}: {}'.format(*k) for k in enumerate(data)))
    #return dlist

def sort_url(dlist):
    print(dlist)

def main():
    """
    Main Function
    """
    get_url(url)
    sort_url(dlist)
    return


if __name__ == "__main__":
    main()

    exit(0)
