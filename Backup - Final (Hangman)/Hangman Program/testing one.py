# Importing the required modules
import threading
from tkinter import *
from tkinter import ttk
import mysql.connector as mycon
import pygame,time
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
from tkinter import messagebox
import program2demo as p
import trial as t


g = [0]# player ID
g[0] = 1

global v
v = 0
j = 0

#Sound
buttonboi = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\buttonsound.wav")
lostboi = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\lost.wav")
winboi = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\win.wav")
keyboi = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\keybutton.wav")
miscbutton = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\miscbutton.wav")

# Setting Sound Volume
miscbutton.set_volume(0.8)
buttonboi.set_volume(0.8)
lostboi.set_volume(0.8)
winboi.set_volume(0.8)
keyboi.set_volume(0.8)


global score1# Player_1 score
global score2# Player_2 score

chancesr1 = 0
chancesr2 = 0

#Iteration variable
global m
m = 1

#Function for quiting game
def quitreal():
    miscbutton.play()
    global qt
    qt = Tk()
    qt.title("Quit")
    qt.geometry("1920x1080")

    #Setting_Background
    C = Canvas(qt, bg="blue", height=250, width=300)
    filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Background2d.png")
    background_label = Label(qt, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place()
    result = messagebox.askquestion("Quit","Are you sure you want to quit? ")
    if result == "yes":
        qt.destroy()
        pygame.quit()
        sys.exit()
    else:
        g[0]=4
        realstart()
    qt.mainloop()

#Start_Game    
def realstart():
 global leveln,klm
 
 vb = pygame.mixer.music.get_volume()   
 if vb == 0:
      pygame.mixer.music.set_volume(0)
 else:
      pygame.mixer.music.set_volume(0.8)
 pygame.mixer.music.stop()
 buttonboi.play()   
 global h,buton     
 h = 0
 global j   
 global root1   
 if g[0] == 1:
  root.destroy()
 elif g[0] == 3:
  root1.destroy()
  g[0]=1
 elif g[0]==4:
     qt.destroy()
     g[0]=1
     
 if klm == 0:
     t.ask()
     klm = 1
 #Screen_1  
 lnp,inp = p.hang()
 if lnp == []:
     quitreal()
     return k

    
 # Variables to store player detail   
 global user1,word,hint1,hint2,chances1,user2,word2,hint12,hint22,chances2
 
 #user-1 configuration
 user1 = inp[0]
 word = inp[1].upper()
 hint1 = inp[2].title()
 hint2 = inp[3].title()
 chances1 = inp[4]
 
 #user_2 confguration
 user2 = lnp[0]
 word2 = lnp[1].upper()
 hint12 = lnp[2].title()
 hint22 = lnp[3].title()
 chances2 = lnp[4]
 
 if chances2 == 3:
     leveln = 3
     level = "Professional"
 else:
     leveln = 7
     level = "Amateur"
     
 # Screen_2    
 def starta():
     global window2,rootvol,lk,buton
     pygame.mixer.music.load(r"C:\Users\John Linus\Pictures\Hangman pics\theme2.mp3")
     pygame.mixer.music.play(-1) 
     buttonboi.play()
     if g[0]== 2:    
      window2.destroy()
      
     #creating second window
     window = Tk()
     window.title("Hangman")
     window.geometry("1920x1080")

     #Adding background in secondwindow
     C = Canvas(window, bg="blue", height=250, width=300)
     filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Background2d.png")
     background_label = Label(window, image=filename)
     background_label.place(x=0, y=0, relwidth=1, relheight=1)
     C.place()
           

     d=[]
     # Function for features on the secondary window
     def start():
        global leveln
        global chancesr1,chancesr1
        global buton
        global rootvol,v,timems1,timems2,lk
        global label
        global t 
        global j
        
        # Function for timer
        def countdown():
             global leveln
             global label
             global t,rootvol,v,v1,v2,chancesr1,chancesr1
             global window2,j,mins,secs,minute1,seconds1,rootvol,timems1,timems2
             global minute2,seconds2
             global times
             print(j)
             secs = 0
             mins = 2
             
             for i in range(120):
               if secs < 10:
                   label.config(text = "0"+str(mins)+":"+"0"+str(secs))
               else:
                   label.config(text = "0"+str(mins)+":"+str(secs))
               if secs == 0:
                   mins-=1
                   secs = 59
               secs = secs-1
               if j==1:
                   v = (mins*60)+(secs)
                   j=0
                   return
               if mins <0:

                    img=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\pic9.png")
                    l100=Label(image = img)
                    l100.image=img
                    l100.place(x = 600, y = 70)
                    pygame.mixer.music.stop()
                    lostboi.play()
                    messagebox.showinfo("Time up","Too bad, you were too slow!",)
                    messagebox.showinfo("Correct word","   \"" + a+ "\"   ")
                    
                    if g[0] == 1:
                      v1 = 0
                      timems1 = "00"+":"+"00"
                      
                      minutes1 = mins
                      seconds1 = secs
                      chancesr1 = 0
                      g[0] = 2
                      window.destroy()
                      window2 = Tk()
                      window2.title("Hangman")
                      window2.configure(bg='ivory4')
                      window2.geometry("1920x1080")
                      C = Canvas(window2, bg="blue", height=250, width=300)
                      filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Background2d.png")
                      background_label = Label(window2, image=filename)
                      background_label.place(x=0, y=0, relwidth=1, relheight=1)
                      C.place()
                      ims = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\clicktocontinue.png")
                      startbutton1 = Button(window2,image = ims,command=starta,bg ="lime green")
                      startbutton1.place(x=450,y=330)
                      window2.mainloop()
                      chancesr1 = 0
                      g[0] = 2
                      m=1
                      
                    else:
                      v2 = 0
                      timems2 = "00"+":"+"00"
                      con =  mycon.connect(host = "localhost", user = "root", password = "jlm!sql1308D")
                      mycursor = con.cursor()
                      mycursor.execute("use Hangman")
                      mycursor.execute("select count(PID) from history;")
                      data = mycursor.fetchall()
                      j1 = 0
                      j2 = 0
                      if level == 3:
                          r = 100
                      else:
                          r = 10
                      for i in data:
                          j1 = i
                          for u in j1:
                              j2 = u
                      chancesr2 = 0
                      sql = "insert into history (PID,P,S,C,G) values (%s,%s,%s,%s,%s)"
                      val = [(str(j2+1),user1,str(chancesr1),timems1,level),
                             (str(j2+2),user2,str(chancesr2),timems2,level)
                             ]
                      mycursor.executemany(sql,val)
                      con.commit()
                      con.close()  
                      minutes1 = mins
                      seconds1 = secs
                      chancesr2 = 0
                      
                      global root1   
                      g[0]=3
                      window.destroy()   
                      root1= Tk()
                      root1.geometry("1920x1080")
                      root1.title("Hangman")
                      C = Canvas(root1, bg="blue", height=250, width=300)
                      filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Background2d.png")
                      background_label = Label(root1, image=filename)
                      background_label.image=img
                      background_label.place(x=0, y=0, relwidth=1, relheight=1)
                      C.place()
                      score1 = str(chancesr1)
                      score2 = str(chancesr2)
                      img1=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\result.png")
                      l10=Label(root1,image = img1,bg = "ivory4")
                      l10.place(x=440,y=50)
                      labelf = Label(root1,width=21,height=9,text="\n"+user1.title()+"\n\n"+"Word : "+word+"\n\n"+"Score : "+score1+"\n\n"+"Time left : "+timems1,font=("Lucida Console","20","bold"),bg = "yellow" , fg = "black",pady = 10)
                      labelf.place(x=410,y=150)
                      labelf = Label(root1,width=21,height=9,text="\n"+user2.title()+"\n\n"+"Word : "+word2+"\n\n"+"Score : "+score2+"\n\n"+"Time left : "+timems2,font=("Lucida Console","20","bold"),bg = "yellow" , fg = "black",pady = 10)
                      labelf.place(x=790,y=150)

                      img = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\return to main menu.png")
                      startbutton1 = Button(root1,image = img,bg = "white",command = realstart)
                      startbutton1.image=img
                      startbutton1.place(x=575,y=720)
                      if (chancesr2)>(chancesr1):
                          txt = "Congratulations"+" "+user2.title()+"\n\nYou have won the game!"
                      elif (chancesr2) == (chancesr1):
                          txt = "Uh oh looks like it is a draw "
                      else:
                         txt="Congratulations"+"  "+user1.title()+"\n\n You have won the game!"
                      labelf=Label(root1,width=45,height=4,text=txt,font=("Lucida Console","20","bold"),bg = "yellow" , fg = "black")
                      labelf.place(x=410,y=460)
                      root.mainloop()
                      m=1
                      messagebox.showinfo("","")
                      return
               time.sleep(1)
               
        
        label=Button(window,text = "",bg = "SpringGreen3",fg = "Yellow",font = ("Lucidia Console","16","bold"))
        label.place(x = 720 , y = 10)
        countdown_thread = threading.Thread(target=countdown)
        j = 0
        countdown_thread.start()

        #Function for pausing the game
        def pause5():
            miscbutton.play()
            messagebox.showinfo("Pause","The game has been paused for 5 seconds!")
            time.sleep(5)
            return
        imag = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\pauseb.png") 
        bug=Button(window,image=imag,command = pause5,bg = "lime green")
        bug.image = imag
        bug.place(x=1420,y=730)
        global i1,i2
        
        global k
        k = 1
        global z
        we = 350
        labels.place_forget()
        startbutton.place_forget()
        global hint1,hint2,hint12,hint22
        global hint1r,hint2r
        global chances1
        global chances2
        global chancesvar
        if g[0] == 1:
          a = word  
          chancesvar = chances1
          hint1r = hint1
          hint2r = hint2
          
        else :
          a = word2
          chancesvar = chances2
          hint1r=hint12
          hint2r=hint22
        messagebox.showinfo("Your Hint","  \""+hint1r+"\"  ")

        #Function for showing information of the current window
        def info():
            miscbutton.play()
            txt = "Guess window :\n\n"+"Use the onscreen keyboard to guess the words\n\n"+"Remember to press the Space Button to check for spaces in the program\n\n"+"To access the the main hint click ont the bulb icon.**\n\n"+"The bonus hint will be made available and can be accessed by clicking on the bulb button .***\n\n" +"When you access the bonus hint your score will be decreased by 50 points\n\n" +"** when no of chances of error is greater than 2\n"+"** when no of chances of error is lesser than or equal to 2"
            messagebox.showinfo("Help",txt)
        yu = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\infob.png")
        infobutton = Button(window,image = yu,command = info,bg = "lime green")
        infobutton.image = yu
        infobutton.place(x=1350,y=730)

        def sinfo():
            
            miscbutton.play()
            voice5 = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\Voice 5.wav")
            pygame.mixer.music.set_volume(0.0)
            voice5.play()
            return
        yum = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\SpeechHelp.png")
        sinfobutton = Button(window,image = yum,command = sinfo,bg = "lime green")
        sinfobutton.image = yum
        sinfobutton.place(x=1280,y=730)
        if m == 1:
            f = 350           
            h =""
            if(g[0]==1):
               h=word
            elif(g[0]==2):
               h=word2
            for i in h:
               s = "but"+i                 
               s = Button(window, text="  ",bg="ivory4", fg="white",width=3,height=1,font=('TImes New Roman','20','bold','underline'))
               if i == " ":
                   s = Button(window, text="/",bg="ivory4", fg="white",width=3,height=1,font=('TImes New Roman','20','bold'))
               s.place(x=f, y=400)
               f+=58
          
        # function for accepting input from the on screen keyboard  
        def clicked(alphabet):
               global leveln
               global lk
               global buton
               global t,rootvol,v,timems1,timems2 
               global j,soundscale
               keyboi.play()
               global k,m
               global window2,z
               global chancesr1
               global chancesr2
               global chancesvar
               global word
               global word2
               m=2
               if g[0] == 1:
                 a = word   
               else :
                 a = word2
               b = a
                   
               if alphabet in a:
                for i in range(len(a)):
                       if i in d:
                         continue
                       if alphabet== a[i]:
                         if alphabet != " ":   
                           txt = alphabet
                         else:
                           txt = " : "  
                         s = "but"+alphabet
                         s = Button(window , text=txt ,bg="ivory4", fg="white",width=3,height=1,font=('TImes New Roman','20','bold','underline'))
                         s.place(x=we+i*(58),y=400)
                         d.append(i)
                         k=2
                       
                          

               else:
                      # Calulating the number of errors made by the user
                      #Displaying pictures based on the number of errors made by the user 
                      txt=" NO. OF ERRORS LEFT :"+str(chancesvar-1);
                      label1.configure(text=txt)
                      chancesvar = chancesvar - 1;
                      if chancesvar==6:
                          img=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Pic2.png")
                          l100=Label(image = img)
                          l100.image=img
                          l100.place(x = 600, y = 70) 
                      if chancesvar==5:
                          img=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Pic4.png")
                          l100=Label(image = img)
                          l100.image=img
                          l100.place(x = 600, y = 70) 
                      if chancesvar==4:
                          img=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Pic5.png")
                          l100=Label(image = img)
                          l100.image=img
                          l100.place(x = 600, y = 70) 
                      if chancesvar==3:
                          img=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Pic6.png")
                          l100=Label(image = img)
                          l100.image=img
                          l100.place(x = 600, y = 70) 
                      if chancesvar==2:
                          img=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Pic7.png")
                          l100=Label(image = img)
                          l100.image=img
                          l100.place(x = 600, y = 70) 
                      if chancesvar==0:
                          img=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\pic9.png")
                          l100=Label(image = img)
                          l100.image=img
                          l100.place(x = 600, y = 70) 
                      if chancesvar==1:
                          img=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Pic8.png")
                          l100=Label(image = img)
                          l100.image=img
                          l100.place(x = 600, y = 70) 
                      if chancesvar==2:
                           buttonboi.play()
                           messagebox.showinfo("Bonus","You can now access your bonus hint!"+"\n\n (Points will be reduced if you access it!)")
                           global hint1r,hint2r
                           def but():
                                 miscbutton.play()
                                 global hint1r,hint2r,h
                                 result = messagebox.askquestion("Hint","Are you sure you want to access the second hint ?\n\n")
                                 if result == "yes":    
                                   h += 1 
                                   messagebox.showinfo("HINT","Main Hint\n"+"\""+hint1r+"\""+"\n"+"Bonus Hint : \n"+"\""+hint2r+"\"")
                                 else:
                                   return
                               
                           imgh = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\Hintbutton.png")
                           hintbutton = Button(window,image=imgh,bg ="yellow",command=but)
                           hintbutton.image = imgh
                           hintbutton.place(x = 40 , y = 720)    
       
                      if chancesvar==0:
                        # Creating a connection to a mysql database to store the result of the particular user 
                        j = 1
                        global v1,v2
                        pygame.mixer.music.stop()
                        lostboi.play()
                        messagebox.showinfo("Hanged!","Oops! You have used all your chances!",)
                        messagebox.showinfo("Correct word","   \"" + a+ "\"   ")
                        if g[0] == 1: 
                          chancesr1 = 0
                          v1 = v
                          minutes,seconds = divmod(v1,60)
                          
                          #Displaying the number of seconds remmaining 
                          if seconds < 10:
                             timems1 = "0"+ str(minutes) + ":"+ "0" +str(seconds)
                          else:
                             timems1 = "0"+str(minutes) + ":"+str(seconds) 
                          
                          g[0] = 2
                          window.destroy()
                          window2 = Tk()
                          window2.configure(bg='ivory4')
                          window2.geometry("1920x1080")
                          window2.title("Hangman")
                          C = Canvas(window2, bg="blue", height=250, width=300)
                          filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Background2d.png")
                          background_label = Label(window2, image=filename)
                          background_label.image=img
                          background_label.place(x=0, y=0, relwidth=1, relheight=1)
                          C.place()
                          ims = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\clicktocontinue.png")
                          startbutton1 = Button(window2,image = ims,command=starta,bg ="lime green")
                          startbutton1.place(x=450,y=330)
                          window2.mainloop()
                          chancesr1 = 0
                          g[0] = 2
                          m=1
                          
                        else:

                          #Creating a connection to a mysql database to store the result of the particular user
                          con =  mycon.connect(host = "localhost", user = "root", password = "jlm!sql1308D")
                          mycursor = con.cursor()
                          mycursor.execute("use Hangman")
                          mycursor.execute("select count(PID) from history;")
                          data = mycursor.fetchall()
                          j1 = 0
                          j2 = 0
                          if leveln == 3:
                              r = 100
                          else:
                              r = 10
                          for i in data:
                              j1 = i
                              for u in j1:
                                  j2 = u
                          chancesr2 = 0
                          v2 = v
                          minutes,seconds = divmod(v2,60)
                          if seconds < 10:
                            timems2 = "0"+str(minutes) + ":"+ "0" +str(seconds)
                          else:
                            timems2 = "0"+str(minutes) + ":"+str(seconds) 
                          sql = "insert into history (PID,P,S,C,G) values (%s,%s,%s,%s,%s)"
                          val = [(str(j2+1),user1,str(chancesr1),timems1,level),
                                 (str(j2+2),user2,str(chancesr2),timems2,level)
                                 ]
                          mycursor.executemany(sql,val)
                          con.commit()
                          con.close()
                          global root1   
                          g[0]=3
                          window.destroy()   
                          root1= Tk()
                          root1.title("Hangman")
                          root1.geometry("1920x1080")

                          #Inserting a background
                          C = Canvas(root1, bg="blue", height=250, width=300)
                          filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Background2d.png")
                          background_label = Label(root1, image=filename)
                          background_label.image=img
                          background_label.place(x=0, y=0, relwidth=1, relheight=1)
                          C.place()
                          
                          score1 = str(chancesr1)
                          score2 = str(chancesr2)
                          
                          img1=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\result.png")
                          l10=Label(root1,image = img1,bg = "ivory4")
                          l10.place(x=440,y=50)
                          labelf = Label(root1,width=21,height=9,text="\n"+user1.title()+"\n\n"+"Word : "+word+"\n\n"+"Score : "+score1+"\n\n"+"Time left : "+timems1,font=("Lucida Console","20","bold"),bg = "yellow" , fg = "black",pady = 10)
                          labelf.place(x=410,y=150)
                          labelf = Label(root1,width=21,height=9,text="\n"+user2.title()+"\n\n"+"Word : "+word2+"\n\n"+"Score : "+score2+"\n\n"+"Time left : "+timems2,font=("Lucida Console","20","bold"),bg = "yellow" , fg = "black",pady = 10)
                          labelf.place(x=790,y=150)

                          img = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\return to main menu.png")
                          startbutton1 = Button(root1,image = img,bg = "white",command = realstart)
                          startbutton1.image=img
                          startbutton1.place(x=575,y=720)
                          if (chancesr2)>(chancesr1):
                                txt = "Congratulations"+" "+user2.title()+"\n\nYou have won the game!"
                          elif (chancesr2) == (chancesr1):
                                txt = "Uh oh looks like it is a draw "
                          else:
                                txt="Congratulations"+" "+user1.title()+"\n\n You have won the game!"
                          labelf=Label(root1,width=45,height=4,text=txt,font=("Lucida Console","20","bold"),bg = "yellow" , fg = "black")
                          labelf.place(x=410,y=460)
                          root.mainloop()
                          m=1
                          t=1
                        
               if len(d) == len(b.replace(" ","")):

                      # Display screen and message if the word has been guessed correctly
                      j = 1
                      pygame.mixer.music.stop()
                      winboi.play()
                      m = 1
                      global h
                      img=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Pic10.png")
                      l100=Label(image = img)
                      l100.image=img
                      l100.place(x = 600, y = 70)
                      messagebox.showinfo("Congratulations!", "You have guessed the word right!")
                      if g[0] == 1:
                       if leveln == 3:
                           r = 100
                       else:
                           r = 10   
                       chancesr1 = chancesvar*r
                       if chancesr1 != 0:
                         chancesr1 -= (h*5)
                       v1 = int(v)
                       print(type(v1))
                       minutes,seconds = divmod(v1,60)
                       if seconds < 10:
                         timems1 = "0"+str(minutes) + ":"+ "0" +str(seconds)
                       else:
                         timems1 = "0"+str(minutes) + ":"+str(seconds)
                       g[0] = 2
                       window.destroy()
                       window2 = Tk()
                       window2.configure(bg='ivory4')
                       window2.geometry("1920x1080")
                       window2.title("Hangman")

                       #Inserting Background
                       C = Canvas(window2, bg="blue", height=250, width=300)
                       filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Background2d.png")
                       background_label = Label(window2, image=filename)
                       background_label.place(x=0, y=0, relwidth=1, relheight=1)
                       C.place()
                       ims = PhotoImage(file=r"C:/Users/John Linus/Pictures/Hangman pics/clicktocontinue.png")
                       startbutton1 = Button(window2,image = ims,command=starta,bg = "lime green")
                       startbutton1.place(x=450,y=330)
                       window2.mainloop()
                      
                       
                      else:
                       # Creating a connection to the database to store the results of the particular user
                       con =  mycon.connect(host = "localhost", user = "root", password = "jlm!sql1308D")
                       mycursor = con.cursor()
                       mycursor.execute("use Hangman")
                       mycursor.execute("select count(PID) from history;")
                       data = mycursor.fetchall()
                       j1 = 0
                       j2 = 0
                       if leveln == 3:
                           r = 100
                       else:
                           r = 10
                       for i in data:
                           j1 = i
                           for u in j1:
                               j2 = u

                       #player_2 score        
                       chancesr2 = chancesvar*r
                       if chancesr2 != 0:
                         chancesr2 -= (h*5)
                       v2 = v
                       minutes,seconds = divmod(v2,60)
                       if seconds < 10:
                         timems2 = "0"+str(minutes)+ ":"+ "0" +str(seconds)
                       else:
                         timems2 = "0"+str(minutes) + ":"+str(seconds)  
                       sql = "insert into history (PID,P,S,C,G) values (%s,%s,%s,%s,%s)"
                       val = [(str(j2+1),user1,str(chancesr1),timems1,level),
                              (str(j2+2),user2,str(chancesr2),timems2,level)
                             ]
                       mycursor.executemany(sql,val)
                       con.commit()
                       con.close()   
                       m = 1
                       g[0]=3
                       
                       window.destroy()
                       root1= Tk()
                       root1.geometry("1920x1080")
                       root1.title("Hangman")
                       C = Canvas(root1, bg="blue", height=250, width=300)
                       filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Background2d.png")
                       background_label = Label(root1, image=filename)
                       background_label.image=img
                       background_label.place(x=0, y=0, relwidth=1, relheight=1)
                       C.place()
                       score1 = str(chancesr1)
                       score2 = str(chancesr2)
                       img1=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\result.png")
                       l10=Label(root1,image = img1,bg = "lime green")
                       l10.place(x=440,y=50)
                       labelf = Label(root1,width=21,height=9,text="\n"+user1.title()+"\n\n"+"Word : "+word+"\n\n"+"Points : "+score1+"\n\n"+"Time left : "+timems1,font=("Lucida Console","20","bold"),bg = "yellow" , fg = "black",pady = 10)
                       labelf.place(x=410,y=150)
                       labelf = Label(root1,width=21,height=9,text="\n"+user2.title()+"\n\n"+"Word : "+word2+"\n\n"+"Points : "+score2+"\n\n"+"Time left : "+timems2,font=("Lucida Console","20","bold"),bg = "yellow" , fg = "black",pady = 10)
                       labelf.place(x=790,y=150)

                       img = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\return to main menu.png")
                       startbutton1 = Button(root1,image = img,bg = "white",command = realstart)
                       startbutton1.image=img
                       startbutton1.place(x=575,y=720)
                       if (chancesr2)>(chancesr1):
                           txt = "Congratulations"+" "+user2.title()+"\n\nYou have won the game!"
                       elif (chancesr2) == (chancesr1):
                            txt = "Uh oh looks like it is a draw "
                       else:
                            txt="Congratulations"+" "+user1.title()+"\n\n You have won the game!"
                       labelf=Label(root1,width=45,height=4,text=txt,font=("Lucida Console","20","bold"),bg = "yellow" , fg = "black")
                       labelf.place(x=410,y=460)
                       root.mainloop()
                       
       
        def but():
            miscbutton.play()
            messagebox.showinfo("MAIN HINT","\""+hint1r+"\"")
        imgh = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\Hintbutton.png")
        hintbutton = Button(window,image=imgh,bg ="lime green",command=but)
        hintbutton.image = imgh
        hintbutton.place(x = 40 , y = 720)
            
        label1=Button(window,text=" NO. OF ERRORS LEFT :"+str(chancesvar),font = ("Lucidia Console","13","bold"),bg = "DeepSkyBlue2",fg = "white")
        label1.place(x = 637 , y = 737)
        
             
        img=PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Pic1.png")
        l101=Label(window,image = img)
        l101.image=img
        l101.place(x = 600, y = 70)
        imgj = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\seperator.png")
        labelsep = Label(window,image = imgj,bg = "Yellow")
        labelsep.image = imgj
        labelsep.place(x=350,y=465)
        #First row of buttons
        btn1 = Button(window, text="Q",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("Q"))
        btn1.place(x = 450, y = 500)
        btn2 = Button(window, text="W",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("W"))
        btn2.place(x = 510, y = 500)
        btn3 = Button(window, text="E",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("E"))
        btn3.place(x = 570, y = 500)
        btn4 = Button(window, text="R",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("R"))
        btn4.place(x = 630, y = 500)
        btn5 = Button(window, text="T",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("T"))
        btn5.place(x = 690, y = 500)
        btn6 = Button(window, text="Y",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("Y"))
        btn6.place(x = 750, y = 500)
        btn7 = Button(window, text="U",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("U"))
        btn7.place(x = 810, y = 500)
        btn8 = Button(window, text="I",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("I"))
        btn8.place(x = 870, y = 500)
        btn9 = Button(window, text="O",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("O"))
        btn9.place(x = 930, y = 500)
        btn10 = Button(window, text="P",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("P"))
        btn10.place(x = 990, y = 500)

        #Second row
        btn11= Button(window, text="A",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("A"))
        btn11.place(x = 480, y = 555)
        btn12 = Button(window, text="S",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("S"))
        btn12.place(x = 540, y = 555)
        btn13 = Button(window, text="D",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("D"))
        btn13.place(x = 600, y = 555)
        btn14 = Button(window, text="F",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("F"))
        btn14.place(x = 660, y = 555)
        btn15= Button(window, text="G",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("G"))
        btn15.place(x = 720, y = 555)
        btn16 = Button(window, text="H",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("H"))
        btn16.place(x = 780, y = 555)
        btn17 = Button(window, text="J",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("J"))
        btn17.place(x = 840, y = 555)
        btn18 = Button(window, text="K",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("K"))
        btn18.place(x = 900, y = 555)
        btn19 = Button(window, text="L",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("L"))
        btn19.place(x = 960, y = 555)

        #Third row of buttons
        btn20 = Button(window, text="Z",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("Z"))
        btn20.place(x = 540, y = 610)
        btn21= Button(window, text="X",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("X"))
        btn21.place(x = 600, y = 610)
        btn22 = Button(window, text="C",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("C"))
        btn22.place(x = 660, y = 610)
        btn23 = Button(window, text="V",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("V"))
        btn23.place(x = 720, y = 610)
        btn24 = Button(window, text="B",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("B"))
        btn24.place(x = 780, y = 610)
        btn25 = Button(window, text="N",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("N"))
        btn25.place(x = 840, y = 610)
        btn26 = Button(window, text="M",bg="snow", fg="navy",width=3,height=1,font=('TImes New Roman','20','bold'),command=lambda: clicked("M"))
        btn26.place(x = 900, y = 610)

        #Fourth row
        btn27 = Button(window,text="SPACE",bg="snow", fg="navy",width = 18,height = 1,font=("TImes New Roman",'20','bold'),command=lambda:clicked(" "))
        btn27.place(x =600,y=665)
     #button to start the game
        #######
     imgs = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\yes.png")
     imgl = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\ready2.png")
     labels = Label(window,image=imgl,bg ="lime green")
     labels.place(x=450,y=280)
     startbutton = Button(window,image = imgs,bg = "royal blue",command = start)
     m=1
     startbutton.place(x=690,y=360)
     window.mainloop()
 starta()
 

root= Tk()
root.geometry("1920x1080")
root.title("Hangman")
C = Canvas(root, bg="blue", height=250, width=300)
filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Background2d.png")
background_label = Label(root, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.place()
ims = PhotoImage(file=r"C:\Users\John Linus\Pictures\Hangman pics\startgame.png")
klm = 0
startbutton1 = Button(root,image = ims,command=realstart,bg = "lime green")
startbutton1.place(x=450,y=330)
root.mainloop()
