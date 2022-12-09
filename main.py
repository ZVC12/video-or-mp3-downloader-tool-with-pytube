from pytube import YouTube
import pyfiglet
import os
print(pyfiglet.figlet_format("ZVC",font = "banner3-D" ))
print("mp4(1)\nmp3(2)\ncikis(3)")
try:
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
        mp3()
    elif download == 3:
        quit()


except(ValueError()):
    print("lütfen menüde belirtilen rakamlardan birini seçiniz !")

    