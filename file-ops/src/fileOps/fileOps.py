#
import re

from re import findall

def getLine(fname, lnumber):
    """ 
    function to jump to a line number in a file and read a line.

    args: 
        fname   (str): path to the input file
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
    function to read a large file and find lines that match a criteria.

    args:
        fin     (str): path to the input file
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


def matchToFile(fin, pattern, fout):
    """
    function to find lines that match a criteria and write them to another file.

    args:
        fin     (str): path to the input file
        pattern (str): regex pattern to be matched (ex: r'<title.*>(.*)<\/title>' to search fir titles in an xml file)
        fout    (str): path to the output file
    returns:
        (file obj) fout filled in with all the lines from fin that contain a match of the pattern (regex)
    """
    with open(fin, "r") as fid:
        for i, line in enumerate(fid, start=1):
            matches = re.findall(pattern, line)
            if len(matches) > 0:
                fout.write(line)
        else:
            print("EOF reached.")

    fout.close()

