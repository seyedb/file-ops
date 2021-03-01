## File Operations
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

Python scripts to perform the following file operations:
* Jump to a line number in a file and read a line.
* Read a large file as a stream of lines and filter only the lines that match a criteria.
* Read a large file, filter only the lines that match a criteria, and redirect and write those filtered lines to another file.
* Read a JSON input and load it into an object.


### Timing Results
The following timings have been obtained by reading a wikimedia abstracts dump file (an xml file of size 5.8GB with almost 75.6M lines - can be downloaded [here](https://dumps.wikimedia.org/enwiki/latest/)). 
