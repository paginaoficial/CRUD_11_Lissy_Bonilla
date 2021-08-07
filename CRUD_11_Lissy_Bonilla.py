from tkinter import *
from tkinter import ttk

from mysql.connector import cursor
import demo_database

window = Tk()
window.geometry("370x570")
frame_app = Frame(window, width=1200, height=600, )
window.title('TransferCloud')
my_table = ttk.Treeview(window)
frame_app.pack()




# Inicializando las variables para almacenar lo que escriba el usuario en las cajas de Texto (Entry)
cuenta = IntVar()
nombre = StringVar()
monto = IntVar()


def crear_registro():
# Creando función "agregar_sala()", función que se ejecuta la dar clic en el botón "Agregar"
# Obteniendo los valores de los widgets Entry mediante la función "GET()" 
    # y almacenandolos en las variables previamente inicializadas
    cuenta = entry_nombre.get()
    nombre = entry_edad.get()
    monto = entry_apellido.get()
    
    
    # creando un objeto de la Base de datos "MyDatabase", para acceder a la función "insert_db"
    db_demo = demo_database.MyDatabase()
    # ejecutando la función "insert_db" y enviando las variables como parámetros
    db_demo.insert_db(cuenta, nombre, monto)




import mysql.connector
connection =mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="db_demo")

cursor = connection.cursor()
cursor.execute("SELECT CUENTA ,NOMBRE, MONTO  FROM TBL_USUARIOS")


     
    
    
my_table = ttk.Treeview(window)
    

registro=0
for fila in cursor:
    registro=registro+1
    print(str(registro) + "-"+str(fila))
      
    cuenta = fila[0]
    nombre = fila[1]
    monto = fila[2]
    
    my_table.insert(parent="", index="end", iid=registro, text=str(registro),
        values=(cuenta, nombre, monto))
connection.close() 


        # Define Our Columns 
my_table['columns'] = ('CUENTA', 'NOMBRE', 'MONTO')

        # Formate Our Columns
my_table.column('#0', width=10, minwidth=50)
my_table.column('CUENTA', anchor=W, width=85)
my_table.column('NOMBRE', anchor=W, width=130)
my_table.column('MONTO', anchor=W, width=120)


        # Create Headings
my_table.heading('CUENTA', text='#CUENTA', anchor=W)
my_table.heading('NOMBRE', text='NOMBRE', anchor=W)
my_table.heading('MONTO', text='MONTO ', anchor=W)


        # Pack to the screen
my_table.place(x=10, y=330)


# Widgets dentro del contender OPTIONS
frame_form = Frame(window, width=350, height=300, bg="#0384fc")
frame_form.place(x=10, y=20)
label_nombre = Label(frame_form, 
              text="N° DE CUENTA:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#0384fc")
label_nombre.place(x=30, y=30)
entry_nombre = Entry(frame_form, justify=LEFT, width=25, 
             font=("Century Gothic", "14"))
entry_nombre.place(x=30, y=70)

label_edad = Label(frame_form, 
              text="NOMBRE:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#0384fc")
label_edad.place(x=30, y=100)
entry_edad = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_edad.place(x=30, y=140)

label_apellido = Label(frame_form, 
              text="MONTO A INGRESAR:",
              font=("Century Gothic", "20", "bold"),
              fg="white",
              bg="#0384fc")
label_apellido.place(x=30, y=170)
entry_apellido = Entry(frame_form, justify=LEFT, width=25, 
                font=("Century Gothic", "14"))
entry_apellido.place(x=30, y=210)


button_agregar = Button(frame_form, text="REGISTRAR", 
                        font=("Century Gothic", "14", "bold"),
                        command=crear_registro)
button_agregar.place(x=110, y=250)

window.mainloop()
