#
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


