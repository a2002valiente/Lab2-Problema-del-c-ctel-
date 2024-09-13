---
editor_options: 
  markdown: 
    wrap: 72
---

------------------------------------------------------------------------

# ***LABORATORIO 2 : Problema del cóctel***

------------------------------------------------------------------------

Procesamiento digital de señales

Carolina Corredor BMED B\
UMNG

------------------------------------------------------------------------

> **OBJETIVO** : Aplicar el análisis en frecuencia de señales de voz en
> un problema de captura de señales mezcladas.

------------------------------------------------------------------------

**Descripción** : Se nos planea la siguiente situacion :

> > En un evento tipo coctel, se instalaron varios micrófonos para
> > escuchar lo que las personas estaban hablando; una vez terminó la
> > fiesta, se solicitó a los ingenieros que entregaran el audio de la
> > voz de uno de los participantes. Los ingenieros analizaron las
> > señales grabadas por los micrófonos eran mezclas de señales que
> > provenían de diferentes fuentes (personas) para todos los casos y se
> > encontraron con el problema de aislar la voz de interés. El problema
> > de la "fiesta de cóctel" se refiere a la capacidad de un sistema
> > para concentrarse en una sola fuente sonora mientras filtra las
> > demás en un entorno con múltiples emisores de sonido. Este problema
> > es común en sistemas de audición tanto humanos como artificiales, y
> > su resolución es esencial en aplicaciones como la mejora de la voz,
> > el reconocimiento de habla y la cancelación de ruido. Para este
> > laboratorio se nos pide recrear esta situación donde se utilizaron 3
> > celulares que hacian como micrófonos estos deben estar ubicados de
> > manera que cada uno capture diferentes combinaciones de las señales
> > provenientes de las tres fuentes, las 3 personas se encontrarán en
> > posiciones fijas dentro de la sala de laboratorio. Deben estar
> > localizados a distancias diferentes y orientados en distintas
> > direcciones para simular un entorno de “fiesta de cóctel”

Acontinuación se muestra la ubicación de las personas y dónde se
colocaron los micrófonos

![ESCENARIO](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/16e65a8e803746225eb4d7982b1b483d5951b6e3/ESCENARIO.jpeg)

Para capturar estas señales los 3 participantes hablarán al mismo tiempo
pero cada uno diciendo una frase distinta siendo asi captadas por los
micrófonos para después ser procesadas y guardadas en el programa de
spyder en lenguaje de phyton para ser analizadas. Se nos pide lo
siguiente para este laboratorio :

-Calcular el SNR de cada una de las señales y graficarlas.

-Realizar un análisis temporal y espectral de las señales capturadas por
cada micrófono, identificando las características principales de cada
fuente sonora. Para realizar el análisis espectral, se recomienda
utilizar la transformada de Fourier discreta (DFT) o la transformada
rápida de Fourier (FFT), describiendo la información que se puede
obtener con cada una de ellas.

-Investigar los métodos de separación de fuentes, como el Análisis de
Componentes Independientes (ICA), el Beamforming, entre otros, para
aislar la señal de interés a partir de las señales capturadas por los
micrófonos.

#### ***INSTRUCCIONES***

1.  Como se explico anteriormente se grabo en la sala del laboratorio
    insonorizada acomodandonos de forma estrategica: -la primera fuente
    del ruido ambiente se encuentra en la mitad de la sala,la segunda
    fuente (persona1) esta paralela a la fuente 1 ubicada un metro y
    medio de esta , el microfono 1 esta 50 cm de la persona 1 con una
    orientacón de 90 grados justo detras de la persona 1 -la tecera
    fuente (persona2)esta ubicada a un metro de la fuente 1 con una
    orientación de 30 grados detras del microfono 2 a una distancia de
    70 cm de la persona 2 -la cuarta fuente (persona3) esta ubicada a
    dos metros de la fuente 1 en una orientación de 140 grados a un
    lateral del microfono 3 a una distancia de 50 cm.

Esto se hizo con el objetivo de poder grabar las frases durante 10
segundos para despues recortarlas y dejarlas todas en el mismo tiempo de
inicio

2.  Para subirlas al programa debimos convertir los audios a formato wav
    para que sean leidos y los entienda el programa los llamamos con la
    funcion "wavfile.read".

-   Se importan las librerias correspondientes.

-   Se suben las 3 señales y el ruido blanco

-   Se genera un vector de tiempo

-   Se grafican los ruidos blancos

Se crearon arreglos para poder definir el tiempo maximo que dura la
señal de captura de las 3 señales realizando la operacion de longitud
total del vector cantidad de muestras sobre frecuencia,la frecuencia de
muestreo que se utilizo fue 48000 Hz cumpliendo con el teorema de
Nyquist ya que la precepción audible de una persona es de 20000 Hz

