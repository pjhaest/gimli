# CODING=Utf-8
"""Plotting utilities used througout the mplviewer package."""

import os
import time

import matplotlib.animation as animation
import matplotlib.pyplot as plt

import pygimli as pg

holdAxes__ = 0


def updateAxes(ax, a=None, force=False):
    """For internal use."""
    if not holdAxes__:
        try:
            ax.figure.canvas.draw_idle()
            if force:
                time.sleep(0.1)
        except BaseException as e:
            pg.warn("Exception raised", e)
            print(ax, a, e)


def hold(val=1):
    """TODO WRITEME."""
    pg.mplviewer.holdAxes__ = val


def wait(**kwargs):
    """TODO WRITEME."""
    # plt.pause seems to be broken in mpl:2.1
    #ax.canvas.draw_onIdle()
    updateAxes(plt.gca())
    plt.show(**kwargs)


def saveFigure(fig, filename, pdfTrim=False):
    """Save figure as pdf."""
    if '.pdf' in filename:
        filename = filename[0:filename.find('.pdf')]
    fig.savefig(filename + '.pdf', bbox_inches='tight')
    # pdfTrim=1
    if pdfTrim:
        try:
            print("trying pdf2pdfS ... ")
            os.system('pdf2pdfBB ' + filename + '.pdf')
            os.system('pdf2pdfS ' + filename + '.pdf')
        except BaseException as _:
            print("fail local convert. Should be no problem.")


def saveAxes(ax, filename, adjust=False):
    """Save axes as pdf."""
    if adjust:
        adjustWorldAxes(ax)

    updateAxes(ax, force=True)
    saveFigure(ax.figure, filename)


def prettyFloat(v):
    """Return a pretty string for a given value suitable for graphical output."""
    if abs(round(v)-v) < 1e-4 and abs(v) < 1e3:
        return str(int(round(v,1)))
    elif abs(v) == 0.0:
        return "0"
    elif abs(v) > 1e3 or abs(v) <= 1e-3:
        return str("%.1e" % v)
    elif abs(v) < 1e-2:
        return str("%.4f" % round(v,4))
    elif abs(v) < 1e-1:
        return str("%.3f" % round(v,3))
    elif abs(v) < 1e0:
        return str("%.2f" % round(v,2))
    elif abs(v) < 1e1:
        return str("%.1f" % round(v,1))
    elif abs(v) < 1e2:
        return str("%.1f" % round(v,1))
    else:
        return str("%.0f" % round(v,1))


def renameDepthTicks(ax):
    """Switch signs of depth ticks to be positive"""
    ticks = ax.yaxis.get_majorticklocs()
    tickLabels = []
    for t in ticks:
        tickLabels.append(prettyFloat(-t))

    ax.set_yticklabels(tickLabels)
    #insertUnitAtNextLastTick(ax, 'm', xlabel=False)
    updateAxes(ax)


def insertUnitAtNextLastTick(ax, unit, xlabel=True, position=-2):
    """Replace the last-but-one tick label by unit symbol."""
    if xlabel:
        labels = ax.get_xticklabels()
        labels[position] = unit
        ax.set_xticklabels(labels)
    else:
        labels = ax.get_yticklabels()
        labels[-position] = unit
        ax.set_yticklabels(labels)


def adjustWorldAxes(ax):
    """Set some common default properties for an axe."""
    ax.set_ylabel('Depth (m)')
    ax.set_xlabel('$x$ (m)')

    renameDepthTicks(ax)
    plt.tight_layout()
    updateAxes(ax)


def setOutputStyle(dim='w', paperMargin=5, xScale=1.0, yScale=1.0, fontsize=9,
                   scale=1, usetex=True):
    """Set preferred output style."""
    if dim == 'w':
        dim = 0
    else:
        dim = 1

    a4 = [21.0, 29.7]

    inches_per_cm = 1. / 2.54
    # inches_per_pt = 1.0 / 72.27  # pt/inch (latex)
    # goldenMean = (1.0 + np.sqrt(5.0)) / 2.0

    textwidth = (a4[0] - paperMargin) * inches_per_cm

    fig_width = textwidth * xScale  # fig width in inches
    fig_height = textwidth * yScale  # fig height in inches

    fig_size = [fig_width * scale, fig_height * scale]

    # print "figsize:", fig_size
    # fig.set_size_inches(fig_size)

    # from matplotlib import rc
    # rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    # rc('font',**{'family':'serif','serif':['Palatino']})

    params = {
        'backend': 'ps',
        # 'font.weight'       : 'bold',
        'ax.labelsize': fontsize * scale,
        'font.size': fontsize * scale,
        'legend.fontsize': fontsize * scale,
        'xtick.labelsize': fontsize * scale,
        'ytick.labelsize': fontsize * scale,
        # font.sans-serif     : Bitstream Vera Sans, ...
        # 'font.cmb10'     : 'cmb10',
        # 'font.family'         : 'cursive',
        'font.family': 'sans-serif',
        # 'font.sans-serif'   : 'Helvetica',
        'text.usetex': usetex,
        'figure.figsize': fig_size,
        'xtick.major.pad': 4 * scale,
        'xtick.minor.pad': 4 * scale,
        'ytick.major.pad': 4 * scale,
        'ytick.minor.pad': 4 * scale,
        'xtick.major.size': 4 * scale,  # major tick size in points
        'xtick.minor.size': 2 * scale,  # minor tick size in points
        'ytick.major.size': 4 * scale,  # major tick size in points
        'ytick.minor.size': 2 * scale,  # minor tick size in points
        'lines.markersize': 6 * scale,
        'lines.linewidth': 0.6 * scale
    }
    plt.rcParams.update(params)


