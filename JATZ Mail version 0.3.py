import smtplib, turtle, webbrowser, random, time
from tkinter import *

loaduprandom = random.randrange(0, 100)
defaultColor = 'lightblue'
developerPassword = 'iamdev'
adsendpass = 'LI.5K_R<\\C9648*8'
accPass = 'wushman123!123'

def sentAni():
    john = turtle.Turtle()
    john.hideturtle()
    john.penup()
    john.speed(0)
    john.left(120)
    john.forward(120)
    john.left(90)
    john.color("red")
    john.pendown()
    john.circle(140)
    for i in range(30):
        john.left(10)
        john.circle(140)
    john.penup()
    john.color("green")
    style1 = ("Times", 40, "bold")
    john.write("Email Sent!", font=style1, align='center')

def sendoutads():
    verAP1 = input('Enter ad verification password: ')
    if verAP1 == adsendpass:
        Wdev = int(input('Which developer are you? 1 = A.Z\t2 = J.T \t3 = L.S: '))
        if Wdev == 1:
            dtsvct = 'aidan.zeleniy@gmail.com'
        elif Wdev == 2:
            dtsvct = 'jonathantetry2309@gmail.com'
        elif Wdev == 3:
            dtsvct = '123lukeshostak@gmail.com'
        VvCc = str(random.randint(10000000000, 99999999999))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('eggowafflesarebadlmao123@gmail.com', accPass)
        server.sendmail('eggowafflesarebadlmao123@gmail.com', dtsvct, VvCc)
        print('An Email with a verification code was sent to that developer')
        VCAI = int(input('Verification Code: '))
        if VCAI == int(VvCc):
            ad_fileINP = input('What email file do you want to use. Include .txt at the end: ')
            ad_file = open(ad_fileINP, 'r')
            for email__ in ad_file:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login('jatzmailofficial@gmail.com', '8JATZ39#')
                server.sendmail('eggowafflesarebadlmao123@gmail.com', email__, 'GET JATZMAIL NOW!! FOR FREE\n\nOUR WEBPAGE: https://sites.google.com/view/jatzmail/home\nOUR GITHUB REPOSITORY: https://github.com/Manbush/JATZ-Mail')
            print('Complete!')
        else:
            print('Invalid Verification Code')
    else:
        print('Invalid Ad Verification Password')
def devSec():
    def rememberPassword():
        global passwordRemembered
        passwordRemembered = passR.get()
    if devPassword.get() == developerPassword:
        root.geometry('800x400')
        devF = Frame(root, background='#bfebff').place(x=0, y=250, width=800, height=200)
        devCB = Button(devF, text='Close Dev Section', command=lambda:root.geometry('800x250')).place(x=5, y=283, width=200, height=24)
        #passR = StringVar()
        #passRem = Entry(devF, textvariable=passR).place(x=210, y=255, width=200, height=24)
        #passRemL = Label(devF, text='Enter password to remember (this session only)', bg='#bfebff').place(x=415, y=255)
        #SPB = Button(devF, text='Save Password', command=rememberPassword).place(x=5, y=255, width=200, height=24)
    elif devPassword.get() == 'iamadmin':
        root.geometry('800x400')
        adF = Frame(root, background='#ff4d4d').place(x=0, y=250, width=800, height=200)
        adCB = Button(adF, text='Close Admin Section', command=lambda:root.geometry('800x250')).place(x=5, y=254, width=200, height=24)
        adB = Button(adF, text='Send Ads', command=sendoutads).place(x=5, y=283, width=200, height=24)
    else:
        print('Invalid Developer password')
