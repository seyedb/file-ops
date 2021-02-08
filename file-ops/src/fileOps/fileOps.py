#
import re

from re import findall

def getLine(fname, lnumber):
    """ 
    function to jump to a line number in a file and read a line.

    args: 
        fname   (str): file's name
        lnumber (int): line number
    retunrs:
        (str) string containing the contents of the lnumber'th line 
    """

    if lnumber <= 0:
        print("Error: Invalid line number!")
        return

    with open(fname, "r") as fid:
        for i, line in enumerate(fid, start=1):
            if i == lnumber:
                print(line)
                break
        else:
            print("Error: EOF reached!")


def findPattern(fin, pattern):
    """
    function to read a large file and find lines that match a criteria

    args:
        fin     (str): file's name
        pattern (str): regex pattern to be matched (ex: r'<title.*>(.*)<\/title>' to search fir titles in an xml file)
    returns:
        (list) list of matches found
    """
    matchlist = []
    with open(fin, "r") as fid:
        for i, line in enumerate(fid, start=1):
            matches = re.findall(pattern, line)
            if len(matches) > 0:
                matchlist.extend(matches)
        else:
            print("EOF reached.")

    return matchlist

