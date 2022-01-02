# Lector-de-Codigo-de-Barras

### Es un pequeño script para leer el codigo de barras de un pdf y que lo renombre al pdf con su numero extraido del codigo de barras.

_(Ya que los pdf son nombrados por un scanner que los crea al digitalizarlos y le pone como nombre la fecha y un numero consecutivo...)_

## El principio y el final del proceso seria lo siguiente:

![Image text](https://github.com/Javier-I-Morales/Lector-de-Codigo-de-Barras/blob/main/Lector_de_codigos/Imagenes/uno.png) ![Image text](https://github.com/Javier-I-Morales/Lector-de-Codigo-de-Barras/blob/main/Lector_de_codigos/Imagenes/dos.png)

- - -

# La interfaz al iniciar se ve así:

![Image text](https://github.com/Javier-I-Morales/Lector-de-Codigo-de-Barras/blob/main/Lector_de_codigos/Imagenes/Interfaz.png)


La ubicación del codigo de barras esta seteado en el mismo dependiendo de la necesidad y utilizando las coordenadas X e Y...

```
codigo = imagen[413:461, 421:583]
```
_Más o menos seria algo así: _

![image text](https://github.com/Javier-I-Morales/Lector-de-Codigo-de-Barras/blob/main/Lector_de_codigos/Imagenes/imagen%20codigo.png)

### Elegimos las carpetas donde estan los pdf y donde se depositaran los resultados

![Image text](https://github.com/Javier-I-Morales/Lector-de-Codigo-de-Barras/blob/main/Lector_de_codigos/Imagenes/menu_carpetas.png)

### Una vez elegida la carpeta con los doc el boton se puede accionar para empezar el proceso

![image text](https://github.com/Javier-I-Morales/Lector-de-Codigo-de-Barras/blob/main/Lector_de_codigos/Imagenes/Interfaz%20antes%20del%20proceso.png)

### Mientras va renombrando nos va mostrando la cantidad de archivos renombrados y los que faltan renombrar

![Image text](https://github.com/Javier-I-Morales/Lector-de-Codigo-de-Barras/blob/main/Lector_de_codigos/Imagenes/Interfaz%20procesando.png)

### Terminado el proceso nos muestra los resultados

![Image text](https://github.com/Javier-I-Morales/Lector-de-Codigo-de-Barras/blob/main/Lector_de_codigos/Imagenes/Interfaz%20proceso%20terminado.png)