````         
```         

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import  wavfile
from scipy.fft import fft
from scipy.signal import stft, istft
from sklearn.decomposition import FastICA
from scipy.signal import butter, lfilter
from sklearn.decomposition import FastICA
from sklearn.decomposition import FastICA

######################### RUIDOS AMBIENTE #########################
######################### RUIDO AMBIENTE 1 #########################

fsA1, dataA1 = wavfile.read('A1.wav') #Se extraen los datos del audio en dos arreglos 
amb1=fsA1, dataA1 #Se asigna una variable a los arreglos extraidos para poder manipularlos
n1=len(dataA1) #Se asigna una variable de la longitud total del arreglo para calculos posteriores
tmax= len(dataA1)/fsA1 #Se calcula el tiempo en segundos para el eje x
t= np.linspace(0, tmax,len(dataA1)) # Se crea un arreglo de valores uniformes con las dimensiones de nuestros datos

plt.figure(1) #Asignacion de espacio para la primera grafica 
plt.plot(t,dataA1,'purple', label= 'ruido ambiente ') #Generamos la grafica de los datos en funcion del tiempo
plt.grid(True)#Agregamos una cuadricula para visualizar de mejor manera
plt.xlabel('tiempo [s]') # asignamos nombre a los ejes con su respectiva unidad 
plt.ylabel('amplitud [mV]')
plt.title('Ruido Ambiente 1') # Damos un titulo a nuestra grafica
plt.legend (loc = 'upper right') #Asignamos la ubicacion de la leyenda dentro de la grafica
plt.ylim(-5000,5000) #Damos limites en el eje y para mejor visualizacion 
plt.show () #mostramos la grafica 


######################### RUIDO AMBIENTE 2 #########################

fsA2, dataA2 = wavfile.read('A2.wav')  #Se extraen los datos del audio en dos arreglos 
amb2=fsA2, dataA2 #Se asigna una variable a los arreglos extraidos para poder manipularlos
n2=len(dataA2) #Se asigna una variable de la longitud total del arreglo para calculos posteriores
tmax2=len(dataA2)/fsA2 #Se calcula el tiempo en segundos para el eje x
t2=np.linspace(0,tmax2,len(dataA2)) #Se crea un arreglo de valores uniformes con las dimensiones de nuestros datos

# SE REALIZA EL MISMO PROCEDIMIENTO DE LA FIGURA 1 PERO CON LOS VALORES DEL SEGUNDO MICROFONO
plt.figure(2)
plt.plot(t2,dataA2,'purple', label= 'ruido ambiente')
plt.grid(True)
plt.xlabel('tiempo [s]')
plt.ylabel('amplitud [mV]')
plt.title('Ruido Ambiente 2')
plt.legend (loc = 'upper right')
plt.ylim(-5000,5000)
plt.show ()

######################### RUIDO AMBIENTE 3 #########################

fsA3, dataA3 = wavfile.read('A3.wav')#Se extraen los datos del audio en dos arreglos 
amb3=fsA3, dataA3 #Se asigna una variable a los arreglos extraidos para poder manipularlos
n3=len(dataA3) #Se asigna una variable de la longitud total del arreglo para calculos posteriores
tmax3=len(dataA3)/fsA3  #Se calcula el tiempo en segundos para el eje x
t3=np.linspace(0,tmax3,len(dataA3))  #Se crea un arreglo de valores uniformes con las dimensiones de nuestros datos

# SE REALIZA EL MISMO PROCEDIMIENTO DE LA FIGURA 1 PERO CON LOS VALORES DEL TERCER MICROFONO
plt.figure(3)
plt.plot(t3,dataA3,'purple', label= 'ruido ambiente')
plt.grid(True)
plt.xlabel('tiempo [s]')
plt.ylabel('amplitud [mV]')
plt.title('Ruido Ambiente 3')
plt.legend (loc = 'upper right')
plt.ylim(-5000,5000)
plt.show ()
```
````

![RUIDO BLANCO
1](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/16e65a8e803746225eb4d7982b1b483d5951b6e3/RUIDO%20AMBIENTE%201.png)

![RUIDO BLANCO
2](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/16e65a8e803746225eb4d7982b1b483d5951b6e3/RUIDO%20AMBIENTE%202.png)

![RUIDO BLANCO
3](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/16e65a8e803746225eb4d7982b1b483d5951b6e3/RUIDO%20AMBIENTE%203.png)

-Acontinuacón se muestra el código para graficar las señales

