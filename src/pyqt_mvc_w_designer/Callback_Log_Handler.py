################################################################################
###                                 Imports                                  ###
################################################################################
#Standard imports
import logging

################################################################################
###                                Class Def                                 ###
################################################################################
class Callback_Log_Handler(logging.Handler):
	"""
	Logging handler that passes the record to a given callback function
	"""
	############################################################################
	def __init__(self, log_cb):
		"""
		PURPOSE: creates a new Callback_Log_Handler
		ARGS:
			log_cb (func): callback function to pass log record to
		RETURNS: new instance of an Callback_Log_Handler
		NOTES:
		"""
		#Call parent constructor
		super().__init__()

		#Save callback
		self.log_cb = log_cb

	############################################################################
	def emit(self, record):
		"""
		PURPOSE: passes log record to callback function
		ARGS:
			record (logging.record): record to log
		RETURNS: none
		NOTES:
		"""
		self.log_cb(record)

################################################################################
###                               End of File                                ###
################################################################################