import mesa
from wolf_sheep.model import WolfSheep
import pandas as pd

def experiment_001 ():

    # Parâmetros padrões da simulação
    # Sem canibalismo

    params = {
        "width": 20,
        "height": 20,
        "initial_sheep": 100,
        "initial_wolves": 50,
        "sheep_reproduce" :0.04,
        "wolf_reproduce": 0.05,
        "wolf_gain_from_food": 20,
        "grass": False,
        "grass_regrowth_time": 30,
        "sheep_gain_from_food": 4,
        "cannibalism_threshold": -1,
        "wolf_gain_from_cannibalism": 10
        }
    
    results = mesa.batch_run(
        WolfSheep,
        parameters=params,
        iterations=100,
        max_steps=300,
        number_processes=1,
        display_progress=True,
    )

    results_df = pd.DataFrame(results)
    results_df.to_csv("experiment_wolfsheep_2022-01-17_normal.csv")

def experiment_002 ():

    # Parâmetros padrões da simulação
    # Valor de corte para canibalismo: 2
    # Energia ganhada por canibalismo: 10

    params = {
        "width": 20,
        "height": 20,
        "initial_sheep": 100,
        "initial_wolves": 50,
        "sheep_reproduce" :0.04,
        "wolf_reproduce": 0.05,
        "wolf_gain_from_food": 20,
        "grass": False,
        "grass_regrowth_time": 30,
        "sheep_gain_from_food": 4,
        "cannibalism_threshold": 2, # Alteração aqui
        "wolf_gain_from_cannibalism": 10
        }
    
    results = mesa.batch_run(
        WolfSheep,
        parameters=params,
        iterations=100,
        max_steps=300,
        number_processes=1,
        display_progress=True,
    )

    results_df = pd.DataFrame(results)
    results_df.to_csv("experiment_wolfsheep_2022-01-17_can-thre-2_can-gain-10.csv")

def experiment_003 ():

    # Parâmetros padrões da simulação
    # Valor de corte para canibalismo: 5
    # Energia ganhada por canibalismo: 10

    params = {
        "width": 20,
        "height": 20,
        "initial_sheep": 100,
        "initial_wolves": 50,
        "sheep_reproduce" :0.04,
        "wolf_reproduce": 0.05,
        "wolf_gain_from_food": 20,
        "grass": False,
        "grass_regrowth_time": 30,
        "sheep_gain_from_food": 4,
        "cannibalism_threshold": 5, # Alteração aqui
        "wolf_gain_from_cannibalism": 10
        }
    
    results = mesa.batch_run(
        WolfSheep,
        parameters=params,
        iterations=100,
        max_steps=300,
        number_processes=1,
        display_progress=True,
    )

    results_df = pd.DataFrame(results)
    results_df.to_csv("experiment_wolfsheep_2022-01-17_can-thre-5_can-gain-10.csv")


def experiment_004 ():

    # Parâmetros padrões da simulação
    # Valor de corte para canibalismo: 5
    # Energia ganhada por canibalismo: 10

    params = {
        "width": 20,
        "height": 20,
        "initial_sheep": 100,
        "initial_wolves": 50,
        "sheep_reproduce" :0.04,
        "wolf_reproduce": 0.05,
        "wolf_gain_from_food": 20,
        "grass": True,
        "grass_regrowth_time": 30,
        "sheep_gain_from_food": 4,
        "cannibalism_threshold": range(-1, 11, 3), # Alteração aqui
        "wolf_gain_from_cannibalism": 10
        }

    results = results = mesa.batch_run(
        WolfSheep,
        parameters=params,
        iterations=500,
        max_steps=350,
        number_processes=1,
        display_progress=True,
    )

    results_df = pd.DataFrame(results)
    results_df.to_csv("experiment_wolfsheep_2022-02-02_can-thre-minus1-to-8_can-gain-10-350maxsteps_grass-true.csv")

# experiment_001()
# experiment_002()
#experiment_003()
experiment_004()