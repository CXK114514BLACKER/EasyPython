import json
import os
import time
from multiprocessing.dummy import Process
from threading import Thread
from time import sleep
from tkinter import *
from winsound import SND_ASYNC, PlaySound

from PIL import Image
from pywifi import Profile, PyWiFi
from pywifi import const as wific_
from requests import get, head
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
    why does him do the library?
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
        class WIFIAUTH:
            OPEN=wific_.AUTH_ALG_OPEN
            SHARED=wific_.AUTH_ALG_SHARED
        def connectwifi(AKM,SSID,KEY,CIPHER=CIPHER.CCMP,AUTH=WIFIAUTH.OPEN,discbuftime=1,conbuftime=2):
            interfaces=PyWiFi()
            REAIf_=interfaces[0]
            REAIf_.disconnect()
            sleep(discbuftime)
            if REAIf_.status==wific_.IFACE_DISCONNECTED:
                PF=Profile()
                PF.akm.append(AKM)
                PF.auth=AUTH
                PF.ssid=SSID
                PF.key=KEY
                PF.cipher=CIPHER
                TEP=REAIf_.ifaces.add_network_profile(PF)
                REAIf_.connect(TEP)
            if REAIf_.status==wific_.IFACE_CONNECTED:
                return True
            else:
                return False
        def disconnetwifi():
            interfaces=PyWiFi()
            REAIf_=interfaces[0]
            REAIf_.disconnect()
    class image:
        def imgformat(image,dir,toformat="png"):
            img=Image.ogen(image)
            img.save(dir+image.split(".")[1]+toformat)
        def imgchange(image,mode):
            img=Image.open(image)
            return img.convert(mode)
        def imgcut(image,ax,ay,bx,by):
            return Image.open(image).crop(box=(ax,ay,bx,by))
    class download:
        def download():
            pass
        def muilthreaddownload(url,path,threadpcs=8):
            file=(path+"\\{}".format(url.split("/")[-1]))
            threadlist=[]
            def threadfunc(function,args):#use new thread to open function
                thread=Thread(target=function,args=args)
                threadlist.append(thread)
                thread.start()
            def WAy(file,start,end):#download chunk
                data_=get(url=url,headers={"Range":f"bytes={start}-{end}"})
                with open(file=file,mode="rb+") as f_:
                    f_.seek(start)
                    f_.write(data_.content)
            size=int(head(url=url).headers["Content-Length"])
            print(size)
            chunksize=size//threadpcs
            print(chunksize)
            with open(file=file,mode="wb"):#create file
                pass
            for s_ in range(threadpcs-1):#start download
                threadfunc(WAy,args=(file,s_*chunksize,(s_+1)*chunksize))
            threadfunc(WAy,args=(file,threadpcs*chunksize,(s_+1)*chunksize))
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
            pi,Π=3.1415926535897932384626433832795028
            homo=114514
            homo_2=1919810
        class graphics:
            def circlesize(radius):
                return (radius**2)*useless.math.mathconst.Π
            def halfcirclesize(radius):
                return (radius**2)*useless.math.mathconst.Π/2
            def polygonsize(radius,edgelong,edgepcs):
                (radius*edgelong)/2*edgepcs
        class solidgraphics:
            def ball():
                pass
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