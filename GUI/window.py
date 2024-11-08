import tkinter
import customtkinter as ctk

class main_window():
    def __init__(self):
        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("blue" ) 

        app = ctk.CTk()  # create CTk window like you do with the Tk window
        app.title("Automatizador")
        app.geometry("800x900")

        tabview = ctk.CTkTabview(master=app,width=750,height=850,fg_color='#242424')
        tabview.pack(padx=1, pady=1)
        tab1=tabview.add("Seleccion")  # add tab at the end
        tabview.set("Seleccion")  # set currently visible tab

        font = ctk.CTkFont(family="Helvetica", size=13,weight='bold')
        label1=ctk.CTkLabel(master=tab1, text="Selecciona la carpeta a utilizar por cada cliente",text_color="#bf5e72",font=font)
        label1.place(relx=0.05,rely=0.05)
        y=0.1
        yb=0.12
        self.directories=[]
        self.buttons=[]
        clientes=['AEXA','CAVAZOS','LEO','PELUSQUI','TICARSA','TRANSLIQUIDOS']
        count=0
        for i in clientes:
            ctk.CTkLabel(master=tab1, text=i,text_color="#83a16d",font=font).place(relx=0.02,rely=y)
            self.directories.append(ctk.CTkEntry(master=tab1,width=450,height=30))
            self.directories[count].place(relx=0.18,rely=y)

            self.buttons.append(ctk.CTkButton(master=tab1, text="Seleccionar", width=100, height=35,text_color="#242424",fg_color='#dfe0dc',hover=False,
                                              command=lambda:self.button_function(count)))
            self.buttons[count].place(relx=0.9, rely=yb, anchor=tkinter.CENTER)
            y+=0.1*.5
            yb+=0.12*.42
            count+=1
        
        path=''
        with open("configs/config.txt","r") as file:
            aux=file.readlines()
            for lin in aux:
                if "[OUTPUT]" in lin:
                    path=lin.replace("[OUTPUT]=",'').replace("\n",'')
                    break
        
        ctk.CTkLabel(master=tab1, text='RESUMEN',text_color="#bf5e72",font=font).place(relx=0.45,rely=yb)
        self.process=ctk.CTkFrame(master=tab1, width=650, height=300,fg_color='#dfe0dc' )
        self.process.place(relx=0.05,rely=yb+0.12*.42)

        self.out=ctk.CTkLabel(master=tab1, text=f'Carpeta destino: {path}',font=font)
        self.out.place(relx=0.05,rely=0.91)

        self.buttons.append(ctk.CTkButton(master=tab1, text="Cambiar ruta Salida", width=100, height=35,fg_color='#8b8b94',hover=False,command=lambda:self.button_function(count)))
        self.buttons[count].place(relx=0.7, rely=0.93, anchor=tkinter.CENTER)

        self.buttons.append(ctk.CTkButton(master=tab1, text="Iniciar", width=100, height=35,fg_color='#83a16d',hover=False,command=lambda:self.start()))
        self.buttons[count+1].place(relx=0.9, rely=0.93, anchor=tkinter.CENTER)

        self.status=ctk.CTkLabel(master=app, text="Aplicacion iniciada correctamente.",width=800,height=30,fg_color="#153f59",
                               corner_radius=8)
        self.status.place(relx=0,rely=0.97)

        app.mainloop()

    def button_function(self,n):
        print(n)
        '''from pathlib import Path
        from tkinter import filedialog
        print(n)
        folder = filedialog.askdirectory()
        if folder:
            self.status.configure(text=f"Carpeta {folder} seleccionada")
            self.directories[n].insert(-1, folder)
        else:
            self.status.configure(text="No se ha seleccionado ningún archivo.")
'''
    def start(self):
        print("Started process")