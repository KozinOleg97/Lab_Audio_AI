from scipy.io import wavfile  # get the api

import numpy as np
import matplotlib.pyplot as mpl
import numpy.fft as nfft
import sys


def load_wav(fileName):
    rate, samples = wavfile.read(filename)

    print(rate, len(samples))
    print(np.min(samples))
    print(np.max(samples))

    mpl.plot(np.arange(0, len(samples)), samples)
    mpl.grid()
    # mpl.show()

    N = len(samples)

    fs = rate
    f = np.arange(0, N) / (N + 1.) * fs

    spec = 2. * (np.abs(nfft.fft(samples, len(samples)))) / N

    mpl.plot(f, spec)
    mpl.grid()
    # mpl.show()

    return spec


def get_min(a, b, c):
    mn = min(a, b, c)
    if mn == a:
        return [0, -1]
    if mn == b:
        return [-1, -1]
    if mn == c:
        return [-1, 0]


def calc_m(v1, v2):
    rows = int(len(v1) / 2)
    cols = int(len(v2) / 2)
    # Matrix = [[0 for x in range(w)] for y in range(h)]

    all_percent = rows * cols

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(abs(v1[i] - v2[j]))
        matrix.append(row)
        print(((i * j) / all_percent) * 100)

    row = rows - 1
    col = cols - 1

    M_res = 0;
    while True:
        M_res += matrix[row][col]

        if col == 0:
            a = sys.maxsize
        else:
            a = matrix[row][col - 1]

        if row == 0:
            c = sys.maxsize
        else:
            c = matrix[row - 1][col]

        if row == 0 & col == 0:
            return M_res
            b = sys.maxsize
        else:
            b = matrix[row - 1][col - 1]

        res = get_min(a, b, c)
        row += res[0]
        col += res[1]

    return M_res


filepath = 'files/'
filename = filepath + input('Type file example: ') + '.wav'
spectr1 = load_wav(filename)

while True:
    filename = filepath + input('Type file 2: ') + '.wav'
    if filename == filepath + "-" + '.wav':
        break

    spectr2 = load_wav(filename)

    print(calc_m(spectr1, spectr2))
