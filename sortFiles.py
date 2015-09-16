import magic
import os
import shutil

def main():
    # read options from maltrieve.cfg
    try:
        configFile = open("maltrieve.cfg", "r")
        for lines in configFile.readlines():
            if "dumpdir" in lines:
                malwareDirectory = lines.strip("\n").split('=')[1].strip(" ")
    except:
        print "No config file"
        exit(0)

    #check for malware directory
    try:
        os.chdir(malwareDirectory)
    except:
        print "malware folder doesn't exist"
        exit(0)

    #define folders to sort into
    fileTypeDirs = ['pdf', 'exe', 'zip', 'jar', 'misc', 'xml', 'html']

    for dirs in fileTypeDirs:
        try:
            os.mkdir(dirs)
        except Exception as e:
            pass
            #print e

    files = os.listdir(".")
    if sorted(fileTypeDirs) == sorted(files):
        print "All files sorted, exiting"
        exit(0)

    if files == []:
        print "Empty Folder"
    else:
        for file in files:
            type = magic.from_file(file)
            if "PE32" in type:
                shutil.move(os.getcwd()+"/"+file, os.getcwd()+"/"+"exe/"+file)
            elif "HTM" in type:
                shutil.move(os.getcwd()+"/"+file, os.getcwd()+"/"+"html/"+file)
            elif "PDF" in type:
                shutil.move(os.getcwd()+"/"+file, os.getcwd()+"/"+"pdf/"+file)
            elif "Zip" in type:
                shutil.move(os.getcwd()+"/"+file, os.getcwd()+"/"+"zip/"+file)
            elif "RAR" in type:
                shutil.move(os.getcwd()+"/"+file, os.getcwd()+"/"+"zip/"+file)
            elif "7z" in type:
                shutil.move(os.getcwd()+"/"+file, os.getcwd()+"/"+"zip/"+file)
            elif "Jar" in type:
                shutil.move(os.getcwd()+"/"+file, os.getcwd()+"/"+"jar/"+file)
            elif "directory" in type:
                pass
            elif "XML" in type:
                shutil.move(os.getcwd()+"/"+file, os.getcwd()+"/"+"xml/"+file)
            elif "XML" in type:
                shutil.move(os.getcwd()+"/"+file, os.getcwd()+"/"+"xml/"+file)
            elif "empty" in type:
                os.remove(os.getcwd()+"/"+file)
                pass
            else:
                print file, type
                shutil.move(os.getcwd()+"/"+file, os.getcwd()+"/"+"misc/"+file)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(0)