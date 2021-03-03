#Importation des modules
import tkinter
from tkinter import *
import tkinter.font as tkFont
from tkinter.ttk import *
from PIL import Image, ImageTk 


#Création + personalisation de la fenetre


window = Tk()
window.geometry("700x500")
window.title("SurfaceApp")
window.iconbitmap("ico.ico")
window.config(bg="white")
#Création de police

font = tkFont.Font(family='Rockwell Extra Bold', size=15, weight='bold')
triangle_img = PhotoImage(file = "triangle_ac.png")
carre_img = PhotoImage(file = "carre_ac.png")
cercle_img = PhotoImage(file = "cercle_ac.png")
losange_img = PhotoImage(file = "losange_ac.png")
rectangle_img = PhotoImage(file = "rectangle_ac.png")
trapeze_img = PhotoImage(file = "trapeze_ac.png")

image_triangle = Image.open("triangle.png" ) 
photo_triangle = ImageTk.PhotoImage(image_triangle)

image_carre = Image.open("carre.png") 
photo_carre = ImageTk.PhotoImage(image_carre)

image_cercle = Image.open("cercle.png") 
photo_cercle = ImageTk.PhotoImage(image_cercle)

image_losange = Image.open("losange.png") 
photo_losange = ImageTk.PhotoImage(image_losange)

image_rectangle = Image.open("rectangle.png") 
photo_rectangle = ImageTk.PhotoImage(image_rectangle)

image_trapeze = Image.open("trapeze.png") 
photo_trapeze = ImageTk.PhotoImage(image_trapeze)

image_triangle_formule = Image.open("formule_triangle.png")
photo_triangle_formule = ImageTk.PhotoImage(image_triangle_formule)

image_trapeze_formule = Image.open("formule_trapeze.png")
photo_trapeze_formule = ImageTk.PhotoImage(image_trapeze_formule)

image_carre_formule = Image.open("formule_carre.png")
photo_carre_formule = ImageTk.PhotoImage(image_carre_formule)

image_cercle_formule = Image.open("formule_cercle.png")
photo_cercle_formule = ImageTk.PhotoImage(image_cercle_formule)

image_rectangle_formule = Image.open("formule_rectangle.png")
photo_rectangle_formule = ImageTk.PhotoImage(image_rectangle_formule)

image_losange_formule = Image.open("formule_losange.png")
photo_losange_formule = ImageTk.PhotoImage(image_losange_formule)

s = Style()
s.configure('My.TFrame', background='white')


