# Python code to Show DateTime 
def datetime():
    import datetime
    now = datetime.datetime.now()
    print("Current Date and Time = ",now.strftime("%Y - %m - %d : %H - %M - %S "))
datetime()
