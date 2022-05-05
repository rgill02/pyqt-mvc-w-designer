################################################################################
###                                 Imports                                  ###
################################################################################
#Standard imports
import pkg_resources
import os

#Third party imports
import matplotlib
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT

#Our imports
from .Abstract_Ctrlr import Abstract_Ctrlr
from .Mpl_Canvas import Mpl_Canvas

################################################################################
###                                Class Def                                 ###
################################################################################
class Mpl_Ctrlr(Abstract_Ctrlr):
	"""
	Controller for the matplotlib widget
	"""
	############################################################################
	def __init__(self, widg, parent=None, logger=None):
		"""
		PURPOSE: creates a new Mpl_Ctrlr
		ARGS:
			widg (QWidget): widget to setup UI in
			parent (Abstract_Ctrlr): parent controller if it has one
			logger (Logger): logger to log to
		RETURNS: new instance of an Mpl_Ctrlr
		NOTES:
		"""
		#Call parent constructor
		ui_file = "ui" + os.sep + "mpl_widg.ui"
		file_stream = pkg_resources.resource_stream(__name__, ui_file)
		ui_content = file_stream.read().decode()
		super().__init__(widg, ui_content, parent=parent, logger=logger)

		#Setup plot
		self.plot_widg = Mpl_Canvas()
		containing_layout = self.widg.plot_widg.parent().layout()
		containing_layout.replaceWidget(self.widg.plot_widg, self.plot_widg)

		#Setup toolbar
		self.tooldbar_widg = NavigationToolbar2QT(self.plot_widg, self.widg)
		containing_layout = self.widg.toolbar_widg.parent().layout()
		containing_layout.replaceWidget(self.widg.toolbar_widg, 
										self.tooldbar_widg)

	############################################################################
	def update_plot(self, plots, xlabel=None, ylabel=None, title=None, 
					xlim=None, ylim=None, grid=True, legend=False):
		"""
		PURPOSE: updates the plot widget
		ARGS:
			plots (list/tuple): if list then a list of tuples, if tuple then a 
				single tuple. Each tuple is a set of args and kwargs for the 
				pyplot plot command
			xlabel (str): label for x axis
			ylabel (str): label for y axis
			title (str): tile of plot
			xlim (list): limits of x axis [min, max]
			ylim (list): limits of y axis [min, max]
			grid (bool): True to show grid, False to not
			legend (bool): True to show legend, False to not
		RETURNS: none
		NOTES:
		"""
		#Handle tuple vs list
		if isinstance(plots, tuple) and not isinstance(plots, list):
			plots = [plots]

		#Get and clear axes
		axes = self.plot_widg.axes
		axes.cla()

		#Plot all plots
		for plot in plots:
			axes.plot(*plot[0], **plot[1])

		#Handle other plot formatting
		if xlabel is not None:
			axes.set_xlabel(str(xlabel))
		if ylabel is not None:
			axes.set_ylabel(str(ylabel))
		if title is not None:
			axes.set_title(str(title))
		if xlim is not None:
			axes.set_xlim(xlim)
		if ylim is not None:
			axes.set_ylim(ylim)
		if grid:
			axes.grid()
		if legend:
			axes.legend(loc="upper right")

		#Draw plot
		self.plot_widg.draw()

################################################################################
###                               End of File                                ###
################################################################################