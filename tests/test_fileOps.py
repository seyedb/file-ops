# these tests are desigend for pytest framework

import fileOps as fo

def test_getLine():
    refline = "JAQUES\tAll the world's a stage,\n"
    reference = "All the world's a stage,"

    fname = "../data/shakespeare.txt"
    lnumber = 1660
    line = fo.getLine(fname, lnumber)

    result = line.partition("\t")[2].rstrip()
    assert result == reference

