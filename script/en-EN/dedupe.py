import getopt
import argparse
import sys


def start(prefix="en-EN/", file_name=input(), suffix="/wordlist.txt", new_file="/new.txt"):
    prefix = "wordlist/" + prefix

    result = dedupe("{}{}{}".format(prefix, file_name, suffix))
    print(result["wordlist"])

    if len(result["dupe"]):
        f = open("{}{}{}dupe.txt".format(prefix, file_name, suffix), "a")
        f.write("Duplicates detected\n")
        f.write("\n".join([str(x) for x in result["dupe"]]))

    f = open("{}{}{}".format(prefix, file_name, new_file), "w")
    f.write("\n".join([str(x) for x in result["wordlist"]]))


def dedupe(file_name):
    print(file_name)
    f = open(file_name, 'r')

    wordlist = list()
    dupe = list()

    for x in f:
        x = x.capitalize().rstrip("\n")
        if x not in wordlist:
            wordlist.append(x)
        else:
            dupe.append(x)

    wordlist.sort()

    return {"wordlist": wordlist, "dupe": dupe}


# Options
options = "i:o:"
long_options = ["input", "output"]

input_dir = str()
output_dir = str()

try:
    # Parsing argument
    arguments, values = getopt.getopt(sys.argv[1:], options, long_options)

    # checking each argument
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-i", "--input"):
            input_dir = currentValue
        elif currentArgument in ("-o", "--output"):
            output_dir = currentValue

except getopt.error as err:
    # output error, and return with an error code
    print(str(err))


# Initialize parser
parser = argparse.ArgumentParser(description="Adding description")
parser.add_argument("-i", "--input", help="Show Output")
parser.add_argument("-o", "--output", help="Show Output")
parser.parse_args()

start(prefix=input_dir, suffix=new_file)
