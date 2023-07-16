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
        self.ui.lightCreate.clicked.connect(self.buttonClicked())
        # self.clicked_before = False

    def initialize_scene(self):
        global sceneRoot
        sceneRoot = hou.node('/obj/')

    def show(self):
        self.ui.show()

    def lightCreator(self):
        self.geo_node = hou.node('/obj/donut')
        self.light_node = sceneRoot.createNode('light')
        self.light_node.setInput(0, self.geo_node)

    def buttonClicked(self):
        # if self.clicked:
        self.x += 1
        for self.x in range(1, 5):
            if self.x < 5:
                self.lightCreator()
            else:
                hou.ui.displayMessage("Already 4 lights in the scene", title="Error", severity=hou.severityType.Error)
        # self.ui.lightCreate.clicked.connect(self.buttonClicked())


win = Lomus()
win.show()