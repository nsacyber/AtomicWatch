import argparse
import os
import re
from glob import glob

def start():

    # initialize values
    firstFound = False

    # regex arrays
    keywords = ['(Atom C2000)', '(Atom C2)', '(ATOM)']
    systeminfo = ['(?:(?:Chassis).*?(VID:\s\w+))', '(Serial Number:\s\w+)']
    ipRegex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    # get values from menu
    args = parseMenu()
    directory = args.searchDirectory
    configKeywords = args.keywordConfig
    searchFileName = args.searchFileName
    fileName = 'raw.log'

    # apply arg values to variables
    if configKeywords:
        keywords = getKeywords(configKeywords)
    if searchFileName:
        fileName = searchFileName

    # recursively search directory
    dirList = searchDir(directory, fileName)

    # find keywords in log files
    for logFilePath in dirList:
        found = infoExtractor(keywords, logFilePath)
        if found:
            firstFound = True
            getIP = logFilePath.split('/')
            ip = re.search(ipRegex, logFilePath)
            if ip:
                print "Found in : " + ip.group(0)
            else:
                print "Found in : " + logFilePath

            # get device info
            info = infoExtractor(systeminfo, logFilePath)
            if info:
                for i in info:
                    print i
            else:
                print "***No device info found, here is the log file where evidence of the Atom C2000 series was found: \n" + logFilePath
            print ""

    # if no results found
    if firstFound == False:
        print "No results found"

# Pull results from file outlined by regex
def infoExtractor(regexes, path):
    results = []
    words_re = re.compile("|".join(regexes), flags=re.S)
    with open(path, 'r') as infile:
        parseMe = infile.read()
        found = re.findall(words_re, parseMe)
        if found:
            for i in found:
                i = filter(None, i)
                results.append(i[0])
    return list(set(results))

# Get all files from directory
def searchDir(path, fileName):
    result = [y for x in os.walk(path) for y in glob(os.path.join(x[0], fileName))]
    return result

# Pull keywords to apply in regex search
def getKeywords(path):
    keywords = None
    if os.path.exists(path):
        keywords = open(path,'r').read().splitlines()
    else:
        print "Path not valid"
    return keywords

def parseMenu():
    parser=argparse.ArgumentParser(description="\'-h' to show this menu")
    parser.add_argument('-p', action='store', dest='searchDirectory', required=True, help='Full path to directory containing logs to search for evidence of Atom C2000 systems')
    parser.add_argument('-s', action='store', dest='keywordConfig', required=False, help='Full path to keyword config file if the defaults do not work.  This config file should contain a list of keywords to search for.')
    parser.add_argument('-f', action='store', dest='searchFileName', required=False, help='The filename to search for within the specified directory. Default: raw.log')
    return parser.parse_args()

if __name__ == "__main__":
    start()
