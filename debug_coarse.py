import copy

import numpy
import math


def GetMult(rows):
    found=False
    while found==False:
        istart=int(round(math.sqrt(rows)))
        for i in range(istart,rows):
            if rows%i==0:
                found=True
                return max(i,rows/i),min(i,rows/i)
        rows+=1


def GetPoro(x1, x2, parameters):
    # Show the image in the middle og the core

    rho_matrix = float(parameters[0])
    rho_fluid = float(parameters[1])
    M = float(parameters[2])
    P = float(parameters[3])
    Q = float(parameters[4])

    Density = M * (x1) + P * (x2) + Q
    Phi = (rho_matrix - Density) / (rho_matrix - rho_fluid)

    return Phi


def UpscalePoro(z, x, y, nblocks, n):
    new = numpy.ones((nblocks, nblocks))

    x = x / n
    x = x.astype(int)
    y = y / n
    y = y.astype(int)

    for xi, yi, zi in zip(x, y, z):
        for xii, yii, zii in zip(xi, yi, zi):
            print(new[xii][yii])
            new[xii][yii] += zii
    for i in enumerate(new):
        for j in enumerate(new[i[0]]):
            new[i[0]][j[0]] = j[1] / float(n ** 2)

    return new


x1 = numpy.random.rand(10, 10) * 1000  # low
x1 = x1.astype(dtype=int)
x2 = copy.deepcopy(x1) + 100  # high
x2 = x2.astype(dtype=int)
nblocks,n=GetMult(x1.shape[0])
x, y = numpy.meshgrid(numpy.arange(x1.shape[0]), numpy.arange(x1.shape[1]),indexing='ij')

parameters=[2650,1,-0.77,1.98,1007,36597.06,-35330.83,233946.02]
z=GetPoro(x1,x2,parameters)

poro_coarse=UpscalePoro(z,x,y,nblocks,n)

Padding_bottom = 0
Padding_top = 0
length = 20 # number os slices
nslices=length-Padding_bottom-Padding_top
nblocks_z,n_z=GetMult(nslices)
nblocks_z = int(nblocks_z)
PORO=numpy.zeros(shape=(nblocks_z,nblocks,nblocks))
ACTNUM=numpy.zeros(shape=(nblocks_z,nblocks,nblocks))
poro_coarse_avg=poro_coarse
for i in range(length):
    # PORO[int((i-Padding_top)/n_z)]=poro_coarse_avg
    # ACTNUM[(i-Padding_top)/n_z]=GetMaskedValues(poro_coarse_avg,0,0)
    poro_coarse_avg = poro_coarse_avg * (i - Padding_top) / ((i - Padding_top) + 1) + poro_coarse / (
            (i - Padding_top) + 1)
    coisa = 0

