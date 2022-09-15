from threading import Timer

def setInterval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, setInterval, [timer, task]).start()

def hello():
    print("do something")
    return False # return True if you want to stop

if __name__ == "__main__":
    setInterval(2.0, hello) # every 2 seconds, "do something" will be printed