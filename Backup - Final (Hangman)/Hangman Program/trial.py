from tkinter import *
import pygame,time
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
buttonboi = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\buttonsound.wav")
miscbutton = pygame.mixer.Sound(r"C:\Users\John Linus\Pictures\Hangman pics\miscbutton.wav")
def trial():
    Main = Tk()
    Main.geometry("1920x1080")
    Main.title("Tutorial")
    C = Canvas(Main,bg="blue",height = 250,width=300)
    filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Backgroundblur.png")
    background_label = Label(Main, image=filename)
    background_label.image = filename
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place()
    
    def previous():
        miscbutton.play()
        global limit
        print(limit)
        img3 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Nextb.png")
        if limit==1:
            return
        elif limit == 2:
            L2.place_forget()
            L1.place(x = 100,y =40)
            limit = 1
            B2.configure(image = BA)
            B1.configure(image = BB)

        elif limit == 3:
            L3.place_forget()
            L2.place(x = 100,y =40)
            limit = 2
            B3.configure(image = BA)
            B2.configure(image = BB)
            
        elif limit == 4:
            L4.place_forget()
            L3.place(x = 100,y =40)
            limit = 3
            B4.configure(image = BA)
            B3.configure(image = BB)
                
        if limit == 5:
            L5.place_forget()
            L4.place(x = 100,y =40)
            button2.configure(text = "Next")
            limit = 4
            B5.configure(image = BA)
            B4.configure(image = BB)
            button2.configure(image = img1)
            button2.image = img1
        return

    print(1)
    def next():
        miscbutton.play()
        img3 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Nextb.png")
        global limit   
        if limit == 1:
            L1.place_forget()
            L2.place(x = 100,y =40)
            print("oh")
            limit=2
            B1.configure(image = BA)
            B2.configure(image = BB)
        elif limit == 2:
            L2.place_forget()
            L3.place(x = 100,y =40)
            print("hello")
            limit=3
            B2.configure(image = BA)
            B3.configure(image = BB)
        elif limit == 3:
            L3.place_forget()
            L4.place(x = 100,y =40)
            print("hi")
            limit = 4
            B3.configure(image = BA)
            B4.configure(image = BB)
        elif limit == 4:
            print("hehe")
            L4.place_forget()
            L5.place(x = 100,y =40)
            limit = 5
            B4.configure(image = BA)
            B5.configure(image = BB)
            button2.configure(image = img3)
            button2.image = img3
        elif limit == 5: 
            Main.destroy()
        return

    LA = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\trial1.png")
    LB = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\trial2.png")
    LC = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\trial3.png")
    LD = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\trial4.png")
    LE = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\trial5.png")

    BA = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\blank1.png")
    BB = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\blank2.png")
    global limit
    limit = 1

    L1 = Label(Main,image = LA,bg = "grey")
    L1.image = LA
    L2 = Label(Main,image = LB,bg = "grey")
    L2.image = LB
    L3 = Label(Main,image = LC,bg = "grey")
    L3.image = LC
    L4 = Label(Main,image = LD,bg = "grey")
    L4.image = LD
    L5 = Label(Main,image = LE,bg = "grey")
    L5.image = LE
    L1.place(x = 100,y =40)

    B1 = Label(Main,image = BB)
    B2 = Label(Main,image = BA)
    B3 = Label(Main,image = BA)
    B4 = Label(Main,image = BA)
    B5 = Label(Main,image = BA)

    B1.place(x = 660,y =750)
    B2.place(x = 700,y =750)
    B3.place(x = 740,y =750)
    B4.place(x = 780,y =750)
    B5.place(x = 820,y =750)


    img1 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Nexta.png")
    img2 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\previous.png")
    button1 = Button(Main,image = img2,bg = "deep sky blue",command = previous)
    button1.image = img2
    button1.place(x = 13,y = 330)
    button2 = Button(Main,image = img1,bg = "deep sky blue",command = next)
    button2.image = img1
    button2.place(x=1470,y = 330)
    Main.mainloop()

def ask():
    Main1 = Tk()
    Main1.geometry("1920x1080")
    Main1.title("Tutorial")
    C = Canvas(Main1,bg="blue",height = 250,width=300)
    filename = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Backgroundblur.png")
    background_label = Label(Main1, image=filename)
    background_label.image = filename
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.place()
    img11 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Tutuorial.png")
    Lab = Label(Main1,image = img11)
    Lab.image = img11
    Lab.place(x=450,y=230)
    def go():
        buttonboi.play()
        But.place_forget()
        But1.place_forget()
        Lab.place_forget()
        Main1.destroy()
        trial()   
        return
    def no():
        buttonboi.play()
        Main1.destroy()
        return
    img12 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\Yes2.png")
    img13 = PhotoImage(file = r"C:\Users\John Linus\Pictures\Hangman pics\no.png")
    But = Button(Main1,image = img12,command = go)
    But.image = img12
    But1 = Button(Main1,image = img13,command = no)
    But1.image = img13
    But.place(x=640,y=360)
    But1.place(x=640,y=430)
    Main1.mainloop()
