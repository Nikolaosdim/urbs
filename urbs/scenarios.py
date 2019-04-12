import pandas as pd

# SCENARIO GENERATORS
# In this script a variety of scenario generator functions are defined to
# facilitate scenario definitions.


def scenario_base(data):
    # do nothing
    return data


def scenario_co2_limit95(data):
    # change global CO2 limit
    global_prop = data['global_prop']
    for stf in global_prop.index.levels[0].tolist():
        global_prop.loc[(stf, 'CO2 limit'), 'value'] /= 4
    return data

def scenario_co2_nolimit(data):
    # change global CO2 limit
    global_prop = data['global_prop']
    for stf in global_prop.index.levels[0].tolist():
        global_prop.loc[(stf, 'CO2 limit'), 'value'] == inf
    return data

def scenario_all_together(data):
    # combine all other scenarios
    data = scenario_stock_prices(data)
    data = scenario_co2_limit(data)
    data = scenario_north_process_caps(data)
    return data
