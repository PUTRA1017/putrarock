# -*- coding: utf-8 -*- 
import LINEPY
from LINEPY import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, pafy, time, timeit, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, wikipedia
from datetime import timedelta, date
from datetime import datetime
from bs4 import BeautifulSoup
import youtube_dl

cl = LINE('EwvYZdgbpVqoeLCraqR7.U9vqKWhBEPl2gR+zr/FkHW.gdqdB4K0d38Ph6fCPIp7vCCCLne2wRZ5WMypdbIj13w=')
cl.log("Auth Token : " + str(cl.authToken))
#channel = LineChannel(cl)
cl.log("Timeline Token : " + str(cl.tl.channelAccessToken))

ki = LINE('EwBGKdG4CNTKpe46mrHa.lu3bCqS5RU/I0Y0Ycd0VQG.H2Aw+m4IYqd9+De7L7TBil3F5wtwkaihRrh4m4xItHA=')
ki.log("Auth Token : " + str(ki.authToken))
#channel1 = LineChannel(ki)
ki.log("Timeline Token : " + str(ki.tl.channelAccessToken))

kk = LINE('Ewb5wuje0UqcJWp1oiX0.2a2mTvzEx0A+udpqO/Ggma.OxZHkC+DhrCzMdWw++1QMkAlu75sD6kvjf2yw3e0D6M=')
kk.log("Auth Token : " + str(kk.authToken))
#channel2 = LineChannel(kk)
kk.log("Timeline Token : " + str(kk.tl.channelAccessToken))

kc = LINE('EwH8J2yVImrUai85wb52.ie1YBXtnd6ZiiWMAt7HOWG.yuicXJGjyzQsBsX3n36VQOsoeDe/7FRseq0tXAbd2YI=')
kc.log("Auth Token : " + str(kc.authToken))
#channel3 = LineChannel(kc)
kc.log("Timeline Token : " + str(kc.tl.channelAccessToken))

ka = LINE('Ew85kFFskBXWGfoqtcZf.U0ZaImTQHUAHfRk76d5dRW.zNvu3lmo8gb/EmocwkLOv6PhT5/4RqcSGbKG38OiJbU=')
ka.log("Auth Token : " + str(ka.authToken))
#channel4 = LineChannel(ka)
ka.log("Timeline Token : " + str(ka.tl.channelAccessToken))


sw = LINE('EwXL3E4lLxN9DdDhAfj2.kzf68PCCs2ZPG1Lr/RWbSG.gZBzL+HXmDBVNShKqmKgMoNVGfiKIRc06wvHm0Gpiy8=')
sw.log("Auth Token : " + str(sw.authToken))
#channel5 = LineChannel(sw)
sw.log("Timeline Token : " + str(sw.tl.channelAccessToken))

