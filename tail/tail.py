
# import useful libraries
import argparse
import os

# define and parse out arguments
parser = argparse.ArgumentParser(description='Tail in Python.')
parser.add_argument('file', metavar='filename', type=str,
                    help='file to open/tail')
parser.add_argument('-n', metavar='N', type=int,
                    default=10,
                    help='number of lines to read')

args = parser.parse_args()

# set variables name from arguments
filename = args.file

# open the file to tail
f = open(filename, 'r')

# seek to the the default number of lines before EOF
f.seek(0, os.SEEK_END)

# define some starting values for the loop
num_newlines = args.n

# start seeking 1 character at a time
seek_ctr = -1

# loop until the desired number of newlines are found
while num_newlines > 0:

    try:
        # seek back 1 char at a time
        f.seek(seek_ctr, os.SEEK_END)
    except:
        # seek back one more time to catch the beginning of the file
        seek_ctr -= 1
        break

    # read the char and check if its a new line
    char = f.read(1)

    if char == "\n":
        num_newlines -= 1

    # keep seeking backwards
    seek_ctr -= 1


# seek to the part of the file we start printing and print
f.seek(seek_ctr + 2, os.SEEK_END)
rest_of_file = f.read()

print rest_of_file