```         

######################### SEÑALES #########################


fsS1, dataS1 = wavfile.read('R1.wav') # Se extraen los datos de cada audio
fsS2, dataS2 = wavfile.read('R2.wav') # Se extraen los datos de cada audio
fsS3, dataS3 = wavfile.read('R3.wav') # Se extraen los datos de cada audio

Senal1=fsS1, dataS1 # Se asigna los datos a un arreglo 
Senal2=fsS2, dataS2 # Se asigna los datos a un arreglo 
Senal3=fsS3, dataS3 # Se asigna los datos a un arreglo 
tempaux1 = dataS1/5 # Se crea un arreglo temporal para calculos posteriores
tempaux2 = dataS2/7 # Se crea un arreglo temporal para calculos posteriores
tempaux3 = dataS3/6 # Se crea un arreglo temporal para calculos posteriores

######################### GRAFICAS #########################

tmaxS1=len(dataS1)/fsS1 #Se calcula el tiempo en segundos para el eje x
tS1=np.linspace(0,tmaxS1,len(dataS1)) #Se crea un arreglo de valores uniformes con las dimensiones de nuestros datos

# SE REALIZA EL MISMO PROCEDIMIENTO DE LA FIGURA 1 PERO CON LOS VALORES DEL PRIMER MICROFONO DE LA SEÑAL
plt.figure(4)
plt.plot(tS1, dataS1,'green', label= 'Señal microfono 1')
plt.grid(True)
plt.xlabel('tiempo [s]')
plt.ylabel('amplitud [mV]')
plt.title('Señal 1')
plt.legend (loc = 'upper right')
plt.show ()

tmaxS2=len(dataS2)/fsS2 #Se calcula el tiempo en segundos para el eje x
tS2=np.linspace(0,tmaxS2,len(dataS2)) #Se crea un arreglo de valores uniformes con las dimensiones de nuestros datos

# SE REALIZA EL MISMO PROCEDIMIENTO DE LA FIGURA 1 PERO CON LOS VALORES DEL SEGUNDO MICROFONO DE LA SEÑAL
plt.figure(5)
plt.plot(tS2, dataS2,'green', label= 'Señal microfono 2 ')
plt.grid(True)
plt.xlabel('tiempo [s]')
plt.ylabel('amplitud [mV]')
plt.title('Señal 2')
plt.legend (loc = 'upper right')
plt.show ()

tmaxS3=len(dataS3)/fsS3 #Se calcula el tiempo en segundos para el eje x
tS3=np.linspace(0,tmaxS3,len(dataS3))#Se crea un arreglo de valores uniformes con las dimensiones de nuestros datos

# SE REALIZA EL MISMO PROCEDIMIENTO DE LA FIGURA 1 PERO CON LOS VALORES DEL TERCER MICROFONO DE LA SEÑAL
plt.figure(6)
plt.plot(tS3, dataS3,'green', label= 'Señal microfono 3')
plt.grid(True)
plt.xlabel('tiempo [s]')
plt.ylabel('amplitud [mV]')
plt.title('Señal 3')
plt.legend (loc = 'upper right')
plt.show ()

    
```

![SEÑAL
1](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/16e65a8e803746225eb4d7982b1b483d5951b6e3/SE%C3%91AL%201.png)

![SEÑAL
2](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/16e65a8e803746225eb4d7982b1b483d5951b6e3/SE%C3%91AL%202.png)

![SEÑAL
3](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/16e65a8e803746225eb4d7982b1b483d5951b6e3/SE%C3%91AL%203.png)

3.  Utilizamos una función para poder encontrar la potencia del ruido
    blanco y de la señal para asi calcular los SNR de las señales,que es
    una medida que compara la potencia de una señal deseada con la
    potencia del ruido de fondo. Se expresa generalmente en decibelios
    (dB) y se utiliza para evaluar la calidad de una señal de
    transmisión,si el SNR es positivo quiere decir que la señal es mas
    grande que el ruido (mayor información) y es negativo el ruido es
    mas grande que la señal (menor informacíon)

