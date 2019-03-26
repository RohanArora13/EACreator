from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import names
import winsound
import threading
import re,string
import webbrowser

import tkinter as tkinter
import tkinter.ttk as ttk
import os
 


duration = 300  # milliseconds
freq = 450  # Hz

binary = r'C:\Program Files\Mozilla Firefox\firefox.exe'
caps = DesiredCapabilities().FIREFOX
caps["pageLoadStrategy"] = "eager"  #  interactive


def makeaccount():
    driver = webdriver.Firefox()
    driver.get("https://www.temp-mail.org")
    window_before=driver.window_handles[0]
    time.sleep(10)
    counter=0
    while("false"):
        try:
            driver.find_element_by_id('mail')
            break
        except:
            time.sleep(2)
            counter+=1
            if (counter>10):
                os._exit(0)

    emailtext = driver.find_element_by_id('mail')
    temp_email = emailtext.get_attribute("value")
    print (temp_email)
    ## copy mail

    
    ### switch to ea
    driver.execute_script('''window.open("https://www.ea.com/register","_blank");''')
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    time.sleep(10)
    ## enter email 
    gotemailpage = "false"
    errornp=0
    while(gotemailpage):
        try:
            inputElement = driver.find_element_by_id('email')
            break
        except:
            time.sleep(3)
            print("Waiting for ea.com")
            if(errornp>4):
                winsound.Beep(freq, duration)
                print("will try more 5 times please wait")
            errornp+=1
            if(errornp>10):
                print("ERROR while loading the www.ea.com/register")
                print("Closing program in 20 seconds... try again later")
                time.sleep(30)
                os._exit(0)


    time.sleep(1)
    inputElement = driver.find_element_by_id('email').send_keys(temp_email)
    driver.find_element_by_id("btn-next").click()
    ## entering details
    time.sleep(4)
    # id 
    name=names.get_first_name()
    origin_id = name+"_"+str(random.randint(200,700))+str(random.randint(20,70))
    print (origin_id)
    txtfile = open(str(origin_id)+".txt", "a")
    txtfile.write("\n"+temp_email)
    txtfile.write("\n"+"origin_id = "+origin_id)
    driver.find_element_by_id('originId').send_keys(origin_id)
    # password
    password = name+randomStringDigits(5)+"@"+str(random.randint(20,70))
    print(password)
    txtfile.write("\n"+"password = "+password)
    driver.find_element_by_id('password').send_keys(password)
    confirmPassword=driver.find_element_by_id('confirmPassword').send_keys(password)
    txtfile.close()
    #security question
    driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/div[1]/div[1]/ul/li[4]/div/div/div[1]/span").click()
    driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/div[1]/div[1]/ul/li[4]/div/div/div[2]/div/div/div[1]/div[1]/a/span").click()
    securityAnswer= driver.find_element_by_id('securityAnswer').send_keys(origin_id)
    #DOB
    driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/div[1]/div[1]/ul/li[7]/div/div[1]/div[1]/span").click()
    driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/div[1]/div[1]/ul/li[7]/div/div[1]/div[2]/div/div/div[1]/div["+str(random.randint(2,7))+"]").click()
    #date random 2 - 25
    driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/div[1]/div[1]/ul/li[7]/div/div[2]/div[1]/span").click()
    driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/div[1]/div[1]/ul/li[7]/div/div[2]/div[2]/div/div/div[1]/div["+str(random.randint(2,25))+"]/a/span").click()
    #year
    driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/div[1]/div[1]/ul/li[7]/div/div[3]/div[1]/span").click()
    driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/div[1]/div[1]/ul/li[7]/div/div[3]/div[2]/div/div/div[1]/div[23]/a/span").click()
    #accept
    driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/div[1]/div[3]/ul/li[3]/div/div/span").click()
    time.sleep(1)
    # next button
    winsound.Beep(freq, duration)
    getwin="false"
    driver.find_element_by_id("submit-btn").click()
    time.sleep(4)
    errornpq=0
    while(getwin):
        #print ("waiting for code")
        try:
            driver.find_element_by_id('firstName')
            break
        except:
            time.sleep(4)
            winsound.Beep(freq, duration)
            print ("Recaptcha or Some input mistake please solve!!")
            errornpq+=1
            if(errornpq>15):
                print("ERROR while filling info in form")
                print("Closing program in 20 seconds... try again later")
                time.sleep(30)
                os._exit(0)
    

    
    driver.find_element_by_id('firstName').send_keys( names.get_first_name())
    time.sleep(0.5)
    driver.find_element_by_xpath("/html/body/div/form/div[3]/div[2]/a[1]").click()
    time.sleep(0.5)
    ## back to temp mail
    driver.switch_to.window(window_before)
    ## keep pressing refresh untill mail comes

    gotcode = "false"
    while(gotcode):
        print ("waiting for code")
        try:
            driver.find_element_by_link_text("Your EA Security Code is:").click()
            break
        except:
            gotcode="true"
            time.sleep(2)
            driver.find_element_by_xpath(' //*[@id="click-to-refresh"]').click()

    print ("code found")

    getcode="false"
    while(getcode):
        #print ("waiting for code")
        try:
            code = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[3]/div/div/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/span[2]/b").text
            break
        except:
            code = "not found"


    print ("code = "+code)
    driver.switch_to.window(window_after)

    ## back to ea 
    time.sleep(2)
    driver.find_element_by_id('emailVerifyCode').send_keys(code)
    driver.find_element_by_xpath('/html/body/div[2]/form/div[3]/div/div[4]/a/span/span').click()
    txtfile = open("eaccount.txt", "a")
    txtfile.write("\nAccount Acitve \n\n")
    txtfile.close()
    print("Account Created....")
    time.sleep(2)
    driver.close()




