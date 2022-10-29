from fipy import * #imports all fipy modules
from scipy.special import erf
from fipy.tools import numerix

# 1D Diffusion mesh PDE equation

mesh = Grid1D(nx = 50, dx = 1) #creating a mesh to hold a 1d solution set
phi = CellVariable(name="Solution Variable", mesh=mesh,value=0) #sets the variable phi that will contain the solution set
phiAnalytical = CellVariable(name="Ananlytical Value", mesh=mesh) #sets the analytical value, which holds the analytical solution to solve the pde

view = Viewer(vars=(phi,phiAnalytical), datamin=0, datamax=1)

val_Left = 1 #Value for left boundary condition
val_Right = 0 #Value for right boundary condition
dx = 1
D = 1

#Setting the boundary conditions below
phi.constrain(val_Left, mesh.facesLeft)
phi.constrain(val_Right, mesh.facesRight)

#Representation of Equation using modules import from the fipy Object
diffusionEquation = TransientTerm() == ExplicitDiffusionTerm(coeff=D)

timeStepDuration = 0.9 * ( dx**2/(2*D) ) #The largest stable timestep that can be taken, limit steps to 90%
steps = 100

x = mesh.cellCenters[0]
t = timeStepDuration*steps

phiAnalytical.setValue(1 - erf(x / (2 * numerix.sqrt(D * t))))  #generates analytical equation
viewer = Viewer(vars=(phi, phiAnalytical),
                    datamin=0., datamax=1.)

for step in range(steps): #loop to generates solution set of pde
    diffusionEquation.solve(var=phi, dt=timeStepDuration)
    viewer.plot()

# Setting a larger timeStepDuration
eqI = TransientTerm() == DiffusionTerm(coeff=D)
newTimeStepDuration =  timeStepDuration * 10
steps //= 10

phi.setValue(val_Right)

#from below plot solutions are less accurate
for step in range(steps):
    eqI.solve(var=phi, dt=newTimeStepDuration)
    viewer.plot()