poll = OEPoll(cl)
call = cl
creator = ["ubbd5509301db7a92f61abfd947e7ca87"]
owner = ["ubbd5509301db7a92f61abfd947e7ca87"]
admin = ["ubbd5509301db7a92f61abfd947e7ca87","ua881db3f7a6989c69eb651673a9db37b"]
staff = ["ubbd5509301db7a92f61abfd947e7ca87"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ka.getProfile().mid
Zmid = sw.getProfile().mid
KAC = [cl,ki,kk,kc,ka]
ABC = [ki,kk,kc,ka]
Bots = [mid,Amid,Bmid,Cmid,Dmid,Zmid]
Saints = admin + staff

protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectghost = []
welcome = []

responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = ka.getProfile().displayName
        
print ("╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ ROCK SELF BOT BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════")
settings = {
    "Picture":False,
    "group":{},
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}

wait = {
    "limit": 1,
    "lang": "JP",
    "likeOn": False,
    "autoCancel":{"on":True, "members":1},
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "unsend":True,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":True,
    "Mentionkick":False,
    "welcomeOn":False,
    "sticker":False,
    "selfbot":True,
    "pelaku": False,
    "mention":"NGINTIPPP!!!",
    "Respontag":"APA AN SIH OM TAG TAG MULU",
    "welcome":"Selamat datang & betah",
    "comment":"Like like & like by PUTRAROCK",
    "message":"Terimakasih sudah add saya 😃\n☆| PUTRAROCK |☆\n\nOpen Tikungan:\n┃🇮🇩┃ 1 hari 1000c\n┃🇮🇩┃ 1 minggu 2 juta 😁\n\nMinat?\nChat aja...",
    "commentBlack":{},
    "commentOn":True  
    }

#read = {
#    "readPoint":{},
#    "readMember":{},
#    "readTime":{},
#    "ROM":{},
#}

read = {
      "readPoint":{},
      "readMember":{},
      "readTime":{},
      "ROM":{},
      "setTime":{}
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)

Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

setTime = {}
setTime = read['setTime']

mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kc.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ka.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   sw.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kk.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kc.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ka.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          sw.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start() 

def likefriend():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil ['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          print ("Like")
        except:
          pass
      else:
          print ("Already Liked")
time.sleep(0.60)
        
#def sendMention(to, mid, firstmessage):
#    try:
#        arrData = ""
#        text = "%s " %(str(firstmessage))
#        arr = []
#        mention = "@x \n"
#        slen = str(len(text))
#        elen = str(len(text) + len(mention) - 1)
#        arrData = {'S':slen, 'E':elen, 'M':mid}
#        arr.append(arrData)
#        today = datetime.today()
#        future = datetime(2018,3,1)
#        hari = (str(future - today))
#        comma = hari.find(",")
#        hari = hari[:comma]
#        teman = cl.getAllContactIdsx()
#        gid = cl.getGroupIdsJoined()
#        tz = pytz.timezone("Asia/Jakarta")
#        timeNow = datetime.now(tz=tz)
#        eltime = time.time() - mulai
#        bot = runtime(eltime)
#        text += mention+"┃🇮🇩┃ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n┃🇮🇩┃ Group : "+str(len(gid))+"\n┃🇮🇩┃ Teman : "+str(len(teman))+"\n┃🇮🇩┃ Expired : In "+hari+"\n┃🇮🇩┃ Version : PUTRAROCK\n┃🇮🇩┃ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n┃🇮🇩┃ Runtime : \n • "+bot
#        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#    except Exception as error:
#        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"◐ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n🐚 Group : "+str(len(gid))+"\n🐚 Teman : "+str(len(teman))+"\n🐚 Expired : In "+hari+"\n🐚 Version : PUTRAGVCBOT\n🐚 Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n🐚 Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))
         
        
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭━━━━━━━━━━━━━━━╮\n" + \
                  "                           MENU \n" + \
                  "    ✡Help\n" + \
                  "    ✡Hpro\n" + \
                  "    ✡Menubot\n" + \
                  "    ✡Menubot2\n" + \
                  "    ✡Media\n" + \
                  "    ✡HelpAdmin\n" + \
                  "    ✡HelpSelf\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n" + \
                  "┃🇮🇩┃ " + key + "Me\n" + \
                  "┃🇮🇩┃ " + key + "Mid「@」\n" + \
                  "┃🇮🇩┃ " + key + "Info「@」\n" + \
                  "┃🇮🇩┃ " + key + "Nk「@」\n" + \
                  "┃🇮🇩┃ " + key + "Kick1「@」\n" + \
                  "┃🇮🇩┃ " + key + "Mybot\n" + \
                  "┃🇮🇩┃ " + key + "Status\n" + \
                  "┃🇮🇩┃ " + key + "About\n" + \
                  "┃🇮🇩┃ " + key + "Restart\n" + \
                  "┃🇮🇩┃ " + key + "Runtime\n" + \
                  "┃🇮🇩┃ " + key + "Creator\n" + \
                  "┃🇮🇩┃ " + key + "Speed/Sp\n" + \
                  "┃🇮🇩┃ " + key + "Sprespon\n" + \
                  "┃🇮🇩┃ " + key + "Tagall\n" + \
                  "┃🇮🇩┃ " + key + "Joinall\n" + \
                  "┃🇮🇩┃ " + key + "Byeall\n" + \
                  "┃🇮🇩┃ " + key + "Byeme\n" + \
                  "┃🇮🇩┃ " + key + "Leave「Namagrup」\n" + \
                  "┃🇮🇩┃ " + key + "Ginfo\n" + \
                  "┃🇮🇩┃ " + key + "Open\n" + \
                  "┃🇮🇩┃ " + key + "Close\n" + \
                  "┃🇮🇩┃ " + key + "Url grup\n" + \
                  "┃🇮🇩┃ " + key + "Gruplist\n" + \
                  "┃🇮🇩┃ " + key + "Infogrup「angka」\n" + \
                  "┃🇮🇩┃ " + key + "Infomem「angka」\n" + \
                  "┃🇮🇩┃ " + key + "Remove chat\n" + \
                  "┃🇮🇩┃ " + key + "Lurking「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Lurkers\n" + \
                  "┃🇮🇩┃ " + key + "Sider「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Updatefoto\n" + \
                  "┃🇮🇩┃ " + key + "Updategrup\n" + \
                  "┃🇮🇩┃ " + key + "Updatebot\n" + \
                  "┃🇮🇩┃ " + key + "Broadcast:「Text」\n" + \
                  "┃🇮🇩┃ " + key + "Setkey「New Key」\n" + \
                  "┃🇮🇩┃ " + key + "Mykey\n" + \
                  "┃🇮🇩┃ " + key + "Resetkey\n" + \
                  "╰━━━━━━━━━━━━━━━╯"
    return helpMessage  
def helpmedia():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = """
   ╔═══════════════               
   ┃🇮🇩┃ Mp3:[Mp3 nama band/lagu]
   ┃🇮🇩┃ ytb:[daftar list youtube]
   ┃🇮🇩┃ wikipedia
   ┃🇮🇩┃ image
   ┃🇮🇩┃ playstore
   ┃🇮🇩┃ id smule
   ┃🇮🇩┃ ID line:「Id Line nya」
   ┃🇮🇩┃ Sholat:「Nama Kota」
   ┃🇮🇩┃ Cuaca:「Nama Kota」
   ┃🇮🇩┃ Lokasi:「Nama Kota」
   ┃🇮🇩┃ Music:「Judul Lagu」
   ┃🇮🇩┃ Lirik:「Judul Lagu」
   ┃🇮🇩┃ Ytmp3:「Judul Lagu」
   ┃🇮🇩┃ Ytmp4:「Judul Video」
   ┃🇮🇩┃ Profileig:「Nama IG」
   ┃🇮🇩┃ Cekdate:「tgl-bln-thn」
   ┃🇮🇩┃ Jumlah:「angka」
   ┃🇮🇩┃ Spamtag「@」
   ┃🇮🇩┃ Spamcall:「jumlahnya」
   ┃🇮🇩┃ Spamcall
   ╰━━━━━━━━━━━━━━━╯"""
    return helpMessage
def helpprotect():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃🇮🇩┃ " + key + "Notag「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Semuapro「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Protecturl「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Protectjoin「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Protectkick「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Protectcancel「on/off」\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃🇮🇩┃ ┃DPK┃ SETTING ┃🇮🇩┃\n──┅━✥ ======= ✥━┅──\n"
    return helpMessage
def helpadmin():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃🇮🇩┃ " + key + "Sticker「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Respon「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Contact「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Autojoin「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Autoadd「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Welcome「on/off」\n" + \
                  "┃🇮🇩┃ " + key + "Autoleave「on/off」\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃🇮🇩┃ ┃DPK┃ ADMIN ┃🇮🇩┃\n──┅━✥ ======= ✥━┅──\n"
    return helpMessage
def helpself():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃🇮🇩┃ " + key + "Admin:on\n" + \
                  "┃🇮🇩┃ " + key + "Admin:repeat\n" + \
                  "┃🇮🇩┃ " + key + "Staff:on\n" + \
                  "┃🇮🇩┃ " + key + "Staff:repeat\n" + \
                  "┃🇮🇩┃ " + key + "Bot:on\n" + \
                  "┃🇮🇩┃ " + key + "Bot:repeat\n" + \
                  "┃🇮🇩┃ " + key + "Adminadd「@」\n" + \
                  "┃🇮🇩┃ " + key + "Admindell「@」\n" + \
                  "┃🇮🇩┃ " + key + "Staffadd「@」\n" + \
                  "┃🇮🇩┃ " + key + "Staffdell「@」\n" + \
                  "┃🇮🇩┃ " + key + "Botadd「@」\n" + \
                  "┃🇮🇩┃ " + key + "Botdell「@」\n" + \
                  "┃🇮🇩┃ " + key + "Refresh\n" + \
                  "┃🇮🇩┃ " + key + "Listbot\n" + \
                  "┃🇮🇩┃ " + key + "Listadmin\n" + \
                  "┃🇮🇩┃ " + key + "Listprotect\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃🇮🇩┃ ┃DPK┃ FAMS┃🇮🇩┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n┣🇮🇩━⏩PUTRAROCKBOT🇮🇩━⏩\n╰━━━━━━━━━━━━━━━╯\n"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "──┅━✥ ======= ✥━┅──\n┃🇮🇩┃ ┃DPK┃ BLACKLIST ┃🇮🇩┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃🇮🇩┃ " + key + "Blc\n" + \
                  "┃🇮🇩┃ " + key + "Ban:on\n" + \
                  "┃🇮🇩┃ " + key + "Unban:on\n" + \
                  "┃🇮🇩┃ " + key + "Ban「@」\n" + \
                  "┃🇮🇩┃ " + key + "Unban「@」\n" + \
                  "┃🇮🇩┃ " + key + "Talkban「@」\n" + \
                  "┃🇮🇩┃ " + key + "Untalkban「@」\n" + \
                  "┃🇮🇩┃ " + key + "Talkban:on\n" + \
                  "┃🇮🇩┃ " + key + "Untalkban:on\n" + \
                  "┃🇮🇩┃ " + key + "Banlist\n" + \
                  "┃🇮🇩┃ " + key + "Talkbanlist\n" + \
                  "┃🇮🇩┃ " + key + "Clearban\n" + \
                  "┃🇮🇩┃ " + key + "Refresh\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃🇮🇩┃ ┃DPK┃ MENU ┃🇮🇩┃\n──┅━✥ ======= ✥━┅──\n"
    return helpMessage1
def helpbot2():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 ="╭━━━━━━━━━━━━━━━╮\n" + \
                  "┃🇮🇩┃ " + key + "Cek sider\n" + \
                  "┃🇮🇩┃ " + key + "Cek spam\n" + \
                  "┃🇮🇩┃ " + key + "Cek pesan \n" + \
                  "┃🇮🇩┃ " + key + "Cek respon \n" + \
                  "┃🇮🇩┃ " + key + "Cek welcome\n" + \
                  "┃🇮🇩┃ " + key + "Set sider:「Text」\n" + \
                  "┃🇮🇩┃ " + key + "Set spam:「Text」\n" + \
                  "┃🇮🇩┃ " + key + "Set pesan:「Text」\n" + \
                  "┃🇮🇩┃ " + key + "Set respon:「Text」\n" + \
                  "┃🇮🇩┃ " + key + "Set welcome:「Text」\n" + \
                  "┃🇮🇩┃ " + key + "Myname:「Nama」\n" + \
                  "┃🇮🇩┃ " + key + "Bot1name:「Nama」\n" + \
                  "┃🇮🇩┃ " + key + "Bot2name:「Nama」\n" + \
                  "┃🇮🇩┃ " + key + "Bot3name:「Nama」\n" + \
                  "┃🇮🇩┃ " + key + "Bot1up「Kirim fotonya」\n" + \
                  "┃🇮🇩┃ " + key + "Bot2up「Kirim fotonya」\n" + \
                  "┃🇮🇩┃ " + key + "Bot3up「Kirim fotonya」\n" + \
                  "┃🇮🇩┃ " + key + "Gift:「Mid korban」「Jumlah」\n" + \
                  "┃🇮🇩┃ " + key + "Spam:「Mid korban」「Jumlah」\n" + \
                  "╰━━━━━━━━━━━━━━━╯\n──┅━✥ ======= ✥━┅──\n┃🇮🇩┃ ┃DPK┃ FAMS┃🇮🇩┃\n──┅━✥ ======= ✥━┅──\n╭━━━━━━━━━━━━━━━╮\n┣🇮🇩━⏩ARIFISTIFIK🇮🇩━⏩\n╰━━━━━━━━━━━━━━━╯\n"
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.updateGroup(X)
                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.updateGroup(X)
                                ki.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.updateGroup(X)
                                    kk.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.updateGroup(X)
                                        kc.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if ka.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            ka.reissueGroupTicket(op.param1)
                                            X = ka.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            ka.kickoutFromGroup(op.param1,[op.param2])
                                            ka.updateGroup(X)
                                            ka.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                ki.reissueGroupTicket(op.param1)
                                                X = ki.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                ki.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        pass
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Hai " + str(ginfo.name))

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " +str(ginfo.name))
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.sendMessage(op.param1,"Haii " + str(ginfo.name))
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"Hai " + str(ginfo.name))
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        ka.sendMessage(op.param1,"Selamat Tinggal\n Group " +str(ginfo.name))
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        ginfo = ka.getGroup(op.param1)
                        ka.sendMessage(op.param1,"Hai " + str(ginfo.name))
             

        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for _mid in gMembMids:
                            cl.cancelGroupInvitation(op.param1,[_mid])
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for _mid in gMembMids:
                                ki.cancelGroupInvitation(op.param1,[_mid])
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                    kk.cancelGroupInvitation(op.param1,[_mid])
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for _mid in gMembMids:
                                        kc.cancelGroupInvitation(op.param1,[_mid])
                                except:
                                    try:
                                        group = ka.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for _mid in gMembMids:
                                            ka.cancelGroupInvitation(op.param1,[_mid])
                                    except:
                                        pass        
                          
                           
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param1 in protectjoin:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                        	kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            ka.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendText(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
                else:
                    pass

        if op.type == 32:
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in wait["blacklist"]:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in wait["blacklist"]:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param3 not in wait["blacklist"]:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param3 not in wait["blacklist"]:
                                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                            except:        
                                                pass
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    ka.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param2])	
                                    except:
                                        print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                                    if op.param2 in wait["blacklist"]:
                                        pass
                                    try:
                                        wait["blacklist"][op.param2] = True
                                        G = ki.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.updateGroup(G)
                                        Ticket = ki.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G = ki.getGroup(op.param1)
                                        G.preventedJoinByTicket = True
                                        ki.updateGroup(G)
                                        Ticket = ki.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                            except:
                                                pass
                return

            if Amid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                ka.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param2])	
                                    except:
                                        print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                                    if op.param2 in wait["blacklist"]:
                                        pass
                                    try:
                                        wait["blacklist"][op.param2] = True 
                                        G = kk.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.updateGroup(G)
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G = kk.getGroup(op.param1)
                                        G.preventedJoinByTicket = True
                                        kk.updateGroup(G)
                                        Ticket = kk.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                            ki.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                            except:
                                                pass
                return

            if Bmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param2])	
                                    except:
                                        print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                                    if op.param2 in wait["blacklist"]:
                                        pass
                                    try:
                                        wait["blacklist"][op.param2] = True
                                        G = kc.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.updateGroup(G)
                                        Ticket = kc.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ka.acceptGroupInvitationByTicket(op.param1,Ticket) 
                                        G = kc.getGroup(op.param1)
                                        G.preventedJoinByTicket = True
                                        kc.updateGroup(G)
                                        Ticket = kc.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                            kk.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                            except:
                                                pass
                return

            if Cmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param2])	
                                    except:
                                        print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                                    if op.param2 in wait["blacklist"]:
                                        pass
                                    try:
                                        wait["blacklist"][op.param2] = True
                                        G = ka.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        ka.kickoutFromGroup(op.param1,[op.param2])
                                        ka.updateGroup(G)
                                        Ticket = ka.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G = ka.getGroup(op.param1)
                                        G.preventedJoinByTicket = True
                                        ka.updateGroup(G)
                                        Ticket = ka.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            ka.kickoutFromGroup(op.param1,[op.param2])
                                            ka.inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                            except:
                                                pass
                return
              
            if Dmid in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        ka.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            ka.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                ka.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    ka.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                                        random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                                        random.choice(KAC).cancelGroupInvitation(op.param1,[op.param2])	
                                    except:
                                        print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                                    if op.param2 in wait["blacklist"]:
                                        pass
                                    try:
                                        wait["blacklist"][op.param2] = True
                                        G = cl.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        G = cl.getGroup(op.param1)
                                        G.preventedJoinByTicket = True
                                        cl.updateGroup(G)
                                        Ticket = cl.reissueGroupTicket(op.param1)
                                    except:
                                        try:
                                            cl.kickoutFromGroup(op.param1,[op.param2])
                                            cl.inviteIntoGroup(op.param1,[op.param3])
                                            ka.acceptGroupInvitation(op.param1)
                                        except:
                                            try:
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                ki.inviteIntoGroup(op.param1,[op.param3])
                                                ka.acceptGroupInvitation(op.param1)
                                            except:
                                                pass
                return 
              
