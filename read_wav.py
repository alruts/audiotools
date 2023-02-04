import scipy.io.wavfile as wavfile
import numpy as nap

def read_wav(file_path):
    """
    Reads a .wav file and returns numpy array and sampling frequency.
    
    Args:
        filename: file to read

    Returns:
        signal: N x 1 or N x 2 numpy array
        fs_hz: sampling frequency in hertz
    """

    fs_hz, audio_signal = wavfile.read(file_path)
    audio_signal = np.array(audio_signal, dtype=float)
    return fs_hz, audio_signal
