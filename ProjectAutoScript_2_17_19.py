import os 
import sys 
from os.path import join

def parse_script(nfile):
    x = 'bash ' + str(nfile)
    print('Opening script: ' + x)
    os.system(x) #Opens script

def sort():
    for root, dirs, files in os.walk('scripts'):
        for f in file:
            filename = join(root, f)
            parse_script(filename)

def main():
    sort()

if __name__ == '__main__':
    main()