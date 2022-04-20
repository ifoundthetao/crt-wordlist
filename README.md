# crt.sh Wordlist
Sometimes you need a wordlist. This pulls from crt.sh from domains that you specify. It'll grab common names and the name values. Then it will split them up, and give unique results.

You can sort alphabetically if you'd like, you can save the file, and you can make it quiet (only showing the domains it's checking), or silent (no output).

# Requirements
* python
* re
* argparse
* requests

# Usage
    usage: crt-wordlist.py [-h] -d DOMAINS [-r] [-o OUTPUT] [-q] [-s]
    
    optional arguments:
      -h, --help            show this help message and exit
      -d DOMAINS, --domains DOMAINS
                            Comma Separated List of domains to check
      -r, --sort            Sorts output alphabetically
      -o OUTPUT, --output OUTPUT
                            Write to a findings to a file.
      -q, --quiet           Suppress output other than sites being checked.
      -s, --silent          Suppress all output