def setPlotStuff(fontsize=7, dpi=None):
    """TODO merge with setOutputStyle.

    Change ugly name.
    """
    from matplotlib import rcParams

    # print(rcParams.keys())

    # rcParams['ax.labelsize'] = fontsize  # REMOVED IN MPL.1.5
    # rcParams['ax.titlesize'] = fontsize  # REMOVED IN MPL.1.5
    # rcParams['ax.linewidth'] = 0.3  # REMOVED IN MPL.1.5
    rcParams['font.size'] = fontsize
    rcParams['xtick.labelsize'] = fontsize
    rcParams['ytick.labelsize'] = fontsize
    rcParams['legend.fontsize'] = fontsize
    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = ['Helvetica']  # ['Times New Roman']
    rcParams['text.usetex'] = False

    #    rcParams['figure.figsize'] = 7.3, 4.2
    rcParams['xtick.major.size'] = 3
    rcParams['xtick.major.width'] = 0.3
    rcParams['xtick.minor.size'] = 1.5
    rcParams['xtick.minor.width'] = 0.3
    rcParams['ytick.major.size'] = rcParams['xtick.major.size']
    rcParams['ytick.major.width'] = rcParams['xtick.major.width']
    rcParams['ytick.minor.size'] = rcParams['xtick.minor.size']
    rcParams['ytick.minor.width'] = rcParams['xtick.minor.width']

    if dpi is not None:
        rcParams['figure.dpi'] = dpi
        rcParams['savefig.dpi'] = dpi


def createAnimation(fig, animate, nFrames, dpi, out):
    """Create animation for the content of a given matplotlib figure.

    Until I know a better place.
    """
    anim = animation.FuncAnimation(fig, animate, frames=nFrames,
                                   interval=0.001, repeat=False)
    anim.save(out + ".mp4", writer=None, fps=20, dpi=dpi, codec=None,
              bitrate=24 * 1024, extra_args=None, metadata=None,
              extra_anim=None, savefig_kwargs=None)
    try:
        print("Create frames ... ")
        os.system('mkdir -p anim-' + out)
        os.system('ffmpeg -i ' + out + '.mp4 anim-' + out + '/movie%d.jpg')
    except BaseException as _:
        pass


def saveAnimation(mesh, data, out, vData=None, plc=None, label='', cMin=None,
                  cMax=None, logScale=False, cmap=None, **kwargs):
    """Create and save an animation for a given mesh with a set of field data.

    Until I know a better place.
    """
    dpi = 92
    scale = 1
    fig = plt.figure(facecolor='white',
                     figsize=(scale * 800 / dpi, scale * 490 / dpi), dpi=dpi)
    ax = fig.add_subplot(1, 1, 1)

    gci = pg.mplviewer.drawModel(ax, mesh, data=data[0], cMin=cMin, cMax=cMax,
                                 cmap=cmap, logScale=logScale)

    pg.mplviewer.createColorbar(gci, label=label, pad=0.55)

    if plc:
        pg.show(plc, ax=ax)

    adjustWorldAxes(ax)

    def animate(i):
        """TODO WRITEME."""
        print(out + ": Frame:", i, "/", len(data))

        if vData is not None:
            ax.clear()
            pg.mplviewer.holdAxes_ = 1
            pg.mplviewer.drawModel(ax, mesh, data=data[i], cMin=cMin,
                                   cMax=cMax, cmap=cmap, logScale=logScale)
            pg.mplviewer.drawStreams(ax, mesh, vData[i], **kwargs)
        else:
            print(min(data[i]), max(data[i]))
            pg.mplviewer.setMappableData(gci, data[i], cMin=cMin, cMax=cMax,
                                         logScale=logScale)

        plt.pause(0.001)

    createAnimation(fig, animate, int(len(data)), dpi, out)


def plotLines(ax, line_filename, linewidth=1.0, step=1):
    """Read lines from file and plot over model."""
    xz = np.loadtxt(line_filename)
    n_points = xz.shape[0]
    if step == 2:
        for i in range(0, n_points, step):
            x = xz[i:i + step, 0]
            z = xz[i:i + step, 1]
            ax.plot(x, z, 'k-', linewidth=linewidth)
    if step == 1:
        ax.plot(xz[:, 0], xz[:, 1], 'k-', linewidth=linewidth)


def createTwinX(ax):
    """Utility function to create or return an existing a twin x axes for ax."""
    return _createTwin(ax, 'twinx')


def createTwinY(ax):
    """Utility function to create or return an existing a twin x axes for ax."""
    return _createTwin(ax, 'twiny')


def _createTwin(ax, funct):
    """Utility function to create or return an existing a twin x axes for ax."""
    tax = None
    for other_ax in ax.figure.axes:
        if other_ax is ax:
            continue
        if other_ax.bbox.bounds == ax.bbox.bounds:
            tax = other_ax

    if tax is None:
        tax = getattr(ax, funct)()

    return tax
