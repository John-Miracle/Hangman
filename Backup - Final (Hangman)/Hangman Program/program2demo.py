"""To get the input from Player 1 to play Hangman!"""

# Importing required modules
import mysql.connector as mycon
from datetime import datetime
from tkinter import *
import random
import pygame,time
import threading
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()



# Decision statement variable
c = [0]
c[0] = 1

#List for user1 configuration
d = []

#List for user2 configuration
l = []

y = 50
z = 50

#Sounds
buttonboi = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\buttonsound.wav")
lostboi = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\lost.wav")
winboi = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\win.wav")
keyboi = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\keybutton.wav")
miscbutton = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\miscbutton.wav")
global vb

pygame.mixer.music.set_volume(0.7)

global t
t = 2
y = 50
z = 50

#Function for muting
def mute():
      global i1,i2,buton,t
      miscbutton.play()
      pygame.mixer.music.set_volume(0)
      def unmute():
          global i1,i2,t
          miscbutton.play()
          pygame.mixer.music.set_volume(0.8)
          buton.config(image = i2,command = mute)
      buton.config(image = i1,command = unmute)

#Function for unmuting      
def unmute():
      global i1,i2,buton,t
      miscbutton.play()
      pygame.mixer.music.set_volume(0.8)
      def mute():
          global i1,i2,t
          miscbutton.play()
          pygame.mixer.music.set_volume(0)
          buton.config(image = i1,command = unmute)
      buton.config(image = i2,command = mute)
      
#Function for accepting details from the user
def store():

      
      global mycursor,con,datam

      #Functon to quit leaderboard table
      def end():
          global con
          con.close()
          window1.destroy()
          
      #Creating a new window widget
      window1 = Toplevel()
      #Inserting Background
      C = Canvas(window1, bg="blue", height=250, width=300)
      filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Backgroundblur.png")
      background_label = Label(window1, image=filename)
      background_label.place(x=0, y=0, relwidth=1, relheight=1)
      C.place()
      window1.title("Leaderboard")
      window1.geometry("1920x1080")
      window1.overrideredirect(True)
      con =  mycon.connect(host = "localhost", user = "root", password = "jlm!sql1308D")
      mycursor = con.cursor()
      mycursor.execute("use Hangman")

      #Function for restoring the details 
      def restore():
          window1.destroy()
          global mycursor
          mycursor.execute("DELETE FROM History where PID > 1;")
          con.commit()
      mycursor.execute("select P,S,C,G from history where G != 'None' order by S desc ")
      data1 = mycursor.fetchall()
      mycursor.execute("select TD from history order by S desc")
      data11 = mycursor.fetchall()
      data22 = []
      ch = 0
      for j in data1:
          ch+=1
          if ch==12:
              break
          h = list(j)
          for i in data11:
             g = list(i)
             for k in g:
                 mydate= datetime.strftime(k,"%F")
                 h.append(mydate)
             break
          data22.append(h)
      imag1 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\id.png")
      imag2 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\name.png")
      imag3 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\score.png")
      imag4 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\time.png")
      imag5 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\level.png")
      imag6 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\date.png")
      g2 = Label(window1,image = imag1,bg = "White")
      g2.place(x = 70 , y = 30)
      g2 = Label(window1,image = imag2,bg = "papaya whip")
      g2.place(x = 320 , y = 30)
      g3 = Label(window1,image = imag3,bg = "Yellow")
      g3.place(x = 570 , y = 30)
      g4 = Label(window1,image = imag4,bg = "yellow green")
      g4.place(x = 820 , y = 30)
      g5 = Label(window1,image = imag5,bg = "DarkOrange1")
      g5.place(x = 1070 , y = 30)
      g6 = Label(window1,image = imag6,bg = "red2")
      g6.place(x = 1320 , y = 30)
      n=70
      m=120
      ch = 1
      hc = 0
      for line in data22:        
       data = str(line)
       dat = data.lstrip("[")
       dat2 = dat.rstrip("]")
       da = dat.split(",",4)
       da.insert(0,str(ch))
       ch+=1
       for i in da:
          j = i.rstrip("]")
          s = str(j)+"l"
          j = str(j)
          if hc == 0:
              if len(j) > 13:
                  s = Label(window1,text = j[:6]+"...",bg = "maroon4",fg = "White",font = ("Times New Roman","15","bold"),relief = RAISED,width = 10)
              else:    
                  s = Label(window1,text = j,bg = "maroon4",fg = "White",font = ("Times New Roman","15","bold"),relief = RAISED,width = 10)
          elif hc == 1:
              if len(j) > 13:
                  s = Label(window1,text = j[:6]+"...",bg = "medium turquoise",fg = "White",font = ("Times New Roman","15","bold"),relief = RAISED,width = 10)
              else:    
                  s = Label(window1,text = j,bg = "medium turquoise",fg = "White",font = ("Times New Roman","15","bold"),relief = RAISED,width = 10)
          elif hc == 2:
              if len(j) > 13:
                  s = Label(window1,text = j[:6]+"...",bg = "salmon2",fg = "White",font = ("Times New Roman","15","bold"),relief = RAISED,width = 10)
              else:    
                  s = Label(window1,text = j,bg = "salmon2",fg = "White",font = ("Times New Roman","15","bold"),relief = RAISED,width = 10)        
          else:
              if len(j) > 13:
                  s = Label(window1,text = j[:6]+"...",bg = "orchid1",fg = "White",font = ("Times New Roman","15","bold"),relief = RAISED,width = 10)
              else:    
                  s = Label(window1,text = j,bg = "orchid1",fg = "White",font = ("Times New Roman","15","bold"),relief = RAISED,width = 10)        
          s.place(x=n,y=m)
          n+=250
       hc+=1   
       n=70
       m+=50
      #g1 = Label(window1,text = d)
      #g1.place(x=360,y=10)
      ires = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\restore.png")
      tmag = Button(window1,image = ires,bg = "white",fg = "Black",font = ("Times New Roman","10"),command = restore)
      tmag.place(x = 1400,y=m+70)
      iback = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\back.png")
      tag = Button(window1,image = iback,bg="wheat4", fg="Black",font=('Times New Roman','10'),command = end)
      tag.place(x=690,y=m+30)
      window1.mainloop()
      