#=================#
# ADMIN DI NAKALI #
#=================#
  
        if op.type == 19:
            if op.param3 in mid:
                if op.param2 in Zmid:
                    pass
                elif op.param1 in protectghost:
                    wait["blacklist"][op.param2] = True
                    sw.acceptGroupInvitation(op.param1)
                    time.sleep(0.01)
                    sw.kickoutFromGroup(op.param1,[op.param2])
                    sw.findAndAddContactsByMid(op.param3)              
                    sw.inviteIntoGroup(op.param1,[op.param3])
                    G = sw.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    sw.updateGroup(G)
                    Ti = sw.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    sw.leaveGroup(op.param1)
                    X = cl.getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    cl.updateGroup(X)      
                    ra = cl.getGroup(op.param1)
                    midd = "u29917af2971c4b6ce9835951fabc01b2"
                    cl.inviteIntoGroup(op.param1,[midd])
                    if op.param2 in wait["blacklist"]:
                        pass                    
                    else:
                        wait["blacklist"][op.param2] = True  
                                                                                                                                   
#=====================#
#   MEMBER DI NAKALI  #
#=====================#

#[CADANGAN]#    
        if op.type == 32: #Yang Cancel Invitan langsung ke kick
            if op.param1 in protectcancel:
                if op.param2 not in Bots and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                          cl.sendText(op.param1, "Dont Play Brooooo")
                          cl.kickoutFromGroup(op.param1,[op.param2])  
                         # ki.kickoutFromGroup(op.param1,[op.param2])
                         # kk.kickoutFromGroup(op.param1,[op.param2])
                         # kc.kickoutFromGroup(op.param1,[op.param2])
                         # ka.kickoutFromGroup(op.param1,[op.param2])
                          cl.findAndAddContactsByMid(op.param3)
                         # ki.findAndAddContactsByMid(op.param3)
                         # kk.findAndAddContactsByMid(op.param3)
                         # kc.findAndAddContactsByMid(op.param3)
                         # ka.findAndAddContactsByMid(op.param3)
                          cl.inviteIntoGroup(op.param1,[op.param3])
                          #ki.inviteIntoGroup(op.param1,[op.param3])
                          #kk.inviteIntoGroup(op.param1,[op.param3])
                          #kc.inviteIntoGroup(op.param1,[op.param3])
                          #ka.inviteIntoGroup(op.param1,[op.param3])
                          ra = cl.getGroup(op.param1)
                          midd = "u29917af2971c4b6ce9835951fabc01b2"
                          cl.inviteIntoGroup(op.param1,[midd])
                          #ki.inviteIntoGroup(op.param1,[midd])
                          #kk.inviteIntoGroup(op.param1,[midd])
                          #kc.inviteIntoGroup(op.param1,[midd])
                          #ka.inviteIntoGroup(op.param1,[midd])
                          if op.param2 in wait["blacklist"]:
                              pass
                          #if op.param2 in Setmain["whitelist"]:
                              pass
                          else:
                              wait["blacklist"][op.param2] = True
                    except:
                        pass
                return        
                                  
            if admin in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                pass

                return

            if staff in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.findAndAddContactsByMid(op.param1,staff)
                        ki.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.findAndAddContactsByMid(op.param1,staff)
                            kk.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.findAndAddContactsByMid(op.param1,staff)
                                kc.inviteIntoGroup(op.param1,staff)
                            except:
                                pass

                return

      #  if op.type == 55:
      #      try:
      #          if op.param1 in Setmain["readPoint"]:
      #             if op.param2 in Setmain["readMember"][op.param1]:
      #                 pass
      #             else:
      #                 Setmain["readMember"][op.param1][op.param2] = True
      #                 now2 = datetime.now()
      #                 wait2['readPoint'][msg.to] = msg.id
      #                 wait2['readMember'][msg.to] = ""
      #                 wait2['ROM'][msg.to] = {}
      #                 wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    #print wait2                 
      #          else:
      #             pass
      #      except:
      #          pass
                                            
        if op.type == 55:
            try:
                if op.param1 in read["readPoint"]:
                   Nama = cl.getContact(op.param2).displayName
                   if Nama in read["readMember"][op.param1]:
                       pass
                   else:
                       read["readMember"][op.param1] += "\n-> " + Nama
                       read["ROM"][op.param1][op.param2] = "-> " + Nama
                       read['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                   pass
            except:
                pass
       

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(ABC).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(ABC).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"7839705","STKPKGID":"1192862","STKVER":"1"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Jangan tag saya....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\n┃🇮🇩┃ STKID : " + msg.contentMetadata["STKID"] + "\n┃🇮🇩┃ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n┃🇮🇩┃ STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"┃🇮🇩┃ Nama : " + msg.contentMetadata["displayName"] + "\n┃🇮🇩┃ MID : " + msg.contentMetadata["mid"] + "\n┃🇮🇩┃ Status Msg : " + contact.statusMessage + "\n┃🇮🇩┃ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"┃🇮🇩┃ Nama : " + msg.contentMetadata["displayName"] + "\n┃🇮🇩┃ MID : " + msg.contentMetadata["mid"] + "\n┃🇮🇩┃ Status Msg : " + contact.statusMessage + "\n┃🇮🇩┃ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#                    
#        if op.type == 65:
#            if wait["unsend"] == True:
#                try:
#                    at = op.param1
#                    msg_id = op.param2
#                    if msg_id in msg_dict:
#                        if msg_dict[msg_id]["from"]:
#                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
#                                ginfo = cl.getGroup(at)
#                                AR = cl.getContact(msg_dict[msg_id]["from"])
#                                zx = ""
#                                zxc = ""
#                                zx2 = []
#                                xpesan =  "「 Gambar Dihapus 」\n• Pengirim : "
#                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
#                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
#                                ry = str(cl.displayName)
#                                pesan = ''
#                                pesan2 = pesan+"@x \n"
#                                xlen = str(len(zxc)+len(xpesan))
#                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
#                                zx = {'S':xlen, 'E':xlen2, 'M':AR.mid}
#                                zx2.append(zx)
#                                zxc += pesan2
#                                text = xpesan + zxc + ret_ + ""
#                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
#                                cl.sendImage(at, msg_dict[msg_id]["data"])
#                           else:
#                                ginfo = cl.getGroup(at)
#                                AR = cl.getContact(msg_dict[msg_id]["from"])
#                                ret_ =  "「 Pesan Dihapus 」\n"
#                                ret_ += "• Pengirim : {}".format(str(AR.displayName))
#                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
#                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
#                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
#                                cl.sendMessage(at, str(ret_))
#                        del msg_dict[msg_id]
#                except Exception as e:
#                    print(e)

 #       if op.type == 65:
 #           if wait["unsend"] == True:
 #               try:
 #                   at = op.param1
 #                   msg_id = op.param2
 #                   if msg_id in msg_dict1:
 #                       if msg_dict1[msg_id]["from"]:
 #                               ginfo = cl.getGroup(at)
 #                               AR = cl.getContact(msg_dict1[msg_id]["from"])
 #                               ret_ =  "「 Sticker Dihapus 」\n"
 #                               ret_ += "• Pengirim : {}".format(str(AR.displayName))
 #                               ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
 #                               ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
 #                               ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
 #                               cl.sendMessage(at, str(ret_))
 #                               cl.sendImage(at, msg_dict1[msg_id]["data"])
 #                       del msg_dict1[msg_id]
 #               except Exception as e:
 #                   print(e)                                                
#ADD Bots
        if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot saints")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
        if msg.contentType == 1:
                 if msg._from in admin:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendText(msg.to, "Berhasil menambahkan gambar")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False

        if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

        if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["foto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["foto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

        if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["foto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["foto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["foto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["foto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["foto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["foto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["foto"]:
                            path = ka.downloadObjectMsg(msg_id)
                            del Setmain["foto"][Zmid]
                            ka.updateProfilePicture(path)
                            ka.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["foto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["foto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")
     

        if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = ka.downloadObjectMsg(msg_id)
                     path5 = sw.downloadObjectMsg(msg_id)
                     settings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ka.updateProfilePicture(path4)
                     ka.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     sw.updateProfilePicture(path5)
                     sw.sendMessage(msg.to, "Berhasil mengubah foto profile bot")


        if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendText(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendText(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "menubot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage1))
                              
                        if cmd == "menubot2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot2()
                               cl.sendMessage(msg.to, str(helpMessage1))                              
                        if cmd == "hpro":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = helpprotect()
                               cl.sendMessage(msg.to, str(helpMessage))                        
                        if cmd == "hps":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = helpself()
                               cl.sendMessage(msg.to, str(helpMessage))                               
                        if cmd == "hpa":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = helpadmin()
                               cl.sendMessage(msg.to, str(helpMessage))                                     
                              
                        elif cmd == "hiburan":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = helpmedia()
                               cl.sendMessage(msg.to, str(helpMessage)) 

                        elif cmd == "status":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "┃🇮🇩┃ ┃DPK┃ Protection\n\n"
                                if wait["sticker"] == True: md+="┃🇮🇩┃ Sticker「ON」\n"
                                else: md+="┃🇮🇩┃ Sticker「OFF」\n"
                                if wait["contact"] == True: md+="┃🇮🇩┃ Contact「ON」\n"
                                else: md+="┃🇮🇩┃ Contact「OFF」\n"
                                if wait["talkban"] == True: md+="┃🇮🇩┃ Talkban「ON」\n"
                                else: md+="┃🇮🇩┃ Talkban「OFF」\n"
                                if wait["Mentionkick"] == True: md+="┃🇮🇩┃ Notag「ON」\n"
                                else: md+="┃🇮🇩┃ Notag「OFF」\n"
                                if wait["detectMention"] == True: md+="┃🇮🇩┃ Respon「ON」"
                                else: md+="┃🇮🇩┃ Respon「OFF」\n"
                                if wait["autoJoin"] == True: md+="┃🇮🇩┃ Autojoin「ON」\n"
                                else: md+="┃🇮🇩┃ Autojoin「OFF」\n"
                                if wait["autoAdd"] == True: md+="┃🇮🇩┃ Autoadd「ON」\n"
                                else: md+="┃🇮🇩┃ Autoadd「OFF」\n"
                                if msg.to in welcome: md+="┃🇮🇩┃ Welcome「ON」\n"
                                else: md+="┃🇮🇩┃ Welcome「OFF」\n"
                                if wait["autoLeave"] == True: md+="┃🇮🇩┃ Autoleave「ON」\n"
                                else: md+="┃🇮🇩┃ Autoleave「OFF」\n"
                                if msg.to in protectqr: md+="┃🇮🇩┃ Protecturl「ON」\n"
                                else: md+="┃🇮🇩┃ Protecturl「OFF」\n"
                                if msg.to in protectjoin: md+="┃🇮🇩┃ Protectjoin「ON」\n"
                                else: md+="┃🇮🇩┃ Protectjoin「OFF」\n"
                                if msg.to in protectkick: md+="┃🇮🇩┃ Protectkick「ON」\n"
                                else: md+="┃🇮🇩┃ Protectkick「OFF」\n"
                                if msg.to in protectcancel: md+="┃🇮🇩┃ Protectcancel「ON」\n"
                                else: md+="┃🇮🇩┃ Protectcancel「OFF」\n"
                                if msg.to in protectghost: md+="┃🇲🇨┃ Protectghost「ON」\n"
                                else: md+="┃🇲🇨┃ Protectghost「OFF」\n"                                                      
                                cl.sendMessage(msg.to, md+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendText(msg.to,"Creator ROCKBOT") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "about" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(msg.to, sender, "「 Type Selfbot 」\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)
                              
                        elif cmd == "aim" or text.lower() == 'aim':
                            if msg._from in admin:
                               me = cl.getContact(msg._from)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               cl.sendMessage1(msg)                         
                               cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus) 
                               cover = cl.getProfileCoverURL(mid)    
                               cl.sendImageWithURL(msg.to, cover)         
                                                
                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)
                            
                        elif text.lower() == "mymid":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, msg._from)    

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "┃🇮🇩┃ Nama : "+str(mi.displayName)+"\n┃🇮🇩┃ Mid : " +key1+"\n┃🇮🇩┃ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybots":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Amid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Bmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Cmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Dmid}
                               cl.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': Zmid}
                               cl.sendMessage1(msg)

                        elif text.lower() == "hapus chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   sw.removeAllMessages(op.param2)
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   ka.removeAllMessages(op.param2)
                                   cl.sendText(msg.to,"Chat dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Silahkan gunakan seperti semula...")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif msg.text in ["cancel","Cancel"]:
                          if msg._from in admin:
                            if msg.toType == 2:
                                X = cl.getGroup(msg.to)
                                if X.invitee is not None:
                                    gInviMids = [contact.mid for contact in X.invitee]
                                    cl.cancelGroupInvitation(msg.to, gInviMids)
                                else:
                                    if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"No one is inviting")
                                    else:
                                        cl.sendText(msg.to,"Sorry, nobody absent")
                            else:
                                if wait["lang"] == "JP":
                                    cl.sendText(msg.to,"Can not be used outside the group")
                                else:
                                    cl.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)    
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "┃🇮🇩┃ ┃DPK┃ Family Grup Info\n\n┃🇮🇩┃ Nama Group : {}".format(G.name)+ "\n┃🇮🇩┃ ID Group : {}".format(G.id)+ "\n┃🇮🇩┃ Pembuat : {}".format(G.creator.displayName)+ "\n┃🇮🇩┃ Waktu Dibuat : {}".format(str(timeCreated))+ "\n┃🇮🇩┃ Jumlah Member : {}".format(str(len(G.members)))+ "\n┃🇮🇩┃ Jumlah Pending : {}".format(gPending)+ "\n┃🇮🇩┃ Group Qr : {}".format(gQr)+ "\n┃🇮🇩┃ Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "┃🇮🇩┃ ┃DPK┃ Family Grup Info\n"
                                ret_ += "\n┃🇮🇩┃ Nama Group : {}".format(G.name)
                                ret_ += "\n┃🇮🇩┃ ID Group : {}".format(G.id)
                                ret_ += "\n┃🇮🇩┃ Pembuat : {}".format(gCreator)
                                ret_ += "\n┃🇮🇩┃ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n┃🇮🇩┃ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n┃🇮🇩┃ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┃🇮🇩┃ Group Qr : {}".format(gQr)
                                ret_ += "\n┃🇮🇩┃ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "┃🇮🇩┃ "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"┃🇮🇩┃ Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    ka.leaveGroup(i)
                                    sw.leaveGroup(i)
                                   # kd.leaveGroup(i)
                                   # ke.leaveGroup(i)
                                   # kf.leaveGroup(i)
                                   # kg.leaveGroup(i)
                                   # kh.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "friendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
                              
                        elif cmd == "gruplist4":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ka.getGroupIdsJoined()
                               for i in gid:
                                   G = ka.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ka.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")
       

                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "gt2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)
                                    
                        elif msg.text in ["Cancelall"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                gid = cl.getGroupIdsInvited()
                            for i in gid:
                                cl.rejectGroupInvitation(i)
                            if wait["lang"] == "JP":
                                cl.sendText(msg.to,"All invitations have been refused")
                            else:
                                cl.sendText(msg.to,"æ‹’ç» äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")	            

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "updatefoto":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["foto"][mid] = True
                                cl.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["foto"][Amid] = True
                                ki.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["foto"][Bmid] = True
                                kk.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot3up":
                            if msg._from in admin:
                                Setmain["foto"][Cmid] = True
                                kc.sendText(msg.to,"Kirim fotonya.....")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["foto"][Dmid] = True
                                ka.sendText(msg.to,"Kirim fotonya.....")
                                                                         
                        elif cmd == "bot5up":
                            if msg._from in admin:
                                Setmain["foto"][Zmid] = True
                                sw.sendText(msg.to,"Kirim fotonya.....")

                        elif cmd.startswith("myname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ka.getProfile()
                                profile.displayName = string
                                ka.updateProfile(profile)
                                ka.sendMessage(msg.to,"Nama diganti jadi " + string + "")        

                        elif cmd.startswith("botkicker: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#===========BOT UPDATE============#
                        elif cmd == "tag" or text.lower() == '😆':
                          if wait["selfbot"] == True:
                            if msg._from  in admin:
                               group = cl.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4, nm5, nm6, nm7, nm8, nm9, nm10, jml = [], [], [], [], [], [], [], [], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 65:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                               if jml > 160 and jml < 180:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, len(nama)-1):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                               if jml > 180 and jml < 200:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, len(nama)-1):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                               if jml > 200 and jml < 220:
                                   for i in range (0, 20):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 40):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 60):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 80):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 100):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 120):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 140):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, 160):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   for q in range (160, 180):
                                       nm9 += [nama[q]]
                                   mentionMembers(msg.to, nm9)
                                   for r in range (180, 200):
                                       nm10 += [nama[r]]
                                   mentionMembers(msg.to, nm10)
                                   for s in range (200, len(nama)-1):
                                       nm11 += [nama[s]]
                                   mentionMembers(msg.to, nm11)     
 


                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃DPK┃ Family bot\n\n"+ma+"\nTotal「%s」Family Bots" %(str(len(Bots))))

                        elif cmd == "listadmin2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃DPK┃ Family admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Family Saints" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃DPK┃ Family Protection\n\n┃🇮🇩┃ PROTECT URL :\n"+ma+"\n┃🇮🇩┃ PROTECT KICK :\n"+mb+"\n┃🇮🇩┃ PROTECT JOIN :\n"+md+"\n┃🇮🇩┃ PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))
                                
                        elif cmd == "grouppicture":
                          if msg.toType == 2:
                            group = cl.getGroup(to)
                            groupPicture = "http://dl.profile.line-cdn.net/{}".format(group.pictureStatus)
                            cl.sendImageWithURL(to, groupPicture)
                        elif cmd == "groupname":
                          if msg.toType == 2:
                            group = cl.getGroup(to)
                            cl.sendMessage(to, "Nama Group : {}".format(group.name))
                        elif cmd == "groupid":
                          if msg.toType == 2:
                            group = cl.getGroup(to)
                            cl.sendMessage(to, "Group ID : {}".format(group.id))
                                                
                        elif cmd == "memberlist2":
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                num = 0
                                ret_ = "╔══[ List Member ]"
                                for contact in group.members:
                                            num += 1
                                            ret_ += "\n╠ {}. {}".format(num, contact.displayName)
                                ret_ += "\n╚══[ Total {} Members]".format(len(group.members))
                                cl.sendMessage(to, ret_)
                        elif cmd == "pendinglist2":
                            if msg.toType == 2:
                                group = cl.getGroup(to)
                                ret_ = "╔══[ Pending List ]"
                                no = 0
                            if group.invitee is None or group.invitee == []:
                               return cl.sendMessage(to, "Tidak ada pendingan di" +str(G.name))
                            else:
                                for pending in group.invitee:
                                            no += 1
                                            ret_ += "\n╠ {}. {}".format(str(no), str(pending.displayName))
                                ret_ += "\n╚══[ Total {} Pending]".format(str(len(group.invitee)))
                                cl.sendMessage(to, str(ret_))  
            
                        elif cmd.startswith("updategroupname2: "):
                          if msg.toType == 2:
                            if msg._from in admin:
                                sep = text.split(" ")
                                groupname = text.replace(sep[0] + " ","")
                            if len(groupname) <= 20:
                                group = cl.getGroup(to)
                                group.name = groupname
                                cl.updateGroup(group)
                                cl.sendMessage(to, "Berhasil mengubah nama group menjadi : {}".format(groupname))
                        
                        elif cmd == "myprofile" or text.lower() == 'myprofile':
                            if msg._from in admin:
                                contact = cl.getContact(sender)
                                cover = cl.getProfileCoverURL(sender)
                                result = "╔══[ Details Profile ]"
                                result += "\n╠ Display Name : @!"
                                result += "\n╠ Mid : {}".format(contact.mid)
                                result += "\n╠ Status Message : {}".format(contact.statusMessage)
                                result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                                result += "\n╠ Cover : {}".format(str(cover))
                                result += "\n╚══[ Finish ]"
                                cl.sendImageWithURL(to, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                cl.sendMention(to, result, [sender])    
                                  

                        elif cmd == "respon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ki.sendMessage(msg.to,responsename1)
                                kk.sendMessage(msg.to,responsename2)
                                kc.sendMessage(msg.to,responsename3)
                                ka.sendMessage(msg.to,responsename4)

                        elif cmd == "bot in":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    anggota = [Dmid,Bmid,Cmid,Amid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    ki.acceptGroupInvitation(msg.to)
                                    ka.acceptGroupInvitation(msg.to)
                                    
                                except:
                                    pass

                        elif cmd == "pin2 on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ka.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ka.updateGroup(G)
                                cl.sendMessage(msg.to, "Semua SelfBot Ready di " +str(G.name))

                        elif cmd == "pin2 off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ki.sendText(msg.to, "Bye bye fams" +str(G.name))
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                ka.leaveGroup(msg.to)
                                cl.sendMessage(msg.to, "Semua SelfBot Sudah Pulang dari " +str(G.name))
                                
                        elif cmd == "bye me":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                cl.sendText(msg.to, "Bye bye fams " +str(G.name))
                                cl.leaveGroup(msg.to)                                

                        elif cmd.startswith("leave "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "Silahkan admin invite atau masukan kembali")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        cl.sendMessage(msg.to,"Berhasil keluar dari grup " +h)

                        elif cmd == "bot1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "bot2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "bot3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)
                                
                        
                        elif cmd == "bot4":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ka.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ka.updateGroup(G)        
                                
                        elif cmd == "bot in":
                            if msg._from in owner:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = Ticket
                                ki.updateGroup(G) 
                                ki.sendMessage(msg.to," Siap di room " + str(G.name))

                        elif cmd == "kicker in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "kicker bye":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                sw.leaveGroup(msg.to)
                                
                        elif cmd == "bot bye":
                            if msg._from in owner:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                cl.sendMessage(msg.to, "Bot sudah keluar dari " +str(G.name))
                                
                        elif cmd == "stay on":
                          if msg._from in admin:    
                              midd = "u29917af2971c4b6ce9835951fabc01b2"
                              cl.inviteIntoGroup(msg.to,[midd])
                              cl.sendMessage(msg.to,"Ghost Self Stay")
                        elif cmd == "stay2 on":
                          if msg._from in admin:    
                              midd = "u29917af2971c4b6ce9835951fabc01b2"                        
                              ki.inviteIntoGroup(msg.to,[midd])
                              ki.sendMessage(msg.to, "Ghost Self Siap")
                        elif cmd == "stay3 on":
                          if msg._from in admin:    
                              midd = "u29917af2971c4b6ce9835951fabc01b2"                        
                              kk.inviteIntoGroup(msg.to,[midd])
                        elif cmd == "stay4 on":
                          if msg._from in admin:    
                              midd = "u29917af2971c4b6ce9835951fabc01b2"                        
                              kc.inviteIntoGroup(msg.to,[midd])
                        elif cmd == "stay5 on":
                          if msg._from in admin:    
                              midd = "u29917af2971c4b6ce9835951fabc01b2"                        
                              ka.inviteIntoGroup(msg.to,[midd])         

                        elif cmd == "sprespon":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "┃🇮🇩┃ ┃DPK┃ Speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "fast" or cmd == "fast":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                              
                        elif cmd == "sp":
                            	if msg._from in admin:
                            		cl.sendMessage(msg.to, "❂➣ ʟᴏᴀᴅɪɴɢ...")
                            		sp = int(round(time.time() *1000))
                            		cl.sendMessage(msg.to," %sms" % (sp - op.createdTime))
                        elif cmd == "speed":
                            	if msg._from in admin:
                            		start = time.time()
                            		cl.sendMessage(msg.to, "❂➣ ʟᴏᴀᴅɪɴɢ...")
                            		elapsed_time = time.time() - start
                            		cl.sendMessage(msg.to, " %sms" % (elapsed_time))  
                                
                        elif cmd.startswith("stealmid "):
                            	if msg._from in admin:
                            		if 'MENTION' in msg.contentMetadata.keys()!= None:
                            			names = re.findall(r'@(\w+)', text)
                            			mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            			mentionees = mention['MENTIONEES']
                            			lists = []
                            			for mention in mentionees:
                            				if mention["M"] not in lists:
                            					lists.append(mention["M"])
                            				ret_ = "[ Mid User ]"
                            				for ls in lists:
                            					ret_ += "\n{}".format(str(ls))
                            				cl.sendMessage(msg.to, str(ret_))
                        elif cmd.startswith("stealname "):
                            	if msg._from in admin:
                            		if 'MENTION' in msg.contentMetadata.keys()!= None:
                            			names = re.findall(r'@(\w+)', text)
                            			mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            			mentionees = mention['MENTIONEES']
                            			lists = []
                            			for mention in mentionees:
                            				if mention["M"] not in lists:
                            					lists.append(mention["M"])
                            				ret_ = "[ Mid User ]"
                            				for ls in lists:
                            					contact = cl.getContact(ls)
                            					cl.sendMessage(msg.to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                        elif cmd.startswith("stealbio "):
                            	if msg._from in admin:
                            		if 'MENTION' in msg.contentMetadata.keys()!= None:
                            			names = re.findall(r'@(\w+)', text)
                            			mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            			mentionees = mention['MENTIONEES']
                            			lists = []
                            			for mention in mentionees:
                            				if mention["M"] not in lists:
                            					lists.append(mention["M"])
                            				for ls in lists:
                            					contact = cl.getContact(ls)
                            					cl.sendMessage(msg.to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(str(contact.statusMessage)))
                            	if msg._from in admin:
                            		if 'MENTION' in msg.contentMetadata.keys()!= None:
                            			names = re.findall(r'@(\w+)', text)
                            			mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            			mentionees = mention['MENTIONEES']
                            			lists = []
                            			for mention in mentionees:
                            				if mention["M"] not in lists:
                            					lists.append(mention["M"])
                            				for ls in lists:
                            					contact = cl.getContact(ls)
                            					path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                            					cl.sendImageWithURL(to, str(path))
                        elif cmd.startswith("stealvideoprofile "):
                            	if msg._from in admin:
                            		if 'MENTION' in msg.contentMetadata.keys()!= None:
                            			names = re.findall(r'@(\w+)', text)
                            			mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            			mentionees = mention['MENTIONEES']
                            			lists = []
                            			for mention in mentionees:
                            				if mention["M"] not in lists:
                            					lists.append(mention["M"])
                            				for ls in lists:
                            					contact = cl.getContact(ls)
                            					path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                            					cl.sendVideoWithURL(to, str(path))
                        elif cmd.startswith("stealcover "):
                            	if msg._from in admin:
                            		if cl != None:
                            			if 'MENTION' in msg.contentMetadata.keys()!= None:
                            				names = re.findall(r'@(\w+)', text)
                            				mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            				mentionees = mention['MENTIONEES']
                            				lists = []
                            				for mention in mentionees:
                            					if mention["M"] not in lists:
                            						lists.append(mention["M"])
                            					for ls in lists:
                            						channel = cl.getProfileCoverURL(ls)
                            						path = str(channel)
                            						cl.sendImageWithURL(to, str(path))  
                        elif cmd.startswith("stealpp "):
                              if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                  names = re.findall(r'@(\w+)', text)
                                  mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                  mentionees = mention['MENTIONEES']
                                  lists = []
                                  for mention in mentionees:
                                    if mention["M"] not in lists:
                                      lists.append(mention["M"])
                                    for ls in lists:
                                      path = "http://dl.profile.line.naver.jp/" + cl.getContact(ls).pictureStatus
                                      cl.sendImageWithURL(msg.to, str(path))    
                                      
                        elif msg.text == "Cctv":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                cl.sendText(msg.to, "Cek CCTV")
                                try:
                                    del read['readPoint'][msg.to]
                                    del read['readMember'][msg.to]
                                except:
                                    pass
                                now2 = datetime.now()
                                read['readPoint'][msg.to] = msg.id
                                read['readMember'][msg.to] = ""
                                read['ROM'][msg.to] = {}
                                read['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                                print (read)
                             

                        elif msg.text == "Ciduk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.to in read['readPoint']:
                                if read["ROM"][msg.to].items() == []:
                                    chiya = ""
                                else:
                                    chiya = ""
                                    for rom in read["ROM"][msg.to].items():
                                        print (rom)
                                        chiya += rom[1] + "\n"

                                cl.sendText(msg.to, "╔═══════════���═══%s\n╠════════════════\n%s╠═══════════════\n║☯Yang CCTV☯\n╠═══════════════\n║☯BINTITAN☯\n║☯BISULAN☯\n║☯PANUAN☯\n║☯KURAPAN☯\n╠═══════════════\n║☯Amiin Ya Allah☯\n╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (read['readMember'][msg.to],chiya,setTime[msg.to]))
                            else:
                                cl.sendText(msg.to, "☯���☯☯☯☯☯☯☯☯☯\n☯Ketik [Cctv] Dulu Dudul☯\n☯☯☯☯☯☯☯☯☯☯☯"  )
                                
                        elif msg.text == "Shows offenders:on":
                          if msg._from in admin:
                            if wait["pelaku"] == True:
                                if wait["lang"] == "JP":
                                    cl.sendText(msg.to,"already activated")
                                else:
                                    cl.sendText(msg.to,"enable ")
                            else:
                                wait["pelaku"] = True
                                if wait["lang"] == "JP":
                                    cl.sendText(msg.to,"already activated")
                                else:
                                    cl.sendText(msg.to,"enable ")
                        elif msg.text == "Shows offenders:off":
                          if msg._from in admin:
                            if wait["pelaku"] == False:
                               if wait["lang"] == "JP":
                                  cl.sendText(msg.to,"already unactivated")
                               else:
                                  cl.sendText(msg.to,"disable ")
                            else:
                                wait["pelaku"] = False
                                if wait["lang"] == "JP":
                                   cl.sendText(msg.to,"already unactivated")
                                else:
                                   cl.sendText(msg.to,"disable")
         
                        elif "Gcancel:" in msg.text:
                          if msg._from in admin:
                            try:
                                strnum = msg.text.replace("Gcancel:","")
                                if strnum == "off":
                                    wait["autoCancel"]["on"] = False
                                    if wait["lang"] == "JP":
                                        cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                                    else:
                                        cl.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                                else:
                                    num =  int(strnum)
                                    wait["autoCancel"]["on"] = True
                                    if wait["lang"] == "JP":
                                        cl.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                                    else:
                                        cl.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                            except:
                                if wait["lang"] == "JP":
                                    cl.sendText(msg.to,"Value is wrong")
                                else:
                                    cl.sendText(msg.to,"Bizarre ratings")
                                    
                        elif msg.text in ["Like:friend", "Bot like temen"]:
                                print ("[Command]Like executed")
                                cl.sendText(msg.to,"pertamax")
                                try:
                                    likefriend()
                                except:
                                    pass
                             
                        elif "Cek zodiak " in msg.text:
                                tanggal = msg.text.replace("Cek zodiak ","")
                                r=requests.get('https://script.google.com/ macros/exec?service=AKfycbw7gKzP-WYV 2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                lahir = data["data"]["lahir"]
                                usia = data["data"]["usia"]
                                ultah = data["data"]["ultah"]
                                zodiak = data["data"]["zodiak"]
                                cl.sendText(msg.to,"Tanggal Lahir: "+lahir+"\n\nUsia:"+usia+"\n\nUltah: "+ultah+"\n\nZodiak: "+zodiak)
                   
                                                                                                               
#=======================7===================
                        elif "kedapkedip " in msg.text.lower():
                          if msg._from in admin:
                              txt = msg.text.replace("kedapkedip ", "")
                              t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                              t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                              cl.sendText(msg.to, t1 + txt + t2)
#-------Cek sider biar mirip kek siri-----------------------------
                        elif "Setlastpoint" in msg.text:
                          if msg._from in admin:
                              subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                             #cl.sendText(msg.to, "Checkpoint checked!")
                              cl.sendText(msg.to, "Set the lastseens' point(｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                              print ("Setlastpoint")
#--------------------------------------------
                        elif "Viewlastseen" in msg.text:
                          if msg._from in admin:
	                            lurkGroup = ""
	                            dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                           #   with open('dataSeen/'+msg.to+'.txt','r') as rr == True:
                                #  contactArr = rr.readlines()
                                #  for v in xrange(len(contactArr) -1,0,-1):
                                #      num = re.sub(r'\n', "", contactArr[v])
                                #      contacts.append(num)
                                #      pass
                                #  contacts = list(set(contacts))
                                #  for z in range(len(contacts)):
                                #      arg = contacts[z].split('|')
                                #      userList.append(arg[0])
                                #      timelist.append(arg[1])
                               #   uL = list(set(userList))
                               #   for ll in range(len(uL)):
                               #       try:
                              #            getIndexUser = userList.index(uL[ll])
                              #            timeSeen.append(time.strftime("%d日 %H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                              #            recheckData.append(userList[getIndexUser])
                              #        except IndexError:
                               #           conName.append('nones')
                              #            pass
                                #  contactId = cl.getContacts(recheckData)
                                #  for v in range(len(recheckData)):
                                #      dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                                #      pass
                                #  if len(dataResult) > 0:
                                #      grp = '\n• '.join(str(f) for f in dataResult)
                                #      total = '\nThese %iuesrs have seen at the lastseen\npoint(｀・ω・´)\n\n%s' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                                #      cl.sendText(msg.to, "• %s %s" % (grp, total))
                                #  else:
                                #      cl.sendText(msg.to, "Sider ga bisa di read cek setpoint dulu bego tinggal ketik\nSetlastpoint\nkalo mau liat sider ketik\nViewlastseen")
                                #  print ("Viewlastseen")
#=============================,=============       
                                

                        elif "InviteMeTo: " in msg.text:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                gid = msg.text.replace("InviteMeTo: ","")
                                if gid == "":
                                    cl.sendText(msg.to,"Invalid group id")
                                else: 
                                    try:
                                        ki.findAndAddContactsByMid(msg.from_)
                                        ki.inviteIntoGroup(gid,[msg.from_])
                                    except:
                                        ki.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu") 
                                        
                        elif "Invite me" in msg.text:
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.findAndAddContactsByMid(msg.from_)
                                    cl.inviteIntoGroup(i,[msg.from_])
                                    cl.sendText(msg.to, "successfully invited you to all groups")            
                                
                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['readPoint'][msg.to] = msg_id
                                 Setmain['readMember'][msg.to] = {}
                                 cl.sendText(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['readPoint'][msg.to]
                                 del Setmain['readMember'][msg.to]
                                 cl.sendText(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['readPoint']:
                                if Setmain['readMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['readMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['readPoint'][msg.to]
                                        del Setmain['readMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['readPoint'][msg.to] = msg.id
                                    Setmain['readMember'][msg.to] = {}
                                else:
                                    cl.sendText(msg.to, "User kosong...")
                            else:
                                cl.sendText(msg.to, "Ketik lurking on dulu")

                        elif cmd == "intai on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "intai off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  cl.sendMessage(msg.to, "Sudak tidak aktif")
                                  
                        elif text.lower() == '?kickall':
                          if msg._from in owner:
                            if msg.toType == 2:
                                print ("[ 19 ] KICK ALL MEMBER")
                                _name = msg.text.replace("?kickall","")
                                gs = cl.getGroup(msg.to)
                                gs = ki.getGroup(msg.to)
                                gs = kk.getGroup(msg.to)
                                gs = kc.getGroup(msg.to) 
                                gs = ka.getGroup(msg.to)
                            cl.sendMessage(msg.to,"「 Bye All 」")
                            cl.sendMessage(msg.to,"「 Sory guys 」")
                            targets = []
                            for g in gs.members:
                                    if _name in g.displayName:
                                        targets.append(g.mid)
                                    if targets == []:
                                         cl.sendMessage(msg.to,"Not Found")
                            else:
                                    for target in targets:
                                       if target not in Bots:
                                         if target not in owner:
                                           if target not in admin:
                                                try:
                                                    klist=[cl,ki,kk,kc,ka]
                                                    kicker=random.choice(klist)
                                                    kicker.kickoutFromGroup(msg.to,[target])
                                                    print (msg.to,[g.mid])
                                                except:
                                                    cl.sendMessage(msg.to,"")            
                                  

#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n┃🇮🇩┃ Lokasi : " + data[0]
                                         ret_ += "\n┃🇮🇩┃ " + data[1]
                                         ret_ += "\n┃🇮🇩┃ " + data[2]
                                         ret_ += "\n┃🇮🇩┃ " + data[3]
                                         ret_ += "\n┃🇮🇩┃ " + data[4]
                                         ret_ += "\n┃🇮🇩┃ " + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n┃🇮🇩┃ Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n┃🇮🇩┃ Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n┃🇮🇩┃ Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n┃🇮🇩┃ Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n┃🇮🇩┃ Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n┃🇮🇩┃ Location : " + data[0]
                                    ret_ += "\n┃🇮🇩┃ Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendText(msg.to, str(ret_))
                                   except:
                                       cl.sendText(to, "Lirik tidak ditemukan")
                            
                        elif cmd.startswith("music: "):
                           if msg._from in admin:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══[ Music ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Waiting Audio ]"
                                      cl.sendText(msg.to, str(ret_))
                                      cl.sendText(msg.to, "Mohon bersabar musicnya lagi di upload")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendText(to, "Musik tidak ditemukan")

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendText(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n┃🇮🇩┃ Author : ' + str(vid.author)
                                    durasi = '\n┃🇮🇩┃ Duration : ' + str(vid.duration)
                                    suka = '\n┃🇮🇩┃ Likes : ' + str(vid.likes)
                                    rating = '\n┃🇮🇩┃ Rating : ' + str(vid.rating)
                                    deskripsi = '\n┃🇮🇩┃ Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("ytmp3: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n┃🇮🇩┃ Author : ' + str(vid.author)
                                    durasi = '\n┃🇮🇩┃ Duration : ' + str(vid.duration)
                                    suka = '\n┃🇮🇩┃ Likes : ' + str(vid.likes)
                                    rating = '\n┃🇮🇩┃ Rating : ' + str(vid.rating)
                                    deskripsi = '\n┃🇮🇩┃ Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendText(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))
                                
                        elif cmd.startswith("mp3 "):
                          if msg._from in admin:    
                            try:
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split(":")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "━━━━[ List Lagu ]━━━━"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n  ━━[ Total {} Lagu ]━━".format(str(len(data["result"])))
                                    ret_ += "\n\nUntuk Melihat Details Musik, Silahkan Ketik \n❧「 {}mp3 {}:nomor 」 ".format(str(),str(search))
                                    ret_ += "\n❧「 {}Lirik {}:nomor 」 ".format(str(),str(search))
                                    cl.sendMessage(msg.to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "┏━━━━[ Detail Musik ]━━━━"
                                            ret_ += "\n┃┃ Title : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n┃┃ Album : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n┃┃ Size : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n┗━━[ Tunggu Audionya ]━━━"
                                            cl.sendMessage(msg.to, str(ret_))
                                            cl.sendAudioWithURL(msg.to, str(data["result"]["mp3"][0]))
                            except Exception as error:
                                pass 
                        
                        elif 'playstore ' in msg.text.lower():
                              tob = msg.text.lower().replace('playstore ',"")
                              cl.sendText(msg.to,"Please wait...")
                              cl.sendText(msg.to,"Title : "+tob+"\nSource : Google Play\nLinknya : https://play.google.com/store/search?q=" + tob)
                              cl.sendText(msg.to,"This is link aplication")              
                         
                        elif "Wikipedia " in msg.text:
                          try:
                              wiki = msg.text.lower().replace("Wikipedia ","")
                              wikipedia.set_lang("id")
                              pesan="Title ("
                              pesan+=wikipedia.page(wiki).title
                              pesan+=")\n\n"
                              pesan+=wikipedia.summary(wiki, sentences=1)
                              pesan+="\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except:
                                  try:
                                      pesan="Over Text Limit! Please Click link\n"
                                      pesan+=wikipedia.page(wiki).url
                                      cl.sendText(msg.to, pesan)
                                  except Exception as e:
                                      cl.sendText(msg.to, str(e))  
                          
                        elif cmd.startswith("smule: "):
                          if msg._from in admin:    
                            try:
                                separate = msg.text.split(" ")
                                smule = msg.text.replace(separate[0] + " ","")
                                links = ("https://smule.com/"+smule)
                                ss = ("http://api2.ntcorp.us/screenshot/shot?url={}".format(urllib.parse.quote(links)))
                                put.sendMessage(msg.to, "Sedang Mencari...")
                                time.sleep(2)
                                cl.sendMessage(msg.to, "ID Smule : "+smule+"\nLink : "+links)
                                cl.sendImageWithURL(msg.to, ss)
                            except Exception as error:
                                pass                                
                            	   
                 
                        elif cmd.startswith("image: "):
                          if msg._from in admin:
                           separate = msg.text.split(" ")
                           search = msg.text.replace(separate[0] + " ","")
                           with requests.session() as web:
                             web.headers["User-Agent"] = random.choice(settings["userAgent"])
                             r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                             data = r.text
                             data = json.loads(data)
                             if data["result"] != []:
                                items = data["result"]
                                path = random.choice(items)
                                a = items.index(path)
                                b = len(items)
                                cl.sendImageWithURL(to, str(path)) 
                                
                        elif cmd.startswith("ytb "):
                          if msg._from in admin:
                                sep = text.split(" ")
                                txt = msg.text.replace(sep[0] + " ","")
                                cond = txt.split("|")
                                search = cond[0]
                                url = requests.get("http://api.w3hills.com/youtube/search?keyword={}&api_key=86A7FCF3-6CAF-DEB9-E214-B74BDB835B5B".format(search))
                                data = url.json()
                                if len(cond) == 1:
                                        no = 0
                                        result = "╔══[ Youtube Search ]"
                                        for anu in data["videos"]:
                                                no += 1
                                                result += "\n╠ {}. {}".format(str(no),str(anu["title"]))
                                        result += "\n╚══[ Total {} Result ]".format(str(len(data["videos"])))
                                        cl.sendMessage(to, result)
                                elif len(cond) == 2:
                                        num = int(str(cond[1]))
                                        if num <= len(data):
                                                search = data["videos"][num - 1]
                                                ret_ = "╔══[ Youtube Info ]"
                                                ret_ += "\n╠ Channel : {}".format(str(search["publish"]["owner"]))
                                                ret_ += "\n╠ Title : {}".format(str(search["title"]))
                                                ret_ += "\n╠ Release : {}".format(str(search["publish"]["date"]))
                                                ret_ += "\n╠ Viewers : {}".format(str(search["stats"]["views"]))
                                                ret_ += "\n╠ Likes : {}".format(str(search["stats"]["likes"]))
                                                ret_ += "\n╠ Dislikes : {}".format(str(search["stats"]["dislikes"]))
                                                ret_ += "\n╠ Rating : {}".format(str(search["stats"]["rating"]))
                                                ret_ += "\n╠ Description : {}".format(str(search["description"]))
                                                ret_ += "\n╚══[ {} ]".format(str(search["webpage"]))
                                                cl.sendImageWithURL(to, str(search["thumbnail"]))
                                                cl.sendMessage(to, str(ret_))                                                

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "┃🇮🇩┃ Link : " + "https://www.instagram.com/" + instagram
                                text = "┃🇮🇩┃ Name : "+namaIG+"\n┃🇮🇩┃ Username : "+usernameIG+"\n┃🇮🇩┃ Biography : "+bioIG+"\n┃🇮🇩┃ Follower : "+followerIG+"\n┃🇮🇩┃ Following : "+followIG+"\n┃🇮🇩┃ Post : "+mediaIG+"\n┃🇮🇩┃ Verified : "+verifIG+"\n┃🇮🇩┃ Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"┃🇮🇩┃ I N F O R M A S I ┃🇮🇩┃\n\n"+"┃🇮🇩┃ Date Of Birth : "+lahir+"\n┃🇮🇩┃ Age : "+usia+"\n┃🇮🇩┃ Ultah : "+ultah+"\n┃🇮🇩┃ Zodiak : "+zodiak)
                            
                        elif cmd.startswith("date: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91ARs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"🐚 I N F O R M A S I 🐚\n\n"+"🐚 Date Of Birth : "+lahir+"\n🐚 Age : "+usia+"\n🐚 Ultah : "+ultah+"\n🐚 Zodiak : "+zodiak)    

                        elif cmd.startswith("jumlah: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["limit"] = num
                                cl.sendText(msg.to,"Total Spamtag Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendText(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["limit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        call.acquireGroupCallRoute(to)
                                        call.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendText(msg.to,str(e))
                                else:
                                    cl.sendText(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ka.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9) 

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["message1"]))
                                      ki.sendMessage(midd, str(Setmain["message1"]))
                                      kk.sendMessage(midd, str(Setmain["message1"]))
                                      kc.sendMessage(midd, str(Setmain["message1"]))
                                      ka.sendMessage(midd, str(Setmain["message1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcomeself ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcomeself ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome Msg sudah aktif"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome Msg diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome Msg dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome Msg sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)
                                    
                        elif 'Jsself ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Jsself ','')
                              if spl == 'on':
                                  if msg.to in protectghost:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect ghost diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectghost:
                                         protectghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect ghost dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect ghost sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)             

                        elif 'Protecturl ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protecturl ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url sudah aktif"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectkick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectkick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick sudah aktif"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectjoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectjoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join sudah aktif"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Protectcancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Protectcancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel sudah aktif"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel diaktifkan\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel dinonaktifkan\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel sudah tidak aktif"
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

                        elif 'Allproself ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allproself ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectghost:
                                      msgs = ""
                                  else:
                                      protectghost.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Diaktifkan」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectghost:
                                         protectghost.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「Dinonaktifkan」\n" + msgs)

#===========KICKOUT============#
                        elif ("Nk " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           sw.kickoutFromGroup(msg.to, [target])
                                           sw.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                          # cl.updateGroup(X)
                                          # ra = cl.getGroup(msg.to)
                                           midd = "u4b33cd1bef166da43ac924a0ba556f1d"
                                           cl.inviteIntoGroup(op.param1,[midd])
                                           cl.updateGroup(X)
                                       except:
                                           pass

                        elif ("Kick1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           random.choice(ABC).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

#===========ADMIN ADD============#
                        elif ("Adminselfadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffselfadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botselfadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Adminselfdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffselfdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botselfdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendText(msg.to,"Berhasil di Refresh...")

                        elif cmd == "contact admin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact staff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "contact bot" or text.lower() == 'contact bot':
                            if msg._from in admin:
                                ma = ""
                                for i in Bots:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendText(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendText(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendText(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendText(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendText(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendText(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendText(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendText(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendText(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendText(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendText(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendText(msg.to,"Auto add dinonaktifkan")
                                
                        if cmd == "unsendself on":
                            if msg._from in admin:
                                wait["unsend"] = True
                                cl.sendMessage(msg.to, "Deteksi Unsend Diaktifkan")
                                
                        if cmd == "unsendself off":
                            if msg._from in admin:
                                wait["unsend"] = False
                                cl.sendMessage(msg.to, "Deteksi Unsend Dinonaktifkan")  
                                         

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendText(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendText(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "gtself on" or text.lower() == 'gtself on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendText(msg.to,"Join ticket diaktifkan")

                        elif cmd == "gtself off" or text.lower() == 'gtself off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendText(msg.to,"Notag dinonaktifkan")
                                
                        elif msg.text in ["Auto like:on"]:
                          if msg._from in admin:
                            if wait["likeOn"] == True:
                                if wait["lang"] == "JP":
                                    cl.sendText(msg.to,"Done。")
                            else:
                                wait["likeOn"] = True
                                if wait["lang"] == "JP":
                                    cl.sendText(msg.to,"Already。")
                        elif msg.text in ["Auto like:off"]:
                          if msg._from in admin:
                            if wait["likeOn"] == False:
                                if wait["lang"] == "JP":
                                    cl.sendText(msg.to,"Done。")
                            else:
                                wait["likeOn"] = False
                                if wait["lang"] == "JP":
                                    cl.sendText(msg.to,"Already。")        
                                

#===========COMMAND BLACKLIST============#

                        elif msg.text in ["Reject"]:
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               gid = cl.getGroupIdsInvited()
                               for i in gid:
                                   cl.rejectGroupInvitation(i)
                               if wait["lang"] == "JP":
                                   cl.sendText(msg.to,"Semua Spam Undangan Telah Di Tolak")
                               else:
                                   cl.sendText(msg.to,"拒绝了全部的邀请。")
                     
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendText(msg.to,"Kirim kontaknya...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃DPK┃ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"┃🇮🇩┃ ┃DPK┃ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses membersihkan " +mc)
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["message1"] = spl
                                  cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group4 = ka.findGroupByTicket(ticket_id)
                                     ka.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     ka.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                      
                                                                                                                      
    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
