import argparse, os
from argparse import Namespace

if __name__ == "__main__":
    msg = "Input a command."

    parser = argparse.ArgumentParser(description=msg)
    #parser.add_argument('integers', metavar = 'N', type = int, nargs = '+', help = 'an integer for the accumulator')
    #parser.add_argument('--sum', dest = 'accumulate', action = 'store_const', const = sum, default = max, 
    #                    help = 'sum the integers (default: find the max)')
    
    parser.add_argument('-c', '--countbits', help = 'count the number of bits in a file', 
                        action = 'store_true')
    parser.add_argument('filename',metavar = 'f', type = argparse.FileType('r'), help = 'a file name')
    args: Namespace = parser.parse_args()

    print("hello")
    #print(args.accumulate(args.integers))
    if args.countbits:
        file_size = os.stat(args.filename)
        print(file_size)
   
    