# Main funtion for getting input from users
def hang():
     global vb
     vb = pygame.mixer.music.get_volume() 
     print(vb," ","1")

     if vb == 0:           
            pygame.mixer.music.set_volume(0)
     else:           
            pygame.mixer.music.set_volume(0.8)            
     global rootvol,t,buton,datam
     t = 1
     pygame.mixer.music.load(r"C:\Users\John Linus\Pictures\Hangman pics\theme3.mp3")
     pygame.mixer.music.play(-1)    
        
     #Function for proceeding onto the next set of entry fields
     def click():
       global vb
       global buton,b1,b2
       buttonboi.play()  
       #Decision statement for accepting user names  
       if c[0] == 1:
        ans4 = inp4.get()
        ans5 = inp5.get()
        if (ans4=="" or ans5==""):
            messagebox.showwarning("Warning","Please fill all the fields!")
            c[0]=1
        else:   
         global d,tag,imq,quiti
         ans4 = inp4.get()
         ans5 = inp5.get()      
         homebutton.place(x=1420,y=730)
         b1.place_forget()
         b2.place_forget()
         quiti.place_forget()
         l11.place_forget()
         l4.place_forget()
         l5.place_forget()
         inp4.place_forget()
         inp5.place_forget()
         ans4 = inp4.get()
         ans5 = inp5.get()
         d.append(ans4)
         l.append(ans5)
         lab1.place(x = 620, y = 160)
         l1.place(x=450,y=220)
         l2.place(x=450,y=315)
         l3.place(x=450,y=410)
         inp1.place(x=450,y=260)
         inp2.place(x=450,y=355)
         inp3.place(x=450,y=450)
         global EA,EB,EC
         EA = inp1.get()
         EB = inp2.get()
         EC = inp3.get()
         def show1():
           global EA,inp1
           inp1.configure(show = EA)
           def hide():
              global E1,inp1,H,S
              inp1.configure(show="*")
              E1.configure(image = S , command = show1)
              return
           E1.configure(image = H,command = hide)
           return
         def show2():
           global EB,inp2
           inp2.configure(show = EB)
           def hide():
              global E1,inp2,H,S
              inp2.configure(show="*")
              E2.configure(image = S, command = show2)
              return
           E2.configure(image = H,command = hide)
           return
         def show3():
           global EC,inp3,H,S
           inp3.configure(show = EC)
           def hide():
              global E3,inp3,H,S
              inp3.configure(show="*")
              E3.configure(image = S , command = show3)
              return
           E3.configure(image = H,command = hide)
           return
            
         global E1,E2,E3,S,H
         S = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Show.png")
         H = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Hide.png")
         E1 = Button(window0,image = S,command=show1)
         E2 = Button(window0,image = S,command=show2)
         E3 = Button(window0,image = S,command=show3)
         E1.place(x=1050,y=260)
         E2.place(x=1050,y=355)
         E3.place(x=1050,y=450)
         c[0]=2
            
       #Decision statement for accepting user1 config 
       elif c[0] == 2:      
            ans1 = inp1.get()
            ans2 = inp2.get()
            ans3 = inp3.get()
            if (ans1=="" or ans2=="" or ans3==""):
              messagebox.showwarning("Warning","Please fill all the fields!")
              c[0]=2
            elif (len(ans1)>15):
              messagebox.showwarning("Warning","Please keep the length of the word to 15 characters!")
              c[0]=2 
            else:
             E1.place_forget()
             E2.place_forget()
             E3.place_forget()     
             d.append(ans1)
             d.append(ans2)
             d.append(ans3)
             inp1.place_forget()
             inp2.place_forget()
             inp3.place_forget()
             inp1a.place(x=450,y=260)
             inp2b.place(x=450,y=355)
             inp3c.place(x=450,y=450)
             lab1.place_forget()
             l1.place_forget()
             l2.place_forget()
             l3.place_forget()
             lab2.place(x = 620, y = 160)
             l1.place(x=450,y=220)
             l2.place(x=450,y=315)
             l3.place(x=450,y=410)
             global EAa,EBa,ECa,E1a,E2a,E3a
             EAa = inp1a.get()
             EBa = inp2b.get()
             ECa = inp3c.get()
             def show1():
               global EAa,inp1a,S,H
               inp1a.configure(show = EAa)
               def hide():
                  global E1a,inp1
                  inp1a.configure(show="*")
                  E1a.configure(image=S,command = show1)
                  return
               E1a.configure(image=H,command = hide)
               return
             def show2():
               global EBa,inp2b,S,H
               inp2b.configure(show = EBa)
               def hide():
                  global E1a,inp2b
                  inp2b.configure(show="*")
                  E2a.configure(image = S  , command = show2)
                  return
               E2a.configure(image = H,command = hide)
               return
             def show3():
               global ECa,inp3c,S,H
               inp3c.configure(show = ECa)
               def hide():
                  global E3a,inp3c
                  inp3c.configure(show="*")
                  E3a.configure(image = S  , command = show3)
                  return
               E3a.configure(image = H ,command = hide)
               return
             E1a = Button(window0,image = S,command=show1)
             E2a = Button(window0,image = S,command=show2)
             E3a = Button(window0,image = S,command=show3)
             E1a.place(x=1050,y=260)
             E2a.place(x=1050,y=355)
             E3a.place(x=1050,y=450)
             c[0] = 3
            
       #Decision statement for accepting user2 config  
       elif c[0] == 3:
             pans1 = inp1a.get()
             pans2 = inp2b.get()
             pans3 = inp3c.get()
             if (pans1=="" or pans2=="" or pans3==""):
              messagebox.showwarning("Warning","Please fill all the fields!")
              c[0]=3
             elif (len(pans1)>15):
              messagebox.showwarning("Warning","Please keep the length of the word to 15 characters!")
              c[0]=3 
             else:
              l.append(pans1)
              l.append(pans2)
              l.append(pans3)
              lab2.place_forget()
              inp1a.place_forget()  
              inp2b.place_forget()
              inp3c.place_forget()
              l1.place_forget()
              l2.place_forget()
              l3.place_forget()
              l14.place(x=450,y=220)
              l12.place(x=620,y=340)
              l13.place(x=620,y=300)
              c[0] = 4
              E1a.place_forget()
              E2a.place_forget()
              E3a.place_forget()
              tag["image"] = imq
            
       #Decision statement for accepting level of difficulty     
       elif c[0]==4:
           
           if(r.get()==0):
             d.append(7)
             l.append(7)
           elif(r.get() == 2) :
             d.append(3)
             l.append(3)    
           t = 1
           window0.destroy()
           

       
         

     #Creating Mainwindow   
     window0 = Tk()
     window0.title("Hangman")

     #Inserting Background 
     C = Canvas(window0, bg="blue", height=250, width=300)
     filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Background2d.png")
     background_label = Label(window0, image=filename)
     background_label.place(x=0, y=0, relwidth=1, relheight=1)
     C.place()
     c[0] = 0

     #function for entering into the home screen
     def home():
           
          global vb,b1,b2,E1a,E2a,E3a 
          global buton,datam
          miscbutton.play()
          global d,l
          d.clear()
          l.clear()
          global l10,l11,l4,inp4,l5,inp5,l1,l2,inp1,inp2,l3,inp3,l14,r,l12,l13,lab1,lab2,imq,tag,quiti,inp1a,inp2b,inp3c 
          global c
            
          if c[0] == 2:
              result = messagebox.askquestion("Warning","Are you sure you want to return to Home ? \n\n All the data which you have entered till now  will be lost !") 
              if result == "yes":
               homebutton.place_forget()
               lab1.place_forget()
               l1.place_forget()
               l2.place_forget()
               l3.place_forget()
               inp1.place_forget()  
               inp2.place_forget()
               inp3.place_forget()
               E1.place_forget()
               E2.place_forget()
               E3.place_forget()
              else:
                  return
                
          elif c[0] == 3:
              result = messagebox.askquestion("Warning","Are you sure you want to return to Home ? \n\n All the data which you have entered till now  will be lost !") 
              if result == "yes":
               homebutton.place_forget()
               lab2.place_forget()
               l1.place_forget()
               l2.place_forget()
               l3.place_forget()
               inp1a.place_forget()  
               inp2b.place_forget()
               inp3c.place_forget()
               E1a.place_forget()
               E2a.place_forget()
               E3a.place_forget()
              else:
                  return
              
          elif c[0] == 4:
              result = messagebox.askquestion("Warning","Are you sure you want to return to Home ? \n\n All the data which you have entered till now  will be lost !") 
              if result == "yes":
               homebutton.place_forget()
               l14.place_forget()
               l12.place_forget()
               l13.place_forget()
              else:
                  return
         
          c[0] = 1  
          #Title
          img1=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Title.png")
          l10=Label(window0,image = img1,bg = "lime green")
          l10.place(x=4,y=15)

          #Leaderboard
          img2=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Leaderboardb.png")
          l11=Button(window0,image = img2,bg = "slate gray",command = store)
          l11.place(x=615,y=720)

          #User details show_1
          def speech():
            try:
                import speech_recognition as sr
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print('speak anything')
                    audio=r.listen(source,timeout=3)
                    text=str(r.recognize_google(audio))
                    inp4.insert(0,text)
            except:
                messagebox.showinfo("Error","Try Again!")
          def speech2():
            try:
                import speech_recognition as sr
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print('speak anything')
                    audio=r.listen(source,timeout=3)
                    text=str(r.recognize_google(audio))
                    inp5.insert(0,text)
            except:
                messagebox.showinfo("Error","Try Again!")
          
          img8=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Player One Name.png")
          l4 = Label(window0,image=img8,bg = "OliveDrab2")
          l4.place(x=450,y=225)
          inp4 = Entry(window0,bg="white", fg="Black",font=('Times New Roman','18','bold'),width=50)
          inp4.place(x=450,y=260)
          inp4.config(highlightbackground="black")
          img9=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Player Two Name.png")
          l5 = Label(window0,image=img9,bg = "lime green") 
          inp5 = Entry(window0,bg="white", fg="Black",font=('Times New Roman','18','bold'),width=50)
          l5.place(x=450,y=356)
          inp5.place(x=450,y=390)
          global i1,i2
          
          speak = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\speech.png")
          b1=Button(window0,image = speak,command=speech,bg = "White")
          b1.place(x=1050,y=260)
          b2=Button(window0,image = speak,command=speech2,bg = "White")
          b2.place(x=1050,y=390)      
          
            
          #Volume
          global vb
          print(vb," ","2")
          i1 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\unmute.png")
          i2 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\mute.png")
          if vb == 0:
             buton = Button(window0,image = i1,command = unmute,bg = "lime green")  
          else:
             buton = Button(window0,image = i2,command = mute,bg = "lime green")
          buton.place(x = 1280 , y = 730)
          
          #Word details show_3
          window0.geometry("1920x1080")
          img5=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Word Enter.png")
          l1 = Label(window0,image=img5,bg = "lime green")
          inp1 = Entry(window0,show = "*",bg="white", fg="Black",font=('Times New Roman','18','bold'),width=50)
          img6=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Hint 1.png")
          l2 = Label(window0,image=img6,bg = "OliveDrab2")
          inp2 = Entry(window0,show = "*",bg="white", fg="Black",font=('Times New Roman','18','bold'),width=50)
          img7=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Hint 2.png")
          l3 = Label(window0,image=img7,bg = "light steel blue")
          inp3 = Entry(window0,show = "*",bg="white", fg="Black",font=('Times New Roman','18','bold'),width=50)

          inp1a = Entry(window0,show = "*",bg="white", fg="Black",font=('Times New Roman','18','bold'),width=50)
          inp2b = Entry(window0,show = "*",bg="white", fg="Black",font=('Times New Roman','18','bold'),width=50)
          inp3c = Entry(window0,show = "*",bg="white", fg="Black",font=('Times New Roman','18','bold'),width=50)

          #Difficulty level show_4
         
          img100=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Select difficulty.png")
          l14=Label(window0,image = img100,bg = "lime green")
          r=IntVar()
          img3=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\professional.png")
          l12=Radiobutton(window0,image = img3,variable=r,value=2,bg = "khaki")
          img4=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\amateur.png")
          l13=Radiobutton(window0,image = img4,variable=r,value=0,bg = "khaki")
          
          #Main entry button
          imq = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\play.png")
          imk = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\Next.png")
          tag = Button(window0,image = imk ,bg="lime green",command = click)
          tag.place(x=690,y=510)

          
          #help button
          def helpme():
             miscbutton.play()
             if c[0] == 1:
                txt="Enter your’s  and  your opponent’s name. \n\n"+"Click on QUIT  to exit the game\n\n"+"Click on LEADERBOARD to access the leaderboard" 
                messagebox.showinfo("HOMESCREEN",txt)
             elif c[0] == 2:
                txt = "To be filled by PLAYER 2\n\n"+"Enter the word to be guessed and the required hints\n\n"+"Click on home button to return to homescreen"  
                messagebox.showinfo("PLAYER:1 CONFIG",txt)
             elif c[0] == 3:
                txt = "To be filled by PLAYER 1\n\n"+"Enter the word to be guessed and the required hints\n\n"+"Click on home button to return to homescreen"  
                messagebox.showinfo("PLAYER:2 CONFIG",txt)
             elif c[0] == 4:
                txt ="Select difficulty level\n\n" +" Amateur : 7 Errors allowed\n\n" + "Professional : 3 Errors allowed\n\n"+"Default : Amateur"  
                messagebox.showinfo("SELECT DIFFICULTY",txt) 
          hi = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\infob.png")
          help = Button(window0,image = hi,bg="lime green",command = helpme)
          help.place(x=1350,y=730)

          #help button
          global asd
          asd = 1
          def Speechhelp():
             
             global mute,asd
             miscbutton.play()
             
             if c[0] == 1:
                   
                 if asd == 1:
                       voice1 = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\Voice 1.wav")
                       mute()
                       voice1.set_volume(2)
                       voice1.play()
                       asd = 2
                 else:
                       
                       voice1a = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\Voice 1a.wav")
                       mute()
                       voice1a.set_volume(2)
                       voice1a.play()
                       
             elif c[0] == 2:
                 voice2 = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\Voice 2.wav")
                 mute()
                 voice2.set_volume(2)
                 voice2.play()
                
             elif c[0] == 3:
                 voice3 = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\Voice 3.wav")
                 mute()
                 voice3.set_volume(2)
                 voice3.play()
             elif c[0] == 4:
                 voice4 = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\Voice 4.wav")
                 mute()
                 voice4.set_volume(2)
                 voice4.play()
                 
          sh = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\SpeechHelp.png" )
          shelp = Button(window0,image = sh,bg="lime green",command = Speechhelp)
          shelp.place(x = 1210 , y = 730)
         
          #quit
          def quitb():
             miscbutton.play()
             window0.destroy()
          ui = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\quit.png")
          quiti = Button(window0,image = ui,bg="lime green",command = quitb)
          quiti.place(x=45,y=735)
         
          #user config
          imga = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\player1config.png")
          imgb = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\player2config.png")
          lab1 = Label(window0,image=imga,bg="dark khaki")
          lab2 = Label(window0,image=imgb,bg="dark khaki")
          window0.mainloop()

     #home button
     uj = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\homeb.png")
     homebutton = Button(window0,image = uj,bg = "lime green" ,command=home)
     home()
     
     print(vb," ","3")

     pygame.mixer.music.stop()
     return l,d

 
