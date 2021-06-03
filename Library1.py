# -*- coding: utf-8 -*-
"""
Created on Mon May 31 22:04:49 2021

@author: BHUVAN PANDEY
"""

# -*- coding: utf-8 -*-
"""
Created on Sun May 30 21:24:37 2021

@author: BHUVAN PANDEY
"""
def head(title):
    system("cls")
    print("-"*140)
    print("Personal Voice Enabled Library Management Tool".center(140))
    print("-"*140)
    if title:
        print(title.center(140))
        print("-"*140)
def body(text,b=False,e=False):
    if b:
        print("\n\n")
        print("-"*140)
        print("+","-"*138,"+",sep="")
    print("| ",text.center(136)," |",sep="")
    if e:
        print("+","-"*138,"+",sep="")
    
import mysql.connector as a
import sys
from os import *
head(title="Importing Libraries")
import pyttsx3 as pt
import getpass as gt
import speech_recognition as sr
import pyaudio
conn=a.connect(host="localhost",user="root",passwd="bp15072000",database="Library")

        

def addbook():
    bn=input("Enter BOOK Name : ")
    bc=input("Enter BOOK Code : ")
    total=input("Total Books : ")
    subject=input("Enter Subject : ")
    data=(bn,bc,total,subject)
    sql='insert into Books values(%s,%s,%s,%s)'
    c=conn.cursor()
    c.execute(sql,data)
    conn.commit()
    print(">------------------------------------------------------------------<")
    print("Data Entered Successfully")
    pt.speak("Data Entered Successfully")
    main()
def issue_book():
    name=input("Enter your name: ")
    r_no1=input("Enter  your registration number : ") 
    book_code=input("Enter boook code : ")
    issue_date=input("Enter issue date : ")
    sql="insert into Issue values (%s,%s,%s,%s)"
    data=(name,r_no1,book_code,issue_date)
    c=conn.cursor()
    c.execute(sql,data)
   
    
    
    conn.commit()
    print("<-------------------------------------------------------------------<")
    print("Book issued to :",name)
    pt.speak("Book SUCCESSFULLY ISSUED :")
    bookup(book_code,-1)
def submit_book():
    name=input("Enter  your Name : " )
    r_no=input("Enter your registration number : ")  
    book_code=input("Enter Book Code : ")
    submit_date=input("Enter submit date : ")
    sql="insert into Submit values(%s,%s,%s,%s)"
    data=(name,r_no,book_code,submit_date)
    c=conn.cursor()
    c.execute(sql,data)
    conn.commit()
    print("<------------------------------------------------------------------<")
    print("Book submitted from :",name)
    pt.speak("Book successfully submitted :")
    bookup(book_code,1)
    
def bookup(book_code,u):
    sql="select total_books from Books where book_code=%s "
    data=(book_code,)
    c=conn.cursor()
    c.execute(sql,data)
    myresult=c.fetchone()
    t=myresult[0]+u 
    sql1="update Books set total_books=%s where book_code=%s"
    data1=(t,book_code)
    c.execute(sql1,data1)
    
    conn.commit()
    main()
def delete_book():
    book_code=input("Enter Book Code : ")
    sql="delete from books where book_code=%s"
    data=(book_code,)
    c=conn.cursor()
    c.execute(sql,data)
    conn.commit()
    main()
def display_book():
    a="SELECT  * FROM Books"
    c=conn.cursor()
    c.execute(a)
    myresult=c.fetchall()   
    for i in myresult:
        print("Book name : ",i[0])
        print("Book_code :" ,i[1])
        print("Total Books :",i[2])
    main()
    
def main():
    
    print("""
    >-------------------------WELCOME TO LIBRARY MANAGER----------------------<
    1.ADD BOOK
    2.ISSUE BOOK
    3.SUBMIT BOOK
    4.DELETE BOOK
    5.DISPLAY BOOKS
    6. EXIT FROM THE APP
    """)
    print("I am still there to help you. How can I help you?")
    pt.speak("I am still there to help you. How can I help you?")
    body("",e=True)
    print()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("start saying what you want me to do............. ")
        pt.speak("start saying what you want me to do.............")
        audio=r.listen(source)
        print("stop now.....")
        pt.speak("stop now......")
        body("speech completed..........stop now")
        pt.speak("speech completed........stop now")
        text=r.recognize_google(audio)
        print(text)
        x=text.lower()
   
    print(">----------------------------------------------------------------<")
    if"add" in x or "insert "in x and "book" in x:
        addbook()
    if "issue " in x or "give "  in x and ("book" in x or "to someone" in x):
        issue_book()
    if "submit " in x and "book" in x:
        submit_book()
    if ("delete" in x or "remove" in x) and "book" in x:
        delete_book()
    elif ("display " in x or "show " in x) and ("all book" in x or "all books" in x or "books" in x):
        display_book()
    elif "exit "in x or "exit from app " in x:
        sys.exit()
    
    else:
        body("WRONG CHOICE ,PLEASE ENTER RIGHT CHOICE ")
        pt.speak("Wrong choice please enter right choice :")

    main()        
    
def pswd():
    
    pt.speak("Enter your Password :")
    ps=gt.getpass("Enter your password :")
    apass="Gehu@1507"
    if ps==apass:
        head("Welcome To Library Management Tool")
        body("Hello I am  your own personal ,voice enabled Library Manager ",True)
        pt.speak("Hello I am  your own personal ,voice enabled Library Manager ")
        body("")
        body("Let me Introduce Myself")   
        pt.speak("Let me Introduce Myself")
        body("")
        body("i can listen your voice, plz speak when you want me to do task........")
        pt.speak(" i can listen your voice,plz speak when you want me to do task..........")
        body("")
        body("I am made for windows only but soon be available on linux.")
        pt.speak("I am made for windows only,but soon be available on linux.")
        body("")

        body("""I have interesting features,Hit enter button to explore my Features""")
        pt.speak("I have interesting features,Hit enter button to explore my Features")
        body("")
        body("")
        body("Press Enter to Continue.")
        pt.speak("Press Enter to Continue")
        body("",e=True)
        input()
        main()
    else:
        print("Wrong Password :")
        pt.speak('Wrong Password ,plz enter your password again:')
        pswd()
pswd()        
         