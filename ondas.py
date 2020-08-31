import sys

sys.path.insert(1, 'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import CosSignal
from thinkdsp import decorate

import matplotlib.pyplot as plt

seno = SinSignal(freq=400, amp=1, offset=0)
coseno = CosSignal(freq=750, amp=1, offset=0)

decorate(xlabel="Tiempo (s)")
decorate(ylabel="Amplitud")


seno.plot()
coseno.plot()

plt.show()