```         
   ######################### CALCULOS DE POTENCIA Y SNR #########################


# Calculamos la potencia del ruido (A1) y de la señal (S1)
potencia_A1 = np.sum(np.abs(dataA1**2)) / len(dataA1) #Realizamos la sumatoria 
#de los valores al cuadrado del vector y dividimos por la longitud del arreglo
potencia_S1 = np.sum(np.abs(tempaux1**2)) / len(dataS1)
snr_A1_S1 = 10 * np.log10(potencia_S1 / potencia_A1) # Calculamos el SNR (en dB)
print(f"SNR (A1/R1): {snr_A1_S1:.2f} dB") # Imprimimos el resusltado

#////////////////////////////////////////////////////////////////////////////#

# Calcular la potencia promedio del ruido (A2) y de la señal (S2)
potencia_A2 = np.sum(np.abs(dataA2**2)) / len(dataA2) #Realizamos la sumatoria 
#de los valores al cuadrado del vector y dividimos por la longitud del arreglo
potencia_S2 = np.sum(np.abs(tempaux2**2)) / len(dataS2)
snr_A2_S2 = 10 * np.log10(potencia_S2 / potencia_A2)# Calcular el SNR (en dB)
print(f"SNR (A2/R2): {snr_A2_S2:.2f} dB") # Imprimimos el resusltado

#////////////////////////////////////////////////////////////////////////////#

# Calcular la potencia promedio del ruido (A3) y de la señal (R3)
potencia_A3 = np.sum(np.abs(dataA3**2)) / len(dataA3)#Realizamos la sumatoria 
#de los valores al cuadrado del vector y dividimos por la longitud del arreglo
potencia_S3 = np.sum(np.abs(tempaux3**2)) / len(dataS3)
snr_A3_S3 = 10 * np.log10(potencia_S3 / potencia_A3)# Calcular el SNR (en dB)
print(f"SNR (A3/R3): {snr_A3_S3:.2f} dB") # Imprimimos el resusltado
    
```

> > -   En este caso como se puede observar en la imagen los SNR que
> >     hallamos tienen un valor positivo en las 3 señales con lo que
> >     podemos concluir que tiene una mejor calidad de transmisión o
> >     comunicación, ya que sera mas clara y con menos interferencias
> >     aunque los valores no son tan altos esto puede decir que la
> >     señal es detectable pero tiene una cantidad significativa de
> >     ruido presente

![SNR](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/16e65a8e803746225eb4d7982b1b483d5951b6e3/CALCULOS%20SNR.png)

> **PRIMERRA TOMA** \> Cuando se realizo el ejercicio pedido en el
> laboratorio los datos que obtuvimos no fueron los mejores ya que el
> SNR que arrojo de las señales fueron negativos y bajitos lo que nos
> indica que hay mayor ruido que señal siendo asi una señal debil con
> mucha interferencia. Esto pudo suceder por muchos factores como el
> nivel del ruido blanco ya que esto dificulto debido al tono de voz que
> se manejo fue mas leve y la ubicación en la que se encontraron los
> microfonos.

![SNR PRIMERA
TOMA](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/snr1.png)

> > Debido a esto se volvieron a tomar los datos en el la sala
> > insonorizada del laboratorio dandonos esta ves SNR mejores para
> > poder analizarlos con lo pedido en la guia.

4.  Para hallar el espectro de la frecuencia en cada una de nuestras
    señales y ruidos blancos fue necesaria la aplicación de la
    transformada rápida de Fourier ( FFT), la cual es una herramienta
    matemática que permite descomponer la señal deseada en componentes
    individuales de frecuencia, es decir pasar nuestra señales a el
    dominio de la frecuencia del dominio temporal en el que se
    encontraba, la cual nos ayudara a saber que frecuencias están
    presentes en cada una de nuestras señales y con que intensidad.

En cada uno de los 6 espectros de las señales graficamos solo la mitad
positiva del espectro esto debido a que el espectro de la FFT de una
señal es real simétrica, y por ello evitamos la redundancia del mismo,
por otro lado en el eje x observaremos la frecuencia en (Hz) además
utilizamos la función plt.semilogx() con el fin de hacer que el eje X
sea logarítmico para poder visualizar mejor los espectros de las
señales, y el eje y donde se encuentra la amplitud (mV) es lineal.

