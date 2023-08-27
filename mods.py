import os
import shutil
print("loading...")
with open("mods.txt", "a+") as f:
    def start():
        f.seek(0)
        if f.read() == "":
            path = getpath("enter location of minecraft mods folder: ")
            if path != "":
                f.write(path+"\n")
            else:
                start()
        reload()
    def helpmsg():
        print("help message")
    def quitmods():
        match input("close? y/n \n"):
            case "y":
                quit()
            case "n":
                pass
            case _:
                print("invalid answer")
                quitmods()
    def activemods():
        print("active mods:")
        for i in os.listdir(file[0]):
            try:
                print("   " + modfiles[i])
            except KeyError:
                print(" ? " + i)
    def reload():
        f.seek(0)
        global file
        global modnames
        global modfiles
        global rmodfiles
        file = (f.read().split("\n"))[:-1]
        modnames = {}
        modfiles = {}
        rmodfiles = {}
        for i in file[1:]:
            i = i.split(":")
            modnames[i[2]] = i[0] + ":" + i[1]
            modfiles[i[1].split("/")[-1]] = i[2]
        for i in modfiles:
            rmodfiles[modfiles[i]] = i
    def addmods():
        path = getpath("enter mod location: ")
        if path != "":
            f.write(path+":")
            f.write(input("enter mod name: ")+"\n")
            reload()
    def getpath(prompt):
        path = input(prompt).replace("\\","/")
        if os.path.exists(path):
            return path
        else:
            print("file or directory does not exist")
            return ""
    def installedmods():
        print("installed mods:")
        for i in modnames:
            print("   " + i)
    def putmod():
        mod = input("mod to add to minecraft: ")
        if mod in modnames:
            shutil.copy(modnames[mod], file[0])
            print("installed mod " + rmodfiles[mod])
        else: 
            print("no such mod")
    def removemod():
        mod = input("mod to remove from minecraft: ")
        if mod in rmodfiles:
            mod = rmodfiles[mod]
        if mod in os.listdir(file[0]):
            os.remove(file[0] + "/" + mod)
            print("removed mod " + mod)
        else:
            print("mod is not active")
    def debug():
        print("DEBUG:")
        print()
    def ask():
        match input(">>>"):
            case "h": helpmsg()
            case "q": quitmods()
            case "am": activemods()
            case "a": addmods()
            case "d": debug()
            case "im": installedmods()
            case "p": putmod()
            case "r": removemod()
            case _:
                print("unknown command. type 'help' or 'h' to see list of available commands")
    start()
    while True:
        ask()
