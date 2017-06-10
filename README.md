# AtomicWatch
Intel Atom C2000 series discovery tool that parses log files and returns results if a positive match is found. 

## Description
This script is a parsing tool intended to recursively traverse a directory populated with config files from various devices on the network in question.
Seek an administrator to assist in acquiring all network device configs.
Run the script against the top-most directory.
Positive results returned from the script are reflective of devices running the Atom C2000 series chipsets.

## Run
python2 parse.py -p /path/to/config/directory -f configFileName.conf

## Links
* [Faulty Intel Atom C2000 processor series will likely result in abrupt device failure](https://www.iad.gov/iad/library/ia-advisories-alerts/faulty-intel-atom-c2000-processor.cfm)

## License
See [LICENSE](./LICENSE.md).

## Disclaimer
See [DISCLAIMER](./DISCLAIMER.md).
