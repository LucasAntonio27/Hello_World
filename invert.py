import winsound
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


def main():
    fname = 'stereo_audio.wav'
    fsseis, seis = wavfile.read(fname)
    seis = seis / 2**15  # sinal entre -1 e 1
    T = 0.6  # echo em s
    A = 0.8  # atenuacao do echo
    K = 14  # quantidade de echoes
    N = int(T * fsseis)  # pontos por periodo de echo

    sieis = seis[-1::-1]
    plt.plot(sieis)
    plt.title('Trecho invertido no tempo')
    plt.grid()
    plt.show()

    # para ouvir:
    fname = 'invert.wav'
    samples = sieis * 2**15
    samples = samples.astype(np.short)
    wavfile.write(fname, fsseis, samples)
    winsound.PlaySound(fname, winsound.SND_FILENAME)
