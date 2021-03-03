# Sudhi Jose
import csv
import string
import os
import io
def main():
    filename = "hi.csv"
    output_file = "out.csv"
    reader(filename,output_file)

def reader(filename,output_file):
    with io.open (filename,'r',encoding="utf8") as csvfile:
        writers(csvfile,output_file)

def writers(csvfile,output_file):
    # add specail charactor
    remove_bar =  ["#","$","[]"] 
    line = ''
    with io.open (output_file,"w",encoding="utf8") as ofile:
        newf = csv.writer(ofile)
        for x in csvfile:
            line = str(x)
            for sp in remove_bar:
                line = str.replace(line,sp,'')
            newf.writerow(line.split(','))
 
if __name__=="__main__":
    main()