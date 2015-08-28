#!/usr/bin/env python3

import sys
import getopt

def patchMethod (inFile, outFile, patchFile):
    inl = inFile.readline()
    for patch in patchFile:
        if (patch[0] == '-'):
            while (inl.strip()):
                if (inl == patch[2:]):
                    inl = inFile.readline()
                    break
                outFile.write(inl)
                inl = inFile.readline()
        elif (patch[0] == '+'):
            while (True):
                if (inl > patch[2:] or not inl.strip()):
                    outFile.write(patch[2:])
                    break
                outFile.write(inl)
                inl = inFile.readline()
        else:
            print("Error no valid patch file")
            sys.exit(1)

def diffMethod (inFile, outFile, patchFile):
    inl = inFile.readline()
    outl = outFile.readline()

    while (inl.strip() or outl.strip()):
        if (inl.strip() == outl.strip()):
            #patchFile.write("o " + inl)
            inl = inFile.readline()
            outl = outFile.readline()
        elif ((inl < outl or not outl.strip()) and inl.strip()):
            patchFile.write("- " + inl)
            inl = inFile.readline()
        elif ((inl > outl or not inl.strip()) and outl.strip()):
            patchFile.write("+ " + outl)
            outl = outFile.readline()

def main (args=sys.argv):
    prog = args[0]
    args = args[1:]
    try:
       opts, args = getopt.getopt(args, "hi:p:o:m:", ["help", "inFile=", "patch=", "outFile=", "mode="])
    except getopt.GetoptError as err:
       usage()
       sys.exit(2)

    inFile = None
    outFile = None
    patchFile = None

    for opt, opt_val in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-i", "--inFile"):
            inFile = opt_val
        elif opt in ("-o", "--outFile"):
            outFile = opt_val
        elif opt in ("-p", "--patch"):
            patchFile = opt_val
        elif opt in ("-m", "--mode"):
            if (opt_val == "diff"):
                prog = "sdiff"
            elif (opt_val == "patch"):
                prog = "spatch"
        else:
            assert False, "unhandled option"

    if (prog == "spatch"):
        if (not inFile):
            print("Error: in file has to be specified")
            usage()
            sys.exit(1)
        inf = open(inFile, 'r')

        if (outFile == None):
            outf = sys.stdout
        else:
            outf = open(outFile, 'w')

        if (patchFile == None):
            patchf = sys.stdin
        else:
            patchf = open(patchFile, 'r')

        patchMethod(inf, outf, patchf)

        outf.close()
        patchf.close()
        inf.close()

    elif (prog == "sdiff"):
        if (not inFile or not outFile):
            print("Error: In and out file has to be specified")
            usage()
            sys.exit(1)

        inf = open(inFile, 'r')
        outf = open(outFile, 'r')

        if (patchFile == None):
            patchf = sys.stdout
        else:
            patchf = open(patchFile, 'w')

        diffMethod(inf, outf, patchf)

        inf.close()
        outf.close()
        patchf.close()


def usage ():
    print("-m --mode [diff or patch]")
    print("-i --inFile input file")
    print("-o --outFile output file")
    print("-p --patchFile patch file")

if __name__ == "__main__":
    main()
