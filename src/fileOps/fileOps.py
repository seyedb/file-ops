#
import os
import sys
import fileinput

from re import findall
from json import loads

def getLine(fname, lnumber):
    """ 
    Function to jump to a line number in a file and read a line.

    args: 
        fname (str): path to the input file
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
                return line
                break
        else:
            print("Error: EOF reached!")

def addLineNumber(fin, fout):
    """
    Reads a file and writes every line of the file to another file with line number added 

    args: 
        fin (str): path to the input file
    returns:
        (file obj) fout same as fin but with line numbers
    """
    fout_id = open(fout, "w")

    with open(fin, "r") as fin_id:
        for i, line in enumerate(fin_id, start=1):
            fout_id.write("%d  %s" % (i, line))

    fout_id.close()

def addLineNumber_inplace(fins):
    """
    Reads a collection of files and adds line numbers to every line of those files in place

    args:
        fins (tuple of str): paths to the input files to be edited
    returns:
        (file objs) every file in fins with line numbers added to their lines
    """
    for line in fileinput.input(files=fins, inplace=True):
        sys.stdout.write('%d %s' % (fileinput.filelineno(), line))

def getLine_binarysearch(fname, lnumber):
    """
    Function to jump to a line number in a file and read that line. 
    NOTE: uses a binary search approach to find the line number, therefore, the file needs to have line numbers

    args:
        fname (str): path to the input file that has line numbers
        lnumber (int): line number
    retunrs:
        (str) string containing the contents of the lnumber'th line 
    """
    fid = open(fname, "r")

    left = 0
    right = os.path.getsize(fname) # interval of bytes
    mid = 0

    sol = None
    while left <= right:
        mid = left + (right - left)//2

        # move the pinter to the offset mid
        fid.seek(mid)
        # wherever we are, go to the end of the line, after this the pointer is moved to
        # the beginning of the next line
        fid.readline()
        # read the entire line
        line = fid.readline()
        ln = int(line.split()[0])

        if lnumber > ln:
            left = mid + 1
        elif lnumber < ln:
            right = mid - 1
        else:
            sol = " ".join(line.split()[1:])
            fid.close()
            return sol

    fid.close()
    return sol

def findPattern(fin, pattern):
    """
    Function to read a large file and find lines that match a criteria.

    args:
        fin (str): path to the input file
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
    Function to find lines that match a criteria and write them to another file.

    args:
        fin (str): path to the input file
        pattern (str): regex pattern to be matched (ex: r'<title.*>(.*)<\/title>' to search fir titles in an xml file)
        fout (str): path to the output file
    returns:
        (file obj) fout filled in with all the lines from fin that contain a match of the pattern (regex)
    """
    fout_id = open(fout, "w")
    with open(fin, "r") as fin_id:
        for i, line in enumerate(fin_id, start=1):
            matches = re.findall(pattern, line)
            if len(matches) > 0:
                fout_id.write(line)
        else:
            print("EOF reached.")

    fout_id.close()

def jsonToDict(json_file):
    """
    Function to read in a JSON file and convert it into a distionary.

    args:
        json_file (str): path to the input file
    returns:
        (dict) a dictionary containg the data from the input JSON file
    """
    with open(json_file, "r") as fid:
        dout = json.loads(fid.read())

    return dout

class loaded_json(object):
    """
    Class containing data loaded from an input JSON file.

    usage:
        jsondata = loaded_json(file_path)

    TODO: make the class iterable.
    """
    def __init__(self, json_file):
        with open(json_file, "r") as fid:
            self.__dict__ = json.loads(fid.read())


