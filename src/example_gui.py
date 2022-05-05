import logging

from pyqt_mvc_w_designer import GUI_Runner
from pyqt_mvc_w_designer import Example_Ctrlr

gui_runner = GUI_Runner.GUI_Runner(Example_Ctrlr.Example_Ctrlr, 
								   window_title="Example", show_console=True, 
								   log_lvl=logging.DEBUG)
gui_runner.run()