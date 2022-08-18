#cython: boundscheck=False, wraparound=False, nonecheck=False, language_level=3

import numpy as np
cimport numpy as np


def IFS(edgepoints, int cycles, float perc):
    cdef int dimensions = len(edgepoints[0])
    cdef list points = [[0] for i in range(dimensions)]
    cdef long[:] randpoints = np.random.randint(0,len(edgepoints.),cycles,dtype=long)
    cdef int i, j
    cdef float v, lastpoint, newpoint
    for i in range(1,cycles):
        for j,v in enumerate(edgepoints[randpoints[i]]):
            lastpoint = points[j][i-1]
            newpoint = lastpoint+(perc*(v-lastpoint))
            points[j].append(newpoint)
    return points

def branchingIFS(edgepoints, int cycles, float perc, int maxpaths=0):
    cdef int dimensions = len(edgepoints[0])
    cdef list points = []
    cdef list temp, edgepoints, lastpoint
    cdef int i, j, k, p
    
    cdef float v, newpoint
    for i in range(1,cycles):
        for edgepoint in edgepoints:
        lastpoints = [i[1] for i in points[i-1]]
            temp = []
            for p in edgepoint:
                
                newpoint = lastpoint+(perc*(v-lastpoint))
                points[j].append(newpoint)
    return points

#cimport cython
#from libc.stdlib cimport malloc, free
#
#def cIFS(list edgepoints, int cycles, float perc):
#    cdef int i, j
#    cdef float v, lp, np
#    cdef int numep = len(edgepoints)
#    cdef int dimensions = len(edgepoints[0])
#    cdef float *points = <float *>malloc(dimensions*cycles*cython.sizeof(float))
#    cdef float *epflat = <float *>malloc(dimensions*numep*cython.sizeof(float))
#    for i in range(numep):
#        for j in range(dimensions):
#            epflat[i+i+j] = edgepoints[i][j] # getting edgepoint: 2x numpoint and add dimension
#
    #with nogil:
    #    for i in range(1,cycles):
    #        for j,v in enumerate(random.choice(edgepoints)):
    #            lp = points[j][i-1]
    #            np = lp+(perc*(v-lp))
    #            points[j].append(np)
    #
    #    free(points)
    #    free(epflat)
    #
    #return points
