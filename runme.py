import os
import shutil
import urbs


input_files = 'Input'
result_name = 'Mimo-ex'
result_dir = urbs.prepare_result_directory(result_name)  # name + time stamp

# copy input file to result directory
try:
    shutil.copytree(input_files, os.path.join(result_dir, 'Input'))
except NotADirectoryError:
    shutil.copyfile(input_files, os.path.join(result_dir, input_files))
# copy runme.py to result directory
shutil.copy(__file__, result_dir)

# objective function
objective = 'cost' # set either 'cost' or 'CO2' as objective

# Choose Solver (cplex, glpk, gurobi, ...)
solver = 'glpk'

# simulation timesteps
(offset, length) = (3500, 168)  # time step selection
timesteps = range(offset, offset+length+1)
dt = 1  # length of each time step (unit: hours)

# detailed reporting commodity/sites
report_tuples = [
    (2050, 'Deutschland', 'Elec'),
    ]

# plotting commodities/sites
plot_tuples = [
    (2050, 'Deutschland', 'Elec'),  
    ]

# add or change plot colors
my_colors = {
    'Deutschland'(230, 200, 200),
    }
for country, color in my_colors.items():
    urbs.COLORS[country] = color

# select scenarios to be run
scenarios = [
             urbs.scenario_base,
			 urbs.scenario_co2_limit95,
			 scenario_co2_nolimit]

for scenario in scenarios:
    prob = urbs.run_scenario(input_files, solver, timesteps, scenario, 
                        result_dir, dt, objective, 
                        plot_tuples=plot_tuples,
                        plot_periods=plot_periods,
                        report_tuples=report_tuples)
