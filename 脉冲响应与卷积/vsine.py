import librosa
import numpy as np
t=2
sr=44100
n=np.arange(int(t*sr))
f=100+(1000-100)*n/(n.size-1)
phase_delta=f/sr
phase=np.zeros(n.size)
for i in range(1,n.size):
    phase[i]=phase[i-1]+phase_delta[i-1]
y=np.sin(2*np.pi*phase)

librosa.output.write_wav('vsine.wav',y.astype(np.float32),sr)

