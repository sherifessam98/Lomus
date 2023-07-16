import hou
from PySide2 import QtCore, QtUiTools, QtWidgets

class Lomus(QtWidgets.QWidget):
	def __init__(self):
		super(Lomus, self).__init__()
		ui_file = '/Users/sherifessam/Desktop/HoudiniLightingTool/Lomus.ui'
		self.ui = QtUiTools.QUiLoader().load(ui_file)
		self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)
		self.ui.lightCreate.clicked.connect(self.buttonClicked)
		self.initialize_scene()


	def initialize_scene(self):
		global sceneRoot
		sceneRoot = hou.node('/obj/')

	def show(self):
	    self.ui.show()

	def buttonClicked(self):
		self.lightCreator()


	def lightCreator(self):
		self.light_node = sceneRoot.createNode('light')
		self.geo_node = sceneRoot.node('/obj/jhgjgh')
		self.light_node.parm('lookat').set(self.geo_node.path())






win = Lomus()
win.show()