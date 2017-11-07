#-*- coding:utf-8 -*-
import os,time
###########################
#     code edit by:whoisk
#   email:
#   2077279363@qq.com
#   seclaen@gmail.com
#   date:
#         2017,11,07
###########################


def Logo():
    Clear()
    print "*"*20
    print 'Welcome Auto Install the linux gui'
    print '*'*20

def Massages():
	print """
        [!]Err0rr plase check and try agin! 
        [back options need waiting 3s...]
        """
	time.sleep(3)

def GetEnter():
    try:
        Tmp=int(input("[#]Ent3r Y0u Ch0!s3 Numb3r>"))
    except:
        Tmp=0
    return Tmp

def Clear():
    try:
        os.system("clear")
    except:
        os.system("cls")
        print "[!]System Error;That Srcipt is Run with Linux System,Plase Running on installed linux sytem computer;"

def InOrUn():
    Clear()
    print """
    ******************************
    0)Install
    1)Unstall
    ******************************
    """

def Choise(x,y):
    PackageList=[
            [
              "apt-get install gnome-core kali-defaults kali-root-login desktop-base",
              "apt-get remove gnome-core"
            ],
            [
              "apt-get install kali-defaults kali-root-login desktop-base kde-plasma-desktop",
              "apt-get remove kde-plasma-desktop"
            ],
            [
              "apt-get install kali-defaults kali-root-login desktop-base kde-plasma-netbook",
              "apt-get remove  kde-plasma-netbook"
            ],
            [ "apt-get install kali-defaults kali-root-login desktop-base kde-standard",
              "apt-get remove kde-standard"
            ],
            [
              "apt-get install kali-defaults kali-root-login desktop-base kde-full",
              "apt-get remove  kde-full"
            ],
            [
              "echo NULL",
              "echo NULL"
            ],
            [
             "apt-get install kali-defaults kali-root-login desktop-base xfce4 xfce4-places-plugin xfce4-goodies",
             "apt-get remove xfce4 xfce4-places-plugin xfce4-goodies"
            ],
            [
             "apt-get install lxde-core lxde kali-defaults kali-root-login desktop-base",
             "apt-get remove lxde-core"
            ],
            [
             "apt-get install kali-defaults kali-root-login desktop-base cinnamon",
             "apt-get remove cinnamon"],
            [
             "apt-get install xorg dmenu conky i3",
             "apt-get remove xorg dmenu conky i3"
            ],
            [
             "apt-get install kali-defaults kali-root-login desktop-base mate-core mate-desktop-environment mate-desktop-environment-extra",
             "apt-get remove  mate-core mate-desktop-environment mate-desktop-environment-extra"
            ]
                   ]
    command=PackageList[x][y]
    print command 
    os.system(command)
    time.sleep(1)
    Options2()



def RollingSet():
    fp=open("Cache","w")
    x="deb http://http.kali.org/kali kali-rolling main non-free contri\n#中科大\ndeb http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib\ndeb-src http://mirrors.ustc.edu.cn/kali kali-rolling main non-free contrib\n#浙大\ndeb http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free\ndeb-src http://mirrors.zju.edu.cn/kali kali-rolling main contrib non-free\n#东软大学\ndeb http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib\ndeb-src http://mirrors.neusoft.edu.cn/kali kali-rolling/main non-free contrib\n#重庆大学\ndeb http://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src http://http.kali.org/kali kali-rolling main non-free contrib\n#官方源\n#deb http://http.kali.org/kali kali-rolling main non-free contrib\n#deb-src http://http.kali.org/kali kali-rolling main non-free contrib\ndeb http://repo.mate-desktop.org/debian wheezy main\ndeb http://http.debian.net/debian wheezy-backports main contribnon-free\n"
    fp.write(x)
    fp.close()
    print "Plase Waiting UPDATA execute..."
    os.system("cat Cache|xargs >/etc/apt/sources.list")
    os.system("rm Cache")
    try:
        os.system("apt-get clean&apt-get update")
    except:
        print "***********************STOP**UPDATA*****************"
    print "******************[DONE-OK-]***************************"
    Options1()



def Options2():
    Clear()
    print """
    ***********************************************
    /1)GNOME
    /2)KDE--plasma
    /3)KDE--netbook
    /4)KDE--standard
    /5)KDE--full
    /7)XFCE
    /8)LXDE
    /9)Cinnamon
    /10)i3wm
    /11)mate
    /99)[Back]
    ***********************************************
    """
    tmp=GetEnter()
    if tmp== 0:
        Options2()
    elif tmp== 99:
        print "!OK"
        exit()
    InOrUn()
    try:
        y=int(input("[0 or 1]>"))
        if y== 0:
            pass
        elif y== 1:
            pass
        else:
            y=0
    except:
        y=0

    if tmp< 12:
        x=tmp-1
        Choise(x,y)
    elif tmp== 99:
        Options1()
    else:
        Massages()
        Options2()


def Options1():
    print """
    ***********************************************
    /1)SET APT ROLLING
    /2)SET SYS GUI
    /3)SET CONFIG  <GUI>
    /99)Exit
    ***********************************************
    """
    tmp=GetEnter()
    if tmp== 1:
        RollingSet()
    elif tmp == 2:
        Options2()
    elif tmp == 3:
        os.system("update-alternatives --config x-session-manager ")
        Options1()
    elif tmp == 99:
        exit()
    else:
        Massages()
        Options1()

def main():
    Logo()
    Options1()



if __name__=="__main__":
    try:
        os.system("rm Cache")
    except:
        pass
    try:
        main()
        Clear()
    except:
        Clear()
        print "[*]A ERRORR;Maybe is user shutdown/exit it;"
