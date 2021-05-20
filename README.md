# LogLooker
This is a script that will look for test words in a .txt file and print the 5 lines before and after the line where the word was found.

## Installation
To install, download a zip file, then extract the files into a directory of your choice. Insert the input files you'd like to parse into that directory, and the script is ready for use.

## Usage
This script can look for an unlimited number of test words. If you would like the output to go to a file, please use output redirection

```python
python logLooker.py inputFile.txt testWord1 testWord2
```

To output to a file:
```python
python logLooker.py inputFile.txt testWord1 testWord2 > outputFile.txt
```

## License
[GPL-v3](https://choosealicense.com/licenses/gpl-3.0/)
