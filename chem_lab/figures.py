import numpy as np
import pathlib as pl
import matplotlib.pyplot as plt
from scipy.stats import  linregress
import matplotlib
matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


def temp_csv_to_graph(file: pl.Path):
    data = np.genfromtxt(file, delimiter=',', skip_header=1)
    x = data[:,0]
    y = data[:,1]
    fig, ax = plt.subplots(1, 1)
    ax.plot(x, y,'r-', scalex=True, scaley=True)
    return fig, ax

if __name__ == '__main__':
    import chempy as cp
    import pylatex as pt
    f1 = pl.Path('./data/part1_trial1.csv')
    f2 = pl.Path('./data/part2_trial1.csv')
    f3 = pl.Path('./data/part3_KOH_temp.csv')
    f4 = pl.Path('./data/part3_KOH_HCl_soln_temp.csv')

    # Part 1 Plot generation
    p1fig, p1ax = temp_csv_to_graph(f1)
    p1ax.set_title('Part I, KOH(s) $\\to$ KOH(aq)')
    p1ax.set_ylabel ('Temperature (C)')
    p1ax.set_xlabel('Time (seconds)')
    p1fig.set_size_inches((6.5,3))
    p1fig.savefig('./report/part1_plot.pgf', bbox_inches='tight')

    # Part 2 Plot generation
    p2fig, p2ax = temp_csv_to_graph(f2)
    p2ax.set_title('Part II, KOH(s) + HCl $\\to$ KCl(aq) + H$_2$O(l)')
    p2ax.set_ylabel ('Temperature (C)')
    p2ax.set_xlabel('Time (seconds)')
    p2fig.set_size_inches((6.5,3))
    p2fig.savefig('./report/part2_plot.pgf', bbox_inches='tight')

    # Part 3 Plot generation
    p3figA, p3axA = temp_csv_to_graph(f3)
    p3axA.set_title('Part III, KOH(aq)')
    p3axA.set_ylabel ('Temperature (C)')
    p3axA.set_xlabel('Time (seconds)')
    p3figA.set_size_inches((6.5,3))
    p3figA.savefig('./report/part3a_plot.pgf', bbox_inches='tight')

    p3figB, p3axB = temp_csv_to_graph(f4)
    p3axB.set_title('Part III, KOH(aq) + HCl(aq)$\\to$ KCl(aq) + H$_2$O(l)')
    p3axB.set_ylabel ('Temperature (C)')
    p3axB.set_xlabel('Time (seconds)')
    p3figB.set_size_inches((6.5,3))
    p3figB.savefig('./report/part3b_plot.pgf', bbox_inches='tight')

    plt.figure(figsize=(6.5,3))
    moles1=np.array([0.05331,0.03975,0.05939,0.04711,0.05508,0.04148])
    moles3=np.array([0.02666,0.01987,0.02982,0.02355,0.02754,0.02074])
    moles2 = np.array([0.0397,0.04256,0.04827,0.03668,0.04483,0.03276])
    heats2 = np.array([3620,3720,4340,3498,4440,2.90e3])
    heats1=np.array([1943.,1539.,2120.,2110.,2577.,1464.])
    heats3=np.array([1621.,1162.,1755.,1579.,2266.,1365.])
    plt.scatter(moles2, heats2)
    plt.scatter(moles1, heats1 )
    plt.scatter(moles3, heats3)
    m1, b1, r1, p1, err1 = linregress(moles1, heats1)
    m3, b3, r3, p3, err3 = linregress(moles3, heats3)
    m2, b2, r2, p2, err2 = linregress(moles2, heats2)
    x2 = np.array([.03, .05])
    x1 = np.array([0.035, 0.065])
    x3 = np.array([0.012, 0.03])
    y1 = m1*x1 + b1
    y2 = m2*x2 + b2
    y3 = m3*x3 + b3

    plt.plot(x2, y2, 'b')
    plt.plot(x1, y1, 'darkorange')
    plt.plot(x3, y3, 'forestgreen')
    plt.savefig('./report/analysis.pgf', bbox_inches='tight')




