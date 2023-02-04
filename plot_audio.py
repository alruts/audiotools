import numpy as np
import matplotlib.pyplot as plt

def plot_audio_signal(signal, fs):
    time = np.arange(0, len(signal))/fs
    plt.plot(time, signal)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Audio Signal')
    plt.show()

if __name__ == '__main__':
    # Example signal
    signal = np.sin(2*np.pi*440*np.arange(44100)/44100)
    fs = 44100 # Sampling frequency in Hz
    plot_audio_signal(signal, fs)
