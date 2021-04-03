import os
import numpy as np
import timeit
import fileOps as fo

def benchmark_getLine(fin, numlines, path):
    """Compare execution time of getLine functions.

    Args:
        fin (str): path to the input file.
        numlines (int): the total number of line of fin.
        path (str): where to store timing results.
    """
    fname, fext = os.path.splitext(fin)

    # fin with line number will be generated in the same path as fin
    fin_wln = '{}{}{}'.format(fname,'_wln',fext)
    fin_wln_inplace = '{}{}{}'.format(fname,'-inplace',fext)

    # add line numbers, compare two functions wrt timing 
    starttime = timeit.default_timer()
    fo.addLineNumber(fin, fin_wln)
    print("addLineNumber :", timeit.default_timer() - starttime)

    starttime = timeit.default_timer()
    fo.addLineNumber_inplace(fin_wln_inplace)
    print("addLineNumber_inplace  :", timeit.default_timer() - starttime)

    # generate sz distinct random integers between 1 and numlines as line numbers to be read
    sz = 1000 
    rng = np.random.default_rng()
    lnumbers = rng.choice(numlines, size=sz, replace=False)
    with open('../data/lnumbers.txt', 'w') as flnums:
        print('\n'.join(map(str, lnumbers)), file=flnums)

    # timing for getLine function
    getline_time=[]
    for ln in lnumbers:
        starttime = timeit.default_timer()
        line = fo.getLine(fin, ln)
        getline_time.append(timeit.default_timer() - starttime)

    with open(path + '/getline_time.txt', 'w') as fgetlinetime:
        print('\n'.join(map(str, getline_time)), file=fgetlinetime)

    # timing for getLine_binarysearch function
    getline_bs_time=[]
    for ln in lnumbers:
        starttime = timeit.default_timer()
        line = fo.getLine_binarysearch(fin_wln, ln)
        getline_bs_time.append(timeit.default_timer() - starttime)

    with open(path + '/getline_binsrch_time.txt', 'w') as fgetlinebstime:
        print('\n'.join(map(str, getline_bs_time)), file=fgetlinebstime)
