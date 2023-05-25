
sys = {
   "a": {
        "b": "hello",
        "e": "hi",
        "f": "hey"
        },
    "c": {
        "d": "world",
        "g": "bye",
        "h": "goodbye",
        "i": {
            "j": {
                "m": "fun",
                "n": "super",
                "o": "cool",
            },
            "k": {
                "p": "nice",
                "q": "good",
                "r": "great",
            },
            "l": {
                "s": {
                    "t": "awesome",
                    "u": "amazing",
                    "v": "fantastic",
                },
                "w": {
                    "x": "wow",
                    "y": "wonderful",
                    "z": "excellent",
                }
            }
        }
    }
}
pointers = ["sys","sys/a","sys/c","sys/a/b","sys/c/d","sys/c/i","sys/c/i/j","sys/c/i/k","sys/c/i/l","sys/c/i/l/s","sys/c/i/l/w","sys/c/i/l/s/t","sys/c/i/l/s/u","sys/c/i/l/s/v","sys/c/i/l/w/x","sys/c/i/l/w/y","sys/c/i/l/w/z"]
file = [sys,sys["a"],sys["c"],sys["a"]["b"], sys["c"]["d"], sys["c"]["i"], sys["c"]["i"]["j"], sys["c"]["i"]["k"], sys["c"]["i"]["l"], sys["c"]["i"]["l"]["s"], sys["c"]["i"]["l"]["w"], sys["c"]["i"]["l"]["s"]["t"], sys["c"]["i"]["l"]["s"]["u"], sys["c"]["i"]["l"]["s"]["v"], sys["c"]["i"]["l"]["w"]["x"], sys["c"]["i"]["l"]["w"]["y"], sys["c"]["i"]["l"]["w"]["z"]]
currentpath = "sys/c/i/l/w/z"


def list(d):
    log = []
    try:
        for key in d.keys():
            log.append(key)
        return log
    except:
        return ""
    
def listnice(d):
    log = list(d)
    for i in log:
        print(i)
def filepath(path):
    return path + "> "

def currentfolder(file,currentpath,pointers):
    for i in range(len(pointers)):
        if currentpath == pointers[i]:
            return list(file[i])

def breakfilepath(currentpath):
    output = ""
    parts = currentpath.split("/")
    if len(parts) > 1:
        parts.pop(len(parts) - 1)
        
        for i in parts:
            output += i
            output += "/"
        return output.rstrip(output[-1])
    else:
        return currentpath

running = True
while running:
    resolve = False
    query = input(filepath(currentpath))
    
    if query == "x":
        running = False
        resolve = True
    
    elif query.startswith("newdir "):

        sys[query[7:]] = {}
        pointers.append(currentpath + "/" + query[7:])
        print(pointers)

    elif query == "pointers":
        print(pointers)
        resolve = True

    elif query == "cd..":
        currentpath = breakfilepath(currentpath)
        resolve = True

    elif query.startswith("cd "):
        if query[3:] in currentfolder(file,currentpath,pointers):
            currentpath += "/" + query[3:]
        else:
            print("not found")
        resolve = True 

    elif query == "":
        resolve = True

    elif query == "dir":
        directorys = currentfolder(file, currentpath, pointers)
        for i in directorys:
            print(i)
    elif query.startswith("list "):
        if query[5:] in currentfolder(file,currentpath,pointers):
            print(isinstance((currentfolder(file,currentpath,pointers)), str))
            print(currentfolder(file,currentpath,pointers))
        else:
            print("not found")
    else:
        for i in range(len(pointers)):
            if query == pointers[i]:
                list(file[i])
                resolve = True
        if not resolve:
            print("not found")