def sendOut():
    start_time = time.time()
    sender_email = emailFrom.get() #Person to send email from
    rec_email = email_sendTo.get() #Person to recieve the email
    # rec_email = "TO: "+rec_email
    if rec_email== "me":
        rec_email = sender_email
    elif rec_email == 'dev1':
        rec_email = 'jonathantetry2309@gmail.com'
    elif rec_email == 'dev2':
        rec_email = 'aidan.zeleniy@gmail.com'
    elif rec_email == '30439039033':
        root.geometry('1000x250')
        rec_email = sender_email
        lolF = Frame(root, background='pink').place(x=800, y=0, width=200, height=250)
        lolL = Label(lolF, text='LOL', font=('Times', 36), bg='pink').place(x=805, y=5)
        closeLOL = Button(lolF, text='Close this junk', command=lambda:root.geometry('800x250')).place(x=805, y=200)
    rec_email = rec_email.split()
    if passwordRemembered != '':
        password = Account_Password.get()
    else:
        password = Account_Password.get()
    message = mess_Send.get() #Message to send
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password) #Does login
    print('Logged Into Server 1/2')
    server.sendmail(sender_email, rec_email, message) #Sends Email
    end_time = time.time()
    print('Message Sent 2/2')
    print('Message Sent Success!')
    print('That took '+str(end_time-start_time)+' seconds')
    sentAni()    
def sim2020():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=PKtnafFtfEo')
def ratejatzmail():
    ratingnum = int(input('RATE OUR EMAIL PROVIDER OUT OF 10. 1 BEING THE WORST AND 10 BEING AWESOME: '))
    rec_email_rate = 'jonathantetry2309@gmail.com'
    yornfeedbackrate = input('TYPE "YES" IF YOU WANT TO SEND FEEDBACK TYPE "NO" TO CONTINUE WITHOUT FEEDBACK: ').upper()
    nameforrate = input('ENTER YOUR NAME OR ENTER "IPNTS" IF YOU WISH TO STAY ANONYMOUS: ').upper()
    if yornfeedbackrate == 'NO':
        if nameforrate != 'IPNTS':
            mess_send_rate = str(ratingnum) + ' WAS THE RATING GIVEN TO JATZ MAIL BY ' + nameforrate
        else:
            mess_send_rate = str(ratingnum) + ' WAS THE RATING GIVEN TO JATZ MAIL'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('eggowafflesarebadlmao123@gmail.com', accPass)
        server.sendmail('eggowafflesarebadlmao123@gmail.com', rec_email_rate, mess_send_rate)
    else:
        feedbackforjatzmailrate = input('WRITE YOUR FEEDBACK MESSAGE TO IMPROVE JATZMAIL: ')
        if nameforrate != 'IPNTS': 
            mess_send_rate = str(ratingnum) + ' WAS THE RATING GIVEN TO JATZ MAIL BY ' + nameforrate + '\nFEEDBACK:\n' + feedbackforjatzmailrate
        else:
            mess_send_rate = str(ratingnum) + ' WAS THE RATING GIVEN TO JATZ MAIL' + '\nFEEDBACK:\n' + feedbackforjatzmailrate
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('eggowafflesarebadlmao123@gmail.com', accPass)
        server.sendmail('eggowafflesarebadlmao123@gmail.com', rec_email_rate, mess_send_rate)
def opensettingswindow():
    def apply1():
        global defaultColor
        defaultColor = settingsbgcolor.get()
    
    setwin = Tk()
    setwin.title('JATZ MAIL SETTINGS')
    setwin.geometry('400x300')
    setwin.resizable(width=False, height=False)

    setf = Frame(setwin, background='#81dbc9').place(x=0, y=0, width=400, height=300)
    settingsbgcolor = StringVar()
    mwbc = Entry(setwin, textvariable=settingsbgcolor).place(x=5, y=5, width=95, height=24)
    mwbcL = Label(setwin, text='Choose background color', bg='#81dbc9', font=('Times', 11)).place(x=105, y=5)
    apply1 = Button(setwin, text='Apply', command=apply1).place(x=300, y=5, width=95, height=24)
    
    setwin.mainloop()
     
root = Tk()
root.title('JATZ MAIL VESRION 0.3')
jatzmailiconwindow = PhotoImage(file='JATZMAILICON.png')
root.iconphoto(False, jatzmailiconwindow)
root.geometry('800x250')
root.resizable(width=False, height=False)
if loaduprandom != 23:
    bgFrame = Frame(root, background=defaultColor).place(x=0, y=0, width=500, height=250)
