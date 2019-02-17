'''
Application modules 
'''

import os
import sys
from os.path import join

'''
Calling main function to initialize sort function
'''

def parse_script(nfile):        #Defining function of parse_script and passing, object nfile.
    x = 'bash' + str(nfile)     #x is a value containing the following: 
                                #-nfile object, which has a property of string, and, the string, -'bash'.
    print('Open script: ' + x)  #Print the string 'Open Script' and value of x.
    os.system(x)                #Opens script,
                                #which is passing the value of x.

'''
Sort the dirs, loop to join root and process 
and giving it a new path/variable name 
pass new path/variable as an agrument 
to be processed
'''

def sort():                                      #Defining sort function not passing any objects
    for root, dirs, files in os.walk('scripts'): #For objects root, dirs, files within os.walk method, scan the root dir 
                                                 #named 'scripts'
        for f in file:           #For files within the dir named 'scripts',
        filename = join(root, f) #filename object has a value, which is joined by a path of the root dir, 
                                 #script dir, and script filename
                                 #modular join, groups object path root dir and 'scripts' dir, and script filename
                                 #Results: 
                                 #'scripts'/ + 'name_of_script'/ => 'scripts'/'name_of_script'
        parse_script(filename)   #passing new path/variable to parse_script() function where parse_script() will scan the root dir path of ./scripts/ by os.walk, 
                                 #then scan and execute the script files by filename within 'scripts/' dir, by connecting the string bash in filename path through os.system
                                 #Result:
                                 #OS reads 'scripts/name_of_script' as 'bash scripts/name_of_script'
'''
 All scripts will run in order
 depending on how you number them.  
'''

def main(): # Call main function which calls function sort 
            #which the parse_script() function then executes the filename of script
    sort(): # OS reads 'scripts/name_of_scrip' or filename as "./"

if __name__ == '__main__':
    main()