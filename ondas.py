import sys

sys.path.insert(1, 'dsp-modulo')


from thinkdsp import SinSignal
from thinkdsp import CosSignal
from thinkdsp import decorate

import matplotlib.pyplot as plt

seno = SinSignal(freq=5, amp=1, offset=0)
coseno = CosSignal(freq=10, amp=1.3, offset=0)

waveSeno = seno.make_wave(duration=1, start=0, framerate=11025)
waveCoSeno = coseno.make_wave(duration=1, start=0, framerate=11025)

waveResult = waveCoSeno + waveSeno

decorate(xlabel="Tiempo (s)")
decorate(ylabel="Amplitud")


waveSeno.plot()
waveCoSeno.plot()
plt.show()

waveResult.plot()
plt.show()

