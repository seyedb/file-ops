# these tests are designed for pytest framework
import pytest
import fileOps as fo
import numpy as np
from collections import Counter
import filecmp
import pickle
import deepdiff

def test_getLine():
    refline = "JAQUES\tAll the world's a stage,\n"
    reference = "All the world's a stage,"

    fname = '../data/shakespeare.txt'
    lnumber = 1660
    line = fo.getLine(fname, lnumber)

    result = line.partition('\t')[2].rstrip()
    assert result == reference

def test_addLineNumber():
    fin = '../data/shakespeare.txt'
    fin_wln = '../data/shakespeare-wln.txt'
    numlines = 4122 # total number of lines

    fo.addLineNumber(fin, fin_wln)

    rng = np.random.default_rng()
    lnumber = rng.integers(low=1, high=numlines)

    line = fo.getLine(fin_wln, lnumber)
    ln = int(line.split()[0])
    assert ln == lnumber

def test_addLineNumber_inplace():
    # for this test do the following copy first to have the required data:
    # > cp ../data/shakespeare.txt ../data/shakespeare-wln-inplace.txt
    fin_wln_inplace = '../data/shakespeare-wln-inplace.txt'
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

    fname = '../data/shakespeare-wln.txt'
    lnumber = 1660
    line = fo.getLine_binarysearch(fname, lnumber)

    result = line.partition('\t')[2].rstrip()
    assert result == reference

def test_getLine_binarysearch_1stline():
    reference = "AS YOU LIKE IT"

    fname = '../data/shakespeare-wln.txt'
    lnumber = 1
    line = fo.getLine_binarysearch(fname, lnumber)

    result = line.partition('\t')[2].rstrip()
    assert result == reference

def test_findPattern():
    fin = '../data/shakespeare.txt'
    pattern = "^ACT.*"

    matchlist = fo.findPattern(fin, pattern)
    reference = Counter({'ACT I': 3, 'ACT II': 7, 'ACT III': 5, 'ACT IV': 3, 'ACT V': 4})
    assert Counter(matchlist) == reference

def test_matchToFile():
    fin = '../data/shakespeare.txt'
    fout = '../data/shakespeare-match.txt'

    # fref is created via:
    # > grep "ACT" ../data/shakespeare.txt > ../data/shakespeare-matchref.txt
    fref = '../data/shakespeare-matchref.txt'

    pattern = "^ACT.*"

    fo.matchToFile(fin, pattern, fout)
    assert filecmp.cmp(fout, fref)

def test_jsonToDict():
    json_file = '../data/exoplanets.json'
    exoplanets = fo.jsonToDict(json_file)

    # reference dictionary has been stored in a binary format using:
#    with open('../data/exoplanets.pkl', 'wb') as fdict:
#        pickle.dump(exoplanets, fdict, pickle.HIGHEST_PROTOCOL)

    refdict = {}
    with open('../data/exoplanets.pkl', 'rb') as fdict:
        refdict = pickle.load(fdict)

    diff = deepdiff.DeepDiff(exoplanets, refdict)
    # the diff must be an empty dictionary
    assert not diff

def test_init_loaded_json():
    refdict = {}
    with open('../data/exoplanets.pkl', 'rb') as fdict:
        refdict = pickle.load(fdict)

    jsondata = fo.loaded_json('../data/exoplanets.json')

    diff = deepdiff.DeepDiff(jsondata.__dict__, refdict)
    assert not diff
