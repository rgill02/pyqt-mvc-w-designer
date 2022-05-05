################################################################################
###                                 Imports                                  ###
################################################################################
#Standard imports
import logging
import io

#PyQt imports
from PyQt5 import uic

################################################################################
###                                Class Def                                 ###
################################################################################
class Abstract_Ctrlr:
	"""
	Abstract base class for the controllers in the MVC pattern for the GUI
	"""
	############################################################################
	def __init__(self, widg, ui_file_content, parent=None, logger=None):
		"""
		PURPOSE: creates a new Abstract_Ctrlr
		ARGS:
			widg (QWidget): widget to setup UI in
			ui_file_content (str): content of corresponding UI file
			parent (Abstract_Ctrlr): parent controller if it has one
			logger (Logger): logger to log to
		RETURNS: new instance of an Abstract_Ctrlr
		NOTES: should inherit from this class and then call its constructor 
			right away
		"""
		#Save arguments
		self.widg = widg
		self.ui_file_content = ui_file_content
		self.parent_ctrlr = parent
		self.logger = logger

		#Store child controllers
		self.child_ctrlrs = []

		#Load our UI file and apply it to our widget
		f = io.StringIO(ui_file_content)
		uic.loadUi(f, self.widg)

		#Setup log function
		if logger is None:
			self.logger = logging.getLogger(__name__)

		#Register with parent
		if parent is not None:
			parent.register_child(self)

	############################################################################
	def about_to_quit(self):
		"""
		PURPOSE: facillitates cleanup before GUI quits
		ARGS: none
		RETURNS: none
		NOTES: main widget controller will call this before the GUI quits and 
			each controller will run it down the chain and call it on its 
			children so you don't have to call this
		"""
		#Clean up children
		for cur_child in self.child_ctrlrs:
			cur_child.about_to_quit()

		#Clean up self
		self.about_to_quit_custom()

	############################################################################
	def about_to_quit_custom(self):
		"""
		PURPOSE: performs any needed cleanup before application quits
		ARGS: none
		RETURNS: none
		NOTES: this will be called for you before GUI quits so you never have 
			to call this
		"""
		#STUB override this if you need cleanup
		pass

	############################################################################
	def register_child(self, child_ctrlr):
		"""
		PURPOSE: registers a child controller with this one
		ARGS:
			child_ctrlr (Abstract_Ctrlr): child controller to register
		RETURNS: none
		NOTES: Abstract_Ctrlr will call this on its own in its constructor if 
			it has a parent so you never need to call this
		"""
		if child_ctrlr not in self.child_ctrlrs:
			self.child_ctrlrs.append(child_ctrlr)

################################################################################
###                               End of File                                ###
################################################################################