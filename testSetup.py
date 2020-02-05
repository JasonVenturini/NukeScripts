readnode = nuke.createNode('Read')

nameList = ['Read', 'ColorCorrect', 'Exposure', 'Glow', 'Glint']
xposit = 50 
nodeList = []

for i in nameList:
    x = nuke.createNode(i)
    nodeList.append(x)