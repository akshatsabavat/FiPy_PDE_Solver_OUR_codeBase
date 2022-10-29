from fipy import * #imports all the necessary modules of FiPy
# Mesh represents the geometry of the Solution
# A Mesh is composed of Cells
# Each Cell is defined by its bounding Vertex Objects
# A Variable is a quantity that changes throughout the evalutaion of the PDE
# MeshVariable consists of an array/ field like structure consisting of many values that is distributed over a field
# The SparseMatrix defines an equations solution
# The BoundaryConditions are used to describe the conditions of the Boundary on the Mesh
# Viewer is used to see the values of the solved variables

a = Variable(value=3) #defining a as a variable of Value = 3
b = a + 32
print(b)

# An equation is a collection of terms, formed by adding or equating 
