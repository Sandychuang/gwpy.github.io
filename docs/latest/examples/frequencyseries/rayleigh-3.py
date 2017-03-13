asd = gwdata.asd(2, 1)
plot = asd.plot()
plot.add_frequencyseries(rayleigh, newax=True, sharex=plot.axes[0])
plot.axes[0].set_xlabel('')
plot.axes[0].set_xlim(40, 2000)
plot.axes[0].set_ylim(1e-23, 5e-21)
plot.axes[0].set_ylabel(r'[strain/\rtHz]')
plot.axes[1].set_ylabel('Rayleigh statistic')
plot.show()