
# coding: utf-8

# In[1]:

from fipy import *


# In[2]:

nx=50
dx=1
mesh = Grid1D(nx=nx, dx=dx)


# In[3]:

phi = CellVariable(name="Solution variable", mesh=mesh, value=0.)


# In[4]:

D=1
valueLeft=0
valueRight=0
phi.constrain(valueLeft,mesh.facesLeft)
phi.constrain(valueRight,mesh.facesRight)
eqX=TransientTerm()==ExplicitDiffusionTerm(coeff = D)


# In[5]:

TimeStepDuration = 0.9 * dx**2/(2*D)
steps = 100


# In[6]:

phiAnalytical = CellVariable(name="analytical value", mesh=mesh)


# In[7]:

viewer = Viewer(vars=(phi, phiAnalytical), datamin=0., datamax=1.)
viewer.plot()


# In[8]:

x = mesh.cellCenters[0]
t = TimeStepDuration * steps


# In[9]:

try:
    from scipy.special import erf 
    phiAnalytical.setValue(1 - erf(x / (2 * numerix.sqrt(D * t)))) 
except ImportError:
    print "The SciPy library is not available to test the solution to     the transient diffusion equation"


# In[10]:

for step in range(steps):
    eqX.solve(var=phi, dt=TimeStepDuration)
    viewer.plot()


# In[11]:

print phi.allclose(phiAnalytical, atol = 7e-4) 


# In[12]:

raw_input("Explicit transient diffusion. Press <return> to proceed...")


# In[13]:

eqI = TransientTerm() == DiffusionTerm(coeff=D)


# In[ ]:

phi.setValue(valueRight)


# In[ ]:

TimeStepDuration*=10
steps//=10
for step in range(steps):
    eqI.solve(var=phi, dt=TimeStepDuration)
    viewer.plot()


# In[ ]:

print phi.allclose(phiAnalytical, atol = 7e-4)
1


# In[ ]:

raw_input("Implicit transient diffusion. Press <return> to proceed...")


# In[ ]:



