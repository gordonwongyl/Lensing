# 1 Jupyter notebooks
The 3 notebooks are loacated in the results folder. They are used for plotting glafic results. The glafic configuration files can be find in the files in their respective lens models. 
## Plots.ipynb
This is used to plot the caustic, the predicted positions of the images and the position and flux errors. To run, read the .dat file to the variable result
and manually change the observational data above. You cal also use LENS and CONSTRAINT variable pick out the model and constraints used, depending on how you chose to name the files.
```python
# Reading from files
# in the order of [imA, imB, imC, imD] 
names = ['A', 'B', 'C', 'D']
obs_position = [(1.066,0.323), (0.,0.), (0.721,1.159), (-0.157,1.021)]
obs_posx = [1.066, 0., 0.721, -0.157]
obs_posy = [0.323, 0., 1.159, 1.021]
position_err = [0.01, 0.01, 0.01, 0.01]
obs_flux = [1.0, 0.65, 1.25, 1.17]
flux_err = [0.04, 0.04, 0.03, 0.04]
color = ['g', 'r', 'b', 'y']

LENS = "sie"
CONSTRAINT = "mcmc2"

result = pd.read_csv('../'+LENS+'/out_point_'+CONSTRAINT+'.dat', sep='\s+', skiprows=1, header=None, names=['pos_x', 'pos_y', 'mag', 'timedelay'])
result = pd.DataFrame(result)
```

## Mass.ipynb
This is for plotting the mass profile of the models. Probably not very helpful.

## Mcmc.ipynb
This is for plotting the distribution and corner plots of an mcmc run. Similar to plots.ipynb, load the file to mcmc_result.
```python
LENS = 'nfw'
CONSTRAINT = 'pos_second_iteration'
mcmc_result = pd.read_csv("../" + LENS + f"/out_mcmc_{CONSTRAINT}.dat", sep='\s+')
```
# 2. Naming for .dat files
## obs files
- obs_point.dat: position constraint only
- obs_point2.dat: position and flux constraint
- obs_point3.dat: flux constraint only

## output files
Generally, the name consists of the type of operations, constraints used maybe some indexing if I retry the same thing. 

# 3. Figures
They can be found in the fig file. Their naming is similar to that of output files. 
