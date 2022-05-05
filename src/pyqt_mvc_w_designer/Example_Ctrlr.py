################################################################################
###                                 Imports                                  ###
################################################################################
#Standard imports
import pkg_resources
import os

#Third party imports
import numpy as np

#PyQt imports
from PyQt5.QtGui import QTextCursor

#Our imports
from .Abstract_Ctrlr import Abstract_Ctrlr
from .Mpl_Ctrlr import Mpl_Ctrlr

################################################################################
###                                Class Def                                 ###
################################################################################
class Example_Ctrlr(Abstract_Ctrlr):
	"""
	Controller for the example widget
	"""
	############################################################################
	def __init__(self, widg, parent=None, logger=None):
		"""
		PURPOSE: creates a new Example_Ctrlr
		ARGS:
			widg (QWidget): widget to setup UI in
			parent (Abstract_Ctrlr): parent controller if it has one
			logger (Logger): logger to log to
		RETURNS: new instance of an Example_Ctrlr
		NOTES:
		"""
		#Call parent constructor
		ui_file = "ui" + os.sep + "example_widg.ui"
		file_stream = pkg_resources.resource_stream(__name__, ui_file)
		ui_content = file_stream.read().decode()
		super().__init__(widg, ui_content, parent=parent, logger=logger)

		#Setup mpl widget
		self.mpl_ctrlr = Mpl_Ctrlr(self.widg.mpl_widg, self, self.logger)

		#Connect buttons
		tmp_func = lambda : self.logger.debug(self.widg.msg_input.text())
		self.widg.debug_button.clicked.connect(tmp_func)
		tmp_func = lambda : self.logger.info(self.widg.msg_input.text())
		self.widg.info_button.clicked.connect(tmp_func)
		tmp_func = lambda : self.logger.warning(self.widg.msg_input.text())
		self.widg.warning_button.clicked.connect(tmp_func)
		tmp_func = lambda : self.logger.error(self.widg.msg_input.text())
		self.widg.error_button.clicked.connect(tmp_func)
		tmp_func = lambda : self.logger.critical(self.widg.msg_input.text())
		self.widg.critical_button.clicked.connect(tmp_func)
		self.widg.plot_button.clicked.connect(self.plot_random)

	############################################################################
	def plot_random(self):
		"""
		PURPOSE: plots a random function
		ARGS: none
		RETURNS: none
		NOTES
		"""
		x = np.arange(100)
		y1 = np.random.rand(x.size)
		y2 = np.random.rand(x.size)

		plots = [
			((x, y1), {"label": "Y1"}),
			((x, y2), {"label": "Y2", "linestyle": "dashed"})
		]
		self.mpl_ctrlr.update_plot(plots, xlabel="Sample", ylabel="Value", 
								   title="Random Plot", 
								   xlim=[np.min(x), np.max(x)], legend=True)

################################################################################
###                               End of File                                ###
################################################################################