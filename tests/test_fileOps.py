# these tests are designed for pytest framework

import fileOps as fo
import numpy as np

def test_getLine():
    refline = "JAQUES\tAll the world's a stage,\n"
    reference = "All the world's a stage,"

    fname = "../data/shakespeare.txt"
    lnumber = 1660
    line = fo.getLine(fname, lnumber)

    result = line.partition("\t")[2].rstrip()
    assert result == reference

def test_addLineNumber():
    fin = "../data/shakespeare.txt"
    fin_wln = "../data/shakespeare-wln.txt"
    numlines = 4122 # total number of lines

    fo.addLineNumber(fin, fin_wln)

    rng = np.random.default_rng()
    lnumber = rng.integers(low=1, high=numlines)

    line = fo.getLine(fin_wln, lnumber)
    ln = int(line.split()[0])
    assert ln == lnumber

def test_addLineNumber_inplace():
    fin = "../data/shakespeare.txt"
    fin_wln_inplace = "../data/shakespeare-wln-inplace.txt"
    numlines = 4122

    fo.addLineNumber_inplace(fin_wln_inplace)

    rng = np.random.default_rng()
    lnumber = rng.integers(low=1, high=numlines)

    line = fo.getLine(fin_wln_inplace, lnumber)
    ln = int(line.split()[0])
    assert ln == lnumber

def test_getLine_binarysearch():
    refline = "JAQUES\tAll the world's a stage,\n"
    reference = "All the world's a stage,"

    fname = "../data/shakespeare-wln.txt"
    lnumber = 1660
    line = fo.getLine_binarysearch(fname, lnumber)

    result = line.partition("\t")[2].rstrip()
    assert result == reference
