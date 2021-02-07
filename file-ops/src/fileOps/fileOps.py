#

def getLine(fname, lnumber):
    """ function to jump to a line number in a file and read a line """
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