elif loaduprandom == 23:
    bgFrame = Frame(root, background='red').place(x=0, y=0, width=500, height=250)
    
bgFrame2 = Frame(root, background='#6fd6e3').place(x=500, y=0, width=300, height=250)

enterMessL = Label(bgFrame, text='Enter Message that you want to send', bg=defaultColor, font=('Times', 11)).place(x=210, y=34)
recEmailL = Label(bgFrame, text="Enter reciever's email", bg=defaultColor, font=('Times', 11)).place(x=210, y=63)
passAccL = Label(bgFrame, text="Enter password to sender's account", bg=defaultColor, font=('Times', 11)).place(x=210, y=92)
fromEmailL = Label(bgFrame, text='Enter email you want to send from', bg=defaultColor, font=('Times', 11)).place(x=210, y=121)
info = Label(bgFrame, text='Discliamer: None of the emails will have subjects.\ndue to Google privacy settings.\nDO NOT PRESS THE SEND BUTTON WITHOUT TYPING THE RECIEVER EMAIL', bg=defaultColor, font=('Arial', 8), relief='solid').place(x=5, y=180)
hotkey = Label(bgFrame2, text='Special', bg='#6fd6e3', font=('Helvetica', 24)).place(x=590, y=5)
hk1L = Label(bgFrame2, text='"dev1" --> developor 1', font=('Times', 11), bg='#6fd6e3').place(x=505, y=50)
hk2L = Label(bgFrame2, text='"dev2" --> developor 2', font=('Times', 11), bg='#6fd6e3').place(x=505, y=71)
hk3L = Label(bgFrame2, text='"me" ---> wushman', font=('Times', 11), bg='#6fd6e3').place(x=505, y=92)
hk4l = Label(bgFrame2, text='To send a message to multiple emails adresses \nadd a space between each address', font=('Times', 11), bg='#6fd6e3', justify='left').place(x=505, y=123)
info2 = Label(bgFrame2, text='All shortcuts must be typed\nin lowercase font and\nwithout quotes.', bg='#6fd6e3', font=('Arial', 12), relief='solid').place(x=550, y=170)
devL = Label(bgFrame, text='Password', bg=defaultColor, font=('Times', 11)).place(x=410, y=5)


sendButton = Button(bgFrame, text='Send Emails', command=sendOut).place(x=5, y=5, width=95, height=24)
devpButton = Button(bgFrame, text='Dev Section', command=devSec).place(x=105, y=5, width=95, height=24)
sim2020Button = Button(bgFrame, text='2020 Simulation', command=sim2020).place(x=5, y=151, width=95, height=24)
feedbackButton = Button(bgFrame, text='Rate JATZ Mail', command=ratejatzmail).place(x=105, y=151, width=95, height=24)
#opensettingsbutton = Button(bgFrame, text='Settings', command=opensettingswindow).place(x=205, y=151, width=95, height=24)
terminatejatzbuttonMS = Button(bgFrame, text='×', bg='#db1812',font=('Times', 14), command=lambda:root.destroy()).place(x=775, y=5, height=20, width=20)

mess_Send = StringVar() 
enterMess = Entry(bgFrame, textvariable=mess_Send).place(x=5, y=34, width=200, height=24)
email_sendTo = StringVar()
enterReciever = Entry(bgFrame, textvariable=email_sendTo).place(x=5, y=63, width=200, height=24)
Account_Password = StringVar()
enterPass = Entry(bgFrame, textvariable=Account_Password).place(x=5, y=92, width=200, height=24)
devPassword = StringVar()
passDev = Entry(bgFrame, textvariable=devPassword).place(x=205, y=5, width=200, height=24)
emailFrom = StringVar()
fromEmail = Entry(bgFrame, textvariable=emailFrom).place(x=5, y=121, width=200, height=24)

root.mainloop()
