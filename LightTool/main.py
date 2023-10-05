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
		self.currentGraph()
		self.click_count = 0
		# Donot use () for calling a function in a click event!!!
		self.ui.lightCreate.clicked.connect(self.lightCreator)


	def currentGraph(self):
		# This function gets the node graph and check for the geo imported
		# in the "file" type node

		# Get the active pane tab
		self.activePane = hou.ui.curDesktop().paneTabOfType(hou.paneTabType.NetworkEditor)

		if self.activePane:
			# Get the active node graph
			self.nodeGraph = self.activePane.pwd()

			if self.nodeGraph:
				# Iterate through all nodes in the active node graph
				for node in self.nodeGraph.allSubChildren():
					if node.type().name() == "geo":
						self.geoNode = node
						print("Geometry found", self.geoNode)

					else:
						break
			else:
				print("No active node graph found.")
		else:
			print("No active pane tab found.")

	def show(self):
		self.ui.show()

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


win = Lomus()
win.show()