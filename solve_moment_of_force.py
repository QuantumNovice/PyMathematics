from numpy import *


system = [
    ['br', 0,0,''],
    ['w', 5,0,800*9.81],
    ['st', 10,0,'']
    ]

SF = ''
SFI = 0
for force in system:
    if force[3] == '':
        SF += force[0]+'+'
    else:
        SFI += force[3]
        
SF += str(SFI)
print(SF)
