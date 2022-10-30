from fipy import *

nx = 200
dx = 0.01
L = nx * dx
mesh = Grid1D(nx = nx, dx = dx) #generates mesh grid of 200 points, divisions of 0.01

potential = CellVariable(name="potential", mesh=mesh, value=0) #Creating the potential cell variable
electrons = CellVariable(name="e-", mesh=mesh)

permitivity = 1 #setting coeff of Diffusion Term for steady state
electrons.valence = -1
chargeDensity = electrons * electrons.valence #defining charge density
chargeDensity.name = "chargeDensity" 

equation_Poisson = (DiffusionTerm(coeff=permitivity) + chargeDensity == 0)
electrons.setValue(1)
potential.constrain(0, mesh.facesLeft)

equation_Poisson.solve(var=potential)
x = mesh.cellCenters[0]
phsi_AnalyticalSol = (x**2)/2 - 2*x 
potentialAnalytical = CellVariable(mesh=mesh, name="analytical solution", value=(phsi_AnalyticalSol))

view = Viewer(vars=(chargeDensity, potential, potentialAnalytical), datamin=0.0, datamax=1.)
view.plot()