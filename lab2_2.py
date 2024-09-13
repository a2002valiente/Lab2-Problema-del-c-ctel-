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


#//////////////////////////////////////////////////////////////////////////////////////#
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