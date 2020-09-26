import sys, time

def welcome():
    f = open("header.txt", "r")
    print (f.read())

def animation():
    
    animation = "|/-\\"

    for i in range(7):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    