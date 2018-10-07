from scipy.io import wavfile as wav
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from scipy.fftpack import fft

file_name = 'sonicare-adult-HX6980.wav'
rate, data = wav.read(file_name)
print "rate = {}".format(rate)
t = data.size

# time domain
N = int(3. / 261 * rate)
S = data.size / 2
matplotlib.rcParams.update({'font.size': 22})
#plt.subplot(211)
plt.plot(np.arange(N) / float(rate) * 1000, data[S:N+S],'o-')
plt.xlabel('time (ms)')
plt.ylabel('amplitude (au)')
plt.title('Sound Wave from Sonicare toothbrush')
plt.autoscale(enable=True, axis='x', tight=True)
plt.grid(True)
plt.show()

# spetrum
fft_out = fft(data)
spectrum = np.abs(fft_out)
M = int(t/2/4/3)
spectrum = spectrum[0:M]
#plt.subplot(212)
plt.autoscale(enable=True, axis='x', tight=True)
f_unit =  1. / (t / rate)
plt.semilogy(np.arange(M) * f_unit, spectrum)
plt.xlabel('frequency (Hz)')
plt.ylabel('amplitude (au)')
plt.title('Power Spectrum from Sonicare toothbrush')
plt.grid(True)
plt.show()
