#files
moshe = "is the best"
file1 = "1"
file2 = "2"
file3 = "3"
file4 = "4"
file5 = "5"
file6 = "6"
filepath = ['D']
currintfolder = filepath[len(filepath)-1]
#folders
D = {
    "home" : {
        "file1":  file1,
        "file2":  file2,
        "file3":  file3,
        
        "projects": {
            "project1": file4,
            "project2": {
                "file5": file5,
            }
        },
    },
    
    "files" : {
        "moshe":  moshe,
        "file6":  file6,
    }
}
#init vars
previos = []
ECHO = True
def filepathformat(filepath):
    b = ''
    for i in filepath:
        b += '['+i+']'
    return b
def path(ECHO,filepath):
    if (ECHO):
        b = ''
        for i in filepath:
            b += i+"\\"
        
        return b[:1]+':'+b[1:]+'>'
    else:
        return ''
#commands
def dir(a,D, currintfolder):
    for items in currintfolder.items():
        print(items)

def cd(a, path):
        return a[3:]

def mkdir(a):
############################################
    D[a[:6:]] = ''
############################################
def echo(a, ECHO):
    if (a[5:] == "off"):
        print("ECHO is off")
        return False
    elif (a[5:] == "on"):
        print("ECHO is on")
        return True
    elif (a == "echo"):
        if (ECHO):
            print("ECHO is on")
            return True
        else:
            print("ECHO is off")
            return False
    else:
        print(a[5:])
        return ECHO


def commands(path, previos, ECHO, currintfolder, D):
    while True:
        currintfolder = filepath[len(filepath)-1]
        a = input(path(ECHO, filepath)).lower()
        previos += [a]
        if (a == "dir"):
            dir(a, D, currintfolder)
        elif (a.startswith("cd ")):
            if (a[3:] in D.keys()):
                filepath.append(cd(a, path))
            elif (a[3:] not in currintfolder.keys()):
                print("Folder not found")
            elif (a[3:] == ".."):
                filepath.pop(len(filepath)-1)
        elif(a.startswith("mkdir ")):
            mkdir(a)
        elif(a == "prv"):
            print(previos)
        elif(a == "exit"):
            break
        elif(a == ''):
            continue
        elif(a == "help"):
            print("\n")
            print("dir - list folders")
            print("cd - change directory")
            print("mkdir - create folder")
            print("prv - print previous commands")
            print("exit - exit application")
            print("help - print help")
            print("echo  - Displays messages, or turns file path on or off")
            print("currintfolder - print current folder")
            print("filepath - print file path in the form of a list")
            print("\n")
        elif(a.startswith("echo")):
            ECHO = echo(a, ECHO)
        elif(a == "filepath"):
            print(filepath)
        elif(a == "currintfolder"):
            print(currintfolder)
        elif(a == "filepathformat"):
            print(filepathformat(filepath))
        else:
            print( "'"+a+"'"+' is not recognized as an internal or external command, operable program or batch file.')



commands(path, previos, ECHO, currintfolder, D)