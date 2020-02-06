strRepeats = nuke.getInput('Enter number of copies:', '10')

intRepeats = int(strRepeats)
bFirstLoop = True

#nukescripts.misc.clear_selection_recursive()
nRecGroup = nuke.nodes.Group()
nRecGroup.begin()

kX_Trans = nuke.Double_Knob('x_trans', 'Translate X:')
kX_Trans.setRange(-50., 50.)
kX_Trans.setValue(20.)
nRecGroup.addKnob(kX_Trans)

kY_Trans = nuke.Double_Knob('y_trans', 'Translate Y:')
kY_Trans.setRange(-50., 50.)
kY_Trans.setValue(20.)
nRecGroup.addKnob(kY_Trans)

kX_Rot = nuke.Double_Knob('rot', 'Rotate:')
kX_Rot.setRange(-20., 20.)
kX_Rot.setValue(0.)
nRecGroup.addKnob(kX_Rot)

kX_Scale = nuke.Double_Knob('scale', 'Scale:')
kX_Scale.setRange(-1., 3.)
kX_Scale.setValue(1.)
nRecGroup.addKnob(kX_Scale)

nInput = nuke.nodes.Input()
nDot = nuke.nodes.Dot()
nDot.setInput(0, nInput)

for i in range(iRepeats):
    nTrans = nuke.nodes.Transform(name = 'tform' + str(i), translate = 'parent.x_trans parent.y_trans', rotate = 'parent.rot', scale = 'parent.scale', center = '960 540')
    nMerge = nuke.nodes.Merge2(name = 'mer' + str(i))
    nMerge.setInput(1,nTrans

    if bFirstLoop:
        bFirstLoop = False
        nTrans.setInput(0, nDot)
        nMerge.setInput(0, nDot)
    else:
        nTrans.setInput(0, nPrevMerge)
        nMerge.setInput(0, nPrevMerge)

    nPrevMerge = nMerge 

nOutput = nuke.nodes.Output()
nOutput.setInput(0, nMerge)

nRecGroup.end()