```         

######################### TRANSFORMADA RAPIDA DE FOURIER #########################

yf = fft(dataA1) #Utilizamos la funcion fft de la libreria SciPy para calcular la transformada
#rapida de fourier de la señal ruido mic 1 para un representacion en el dominio de la frecuencia 
xf = np.fft.fftfreq(n1, 1/fsA1) #Generamos un array de los valores de frecuencia 
# correspondientes a los coeficientes calculados por la FFT.

# GENERAMOS LA GRAFICA CON LOS PASOS DE LA FIGURA 1 TENIENDO EN CUENTA QUE EL EJE X SE REPRESENTA SEMILOG

plt.figure(7)
plt.plot(xf[:n1//2], np.abs(yf[:n1//2]),'orange',label = 'Domino frecuencia ruido 1')  # Solo la mitad positiva del espectro
plt.grid (True)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [mV]')
plt.legend (loc = 'upper left')
plt.title('Ruido 1 - Dominio de la Frecuencia')
plt.semilogx()

yf = fft(dataA2) #Utilizamos la funcion fft de la libreria SciPy para calcular la transformada
#rapida de fourier de la señal ruido mic 2 para un representacion en el dominio de la frecuencia 
xf = np.fft.fftfreq(n1, 1/fsA2)#Generamos un array de los valores de frecuencia 
# correspondientes a los coeficientes calculados por la FFT.
# GENERAMOS LA GRAFICA CON LOS PASOS DE LA FIGURA 1 TENIENDO EN CUENTA QUE EL EJE X SE REPRESENTA SEMILOG
plt.figure(8)
plt.plot(xf[:n1//2], np.abs(yf[:n1//2]),'orange',label = 'Domino frecuencia ruido 2')  # Solo la mitad positiva del espectro
plt.grid (True)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [mV]')
plt.legend (loc = 'upper left')
plt.title('Ruido 2 - Dominio de la Frecuencia')
plt.semilogx()

yf = fft(dataA3)#Utilizamos la funcion fft de la libreria SciPy para calcular la transformada
#rapida de fourier de la señal ruido mic3 para un representacion en el dominio de la frecuencia 
xf = np.fft.fftfreq(n1, 1/fsA3)#Generamos un array de los valores de frecuencia 
# correspondientes a los coeficientes calculados por la FFT.
# GENERAMOS LA GRAFICA CON LOS PASOS DE LA FIGURA 1 TENIENDO EN CUENTA QUE EL EJE X SE REPRESENTA SEMILOG
plt.figure(9)
plt.plot(xf[:n1//2], np.abs(yf[:n1//2]),'orange',label = 'Domino frecuencia ruido 3')  # Solo la mitad positiva del espectro
plt.grid (True)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud[mV]')
plt.legend (loc = 'upper left')
plt.title('Ruido 3- Dominio de la Frecuencia')
plt.semilogx()

#/////////////////////////////////////// FFT PARA SEÑALES /////////////////////////////////////#

yf = fft(dataS1)#Utilizamos la funcion fft de la libreria SciPy para calcular la transformada
#rapida de fourier de la señal del microfono 1 para un representacion en el dominio de la frecuencia 
xf = np.fft.fftfreq(n1, 1/fsS1)#Generamos un array de los valores de frecuencia 
# correspondientes a los coeficientes calculados por la FFT.
# GENERAMOS LA GRAFICA CON LOS PASOS DE LA FIGURA 1 TENIENDO EN CUENTA QUE EL EJE X SE REPRESENTA SEMILOG
plt.figure(10)
plt.plot(xf[:n1//2], np.abs(yf[:n1//2]),label = 'Domino frecuencia señal 1')  # Solo la mitad positiva del espectro
plt.grid (True)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [mV]')
plt.legend (loc = 'upper left')
plt.title('Señal 1 - Dominio de la Frecuencia')
plt.semilogx()


yf = fft(dataS2)#Utilizamos la funcion fft de la libreria SciPy para calcular la transformada
#rapida de fourier de la señal del microfono 2 para un representacion en el dominio de la frecuencia 
xf = np.fft.fftfreq(n1, 1/fsS2)#Generamos un array de los valores de frecuencia 
# correspondientes a los coeficientes calculados por la FFT.
# GENERAMOS LA GRAFICA CON LOS PASOS DE LA FIGURA 1 TENIENDO EN CUENTA QUE EL EJE X SE REPRESENTA SEMILOG
plt.figure(11)
plt.plot(xf[:n1//2], np.abs(yf[:n1//2]),label = 'Domino frecuencia señal 2')  # Solo la mitad positiva del espectro
plt.grid (True)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [mV]')
plt.legend (loc = 'upper left')
plt.title('Señal 2 - Dominio de la Frecuencia')
plt.semilogx()



yf = fft(dataS3)#Utilizamos la funcion fft de la libreria SciPy para calcular la transformada
#rapida de fourier de la señal del microfono 3 para un representacion en el dominio de la frecuencia 
xf = np.fft.fftfreq(n1, 1/fsS3) #Generamos un array de los valores de frecuencia 
# correspondientes a los coeficientes calculados por la FFT.
# GENERAMOS LA GRAFICA CON LOS PASOS DE LA FIGURA 1 TENIENDO EN CUENTA QUE EL EJE X SE REPRESENTA SEMILOG
plt.figure(12)
plt.plot(xf[:n1//2], np.abs(yf[:n1//2]),label = 'Domino frecuencia señal 3')  # Solo la mitad positiva del espectro
plt.grid (True)
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Amplitud [mV]')
plt.legend (loc = 'upper left')
plt.title('Señal 3 - Dominio de la Frecuencia')
plt.semilogx()
```

![ESPECTRO
1](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/R1%20DOMINIO%20F.png)

