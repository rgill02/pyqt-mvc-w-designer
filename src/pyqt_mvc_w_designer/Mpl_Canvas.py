################################################################################
###                                 Imports                                  ###
################################################################################
#Third party imports
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

################################################################################
###                                Class Def                                 ###
################################################################################
class Mpl_Canvas(FigureCanvasQTAgg):
	"""
	Used to integrate a matplotlib plot into a widget
	"""
	############################################################################
	def __init__(self):
		"""
		PURPOSE: creates a new Mpl_Canvas
		ARGS: none
		RETURNS: new instance of an Mpl_Canvas
		NOTES:
		"""
		fig = Figure(figsize=(5,4), dpi=100)
		self.axes = fig.add_subplot(111)
		super().__init__(fig)

################################################################################
###                               End of File                                ###
################################################################################