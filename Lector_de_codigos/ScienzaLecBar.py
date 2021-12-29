import tkinter as tk
from Lector_de_codigos.Lector import lector
from threading import Thread
from tkinter import filedialog as fd
from tkinter import messagebox as mg
import os


lector_codigo = lector()


def carpeta_origen():

    lector_codigo.documentos_sin_renombrar=fd.askdirectory(title='Seleccione Origen')
    label_cantidad_archivos['text']=len(os.listdir(lector_codigo.documentos_sin_renombrar))
    archivo = open('origen.txt','w')
    archivo.write(lector_codigo.documentos_sin_renombrar)
    archivo.close()
    revisa_cantidad()


def carpeta_destino():
    lector_codigo.documentos_renombrados = fd.askdirectory(title='Seleccione Destino')
    label_cantidad_renombrados['text']=len(os.listdir(lector_codigo.documentos_renombrados))
    archivo = open('destino.txt', 'w')
    archivo.write(lector_codigo.documentos_renombrados)
    archivo.close()
    revisa_cantidad()


def acerca():
    mg.showinfo(title='Acerca de', message='Aqui un mensaje...!')


raiz = tk.Tk()
raiz.title("Renombrador")
raiz.resizable(False,False)


def proceso():
    lector_codigo.leer()
    label_estado_modo['text'] = "Fin del Proceso"
    label_cantidad_renombrados['text'] = lector_codigo.renombrados()
    label_cantidad_errores['text'] = lector_codigo.errores()


def mostrar_renombrados():
    label_cantidad_renombrados['text'] = lector_codigo.renombrados()
    label_cantidad_errores['text'] = lector_codigo.errores()
    label_cantidad_renombrados.after(500, mostrar_renombrados)


def ejecutar():
    label_boton.config(state='disabled')
    label_estado_modo['text'] = 'Procesando '
    raiz.update_idletasks()
    hilo.start()
    label_cantidad_renombrados.after(0, mostrar_renombrados)


frame = tk.Frame(raiz, bg="#2C3E50")
frame.pack()

barra_menu = tk.Menu(raiz)
raiz.config(menu=barra_menu)


boton_menu=tk.Menu(barra_menu, tearoff=0, bg='#5D6D7E')
boton_ayuda=tk.Menu(barra_menu, tearoff=0, bg='#5D6D7E')
boton_menu.add_command(label='Carpeta Origen', command=carpeta_origen)
boton_menu.add_command(label='Carpeta Destino', command=carpeta_destino)
boton_ayuda.add_command(label='Ayuda', command=acerca)
barra_menu.add_cascade(label='Menu', menu=boton_menu)
barra_menu.add_cascade(label='Acerca', menu=boton_ayuda)


label_espacio1 = tk.Label(frame)
label_espacio1.pack()
label_espacio1.config(background="#2C3E50")

frame_elementos = tk.Frame(frame, bg="#5D6D7E", width=800, height=62, padx=100, pady=20)
frame_elementos.pack()
frame_elementos.grid_propagate(False)


label_cantidad_archivos_titulo = tk.Label(frame_elementos, text='Cantidad de archivos:', font=(20), bg="#5D6D7E", fg='#ECF0F1')
label_cantidad_archivos_titulo.grid(row=1, column=0, padx=10)


label_cantidad_archivos = tk.Label(frame_elementos, text=lector_codigo.cantidad_para_renombrar, font=(20), bg="#5D6D7E", fg='#ECF0F1')
label_cantidad_archivos.grid(row=1, column=1)


label_espacio2 = tk.Label(frame_elementos, bg="#5D6D7E", width=30)
label_espacio2.grid(row=1, column=2)


label_estado_titulo = tk.Label(frame_elementos, text='Estado: ', font=(20), bg="#5D6D7E", fg='#ECF0F1')
label_estado_titulo.grid(row=1, column=3)


label_estado_modo = tk.Label(frame_elementos, text="Sin Procesar", font=(20), bg="#5D6D7E", fg='#ECF0F1')
label_estado_modo.grid(row=1, column=4)


label_espacio3 = tk.Label(frame, bg="#2C3E50")
label_espacio3.pack()

frame_boton = tk.Frame(frame)
frame_boton.pack()
label_boton = tk.Button(frame_boton, text="RENOMBRAR", command= ejecutar, bg="#95A5A6")
label_boton.pack()


label_espacio4 = tk.Label(frame, bg="#2C3E50")
label_espacio4.pack()


frame_elementos_2 = tk.Frame(frame, padx=210, bg="#34495E")
frame_elementos_2.pack()


label_cantidad_renombrados_titulo = tk.Label(frame_elementos_2, text='Archivos Renombrados:     ', font=(25), fg='#ECF0F1', bg="#34495E")
label_cantidad_renombrados_titulo.grid(row=3, column=0, padx=30, pady=25)

label_cantidad_renombrados = tk.Label(frame_elementos_2, text = lector_codigo.cantidad_renombrados, font=(25),fg='#ECF0F1', bg="#34495E")
label_cantidad_renombrados.grid(row=3, column=1, padx=30, pady=25)

label_cantidad_errores_titulo = tk.Label(frame_elementos_2, text = 'Archivos sin Renombrar:     ', font=(25), fg='#ECF0F1', bg="#34495E")
label_cantidad_errores_titulo.grid(row=4, column=0, padx=30, pady=25)

label_cantidad_errores = tk.Label(frame_elementos_2, text = lector_codigo.cantidad_sin_renombrar, font=(25), fg='#ECF0F1', bg="#34495E")
label_cantidad_errores.grid(row=4, column=1, padx=30, pady=25)

label_espacio5 = tk.Label(frame, bg="#2C3E50")
label_espacio5.pack()


def revisa_cantidad():
    try:
        origen = open('origen.txt','r')
        destino = open('destino.txt','r')
        lector_codigo.documentos_sin_renombrar = origen.read()
        lector_codigo.documentos_renombrados = destino.read()
        origen.close()
        destino.close()
        if lector_codigo.documentos_sin_renombrar != '' :
            label_cantidad_archivos['text'] = len(os.listdir(lector_codigo.documentos_sin_renombrar))
        if label_cantidad_archivos['text'] == 0:
            label_boton.config(state='disabled')
            carpeta_origen()
        elif  lector_codigo.documentos_renombrados == '' or lector_codigo.documentos_renombrados == lector_codigo.documentos_sin_renombrar:
            carpeta_destino()
        else:
            label_boton.config(state='normal')

    except FileNotFoundError:
        origen = open('origen.txt', 'w')
        destino = open('destino.txt', 'w')
        origen.close()
        destino.close()

    except:
        mg.showinfo(title='Info', message='La aplicación se cerrara')
        raiz.destroy()


hilo = Thread(target=proceso)

revisa_cantidad()


raiz.mainloop()


