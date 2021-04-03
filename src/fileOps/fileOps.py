import os
import sys
import fileinput

import re
from re import findall

import json
from json import loads

def getLine(fname, lnumber):
    """Jumps to a line number in a file and reads a line.

    Args:
        fname (str): path to the input file.
        lnumber (int): line number.
    Returns:
        (str) string containing the contents of the lnumber'th line.
    """
    assert(lnumber > 0), "Error: Invalid line number!"

    eof = True
    with open(fname, 'r') as fid:
        for i, line in enumerate(fid, start=1):
            if i == lnumber:
                return line

    assert(not eof), "Error: EOF reached!"

def addLineNumber(fin, fout):
    """Reads a file and writes every line of the file to another file with line number added.

    Args:
        fin (str): path to the input file.
        fout (str): path to the output file.
    Returns:
        (file obj) fout same as fin but with line numbers.
    """
    fout_id = open(fout, 'w')

    with open(fin, 'r') as fin_id:
        for i, line in enumerate(fin_id, start=1):
            fout_id.write('%d %s' % (i, line))

    fout_id.close()

def addLineNumber_inplace(fins):
    """Reads a collection of files and adds line numbers to every line of those files in place.

    Args:
        fins (tuple of str): paths to the input files to be edited.
    Returns:
        (file objs) every file in fins with line numbers added to their lines.
    """
    for line in fileinput.input(files=fins, inplace=True):
        sys.stdout.write('%d %s' % (fileinput.filelineno(), line))

def getLine_binarysearch(fname, lnumber):
    """Jumps to a line number in a file and reads that line. 
    NOTE: 
        uses a binary search approach to find the line number, therefore, the file needs to have line numbers
        use addLineNumber or addLineNumber_inplace to create such a file.

    Args:
        fname (str): path to the input file that has line numbers.
        lnumber (int): line number.
    Returns:
        (str) string containing the contents of the lnumber'th line.
    """
    assert(lnumber > 0), "Error: Invalid line number!"

    fid = open(fname, 'r', errors='replace')

    left = 0
    right = os.path.getsize(fname) # interval of bytes
    mid = 0

    sol = None
    while left <= right:
        mid = left + (right - left)//2

        # Step 1: move the pinter to the offset mid
        fid.seek(mid)
        # Step 2: wherever we are, go to the end of the line
        fid.readline()
        # The pointer is now moved to the beginning of the next line
        # Step 3: read the entire line
        line = fid.readline()
        try:
            ln = int(line.split()[0])
        except IndexError:
            print("Error: line has no line number or EOF reached!")
            break

        if lnumber > ln:
            left = mid + 1
        elif lnumber < ln:
            right = mid - 1
        else:
            sol = line.partition(" ")[2]
            fid.close()
            return sol

    # since in step 3 the pointer is moved to the beginning of the next line, binary search will
    # never find the first line, here is a workaround:
    if abs(right - lnumber) < abs(left - lnumber):
        fid.seek(right)
        rline = fid.readline()
        sol = rline.partition(" ")[2]
    else:
        fid.seek(left)
        lline = fid.readline()
        sol = lline.partition(" ")[2]

    fid.close()
    return sol

def findPattern(fin, pattern):
    """Reads a large file and finds lines that match some criteria.

    Args:
        fin (str): path to the input file.
        pattern (str): regex pattern to be matched (ex: r'<title.*>(.*)<\/title>' to search for titles in an xml file).
    Returns:
        (list) list of matches found.
    """
    matchlist = []
    with open(fin, 'r') as fid:
        for _, line in enumerate(fid, start=1):
            matches = re.findall(pattern, line)
            if len(matches) > 0:
                matchlist.extend(matches)

    if len(matchlist) == 0: print("EOF reached.")
    return matchlist

def matchToFile(fin, pattern, fout):
    """Finds lines that match some criteria and writes them to another file.

    Args:
        fin (str): path to the input file.
        pattern (str): regex pattern to be matched (ex: r'<title.*>(.*)<\/title>' to search for titles in an xml file).
        fout (str): path to the output file.
    Returns:
        (file obj) fout filled in with all the lines from fin that contain a match of the pattern (regex).
    """
    fout_id = open(fout, 'w')
    count = 0
    with open(fin, 'r') as fin_id:
        for _, line in enumerate(fin_id, start=1):
            matches = re.findall(pattern, line)
            if len(matches) > 0:
                fout_id.write(line)
                count += 1

    if count == 0: print("EOF reached.")
    fout_id.close()

def jsonToDict(json_file):
    """Reads in a JSON file and converts it into a dictionary.

    Args:
        json_file (str): path to the input file.
    Returns:
        (dict) a dictionary containing the data from the input JSON file.
    """
    with open(json_file, 'r') as fid:
        dout = json.loads(fid.read())

    return dout

class loaded_json(object):
    """Class containing data loaded from an input JSON file.

    Usage: jsondata = loaded_json(file_path)

    TODO: make the class iterable.
    """
    def __init__(self, json_file):
        with open(json_file, 'r') as fid:
            self.__dict__ = json.loads(fid.read())
