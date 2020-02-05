nameList = ['Read', 'ColorCorrect', 'Glow', 'Glint']
xposit = 60 
nodeList = []

for i in nameList:
    x = nuke.createNode(i)
    # nodeList.append(x)

# for i in nodeList:
#     i['ypos'].setValue(xposit)
#     xposit = xposit - 10
#     print(xposit)

# nodeList[3]