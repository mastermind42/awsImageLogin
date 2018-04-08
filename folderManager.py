import pprint
'''Adam/
Adam/Adam1.jpg
Adam/Adam2.jpg
Adam/Adam3.jpg
Adam/AdamAustin.jpeg
Adam/AdamDog.jpeg
Adam/AdamOut.jpeg
Rohit/
Rohit/10172867_10152368704740540_8431385729323392007_n.jpg
Rohit/10636549_10153761344540540_6082609160550682960_o.jpg
Rohit/11267743_10153319015010540_7542964293192083036_o.jpg
Rohit/11406941_10153319015380540_9163284934602960591_n.jpg
Rohit/12314392_10153715174125540_709293903281691898_o.jpg
Rohit/13041050_10154021444215540_7604066996279735324_o.jpg
Rohit/23632001_10155698625310540_2053053207803241351_o.jpg
Test/
Test/Chicken/
Test/Chicken/Shamoopie/
Test/Kalabi/'''

class File:
  def __init__(self, info):
    self.name = info.name
    self.children = info.children
'''
class Folder:
  def __init__(self, info):
    self.name = info.name
    #self.children = info.children
  def addPath(self, entry):
    pathList = [x.split('/') for x in entry]
    for item in pathList:
      if(not item):
'''

class Node:
  def __init__(self, name, parent, fileOrFolder):
    self.childNodes = [] #children Nodes
    self.path = ''
    self.parentNode = parent # parents Nodes
    self.fileOrFolder = fileOrFolder # 0 for folder, 1 for else
    self.name = name # name of folder or file
  def addChildren(self, newChild):
    self.childNodes.append(newChild)
  def type(self):
    return self.name


class FolderManager:
  root = Node('root', '', 'File')
  def __init__(self, tree):
    self.treeList = [x.split('/') for x in tree]
    for line in self.treeList:
      


tree = ['Adam/', 'Adam/Adam1.jpg', 'Adam/Adam2.jpg', 'Adam/Adam3.jpg', 'Adam/AdamAustin.jpeg',
  'Adam/AdamDog.jpeg', 'Adam/AdamOut.jpeg', 'Rohit/', 'Rohit/10172867_10152368704740540_8431385729323392007_n.jpg',
  'Rohit/10636549_10153761344540540_6082609160550682960_o.jpg', 'Rohit/11267743_10153319015010540_7542964293192083036_o.jpg',
  'Rohit/11406941_10153319015380540_9163284934602960591_n.jpg', 'Rohit/12314392_10153715174125540_709293903281691898_o.jpg',
  'Rohit/13041050_10154021444215540_7604066996279735324_o.jpg', 'Rohit/23632001_10155698625310540_2053053207803241351_o.jpg',
  'Test/', 'Test/Chicken/', 'Test/Chicken/Shamoopie/', 'Test/Kalabi/']

treeList = [x.split('/') for x in tree]



pp = pprint.PrettyPrinter()
# pp.pprint(tree)

x = FolderManager(tree)
pp.pprint(x.tree)