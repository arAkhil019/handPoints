import numpy as np
import math
# import plot_cords as pc

#gives angle w.r.t the x axis
def get_angle(a,b,c):
    radians = np.arctan2(c[1]-b[1],c[0]-b[0]) - np.arctan2(a[1]-b[1],a[0]-b[0])
    angle = np.abs(np.degrees(radians))
    return int(angle)

#to get angle between two lines points
def find_angle(p1, p2, p3):
    # Calculate the slopes of the lines
    m1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
    m2 = (p3[1] - p1[1]) / (p3[0] - p1[0])

    # Calculate the angle between the lines
    angle = np.abs(np.degrees(np.arctan((m2 - m1) / (1 + m1 * m2))))
    return int(angle)

def get3dAngle(p1, p2, p3):
    # Calculate the direction vectors of the lines
    v1 = np.array(p1) - np.array(p2)
    v2 = np.array(p3) - np.array(p2)

    # Calculate the dot product of the direction vectors
    dot_product = np.dot(v1, v2)

    # Calculate the magnitudes of the direction vectors
    magnitude_v1 = np.linalg.norm(v1)
    magnitude_v2 = np.linalg.norm(v2)

    # Calculate the angle between the lines using the dot product and magnitudes
    angle = np.degrees(np.arccos(dot_product / (magnitude_v1 * magnitude_v2)))

    return int(180-angle)

def findVectorAngle(v):
    # Calculate vector 'v' angles with axes
    mag_v = math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    # Calculate angles with planes XY, YZ, XZ using trigonometry
    x = math.degrees(math.acos(v[2] / mag_v))  # angle with XY plane
    y = math.degrees(math.acos(v[0] / mag_v))  # angle with YZ plane
    z = math.degrees(math.acos(v[1] / mag_v)) # angle with XZ plane
    
    return int(x), int(y), int(z)

def normalVector(p1, p2, p3): #correct and re-verified...
    v1 = np.array(p1) - np.array(p2)
    v2 = np.array(p3) - np.array(p2)
    # Calculate the normal vector
    normal = np.cross(v1, v2)
    return normal

def get_anglesList(landmarks):
    lm = landmarks
    angles = []
    order = [1,2,3,5,6,7,9,10,11,13,14,15,17,18,19,'x','y','z','rx','ry','rz','x0','y0']
    for i in range(1,21,4):
        a1 = get3dAngle(lm[0],lm[i],lm[i+1])
        a2 = get3dAngle(lm[i],lm[i+1],lm[i+2])
        a3 = get3dAngle(lm[i+1],lm[i+2],lm[i+3])
        angles.extend([a1,a2,a3])
    angles.extend(list(findVectorAngle(np.array(lm[0])-np.array(lm[9]))))
    angles.extend(list(findVectorAngle(normalVector(lm[5],lm[0],lm[17]))))
    return angles


lm = [(0.44525253772735596, 0.8821181654930115, 1.7824211795414158e-07), (0.5055185556411743, 0.8380296230316162, -0.0243961401283741), (0.5493906140327454, 0.7378312945365906, -0.029051801189780235), (0.5802724361419678, 0.6490132212638855, -0.03229646012187004), (0.6074903607368469, 0.5908128619194031, -0.036020874977111816), (0.5107137560844421, 0.5994343757629395, -0.01634802483022213), (0.5275915265083313, 0.4829970598220825, -0.027896881103515625), (0.5346592664718628, 0.412878155708313, -0.038733404129743576), (0.539794385433197, 0.34869176149368286, -0.0489971898496151), (0.47319844365119934, 0.5840516686439514, -0.017928840592503548), (0.4764889180660248, 0.451710045337677, -0.03053702600300312), (0.478690505027771, 0.3688320517539978, -0.04691867157816887), (0.47890427708625793, 0.29831063747406006, -0.06106304004788399), (0.4376070499420166, 0.5980817079544067, -0.022857332602143288), (0.4275026321411133, 0.4741858243942261, -0.041079629212617874), (0.42326098680496216, 0.3941417932510376, -0.060145117342472076), (0.4193558692932129, 0.3270990252494812, -0.0741955116391182), (0.40452608466148376, 0.6335333585739136, -0.029954329133033752), (0.38570255041122437, 0.5381184220314026, -0.05094871670007706), (0.37436172366142273, 0.47323834896087646, -0.0663001537322998), (0.36657142639160156, 0.41436171531677246, -0.07723076641559601)]
# print(findVectorAngle(normalVector(lm[5],lm[0],lm[17])),findVectorAngle(normalVector(lm[17],lm[0],lm[5])))

# print(get_angle((0,0),(1,1),(2,2))) used to test the get_angle function, was correct.

# print(normalVector((1,2,3),(0,0,0),(3,1,2)))
# print(findVectorAngle((-1,-7,5)),findVectorAngle((1,7,-5)))

def fromCords():
    with open('co-ordinates.txt', 'r') as f:
        lines = f.readlines()
        angles = ''
        for line in lines:
            landmarks = eval(line)
            angles += str(get_anglesList(landmarks))
            angles += '\n'
        with open('angles.txt', 'w') as f:
            f.write(angles)


# print(get3dAngle((3,0,0),(0,0,0),(-3,3,0))) was used to verfiy the get3dAngle function, was corrected.
# print(get_anglesList(lm))
# pc.plotter(landmarks,get_anglesList(landmarks))