Para la primer grafica de frecuencia espectral del ruido blanco (A1),
podemos observar como el espectro presenta una mayor concentración de
energía en las frecuencias mas altas las cuales están por encima de los
1000 Hz aproximadamente; además se observan picos pronunciados en
frecuencias especificas lo que nos indica componentes armónicos en la
señal propios de las características de la fuente de ruido ósea el ruido
blanco que en este caso fue la música, por otro lado vemos como el ruido
se extiende a lo largo de un amplio rango de frecuencias desde los 0,1
Hz hasta los 10.000 Hz esto nos refleja que el ruido proviene de
múltiples fuentes. Al igual que la primer grafica de ruido la segunda y
tercera presenta características similares, como su concentración de
energía por encima de los 100 Hz lo que sugiere el ruido de la música,
aunque en la segunda y tercer grafica se observa cada vez mas como su
amplitud aumenta lo que indica un nivel de ruido extremadamente
significativo en ciertas frecuencias.

![ESPECTRO
2](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/R2%20DOMINIO%20F.png)

![ESPECTRO
3](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/R3%20DOMINIO%20F.png)

![ESPECTRO
4](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/S1%20DOMINIO%20F.png)

Para la primer grafica del espectro de la señal se observa mucha más
concentración de energía en las frecuencias altas por encima de los 100
Hz indicando como siseos o chasquidos o diversas interferencias, también
se observan diversos picos armónicos lo que corresponden a componentes
de frecuencias muy específicos que podrían ser los armónicos de las
voces o características del ruido, además su energía se enfoca en la
región de altas frecuencias, lo cual nos dificulta su debida separación
de señales. De la misma manera que las graficas del espectro de la señal
dos y tres se observan las dominancias en altas frecuencias sus picos y
su amplio rango de frecuencias.

![ESPECTRO
5](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/S2%20DOMINIO%20F.png)

![ESPECTRO
6](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/S3%20DOMINIO%20F.png)

5.  Se realizo la separación de los tres audios, que son las 3 señales
    de nuestro informe, para iniciar con el procesamiento de la señal se
    aseguran las tres señales para que contengan la misma longitud con
    el fin de realizar las debidas operaciones matemáticas en la técnica
    del ICA, para iniciar con la separación de la señal es necesario
    crear una matriz donde cada fila representa una señal de un
    micrófono para facilitar el procesamiento posterior de la aplicación
    ICA. El método ICA es una técnica estadística que busca encontrar un
    conjunto de componentes estadísticamente independientes a partir de
    observaciones multivariadas, es decir que intenta descomponer una
    señal compleja en sus componentes individuales, asumiendo que las
    componentes seleccionadas sean lo más independientes entre sí, al
    aplicar FastICA se busca separar las fuentes independientes a partir
    de la mezcla observadas en los micrófonos con el objetivo de
    recuperar la señal fuente, posteriormente se calcula la energía de
    cada componente separada y encuentra la componente con mayor energía
    que corresponde a la señal de interés (la música de fondo). Por otra
    parte, seleccionamos la componente con mayor energía la cual estamos
    considerando como la señal de interés para normalizarla y evitar
    distorsiones al guardar nuestra señal en el archivo WAV de 16 bits,
    luego se aplica un filtro pasa alto a la señal , ya que este sistema
    modifica la amplitud y/o la fase de las diferentes componentes de
    frecuencia de una señal con el objetivo de mejorar la calidad de la
    señal, es decir que atenuamos las frecuencias bajas de la señal como
    ruido y mantener las frecuencias altas correspondientes a la voz
    para mejorar su calidad resultando en una señal más clara y nítida.
    Por ultimo se guardo la señal resultante en un nuevo archivo WAV
    para realizar el cálculo de las métricas de calidad para cuantificar
    el desempeño de la separación.

-Se muestra el codigo que se empleo para poder extraer el audio.

