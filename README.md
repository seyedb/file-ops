## File Operations
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Python scripts to perform the following file operations:
* Jump to a line number in a file and read a line.
* Read a large file as a stream of lines and filter only the lines that match a criteria.
* Read a large file, filter only the lines that match a criteria, and redirect and write those filtered lines to another file.
* Read a JSON input and load it into an object.


### Timing Results
The following timings have been obtained by reading a wikimedia abstracts dump file (an xml file of size 5.8GB with almost 75.6M lines - the file can be downloaded from [here](https://dumps.wikimedia.org/enwiki/latest/)). 

Adding line numbers to the file:<br />
`addLineNumber : 58.024850428 s`<br />
`addLineNumber_inplace  : 103.272668963 s`

Reading a line at a given line number:<br />
Use `./tools/timingplot.py` to generate an interactive plotly plot. The timing data can be found at: `./data/`

`getline` from the `linecache` module is not practical for large files.<br />
`getLine` uses `enumerate()` to read the file line-by-line.<br />
`getLine_binarysearch` searches for the given line number using binary search. The input file must have line numbers.

<img src=./data/gL.png width="50%" height="50%">
<img src=./data/gLbinsrch.png width="50%" height="50%">

