import json
import os
from re import U
import time
from multiprocessing.dummy import Process
from threading import Thread
from time import sleep
from winsound import SND_ASYNC, PlaySound

from PIL import Image
from pywifi import Profile, PyWiFi
from pywifi import const as wific_
from requests import get, head
from socket import *
import math
print("This is a moudle for noob,it is packing a lot of function")
print("by bilibili:电脑君h")
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
        def connectwifi(AKM,SSID,KEY,CIPHER=CIPHER.CCMP,AUTH=WIFIAUTH.OPEN,discbuftime=1,conbuftime=2,interface=0):
            interfaces=PyWiFi()
            REAIf_=interfaces[interface]#choose interface
            REAIf_.disconnect()#disconnect wifi for next connect
            sleep(discbuftime)#wait disconnect
            if REAIf_.status==wific_.IFACE_DISCONNECTED:
                PF=Profile()#define profile
                PF.akm.append(AKM)
                PF.auth=AUTH
                PF.ssid=SSID
                PF.key=KEY
                PF.cipher=CIPHER
                TEP=REAIf_.ifaces.add_network_profile(PF)
                REAIf_.connect(TEP)#connect
            if REAIf_.status==wific_.IFACE_CONNECTED:
                return True
            else:
                return False
        def disconnetwifi():
            interfaces=PyWiFi()
            REAIf_=interfaces[0]
            REAIf_.disconnect()
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
                    self.ser=socket(socket.AF_INET, socket.SOCK_STREAM)#create socket and bind host and port
                    self.ser.bind((ip,port))
                    return
                def startlisten(self,denyip=[],denymessage="YOUR REQUEST WAS REFUSED"):
                    self.ser.listen(self.port)
                    client=self.ser.accept()#connect to client
                    if client[0] in denyip:#testfor client in denyip
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
            Π=3.1415926535897932384626433832795028
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
                    return ((longradius-shortradius)*4)+(2*useless.math.mathconst.Π*shortradius)
        class solidgraphics:
            def ball(radius):
                return (4/3)*useless.math.mathconst.Π*(radius**3)
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
        pass