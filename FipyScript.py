from fipy import *
# Mesh represents the geometry of the Solution
# A Mesh is composed of Cells
# Each Cell is defined by its bounding Vertex Objects
# A Variable is a quantity that changes throughout the evalutaion of the PDE
# MeshVariable consists of an array/ field like structure consisting of many values that is distributed over a field
a = Variable(value=3)
b = a + 32
print(b)
# An equation is a collection of terms, formed by adding or equating 