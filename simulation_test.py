from simulation import Simulation
from virus import Virus

# tests for simulation.py
# note - you must comment out the argparse section in the main simulation file for this to work

if __name__ == "__main__":
    virus_name = "Disease-itis"
    repro_num = 0.5
    mortality_rate = 0.5
    virus = Virus(virus_name, repro_num, mortality_rate)
    pop_size = 100
    vacc_percentage = 0.0
    initial_infected = 1
    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    sim.run()