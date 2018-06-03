import os, sys
import argparse, binascii

if sys.version_info.major != 3:
    print("[!] This script requires Python 3")
    sys.exit(1)
    
def main(args):
    inj = len(args.inject)
    if inj % 2 == 1:
        print("[!] Bytes to inject must be even, example: 00")
        sys.exit(1)
        
    data = open(args.doc, 'rb').read()
    newBytes = binascii.unhexlify(args.inject)
    repBytes = data[:len(newBytes)]
    data2 = data.replace(data[:len(newBytes)], newBytes, 1)
    print("[+] Replacing {} with {}".format(repBytes, newBytes))
    
    diff = data[len(args.inject):] == data2[len(args.inject):]
    if diff == True:
        print('[+] Old == New')
    else:
        print('[!] Old != New')
    
    with open(args.doc, 'wb') as f:
        f.write(data2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Change Magic Bytes, ', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-b', '--inject', help='Bytes to inject', required=True)
    parser.add_argument('-d', '--doc', help='doc', required=True)
    args = parser.parse_args()
    main(args)