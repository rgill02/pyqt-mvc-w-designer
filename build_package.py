################################################################################
###                                 Imports                                  ###
################################################################################
import os
import subprocess
import argparse

################################################################################
###                                  Main                                    ###
################################################################################
#Get command line arguments
parser = argparse.ArgumentParser(description="Builds package so nothing has to be dynamically loaded")
parser.add_argument("-n", "--no_pyinstaller", action="store_true", help="Skips running pyinstaller")
args = parser.parse_args()

#Find directories
cur_dir = os.path.dirname(os.path.realpath(__file__))
src_dir = os.path.join(cur_dir, "src")
pyqt_mvc_dir = os.path.join(src_dir, "pyqt_mvc_w_designer")
ui_dir = os.path.join(pyqt_mvc_dir, "ui")

#Find all ui files
ui_files = [f for f in os.listdir(ui_dir) if f.endswith(".ui")]

#Read each ui file and save to python file
code_fname = os.path.join(pyqt_mvc_dir, "ui.py")
with open(code_fname, 'w') as fh:
	for ui_file in ui_files:
		ui_no_ext = ui_file[:-3]
		ui_full_path = os.path.join(ui_dir, ui_file)
		with open(ui_full_path, 'r') as ui_fh:
			ui_text = ui_fh.read()
		fh.write('%s = """%s"""\n\n' % (ui_no_ext, ui_text))

#Build example_gui to test package works with pyinstaller
if not args.no_pyinstaller:
	example_gui_fname = os.path.join(src_dir, "example_gui.py")
	subprocess.run(["pyinstaller", "--onefile", example_gui_fname])

################################################################################
###                               End of File                                ###
################################################################################