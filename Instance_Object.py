#RandomInstances.py

import maya.cmds as cmds
import random

random.seed (1234)

result = cmds.ls ( orderedSelection = True )

print ('result: %s' % (result))  

transformName = result[0]

instanceGroupName = cmds.group ( empty =True, n=transformName + '_instance_grp#' )

for i in range (0, 50 ):

    instanceResult = cmds.instance ( transformName, n = transformName + '_instance#' )
    
    cmds.parent ( instanceResult, instanceGroupName )
    
    x = random.uniform (-10, 10,)
    y = random.uniform (20, 0,)
    z = random.uniform (-10, 10,)
    
    cmds.move ( x, y, z, instanceResult )
    
    xRot = random.uniform (0, 360)
    yRot = random.uniform (0, 360)
    zRot = random.uniform (0, 360)
    
    cmds.rotate (xRot, yRot, zRot, instanceResult)
    
    scalingFactor = random.uniform( 0.3, 1.5 )
    
    cmds.scale ( scalingFactor, scalingFactor, scalingFactor, instanceResult )
    
cmds.hide ( transformName ) #IDK

cmds.xform ( instanceGroupName, centerpivot = True )
    
    #print ('instance_result :' + str(instanceResult))