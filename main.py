import numpy as np
import matplotlib.pyplot as plot
import csv
from scipy.interpolate import make_interp_spline



def sineWave(showBool):
    time = np.arange(0, 100, 0.1)
    amplitude = np.sin(time)
    plot.plot(time, amplitude)
    plot.title('Sine wave')
    plot.xlabel('Time')
    plot.ylabel('Amplitude = sin(time)')
    plot.grid(True, which='both')
    plot.axhline(y=0, color='k')
    if(showBool):
        plot.show()
    return amplitude

def storeGraphValues():
    with open('graphData.csv', 'w') as f:
        sineWaveData = ','.join(map(str, sineWave(1).tolist()))
        f.write(sineWaveData)

def CSVtoGraph():
    storeGraphValues()
    x, y = [], []
    with open('graphData.csv','r') as csvfile:
        plots = csv.reader(csvfile, delimiter = ',')
        c = 0
        for row in plots:
            x.append(row)
    y = np.array(x).transpose()
    x = np.arange(0, 100, 0.1)
    X_Y_Spline = make_interp_spline(x, y)
    X_ = np.linspace(x.min(), x.max(), 100)
    Y_ = X_Y_Spline(X_)
    plot.plot(X_, Y_)
    plot.xlabel('Amplitude')
    plot.ylabel('Time')
    plot.title('Sine Wave')
    plot.show()

CSVtoGraph()