################################################################################
###                                 Imports                                  ###
################################################################################
#Standard imports
import logging
import pkg_resources
import os

#PyQt imports
from PyQt5.QtGui import QTextCursor

#Our imports
from .Abstract_Ctrlr import Abstract_Ctrlr
from .Callback_Log_Handler import Callback_Log_Handler

################################################################################
###                                Class Def                                 ###
################################################################################
class Main_Win_Ctrlr(Abstract_Ctrlr):
	"""
	Controller for the main window
	"""
	############################################################################
	def __init__(self, widg, window_title="", show_console=True, 
				 log_lvl=logging.INFO):
		"""
		PURPOSE: creates a new Main_Win_Ctrlr
		ARGS:
			widg (QWidget): widget to setup UI in
			window_title (str): title of window
			show_console (bool): True to show console in window, False to 
				hide it
			log_lvl (logging.LEVEL): level to log at
		RETURNS: new instance of an Main_Win_Ctrlr
		NOTES:
		"""
		#Call parent constructor
		ui_file = "ui" + os.sep + "main_window.ui"
		file_stream = pkg_resources.resource_stream(__name__, ui_file)
		ui_content = file_stream.read().decode()
		super().__init__(widg, ui_content)

		#Setup logger
		self.logger = logging.getLogger("GUI")
		self.logger.setLevel(log_lvl)
		my_log_handler = Callback_Log_Handler(self.log_to_console)
		my_log_handler.setLevel(log_lvl)
		self.logger.addHandler(my_log_handler)

		#Set window title
		self.widg.setWindowTitle(window_title)

		#Show or hide console
		self.widg.frame.setVisible(bool(show_console))

	############################################################################
	def log_to_console(self, record):
		"""
		PURPOSE: logs a message to the console
		ARGS:
			record (logging.record): record to log
		RETURNS: none
		NOTES:
		"""
		#Choose color based on log level
		color = "green"
		if record.levelno == logging.DEBUG:
			color = "blue"
		elif record.levelno == logging.INFO:
			color = "black"
		elif record.levelno == logging.WARNING:
			color = "orange"
		elif record.levelno == logging.ERROR:
			color = "red"
		elif record.levelno == logging.CRITICAL:
			color = "darkRed"

		#Write to console
		text_pattern = '<span style="color:%s">%s: %s</span>\n'
		rich_text = text_pattern % (color, record.levelname.upper(), record.msg)
		self.widg.console_textedit.append(rich_text)
		self.widg.console_textedit.moveCursor(QTextCursor.End)

################################################################################
###                               End of File                                ###
################################################################################