from pytube import YouTube
import pyfiglet
import os
import sys
def yazi():
    print(pyfiglet.figlet_format("ZVC",font = "banner3-D" ))
yazi()
print("(1)Turkish\n(2)English\n ")
dil = input("please choose your language : ")
if dil == "1":
    yazi()
    print("mp4(1)\nmp3(2)\ncikis(3)")
    download = int(input("indirmek istediğiniz dosya türünü seçiniz : "))
    if download == 1:
        def mp4():
            link = str(input("linki giriniz : "))
            yt = YouTube(link)
            stream =yt.streams.get_highest_resolution()
            stream.download()
            print("video indirildi")
            mp4()
    elif download == 2:
        def mp3():
            link = str(input("linki giriniz : "))
            yt = YouTube(link)
            stream =yt.streams.filter(only_audio=True).first()
            indirilmis = stream.download()
            ad,uza = os.path.splitext(indirilmis)
            yeni = ad + '.mp3'
            os.rename(indirilmis, yeni)
            print("görüsmek üzere ! ")
            mp3()
    elif download == 3:
        sys.exit()
elif dil == "2":
    yazi()
    print("mp4(1)\nmp3(2)\nexit(3)")
    download = int(input("please select the file type you want to download :  "))
    if download == 1:
        def mp4():
            link = str(input("please enter link : "))
            yt = YouTube(link)
            stream =yt.streams.get_highest_resolution()
            stream.download()
            print("video downloaded")
        mp4()
    elif download == 2:
        def mp3():
            link = str(input("please enter link : "))
            yt = YouTube(link)
            stream =yt.streams.filter(only_audio=True).first()
            indirilmis = stream.download()
            ad,uza = os.path.splitext(indirilmis)
            yeni = ad + '.mp3'
            os.rename(indirilmis, yeni)
            print("mp3 downloaded")
        mp3()
    elif download == 3:
        print("goodbye ! ")
        sys.exit()
       
