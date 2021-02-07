#

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
            print("Error: EOF has reached!")