root = tkinter.Tk()
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

ttk.Style().configure("TButton", padding=6, relief="flat",
   background="#ccc")

## background imagge
background_image=tkinter.PhotoImage(file = str(os.path.dirname(os.path.abspath(__file__)))+"\\bg.png")
# scale_w = root.winfo_width()/background_image.winfo_width()
# scale_h = root.winfo_hight()/background_image.winfo_height()
# background_image.zoom(scale_w, scale_h)
background_label = tkinter.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# v = tkinter.IntVar()
# v.set(1)  # initializing the choice chrome

# languages = [
#     ("firefox"),
#     ("chrome"),
# ]

# def ShowChoice():
#     print(v.get())

# tkinter.Label(root, 
#          text="""Choose Browser""",
#         # justify = tkinter.LEFT,
#          padx = 20).pack()

# for val, language in enumerate(languages):
#     tkinter.Radiobutton(root, 
#                   text=language,
#                   padx = 20, 
#                   variable=v, 
#                   command=ShowChoice,
#                   value=val).pack(anchor="center")


L1 = tkinter.Label(root, text="(Loop) How many Accounts ")
L1.pack()
# Create a Tkinter variable
tkvar = tkinter.StringVar(root)
 
# Dictionary with options
choices = { '1','2','3','4','5'}
tkvar.set('1') # set the default option
# E1 = tkinter.Entry(root, bd =5)
# E1.pack()
tkinter.OptionMenu(root, tkvar,*choices).pack()


txt = tkinter.Label(root,height=9,width=60 ,text="""Steps To Follow : \n\n1) Run the program Wait for browser to open
    \n2) Dont Touch the browser or CLICK inside browser ("you can minimize it")
    \n3) IF recaptcha Appears Solve it and click 'Next'
    \n4) if you hear beep sounds means AN action is required
    """)
txt.config(state="disabled")
txt.pack(padx=5, pady=10,anchor="w")

def startfunc():
    print("starting..")
    for i in range (0,int(tkvar.get())):
        btn.config(state="disabled")
        btn.config(text="Running..")
        t = threading.Thread(target=makeaccount)
        t.start()
        #print ("running")

def update():
    webbrowser.open('https://rohanarora13.github.io/EACreator/')

import urllib.request

fp = urllib.request.urlopen("https://rohanarora13.github.io/EACreator/")
mybytes = fp.read()

mystr = mybytes.decode("utf8")
fp.close()

#print(mystr)
start="<strong>["
end="]</strong></p>"
ver = mystr[mystr.find(start)+len(start):mystr.rfind(end)]
#print (ver)

#### current verion of program
currentver=1

print("current version = " + str(currentver))

#if(int(ver)==currentver):
btn = ttk.Button(root,text="Run",command=startfunc)
btn.pack(padx=5, pady=10)
root.title("EACreator v1")


def callback(event):
    webbrowser.open_new(r"https://rohanarora13.github.io/EACreator/")

link = tkinter.Label(root, text="EACreator Github & info", fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", callback)
# elif(int(ver)>currentver):
#     btn = ttk.Button(root,text="Update",command=update)
#     btn.pack(padx=5, pady=10)

    
root.mainloop()


    

