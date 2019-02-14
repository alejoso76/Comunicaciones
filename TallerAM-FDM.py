#Alejandro Osorio Trujillo - 1088342470

#Librerias
from scipy import signal
import numpy as np
import scipy
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter

#Funciones de filtro
def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

#Senal 1
t = np.linspace(0, 5, 450)
s1 = 2.5*signal.square(2 * np.pi * 400 * t, 0.7)+2.5
plt.plot(t, s1)
plt.show()
sc1 = np.cos(t*20000)
fff1 = s1*sc1
fourier1 =  scipy.fftpack.fft(fff1)
plt.plot(t, fourier1)
plt.show()

#Senal 2
triang = np.linspace(-0.5, 4.5,450)
s2 =  5*signal.sawtooth(2 * np.pi * 450 * triang, 0.5)
plt.plot(triang, s2)
plt.show()
sc2 = np.cos(triang*300000)
fff2 = s2*sc2
fourier2 =  scipy.fftpack.fft(fff2)
plt.plot(triang, fourier2)
plt.show()

#Senales moduladas y sumadas
sumadas = fourier1 + fourier2
plt.plot(sumadas)
plt.show()

w = np.linspace(0.01,5,450)
L =100000000
C = 0.0000005
R = 1600

#Filtro pasabanda
xl = w*L
xc = 1/w*C
invz = 1/R + 1/xl+1/xc
z= 1/invz
#z = scipy.sqrt(1/((1/R)*(1/R) + (1/xl - 1/xc)*(1/xl - 1/xc)))
H = butter_bandpass_filter(sumadas, 400, 500, 5000)
plt.plot(H)

#plt.show()
supuesta_recuperacion = butter_lowpass_filter(H, 450, 5000)
plt.plot(supuesta_recuperacion)
plt.plot(s1)
plt.show()

'''
filtrada = scipy.signal.convolve(sumadas, H)
plt.plot(filtrada)
plt.show()
'''
