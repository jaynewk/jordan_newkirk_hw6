#!/usr/bin/env python3
import sys
import urllib
import urllib.request
import re
from collections import Counter
from collections import OrderedDict
"""
Open an Apache server error log file and find the top 25 errors.
"""

#url = "http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.full"

def help():
    """
    Usage of the program
    """
    print("The usage is jordan_newkirk_hw6.py <file input>")

def get_url():
    """
    Gets the url of the server error log and gets the file
    Args:
        url: The url of the Apache error log
    Returns:
        List of errors
    """
    
    try:
        url = input()
    except ValueError:
        url is None

    if url is None:
        help()

    resource = urllib.request.urlopen(url)
    global content
    content = resource.read().decode('utf-8')
    #global data
    #data = content.splitlines()
    #global dlist 
    #dlist =('\n'.join('{}: {}'.format(*k) for k in enumerate(data)))
    #return dlist

def sort_url(content):
    """
    Sorts the data from content into a list of errors with count displayed
    """
    # JOHNATHAN MIRABLE REG EXPRESS
    sort = re.findall(r'(?:\[.*?\]) (?:\[.*?\]) (?:\[.*?\]) (.*)', content)
    countlist = OrderedDict(Counter(sort).most_common(25))
    
    print("***TOP 25 PAGE ERRORS***")
    for page, count in countlist.items():
        print("Count = {}, Page  {}".format(count, page))

def main():
    """
    Main Function
    """
    get_url()
    sort_url(content)
    return


if __name__ == "__main__":
    main()

    exit(0)
