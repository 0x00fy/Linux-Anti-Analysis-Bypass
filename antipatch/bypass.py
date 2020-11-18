#!/usr/bin/python3

#/
#   Github.com/0x00fy
#   Linux Anti Analysis Bypass
#\

import os,sys
import os.path


def Helprr():
    print("""
            Usage : python bypass.py ./a.out
              
              Anti Analysis Bypass Techniques
            			
            		Github.com/0x00fy
    """)

def Clear():
    if(os.path.isfile("bypass.so")):   
        os.system("rm -rf bypass.so")    

def Derle():
    os.system("gcc bypass.c -o bypass.so -fPIC -shared -ldl -D_GNU_SOURCE")


def Bypass(binary):
    if os.path.isfile(binary):
        simdikiyer = os.getcwd()
        evillib = simdikiyer + "/bypass.so"
        print("Press [CTRL +C] To Continue..")
        os.system("export LD_PRELOAD=" + evillib + " && gdb -q " + binary) #Gdb Bypass
        exit(1)
    else:
        print("No such file or Directory : " + binary)    
        exit(1)
        
def main():
    try:
        
        Clear()
        binary = sys.argv[1]
        Derle()       
        Bypass(binary)

    except Exception as e:
        Helprr()
        print(e)

if __name__ == '__main__':
    exit(main())