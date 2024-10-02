#!/usr/bin/env
import argparse, os, threading
from argparse import Namespace

if __name__ == "__main__":
    msg = "Input a command."

    parser = argparse.ArgumentParser(description=msg)
    #parser.add_argument('integers', metavar = 'N', type = int, nargs = '+', help = 'an integer for the accumulator')
    #parser.add_argument('--sum', dest = 'accumulate', action = 'store_const', const = sum, default = max, 
    #                    help = 'sum the integers (default: find the max)')
    
    parser.add_argument('-c', '--countbits', help = 'count the number of bits in a file', 
                        action = 'store_true')
    parser.add_argument('filename',metavar = 'f', type = argparse.FileType('r'), 
                        nargs = '*', help = 'at least one file name')
    args: Namespace = parser.parse_args()

    #print("hello")
    #print(args.accumulate(args.integers))

    def read_file(filename):
        with open(filename, 'r', encoding="utf-8") as file:
            content = file.read()
        
        return content
    
    def multi_threaded_file_reader(filenames):
        threads = []
        results = {}

        def read_file_thread(filename):
            #print("here",filename.name)
            result = read_file(filename.name)
            results[filename.name] = result
            
        
        for filename in filenames:
            thread = threading.Thread(target = read_file_thread, args = (filename,))
            threads.append(thread)
            thread.start()
            print("a child thread is exiting: ",filename.name)
        
        for thread in threads:
            thread.join()
        
        return results

    #print(args.filename)
    results = multi_threaded_file_reader(args.filename)
    sep_size = 50
    for file_path, content in results.items():
        print(f"Reading {file_path}:")
        #print(content)
        print("-" * sep_size)
        file_size = os.path.getsize(file_path)
        print(file_size, file_path)
    #for f in args.filename:
        #for line in f:
        # process file...
        #pass
    #https://medium.com/@darshan_doshi/large-file-splitting-with-python-threading-for-improved-performance-616f03e4622c

    '''
    if args.countbits:
        file_size = os.path.getsize(args.filename.name)
        print(file_size, args.filename.name)
    '''
   
    