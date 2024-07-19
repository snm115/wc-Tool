import argparse

if __name__ == "__main__":
    msg = "Input a command."

    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('integers', metavar = 'N', type = int, nargs = '+', help = 'an integer for the accumulator')
    parser.add_argument('--sum', dest = 'accumulate', action = 'store_const', const = sum, default = max, 
                        help = 'sum the integers (default: find the max)')
    
    parser.add_argument('-c', help = 'count the number of bits in a file')
    args = parser.parse_args()

    print("hello")
    print(args.accumulate(args.integers))
    