import os
import time
import fitz
import cv2
from pyzbar.pyzbar import decode
import shutil
from ctypes import *



class lector:

    def __init__(self):

        self.cantidad_para_renombrar = 0
        self.cantidad_renombrados = 0
        self.cantidad_sin_renombrar = 0
        self.documentos_renombrados = None
        self.documentos_sin_renombrar = None

    def renombrados(self):
        return len(os.listdir(self.documentos_renombrados))

    def errores(self):
        return len(os.listdir(self.documentos_sin_renombrar))

    def leer(self):

        documentos = os.listdir(self.documentos_sin_renombrar)

        for doc in documentos:

            try:

                documento = fitz.open(self.documentos_sin_renombrar + '/' + doc)
                pagina = documento.load_page(0)
                trans = fitz.Matrix(2.0, 2.0)
                foto = pagina.get_pixmap(matrix=trans, alpha=False)
                foto.save('informe.png')
                imagen = cv2.imread('../Lector_de_codigos/informe.png')
                codigo = imagen[413:461, 421:583]
                codigo_mas_grande = cv2.resize(codigo, dsize=(300, 180), interpolation=cv2.INTER_CUBIC)
                ret, imagen_mejorada = cv2.threshold(codigo_mas_grande, 127, 255, cv2.THRESH_BINARY)

                datos = decode(imagen_mejorada)

                for barcode in datos:
                    codigo = barcode.data.decode("UTF8")

                print(codigo)
                documento.close()
                shutil.move(self.documentos_sin_renombrar + '/' + doc,
                            self.documentos_renombrados + '/' + codigo + '.pdf')

            except:
                print("no se pudo modificar el nombre del archivo: " + doc)

