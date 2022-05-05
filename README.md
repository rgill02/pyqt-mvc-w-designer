# pyqt-mvc-w-designer
Framework for the Model-View-Controller GUI pattern using PyQt with Qt Designer

## Motivation
Python is my favorite programming language for prototyping and developing tools. Often these tools can benefit from a Graphical User Interface (GUI). I've always found it difficult to design and layout a GUI in code. Writing lines like "window.addButton(x=256, y=347)" just wasn't cutting it for me. Then I discovered PyQt and Qt Designer. Qt Designer is an application that lets you layout your Qt window or widget by dragging and dropping elements into a canvas. PyQt is a Qt library for python that allows the user interface (UI) files output by Qt Designer to be used to build Qt applications in python. This is exactly what I was looking for. However, I felt that using Qt Designer to develop PyQt applications did not lend itself well to the Model-View-Controller (MVC) design pattern, which I find the most intuitive for GUI development. This library aims to solve that problem. It allows you to design the visual components of your widgets or main application using Qt Designer (including nesting custom widgets inside other widgets) and create controllers for those widgets in python. It also gives you the option of placing your main widget inside a commonly used main window with a console output and other useful features. It allows you to develop a GUI in python using Qt Designer and the MVC pattern while decoupling the UI layout from the control code.

## How to Make an Application with pyqt-mvc-w-designer
### Install Qt Designer
Download and install Qt Designer [here](https://build-system.fman.io/qt-designer-download).

### Install pyqt-mvc-w-designer
TODO

## How to Contribute to pyqt-mvc-w-designer
TODO