```         
###################################### EXTRACCION DEL AUDIO  ###############################


# Leemos las señales de los tres micrófonos asginando variables diferentes 
fs1, mic1 = wavfile.read('R1.wav') # Microfono 1
fs2, mic2 = wavfile.read('R2.wav') # Microfono 2
fs3, mic3 = wavfile.read('R3.wav') # Microfono 3

# Aseguramos que las señales sean de igual longitud
min_length = min(len(mic1), len(mic2), len(mic3))
mic1 = mic1[:min_length]
mic2 = mic2[:min_length]
mic3 = mic3[:min_length]

# Creamos una matriz con las señales de los tres micrófonos
signals = np.vstack([mic1, mic2, mic3])

# Aplicar ICA para separar las señales independientes
ica = FastICA(n_components=3, random_state=0) #Con la funcion FastIca de la libreria scikit-learn,
#realizamos la descomposicion en componentes independientes, especificando el numero de microfonos
fuentes_separadas = ica.fit_transform(signals.T).T #ajustamos el modelo ICA a 
# los datos transpuestos y transforma los datos de entrada en las fuentes independientes

# Evaluamos la energía de cada componente para seleccionar la más prominente
energia = np.sum(fuentes_separadas **2, axis=1)
predominante = np.argmax(energia) #devolvemos el índice del valor máximo en el arreglo energia. 
# Esto indica cuál de las componentes independientes tiene la mayor energía.

# Seleccionar la componente con mayor energía
fuente_predominante = fuentes_separadas [predominante]

# Normalizamos la señal resultante para evitar sobrepasar el rango de valores permitidos
fuente_predominante = np.int16(fuente_predominante / np.max(np.abs(fuente_predominante)) * 32767)

# Aplicamos un filtro pasa-altos para atenuar frecuencias no deseadas
def filtro_pasa_altos(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='high', analog=False)
    y = lfilter(b, a, data)
    return y

# Configuramos los parámetros del filtro 
frecuencia_corte = 4700  # Frecuencia de corte en Hz
senal_extraida = filtro_pasa_altos (fuente_predominante, frecuencia_corte, fs1)

# Normalizar la señal filtrada
senal_extraida = np.int16(senal_extraida / np.max(np.abs(senal_extraida)) * 32767)

# Guardar la señal resultante
wavfile.write('output_filtered_ica.wav', fs1, senal_extraida) 

# UNA VEZ LA SEÑAL EXTRAIDA ESTA EN UNA VARIABLE PROCEDEMOS A GRAFICAR COMO EN LA FIGURA 1
print("Separación de fuentes y filtrado completo usando ICA. Archivo guardado como 'output_filtered_ica.wav'.")
tmaxfil= len(senal_extraida)/fs1
tfil= np.linspace(0, tmaxfil,len(senal_extraida))

plt.figure(13)
plt.plot (tfil, senal_extraida,'brown', label = 'Señal audio extraido' )
plt.grid (True)
plt.legend (loc = 'upper left')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud [mV]')
plt.title('Señal extraccion de audio')
plt.show
```

![SEÑAL
EXTRAIDA](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/SE%C3%91AL%20EXTRAIDA.png)

6.Para aplicar las métricas de calidad a la señal extraída empezamos a
aplicar el SNR a la señal calculando la potencia de la señal extraída y
la potencia de la señal del audio de la tercer señal, obteniendo así
mismo la intensidad de la señal extraída , para posteriormente realizar
el calculo del SNR que nos indica que tan fuerte es la señal
deseada(extraída) en comparación con el ruido, por ultimo obtuvimos un
valor de -10,92, lo que nos esta indicando un SNR bajo es decir que la
señal extraída es difícil de entender o analizar puesto que la señal
origen tres es mas grande que la señal extraída.

```         
######################## COMPARACION ################################

# SE REALIZAN METRICAS DE CALIDAD PARA COMPARAR LA SEÑAL EXTRAIDA DE LA SEÑAL ORIGINAL
print ("METRICAS DE CALIDAD PARA COMPARAR LA SEÑAL EXTRAIDA CON LAS SEÑALES ORIGINALES")
print ("\n")
print("CALCULO DEL SNR")
# Calcular la potencia promedio de la señal (S3) y de la señal extraida (E1)
pote_filtro = np.sum(np.abs(senal_extraida)**2) / len(senal_extraida)
# Calcular el SNR (en dB)
snr_S3_F1 = 10 * np.log10(pote_filtro / potencia_S3) # aplicamos la formula de snr 
print(f"SNR (F1/S3): {snr_S3_F1:.2f} dB")

print ("\n")
print("CALCULO DEL ECM (Error cuadratico medio)")

# se calcula el error cuadratico medio 
datarecortado = dataS3 [:384000] # acortamos el arreglo data S3 para poder realizar el calculo
ecm = np.mean ((datarecortado-senal_extraida)**2) # aplicamos la formula de error cuadratico
print ("El error cuadratico medio es:",ecm) # imprimimos el resultado

print ("\n")
print("CALCULO DEL THD (Tasa de distorsion total)")
# se calcula la tasa de distorision total
distor_envol = np.abs (senal_extraida - datarecortado) # se ejecuta la formula de THD 
thd = np.sqrt (np.mean(distor_envol**2)) - np.sqrt (np.mean(datarecortado**2))
print ("La tasa de distorsion total es:",thd) # imrpimimos el resultado 


#GRAFICAMOS LA SEÑAL ORIGINAL SOBREPUESTA EN LA SEÑAL EXTRAIDA A FIN DE COMPARAR ASIGNANDO COLORES 
# Y DIMENSIONES CORRECTAS, SIGUIENDO LOS PASOS DE LA FIGURA 1
plt.figure(14)
plt.plot (tS3, dataS3,'green', label= 'Señal original') # generamos grafica de la señal original
plt.plot (tfil, senal_extraida, 'brown', label = 'Señal audio extraido')# generamos grafica de la señal extraida
plt.grid ( True)
plt.xlabel ('Tiempo [s]')
plt.ylabel('Amplitud [mV]')
plt.title ('COMPARACION SEÑAL EXTRAIDA CON AUDIO ORIGINAL')
plt.legend(loc = 'upper left')
plt.show

#GRFICAMOS LA SEÑAL EXTRAIDA SOBREPUESTA DEL RUIDO AMBIENTE A FIN DE COMPARAR LOS DATOS DE FILTRADO
plt.figure(15)
plt.plot (t3, dataA3,'purple', label= 'Ruido ambiente') #graficamos el ruido ambiente
plt.plot (tfil, senal_extraida, 'brown', label = 'Señal audio extraido') # grficamos la señal extraida 
plt.grid (True)
plt.xlabel ('Tiempo [s]')
plt.ylabel('Amplitud [mV]')
plt.title ('COMPARACION SEÑAL EXTRAIDA CON RUIDO AMBIENTE')
plt.legend(loc = 'upper left')
plt.show
```

