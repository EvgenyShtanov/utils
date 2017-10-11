"""
CP1251 to UTF-8 converter.
Input and output paths mustn't match each other.
There mustn't be recursion in folders.
For own my use only. No warranties and liabilities.
"""
import codecs
import argparse
import os

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="Path to the input files")
ap.add_argument("-o", "--output", required=True, help="Destination path")
args = vars(ap.parse_args())

path_from = args["input"]
path_to = args["output"]

# Walk throught the input Path
x = [i[2] for i in os.walk(path_from)]
for t in x:
    for thefile in t:
        if thefile.endswith((".cpp", ".c", ".h")):
            path_to_sources = path_from + '/' + thefile
            print("path_to_sources = ", path_to_sources)
            try:
                f = codecs.open(path_to_sources, 'r', 'cp1251')
                # Now the contents have been transformed to a Unicode string
                u = f.read()
            except:# UnicodeError, exc:
                print("UnicodeError")
                continue
            # raise UnicodeError('Failed to convert %r' % string)
            dst_path = path_to + '/' + thefile
            out = codecs.open(dst_path, 'w', 'utf-8')
            # And now the contents have been output as UTF-8
            out.write(u)
            print("path_to_dst = ", path_to_sources)
