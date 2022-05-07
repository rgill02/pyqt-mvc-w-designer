# pyqt-mvc-w-designer
Framework for the Model-View-Controller GUI pattern using PyQt with Qt Designer

## Motivation
Python is my favorite programming language for prototyping and developing tools. Often these tools can benefit from a Graphical User Interface (GUI). I've always found it difficult to design and layout a GUI in code. Writing lines like "window.addButton(x=256, y=347)" just wasn't cutting it for me. Then I discovered PyQt and Qt Designer. Qt Designer is an application that lets you layout your Qt window or widget by dragging and dropping elements into a canvas. PyQt is a Qt library for python that allows the user interface (UI) files output by Qt Designer to be used to build Qt applications in python. This is exactly what I was looking for. However, I felt that using Qt Designer to develop PyQt applications did not lend itself well to the Model-View-Controller (MVC) design pattern, which I find the most intuitive for GUI development. This library aims to solve that problem. It allows you to design the visual components of your widgets or main application using Qt Designer (including nesting custom widgets inside other widgets) and create controllers for those widgets in python. It also gives you the option of placing your main widget inside a commonly used main window with a console output and other useful features. It allows you to develop a GUI in python using Qt Designer and the MVC pattern while decoupling the UI layout from the control code.

## How to Make an Application with pyqt-mvc-w-designer
### Install Qt Designer
Download and install Qt Designer [here](https://build-system.fman.io/qt-designer-download).

### Install pyqt-mvc-w-designer
```
pip install pyqt-mvc-w-designer
```

### Design Your Widgets in Qt Designer
Create a new widget in Qt Designer. This can be for your main widget or a child widget; the process is exactly the same.

![Creating a new widget](https://github.com/rgill02/pyqt-mvc-w-designer/blob/master/doc/imgs/designer_startup_window.PNG)

Insert all the elements you want such as labels, buttons, etc. Give them recognizeable names, set their properties, and lay them out how you would like. If you want to embed a child widget in your widget just insert a regular "widget" as a placeholder as shown below. This is the process for embedding one of your own custom widgets, or one of the included widgets, for example the matplotlib plot widget.

![Embedding Child Widget](https://github.com/rgill02/pyqt-mvc-w-designer/blob/master/doc/imgs/designing_example_widg.PNG)

In the example above we are going to embed a matplotlib plot widget where our placeholder widget is. Once you have finished designing your widget, save the design as a ".ui" file, and you are done! You have now completed the "View" portion of the Model-View-Controller pattern.

### Create Controllers for Your Widgets
The practice in this framework is to have one controller per widget (per View). Create a new python class for your controller. I like to call it something like <widget_name>_Ctrlr. Make sure it inherits from "Abstract_Ctrlr". This is the base class for all controllers in this framework
```
class Example_Ctrlr(Abstract_Ctrlr):
    """
    Controller for the example widget
    """
```
You will have to import Abstract_Ctrlr. We will also import our child controllers, in this case the controller for the matplotlib plot widget.
```
from pyqt_mvc_w_designer.Abstract_Ctrlr import Abstract_Ctrlr
from pyqt_mvc_w_designer.Mpl_Ctrlr import Mpl_Ctrlr
```
The constructor's first argument must be the widget object this controller is going to control. It must also have keyword arguments for a parent controller and a logger to be passed in. If the widget you are controlling is a child widget embedded inside a parent widget, then your controller is a child controller to that parent widget's controller. So you would pass in that parent controller to parent keyword argument. The logger argument is used to pass in a logging.Logger from the standard logging module. The GUI framework has its own logger that should be passed in if you want to log to the console. If not logger is passed in then all logging calls within this controller are ignored.
```
def __init__(self, widg, parent=None, logger=None):
    #Call parent constructor
    ui_file = "example_widg.ui"
    with open(ui_file, "r") as fh:
        ui_content = fh.read()
    super().__init__(widg, ui_content, parent=parent, logger=logger)
```
The first thing you will want to do is call the parent constructor for abstract controller. It takes in the widg, parent, and logger arguments as well so you just pass those along. It also takes in the contents of the ui file though. Open the ui file corresponding to your widget and read in its contents (as a string, not binary). Pass the contents of the ui file to the parent constructor. This will initialize the widget passed in with the contents of the ui file. If you have any child widgets in your widget then you will have child controllers. Now is the time to set those up, right after calling the parent constructor.
```
#Setup mpl widget
self.mpl_ctrlr = Mpl_Ctrlr(self.widg.mpl_widg, self, self.logger)
```
We just create an instance of the child controller and pass in its widget (the placeholder widget that we named mpl_widg), ourself because we are its parent controller, and possibly a logger. Here we pass in our logger, because we assume we will be given the GUI logger. Now we can start doing things specific to our controller/widget. I like to connect all of my buttons and initialize all labels and inputs in the controller constructor.
```
self.widg.debug_button.clicked.connect(lambda : self.logger.debug(self.widg.msg_input.text()))
```
Here I have connected the clicked signal for the "debug button" to a function that will grab the input text from the msg_input field and log it under the debug logging level. If you have to perform any cleanup before your controller is destroyed when the application quits you can override the "about_to_quit_custom" method. This method will automatically be called before your controller is destroyed. The deepest child controllers are called first and then it works itself backwards up the tree.
```
def about_to_quit_custom(self):
    #STUB override this if you need cleanup
    print("I'm about to quit!")
```
All thats left is to make custom functions in your controller that update the UI, process data, save to a database, etc. and connect those to signals from your widget. You've now made your "Controller" portion of the Model-View-Controller.

### Creating an Application that Runs Your Main Controller and Displays Your Main Widget
To run your application you will need to use the "GUI_Runner" class.
```
from pyqt_mvc_w_designer.GUI_Runner import GUI_Runner
from pyqt_mvc_w_designer.Example_Ctrlr import Example_Ctrlr
```
Create an instance of a GUI_Runner and pass in your main controller class as well as a few other parameters.
```
gui_runner = GUI_Runner(Example_Ctrlr, window_title="Example", show_console=True, log_lvl=logging.DEBUG)
```
The first argument is the type of controller for your main controller, not an instance of your main controller. The GUI_Runner will create an instance of your controller. The following positional arguments will be passed to your controller during instantiation as *args. The "window_title" keyword argument is the name of the window your application runs in, this is optional and the default is an empty string. The "show_console" keyword argument should be set to True if you want to show the console where messages are logged to, and False if you want to hide it. This is also optional as the default is True. The "log_lvl" keyword argument is the logging level to use. This is a level type from the standard logging library. If you choose INFO then all debug messages will be ignored, just like the standard logging library. This is also optional as its default is INFO. Any other keyword arguments will be passed to your controller upon instantiation as **kwargs. The last step is to run your application. Note this is blocking.
```
gui_runner.run()
```
You have now created a PyQt application following the MVC pattern with this framework. Refer to [Example_Ctrlr.py](https://github.com/rgill02/pyqt-mvc-w-designer/blob/master/src/pyqt_mvc_w_designer/Example_Ctrlr.py) and [example_gui.py](https://github.com/rgill02/pyqt-mvc-w-designer/blob/master/src/example_gui.py) for the full code files for this example. Images of the example application are shown below with and without the console visible. This example application prints a user input message to the console at different logging levels and showcases the matplotlib plot widget by plotting a random signal. You can take a look at [example_widg.ui](https://github.com/rgill02/pyqt-mvc-w-designer/blob/master/src/pyqt_mvc_w_designer/ui/example_widg.ui) and [mpl_widg.ui](https://github.com/rgill02/pyqt-mvc-w-designer/blob/master/src/pyqt_mvc_w_designer/ui/mpl_widg.ui) for reference on how to design widgets like this. I'd recommend loading the UI files in Qt Designer.

![Example Application with No Console](https://github.com/rgill02/pyqt-mvc-w-designer/blob/master/doc/imgs/example_app_no_console.PNG)

![Example Application with Console](https://github.com/rgill02/pyqt-mvc-w-designer/blob/master/doc/imgs/example_app_with_console.PNG)

## Included Widgets/Controllers
TODO add tutorial for plot widget

## How to Contribute to pyqt-mvc-w-designer
TODO

## Author
Ryan Gill

## Support
Post an issue with what you need help with in the [issue tracker](https://github.com/rgill02/pyqt-mvc-w-designer/issues) and I'll do my best to get back to you.
