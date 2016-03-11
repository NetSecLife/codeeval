import sys
import os

def main():
    print(os.stat(sys.argv[1]).st_size)

main()