import webbrowser
import time

i=0
print ("prog strted on "+time.ctime())
while i <= 2:
    time.sleep(3)
    webbrowser.open("https://www.youtube.com/watch?v=xin92Rq3pco")
    print ("break no "+(str(i+1))+" - "+time.ctime())
    i=i+1
    
