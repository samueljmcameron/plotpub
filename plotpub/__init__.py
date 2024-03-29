import matplotlib.pyplot as plt
import math

def PlotPub():
    
    gold = (math.sqrt(5)-1)/2
    figsize=[3.73,3.73*gold]
    params = {'backend': 'pdf',
              'axes.labelsize': 14,
              'font.size': 12,
              'legend.fontsize': 10,
              'xtick.labelsize': 11,
              'ytick.labelsize': 11,
              'text.usetex': True,
              'figure.figsize': figsize,
              'figure.dpi': 200,
              'text.latex.preamble': (r"\usepackage{amstext} \usepackage{amsmath}"
                                      + r" \usepackage{bm} \usepackage{siunitx}"
                                      + r" \usepackage{braket}")}
    plt.rcParams.update(params)


    return figsize


