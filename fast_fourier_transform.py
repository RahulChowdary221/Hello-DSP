import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import scipy.fft
import math
srate=256
Nyquist=srate/2
t=np.arange(0,1,1/srate) #time vector in seconds
x1=5*np.sin(2*np.pi*2*t)
x2=2*np.sin(2*np.pi*4*t)
x3=7*np.sin(2*np.pi*6*t)
x=x1+x2+x3 #combined sinewaves
#calculating Fourier-coefficient
X=scipy.fft.fft(x)/len(t) 
X=2*np.abs(X)
#converting indices into frequency
Hz1=np.linspace(0,Nyquist,math.floor(len(t)/2+1))
plt.figure(figsize=(15,8))
plt.suptitle('Signal and its Fast-Fourier Transform')
style.use('dark_background')
plt.rcParams['xtick.labelsize']=25
plt.rcParams['ytick.labelsize']=25
plt.subplot(2,1,1)
plt.plot(t,x,'r-',label='Sinewave with frequencies 2,4,6')
plt.title('Combined sinewave')
plt.subplot(2,1,2)
markerline, stemlines, baseline = plt.stem(Hz1,X[range(0,len(Hz1))])
plt.setp(stemlines,linewidth=2)
plt.setp(stemlines,color='cyan')
plt.setp(markerline, markersize=8, markerfacecolor='yellow')
plt.xlim(0,10)
plt.ylim(0,max(x)*1.1)
plt.xlabel('frequency in hertzs',fontsize=20)
plt.ylabel('Amplitude',fontsize=20)
plt.title('Fourier Transform of a signal',fontsize=20)
plt.grid(True)
plt.tight_layout()
plt.legend(fontsize=15)
plt.show() 
