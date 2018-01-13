import math
loopvar=1
t=0
z=0
y=0
x=0

while(loopvar==1):
    print('\n'*50)
    print("SB-DOS RPN CALCULATOR", '\n')
    print("", t, '\n', z, '\n', y, '\n', x, '\n')
    cmd=input("$ ")

    try:
        if(type(float(cmd)) == float):
            t,z,y,x=float(z),float(y),float(x),float(cmd)
    except:
        if(str(cmd) == ""):
            t,z,y,x=z,y,x,x
        elif(str(cmd) == "break"):
            break
        
        elif(str(cmd) == "+"):
            t,z,y,x=t,t,z,y+x
        elif(str(cmd) == "-"):
            t,z,y,x=t,t,z,y-x
        elif(str(cmd) == "*"):
            t,z,y,x=t,t,z,y*x
        elif(str(cmd) == "/"):
            t,z,y,x=t,t,z,y/x
        elif(str(cmd) == "^"):
            t,z,y,x=t,t,z,y**x

        elif(str(cmd.lower()) == "clx"):
            t,z,y,x=t,z,y,0.0
        elif(str(cmd.lower()) == "cls"):
            t,z,y,x=0.0,0.0,0.0,0.0
        elif(str(cmd.lower()) == "swap"):
            tempVar=y
            t,z,y,x=t,z,x,tempVar
        elif(str(cmd.lower()) == "up"):
            t,z,y,x=z,y,x,t
        elif(str(cmd.lower()) == "down"):
            t,z,y,x=x,t,z,y
        elif(str(cmd.lower()) == "del"):
            t,z,y,x=t,t,z,y

        elif(str(cmd.lower()) == "sin"):
            t,z,y,x=t,z,y,math.sin(math.radians(x))
        elif(str(cmd.lower()) == "asin"):
            if(x <= 1):
                t,z,y,x=t,z,y,math.degrees(math.asin(x))
            else:
                print("error")
        elif(str(cmd.lower()) == "cos"):
            t,z,y,x=t,z,y,math.cos(math.radians(x))
        elif(str(cmd.lower()) == "acos"):
            if(x <= 1):
                t,z,y,x=t,z,y,math.degrees(math.acos(x))
            else:
                print("error")
        elif(str(cmd.lower()) == "tan"):
            t,z,y,x=t,z,y,math.tan(math.radians(x))
        elif(str(cmd.lower()) == "atan"):
            t,z,y,x=t,z,y,math.degrees(math.atan(x))
