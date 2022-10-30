from fipy import *
from fipy.tools import numerix

nx = 50
dx = 1.
mesh = Grid1D(nx=nx, dx=dx)
phi = CellVariable(name="Solution Variable", mesh=mesh, value=0.0)
phiAnalytical = CellVariable(name="Analytical Solution", mesh=mesh)

D = 1
time = Variable()

valueRight = 0;
valueLeft = (1 + numerix.sin(time)) * 0.5

phi.constrain(valueLeft, mesh.facesLeft)
phi.constrain(valueRight, mesh.facesRight)

equation_Diffusion = TransientTerm() == DiffusionTerm(coeff=D)
view = Viewer(vars=(phi,phiAnalytical), datamin=0.0, datamax=1.0)

#variying the graph plot on time axis from 0.1s to 15s
dt = 0.1
while time() < 15:
    time.setValue(time() + dt)
    equation_Diffusion.solve(var = phi, dt = dt)
    view.plot()

