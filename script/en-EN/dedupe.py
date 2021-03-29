import getopt
import sys
import argparse


def main():
    # Options
    options = "i:o:"
    long_options = ["input", "output"]

    input_dir = "en-EN"
    output_dir = "new.log"

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

    start(prefix=input_dir, new_file=output_dir, file_name=input())


def start(prefix="en-EN/", file_name=input(), suffix="/wordlist.txt", new_file="/new.txt"):
    prefix = "wordlist/" + prefix

    result = dedupe("{}/{}/{}".format(prefix, file_name, suffix))

    if len(result["dupe"]):
        print("Duplicates Detected: {}".format(result["dupe"]))

        f = open("{}/{}/{}".format(prefix, file_name, duplicate_file), "w")
        f.write("Duplicates detected\n")
        f.write("\n".join([str(x) for x in result["dupe"]]))

    f = open("{}{}{}".format(prefix, file_name, new_file), "w")
    f.write("\n".join([str(x) for x in result["wordlist"]]))


def dedupe(file_name):
    f = open(file_name, 'r').read().splitlines()

    wordlist = list()
    dupe = list()

    for x in range(len(f)):
        y = f[x].lstrip(" ").rstrip(" ").lower()
        if wordlist.count(y):
            dupe.append(y.capitalize())
        else:
            wordlist.append(y.capitalize())

    wordlist.sort()

    return {"wordlist": wordlist, "dupe": dupe}


if __name__ == "__main__":
    main()
