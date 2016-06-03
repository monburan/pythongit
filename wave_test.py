import wave
import numpy
import scipy.signal


framerate = 48000
nframes = 1194240
time = 25

t = numpy.arange(0,time,1.0/framerate)
wave_data = scipy.singal.chirp(t,100,time,1000,method='linear')*10000

f = wave.open(r"data.wav","wb")

f.setnchannels(2)
f.setsampwidth(2)
f.setframerate(framerate)
f.writeframes(wave_data.tostring())
f.close()
