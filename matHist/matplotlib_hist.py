from . import header

def mat_hist_func(input_file, output_file):
    # Inputs
    bins = int(input("Enter the number of bins: ") )
    bar_width = float(input("Enter the bar width of the histogram: "))
    c = str(input("Enter the color (string): "))
    x_label = str(input("Enter x-axis label(string): "))
    y_label = str(input("Enter y-axis label(string): "))
    font_size = int(input("Enter the font size (interger): "))
    xlim_l = float(input("Enter the x limits (lower limit): "))
    xlim_u = float(input("Enter the x limits (upper limit): "))
    '''ylim_l = float(input("Enter the y limits (lower limit): "))
    ylim_u = float(input("Enter the y limits (upper limit): "))'''

    data = header.np.genfromtxt(fname=input_file, skip_header=True)   # Will skip the header
    array = data[:]
    n_bins = bins
    hist, bin_edges = header.np.histogram(array, n_bins)
    y = hist/float(len(array))
    x = bin_edges
    x = x[:-1]
    header.plt.bar(x, y, color=c, width=bar_width)
    header.plt.xlabel(x_label, fontsize=font_size)
    header.plt.ylabel(y_label, fontsize=font_size)
    header.plt.xlim(xlim_l, xlim_u)
    header.plt.ylim(0, 1)
    header.plt.xticks(fontsize=font_size)
    header.plt.yticks(fontsize=font_size)
    header.plt.tick_params(axis='both', direction='in')
    header.plt.show()
    header.plt.savefig(output_file, bbox_inches = "tight", dpi=300)
    header.plt.close()