def initiale():
    
        
    def back():
        for widget in window.winfo_children():
            widget.destroy()
        window.update()
        initiale()
    Frame_Top = Frame(window,style='My.TFrame')
    Frame_Top.pack(side=TOP)

    Frame_Middle = Frame(window, relief = SUNKEN)
    Frame_Middle.pack(expand=YES)


    texte = Label(Frame_Top, text="Welcome to the SurfaceApp", font=font, background="white" )
    texte.pack()

    def triangle():
        def calcule():
            f = int(e1.get())
            f2 = int(e2.get())
            z = (f*f2)/2
            e = Label(window, text=str(z))
            e.pack(expand=YES)
            e.after(1000, e.destroy) 
        for i in window.winfo_children():
            i.destroy()
        F_calcule = Frame(window,style='My.TFrame')
        F_calcule.place(x=500,y=400)
        b = Button(window, text="Back",command=back)
        b.pack(anchor=N+W, fill=X)
        canvas = Canvas(window, width = image_triangle.size[0], height = image_triangle.size[1]) 
        canvas.create_image(0,0, anchor =NW, image=photo_triangle)
        canvas.pack(anchor=N)
        formule =  Canvas(window, width = image_triangle_formule.size[0], height = image_triangle_formule.size[1])
        formule.create_image(0,0, anchor =NW, image=photo_triangle_formule)
        formule.place(x=0,y=400)
        l1 = Label(F_calcule, text="Base :")
        l2 = Label(F_calcule,text="Hauteur:")
        e1 = Entry(F_calcule)
        e2 = Entry(F_calcule)
        b2 = Button(F_calcule, text="Calculer", command=calcule)
        l1.grid(column = 1, row= 1)
        l2.grid(column = 1, row = 2)
        e1.grid(column = 2,row = 1)
        e2.grid(column=2,row=2)
        b2.grid(column=2,row=3)        

    def carre():
        def calcule():
            f = int(e1.get())
            z = f*f
            e = Label(window, text=str(z))
            e.pack(expand=YES)
            e.after(1000, e.destroy) 
        for c in window.winfo_children():
            c.destroy()
        F_calcule = Frame(window,style='My.TFrame')
        F_calcule.place(x=500,y=400)
        b = Button(window, text="Back",command=back)
        b.pack(anchor=N+W, fill=X)
        canvas = Canvas(window, width = image_carre.size[0], height = image_carre.size[1]) 
        canvas.create_image(0,0, anchor =NW, image=photo_carre)
        canvas.pack(anchor=N)
        formule =  Canvas(window, width = image_carre_formule.size[0], height = image_carre_formule.size[1])
        formule.create_image(0,0, anchor =NW, image=photo_carre_formule)
        formule.place(x=0,y=400)
        l1 = Label(F_calcule, text="Coté :")
        l2 = Label(F_calcule,text="Coté:")
        e1 = Entry(F_calcule)
        e2 = Entry(F_calcule)
        b2 = Button(F_calcule, text="Calculer",command=calcule)
        l1.grid(column = 1, row= 1)
        l2.grid(column = 1, row = 2)
        e1.grid(column = 2,row = 1)
        e2.grid(column=2,row=2)
        b2.grid(column=2,row=3)

    def cercle():
        def calcule():
            f = int(e1.get())
            z = 2*3.141592*f*f
            e = Label(window, text=str(z))
            e.pack(expand=YES)
            e.after(1000, e.destroy)   
        for c in window.winfo_children():
            c.destroy()
        F_calcule = Frame(window,style='My.TFrame')
        F_calcule.place(x=500,y=400)
        b = Button(window, text="Back",command=back)
        b.pack(anchor=N+W, fill=X)
        canvas = Canvas(window, width = image_cercle.size[0], height = image_cercle.size[1]) 
        canvas.create_image(0,0, anchor =NW, image=photo_cercle)
        canvas.pack(anchor=N)
        formule =  Canvas(window, width = image_cercle_formule.size[0], height = image_cercle_formule.size[1])
        formule.create_image(0,0, anchor =NW, image=photo_cercle_formule)
        formule.place(x=0,y=400)
        l1 = Label(F_calcule, text="Rayon :")
        e1 = Entry(F_calcule)
        b2 = Button(F_calcule, text="Calculer", command=calcule)
        l1.grid(column = 1, row= 1)
        e1.grid(column = 2,row = 1)
        b2.grid(column=2,row=2)

    def losange():
        def calcule():
            f = int(e1.get())
            f2 = int(e2.get())
            z = f*f2
            e = Label(window, text=str(z))
            e.pack(expand=YES)
            e.after(1000, e.destroy) 
        for c in window.winfo_children():
            c.destroy()
        F_calcule = Frame(window,style='My.TFrame')
        F_calcule.place(x=500,y=400)
        b = Button(window, text="Back",command=back)
        b.pack(anchor=N+W, fill=X) 
        canvas = Canvas(window, width = image_losange.size[0], height = image_losange.size[1]) 
        canvas.create_image(0,0, anchor =NW, image=photo_losange)
        canvas.pack(anchor=N)
        formule =  Canvas(window, width = image_losange_formule.size[0], height = image_losange_formule.size[1])
        formule.create_image(0,0, anchor =NW, image=photo_losange_formule)
        formule.place(x=0,y=400)
        l1 = Label(F_calcule, text="Base :")
        l2 = Label(F_calcule,text="Hauteur:")
        e1 = Entry(F_calcule)
        e2 = Entry(F_calcule)
        b2 = Button(F_calcule, text="Calculer", command=calcule)
        l1.grid(column = 1, row= 1)
        l2.grid(column = 1, row = 2)
        e1.grid(column = 2,row = 1)
        e2.grid(column=2,row=2)
        b2.grid(column=2,row=3)

    def rectangle():
        def calcule():
            f = int(e1.get())
            f2 = int(e2.get())
            z = f*f2
            e = Label(window, text=str(z))
            e.pack(expand=YES)
            e.after(1000, e.destroy) 
        for c in window.winfo_children():
            c.destroy()
        F_calcule = Frame(window,style='My.TFrame')
        F_calcule.place(x=500,y=400)
        b = Button(window, text="Back",command=back)
        b.pack(anchor=N+W, fill=X)
        canvas = Canvas(window, width = 170, height = 99) 
        canvas.create_image(0,0, anchor =N+W, image=photo_rectangle)
        canvas.pack(anchor=N)
        formule =  Canvas(window, width = image_rectangle_formule.size[0], height = image_rectangle_formule.size[1])
        formule.create_image(0,0, anchor =NW, image=photo_rectangle_formule)
        formule.place(x=0,y=400)
        l1 = Label(F_calcule, text="Largeur :")
        l2 = Label(F_calcule,text="Longeur:")
        e1 = Entry(F_calcule)
        e2 = Entry(F_calcule)
        b2 = Button(F_calcule, text="Calculer", command=calcule)
        l1.grid(column = 1, row= 1)
        l2.grid(column = 1, row = 2)
        e1.grid(column = 2,row = 1)
        e2.grid(column=2,row=2)
        b2.grid(column=2,row=3)

    def trapeze():
        def calcule():
            f = int(e1.get())
            f2 = int(e2.get())
            f3 = int(e3.get())
            z = ((f+f2)/2)*f3
            e = Label(window, text=str(z))
            e.pack(expand=YES)
            e.after(1000, e.destroy) 
        for c in window.winfo_children():
            c.destroy()
        F_calcule = Frame(window,style='My.TFrame')
        F_calcule.place(x=500,y=400)
        b = Button(window, text="Back",command=back)
        b.pack(anchor=N+W, fill=X)
        canvas = Canvas(window, width = image_trapeze.size[0], height = image_trapeze.size[1]) 
        canvas.create_image(0,0, anchor =NW, image=photo_trapeze)
        canvas.pack(anchor=N)
        formule =  Canvas(window, width = image_trapeze_formule.size[0], height = image_trapeze_formule.size[1])
        formule.create_image(0,0, anchor =NW, image=photo_trapeze_formule)
        formule.place(x=0,y=400)
        l1 = Label(F_calcule, text="Petite Base :")
        l2 = Label(F_calcule,text="Grande Base :")
        l3 = Label(F_calcule,text="Hauteur : ")
        e1 = Entry(F_calcule)
        e2 = Entry(F_calcule)
        e3 = Entry(F_calcule)
        b2 = Button(F_calcule, text="Calculer",command=calcule)
        l1.grid(column = 1, row= 1)
        l2.grid(column = 1, row = 2)
        l3.grid(column= 1, row = 3)
        e1.grid(column = 2,row = 1)
        e2.grid(column=2,row=2)
        e3.grid(column=2,row=3)
        b2.grid(column=2,row=4)



    triangle = Button(Frame_Middle, image=triangle_img, command=triangle)
    carre = Button(Frame_Middle, image=carre_img, command=carre)
    cercle = Button(Frame_Middle, image=cercle_img, command=cercle)
    losange = Button(Frame_Middle, image=losange_img, command=losange)
    rectangle = Button(Frame_Middle, image=rectangle_img, command=rectangle)
    trapeze = Button(Frame_Middle, image=trapeze_img, command=trapeze)

    triangle.grid(column=0,row=0)
    carre.grid(column=1,row=0)
    cercle.grid(column=2,row=0)
    losange.grid(column=3,row=0)
    rectangle.grid(column=4,row=0)
    trapeze.grid(column=5,row=0)










#On lance la fenetre
initiale() 
window.mainloop()
