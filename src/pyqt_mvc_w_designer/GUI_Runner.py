################################################################################
###                                 Imports                                  ###
################################################################################
#Standard imports
import os
import logging

#PyQt imports
from PyQt5.QtWidgets import QApplication, QMainWindow

#Our imports
from .Main_Win_Ctrlr import Main_Win_Ctrlr

################################################################################
###                                Class Def                                 ###
################################################################################
class GUI_Runner:
	"""
	Class that launches and runs the GUI
	"""
	############################################################################
	def __init__(self, ctrlr, *args, window_title="", show_console=True, 
				 log_lvl=logging.INFO, **kwargs):
		"""
		PURPOSE: creates a new GUI_Runner
		ARGS:
			ctrlr (Abstract_Ctrlr): class type of controller that runs 
				main widget (not actually an instance of said class, GUI_Runner 
				will create an instance)
			args (args): args to pass to ctrlr constructor
			kwargs (kwargs): kwargs to pass to ctrlr constructor
			window_title (str): title of window
			show_console (bool): True to show console in window, False to 
				hide it
			log_lvl (logging.LEVEL): level to log at
		RETURNS: new instance of an GUI_Runner
		NOTES:
		"""
		#Save arguments
		self.ctrlr = ctrlr
		self.args = args
		self.kwargs = kwargs
		self.window_title = str(window_title)
		self.show_console = bool(show_console)
		self.log_lvl = log_lvl

	############################################################################
	def run(self):
		"""
		PURPOSE: runs the GUI
		ARGS: none
		RETURNS: (int) return code of QApplication
		NOTES: blocking
		"""
		#Create app and main window
		app = QApplication([])
		window = QMainWindow()

		#Create controller for main window and get logger
		main_win_ctrlr = Main_Win_Ctrlr(window, window_title=self.window_title, 
									 show_console=self.show_console, 
									 log_lvl=self.log_lvl)
		logger = main_win_ctrlr.logger

		#Create main widget controller
		main_widg_ctrlr = self.ctrlr(main_win_ctrlr.widg.main_widg, *self.args, 
									 **self.kwargs, parent=main_win_ctrlr, 
									 logger=logger)

		#Connect about to quit signal
		app.aboutToQuit.connect(main_widg_ctrlr.about_to_quit)

		#Show window and execute pyqt main update loop
		window.show()
		return app.exec()

################################################################################
###                               End of File                                ###
################################################################################