Se grafica la señal original sobrepuesta en la señal extraída con el fin
de compararlas y del mismo modo se grafica la señal extraída sobrepuesta
del ruido ambiente

> > Para la primer grafica podemos observar que ambas señales presentan
> > una forma de onda similar, con picos y valles que coinciden en gran
> > medida. Esto sugiere que la señal extraída conserva las
> > características generales de la señal original, además Las
> > amplitudes máximas y mínimas de ambas señales se encuentran en un
> > rango similar, lo que indica que la señal extraída no ha
> > experimentado grandes cambios en su nivel de energía. Aunque La
> > señal original parece tener más detalle y variaciones en la amplitud
> > en comparación con la señal extraída. Esto podría indicar una
> > pérdida de información durante el proceso de extracción, como la
> > eliminación de altas frecuencias.

![SEÑAL EXTRAIDA SOBREPUESTA DE LA SEÑAL
ORIGINAL](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/COMPARACION%20SE%20Y%20S3.png)

> > Ya para la segunda grafica podemos observar ambas señales presentan
> > un rango de amplitud similar, lo que sugiere que la señal extraída
> > no se desvía significativamente del nivel de energía del ruido
> > ambiente, además tanto el ruido ambiente como la señal extraída
> > muestran fluctuaciones aleatorias en la amplitud, lo que es
> > característico de señales ruidosas. Aunque El ruido ambiente parece
> > tener un patrón más aleatorio y menos estructurado en comparación
> > con la señal extraída. La señal extraída podría mostrar algunos
> > patrones o características que sugieren la presencia de una señal
> > subyacente, aunque débil.

![SEÑAL EXTRAIDA SOBREPUESTA DEL RUIDO
BLANCO](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/COMPARACION%20SE%20Y%20A3.png)

![CALCULO DEL SNR "SEÑAL
EXTRAIDA"](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/CALCULO%20SNR%20FINAL.png)

> > Por otra parte, se calcula el error cuadrático (ECM), el cual es una
> > medida estadística que nos indica, en promedio, qué tan diferentes
> > son dos conjuntos de datos. En el contexto del procesamiento de
> > señales de audio, nos permite cuantificar la diferencia entre una
> > señal original (en este caso, datarecortado) y una señal procesada o
> > reconstruida (en este caso, senal_extraida). Es así como obtenemos
> > un valor de 1020,86 el cual es un valor muy elevado respecto con los
> > resultados esperados, puesto que este valor expresa que existe una
> > gran diferencia entre la señal extraída y la señal original, esto se
> > debe a que se ha perdido información al disminuir las voces y
> > resaltar la señal con mayor intensidad en el audio, es decir que la
> > señal extraída no se parece mucho a la señal original.

![CALCULO
ECM](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/CALCULO%20ECM.png)

> > En cuanto a el ultimo calculo tasa de distorsión total THD, es una
> > medida de cuanto se desvía una señal de una forma de onda ideal (sin
> > distorsión), en este calculo el valor dio 0,9140 este valor nos
> > indica que la señal extraída es bastante similar a la señal
> > original, aunque con mucha distorsión debido a la señal inicial.

![CALCULO
THD](https://github.com/SeebastianOchoa/IMAGENESLAB2/blob/1aab4e9b70a7e769043ac87106e45f5441074ff6/CALCULO%20THD.png)
