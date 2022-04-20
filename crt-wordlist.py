import requests
import re
import argparse

def main(domains, is_silent):
    names = set([])
    for domain in domains:
        if not is_silent:
            print(f"[+] Checking {domain}")
        r = requests.get(f"https://crt.sh/?q={domain}&output=json")
        for cert in r.json():
            names.add(cert["common_name"])
            for name_value in cert["name_value"].split("\n"):
                names.add(name_value)

        for name in names.copy():
            for name_component in re.split('\W+', name):
                names.add(name_component)

    return names

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domains", help="Comma Separated List of domains to check", required=True)
parser.add_argument("-r", "--sort", help="Sorts output alphabetically", action="store_true")
parser.add_argument("-o", "--output", help="Write to a findings to a file.")
parser.add_argument("-q", "--quiet", help="Suppress output other than sites being checked.", action="store_true")
parser.add_argument("-s", "--silent", help="Suppress all output", action="store_true")

args = parser.parse_args()

if __name__ == '__main__':
    domains = args.domains.split(",")
    is_sorted = args.sort
    is_file_save = True if args.output else False
    is_quiet = args.quiet
    is_silent = args.silent

    word_list = main(domains, is_silent)

    if is_sorted:
        word_list = sorted(word_list)

    if is_file_save:
        output_file_name = args.output
        output_file_handle = open(args.output, "w+")

    for word in word_list:
        if is_file_save:
            output_file_handle.write(f"{word}\n")
        if not is_quiet or not is_silent:
            print(word)

    if is_file_save:
        output_file_handle.close()            
