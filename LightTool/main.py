import hou
from PySide2 import QtCore, QtUiTools, QtWidgets
import random


class Lomus(QtWidgets.QWidget):
	def __init__(self):
		super(Lomus, self).__init__()
		ui_file = '/Users/sherifessam/Desktop/HoudiniLightingTool/Lomus.ui'
		self.ui = QtUiTools.QUiLoader().load(ui_file)
		self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)
		self.counter = 0
		self.count = 0
		self.cameraNode = ""
		self.currentGraph()
		self.geoNode = self.traverseSG("geo")
		self.lighChecker()
		self.cameraChecker()
		self.isEmpty = True
		# USE () for calling a function in a click event!!!
		self.ui.resolutionCombo.currentIndexChanged.connect(self.adjustResolution)
		self.show()

	def currentGraph(self):
		# This function gets the node graph and check for the geo imported
		# in the "file" type node

		# Get the active pane tab
		self.activePane = hou.ui.curDesktop().paneTabOfType(hou.paneTabType.NetworkEditor)
		if self.activePane:
			# Get the active node graph
			self.nodeGraph = self.activePane.pwd()
			if not self.nodeGraph:
				# Iterate through all nodes in the active node graph
				print("No active node graph found.")
		else:
			print("No active pane tab found.")

	def traverseSG(self, targetNodeName):
		# This function traverses the scene graph
		# searching for a node type
		self.goal = targetNodeName
		self.target = None
		for node in self.nodeGraph.allSubChildren():
			if node.type().name() == self.goal:
				self.target = node
				break
		return self.target

	def show(self):
		# show the UI
		self.adjustResolution()
		self.ui.show()

	def cameraChecker(self):
		self.cameraCreated = self.traverseSG("cam")
		if self.cameraCreated:
			hou.ui.displayMessage("camera already crated in the scene", title="Error", severity=hou.severityType.Error)
		else:
			# Donot use () for calling a function in a click event!!!
			self.ui.cameraCreateButton.clicked.connect(self.cameraCreator)

	def cameraCreator(self):
		if self.count < 1:
			self.cameraNode = self.nodeGraph.createNode('cam')
			self.cameraNode.setInput(0, self.geoNode)
			self.count += 1
		else:
			hou.ui.displayMessage("Already a camera has been created", title="Error", severity=hou.severityType.Error)

	def lighChecker(self):
		# generalize this code to make it more dynamic
		self.lightCreated = self.traverseSG("hlight::2.0")
		if self.lightCreated:
			hou.ui.displayMessage("light already crated in the scene", title="Error", severity=hou.severityType.Error)
		else:
			# Donot use () for calling a function in a click event!!!
			self.ui.lightCreateButton.clicked.connect(self.lightCreator)

	def lightCreator(self):

		self.x = random.randint(-2.0, 2.0)
		self.y = random.randint(-2.0, 2.0)
		self.z = random.randint(-2.0, 2.0)
		self.random_intensity = random.randint(3.0, 10.0)
		if self.counter < 4:
			self.light_node = self.nodeGraph.createNode('hlight')
			self.light_node.parmTuple('t').set((self.x, self.y, self.z))
			self.light_node.parm('light_intensity').set(self.random_intensity)
			self.light_node.setInput(0, self.geoNode)
			self.counter += 1
		else:
			hou.ui.displayMessage("Already 4 lights has been created", title="Error", severity=hou.severityType.Error)

	def adjustResolution(self):
		# This function aims to adjust the camera resolution
		self.resolutionList = ["640x480", "1280x720", "1920x1080", "3840x2160"]
		if self.isEmpty:
			self.ui.resolutionCombo.addItems(self.resolutionList)
			self.isEmpty = False
		else:
			self.currentText = self.ui.resolutionCombo.currentText()
			res1, res2 = self.currentText.split('x') if 'x' in self.currentText else (self.currentText, "")
			if self.cameraNode:
				self.cameraNode.parmTuple("res")[0].set(res1)
				self.cameraNode.parmTuple("res")[1].set(res2)


win = Lomus()
win.show()