# these tests are designed for pytest framework

import fileOps as fo
import numpy as np
from collections import Counter

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

def test_findPattern():
    fin = "../data/shakespeare.txt"
    pattern = "^ACT.*"

    matchlist = fo.findPattern(fin, pattern)
    reference = Counter({'ACT I': 3, 'ACT II': 7, 'ACT III': 5, 'ACT IV': 3, 'ACT V': 4})
    assert Counter(matchlist) == reference

def test_matchToFile():
    fin = "../data/shakespeare.txt"
    fout = "../data/shakespeare-match.txt"

    # fref is created via:
    # > grep "ACT" ../data/shakespeare.txt > ../data/shakespeare-matchref.txt
    fref = "../data/shakespeare-matchref.txt"

    pattern = "^ACT.*"

    fo.matchToFile(fin, pattern, fout)
    assert filecmp.cmp(fout, fref)

