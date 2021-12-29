# Lector-de-Codigo-de-Barras
Pequeño programita para leer el código de barras de un pdf y renombrar el archivo

### Es un pequeño script para leer el codigo de barras de un pdf y que lo renombre al pdf con su numero extraido del codigo de barras.

_Ya que los pdf son nombrados por un scanner que los crea al digitalizarlos y le pone como nombre la fecha y un numero consecutivo..._

![Image text](https://github.com/Javier-I-Morales/Lector_de_codigos/blob/main/Lector_de_codigos/Imagenes/Interfaz.png)


La ubicación del codigo de barras esta seteado en el mismo dependiendo de la necesidad y utilizando las coordenadas X e Y...

```
codigo = imagen[413:461, 421:583]
```

![image text](https://github.com/Javier-I-Morales/Lector_de_codigos/blob/main/Lector_de_codigos/Imagenes/Interfaz%20antes%20del%20proceso.png)

![Image text](https://github.com/Javier-I-Morales/Lector_de_codigos/blob/main/Lector_de_codigos/Imagenes/Interfaz%20procesando.png)

![Image text](https://github.com/Javier-I-Morales/Lector_de_codigos/blob/main/Lector_de_codigos/Imagenes/Interfaz%20proceso%20terminado.png)
