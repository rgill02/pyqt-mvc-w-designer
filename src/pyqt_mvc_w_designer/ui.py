example_widg = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>example_widg</class>
 <widget class="QWidget" name="example_widg">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>961</width>
    <height>582</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <layout class="QHBoxLayout" name="horizontalLayout_2">
   <item>
    <layout class="QVBoxLayout" name="verticalLayout">
     <item>
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QLabel" name="label">
         <property name="text">
          <string>Message to Log:</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QLineEdit" name="msg_input">
         <property name="text">
          <string>Hello World!</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item>
      <widget class="QPushButton" name="debug_button">
       <property name="text">
        <string>DEBUG</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="info_button">
       <property name="text">
        <string>INFO</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="warning_button">
       <property name="text">
        <string>WARNING</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="error_button">
       <property name="text">
        <string>ERROR</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="critical_button">
       <property name="text">
        <string>CRITICAL</string>
       </property>
      </widget>
     </item>
    </layout>
   </item>
   <item>
    <layout class="QVBoxLayout" name="verticalLayout_2">
     <item>
      <widget class="QWidget" name="mpl_widg" native="true">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Preferred" vsizetype="Preferred">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="plot_button">
       <property name="text">
        <string>Plot Random</string>
       </property>
      </widget>
     </item>
    </layout>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

main_window = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>main_window</class>
 <widget class="QMainWindow" name="main_window">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1070</width>
    <height>799</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout_3">
    <item row="0" column="0">
     <widget class="QSplitter" name="splitter">
      <property name="orientation">
       <enum>Qt::Vertical</enum>
      </property>
      <property name="childrenCollapsible">
       <bool>false</bool>
      </property>
      <widget class="QFrame" name="frame_2">
       <property name="frameShape">
        <enum>QFrame::Box</enum>
       </property>
       <property name="frameShadow">
        <enum>QFrame::Plain</enum>
       </property>
       <layout class="QGridLayout" name="gridLayout_2">
        <item row="0" column="0">
         <widget class="QWidget" name="main_widg" native="true"/>
        </item>
       </layout>
      </widget>
      <widget class="QFrame" name="frame">
       <property name="minimumSize">
        <size>
         <width>0</width>
         <height>0</height>
        </size>
       </property>
       <property name="frameShape">
        <enum>QFrame::Box</enum>
       </property>
       <property name="frameShadow">
        <enum>QFrame::Plain</enum>
       </property>
       <layout class="QGridLayout" name="gridLayout">
        <item row="0" column="0">
         <layout class="QVBoxLayout" name="verticalLayout">
          <item>
           <widget class="QLabel" name="label">
            <property name="text">
             <string>Console:</string>
            </property>
           </widget>
          </item>
          <item>
           <widget class="QTextEdit" name="console_textedit">
            <property name="readOnly">
             <bool>true</bool>
            </property>
            <property name="html">
             <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
            </property>
           </widget>
          </item>
         </layout>
        </item>
       </layout>
      </widget>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>1070</width>
     <height>27</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

mpl_widg = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>mpl_widg</class>
 <widget class="QWidget" name="mpl_widg">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>734</width>
    <height>483</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <pointsize>12</pointsize>
   </font>
  </property>
  <property name="windowTitle">
   <string>mpl_widg</string>
  </property>
  <layout class="QGridLayout" name="gridLayout">
   <item row="0" column="0">
    <widget class="QFrame" name="frame">
     <property name="frameShape">
      <enum>QFrame::Box</enum>
     </property>
     <property name="frameShadow">
      <enum>QFrame::Plain</enum>
     </property>
     <layout class="QVBoxLayout" name="verticalLayout">
      <item>
       <widget class="QWidget" name="toolbar_widg" native="true"/>
      </item>
      <item>
       <widget class="QWidget" name="plot_widg" native="true"/>
      </item>
     </layout>
    </widget>
   </item>
  </layout>
 </widget>
 <resources/>
 <connections/>
</ui>
"""

