import hou
from PySide2 import QtCore, QtUiTools, QtWidgets

class Lomus(QtWidgets.QWidget):
    def __init__(self):
        super(Lomus, self).__init__()
        ui_file = '/Users/sherifessam/Desktop/HoudiniLightingTool/Lomus.ui'
        self.ui = QtUiTools.QUiLoader().load(ui_file)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)
        self.x = 0
        self.initialize_scene()
        self.ui.lightCreate.clicked.connect(self.buttonClick)


    def initialize_scene(self):
        global sceneRoot
        sceneRoot = hou.node('/obj/')

    def show(self):
        self.ui.show()

    def buttonClick(self):
        self.lightCreator()


    def lightCreator(self):
        self.geo_node = hou.node('/obj/donut')
        if self.x < 4:
            self.light_node = sceneRoot.createNode('light')
            self.light_node.setInput(0, self.geo_node)
            self.x += 1
        else:
            hou.ui.displayMessage("Already 4 lights in the scene", title="Error", severity=hou.severityType.Error)



win = Lomus()
win.show()