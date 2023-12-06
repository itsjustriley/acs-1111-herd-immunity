import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus
import argparse



class Simulation(object):
    def __init__(self, virus, pop_size: int, vacc_percentage, initial_infected=1):
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        self.logger = Logger("log.txt")
        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected
        self.person_instances = self._create_population()
        self.newly_infected = []
        self.time_step_counter = 0
        self.total_vaxxed = 0
        self.healthy_interactions = 0
        self.total_interactions = 0

    def _create_population(self):
        people = []
        for i in range(0, self.pop_size):
            if i < self.initial_infected:
                people.append(Person(i, False, self.virus))
            else:
                people.append(Person(i, False))
        return people

    def _simulation_should_continue(self):
        for person in self.person_instances:
            if person.is_alive and person.is_vaccinated == False:
                return True
        return False

    def run(self):
        # This method starts the simulation. It should track the number of 
        # steps the simulation has run and check if the simulation should 
        # continue at the end of each step. 
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        should_continue = True

        while should_continue:
            self.time_step_counter += 1
            current_step = self.time_step_counter
            self.logger.log_time_step(current_step)
            self.time_step()
            should_continue = self._simulation_should_continue()
            

        reason_for_ending = self.find_reason()
        self.logger.final(self.time_step_counter, self.total_vaxxed, (self.pop_size-self.total_vaxxed), reason_for_ending)

    def time_step(self):
        active_infected = 0
        newly_vaccinated = 0
        died = 0
        alive = 0
        for person in self.person_instances:
            if person.is_alive:
                alive += 1
            if person.infection is not None and person.is_alive:
                active_infected += 1
                for i in range(100):
                    random_person = random.choice(self.person_instances)
                    while random_person.is_alive == False or random_person == person:
                        random_person = random.choice(self.person_instances)
                    self.interaction(random_person)
                if person.did_survive_infection(): 
                    newly_vaccinated += 1
                else:
                    died += 1
        self.total_vaxxed = self.total_vaxxed + newly_vaccinated
        total_living = alive - died
        total_deaths = self.pop_size - total_living
        total_infected = len(self.newly_infected)
        self.logger.log_interactions(active_infected, self.healthy_interactions, len(self.newly_infected))
        self.logger.log_infection_survival(died, newly_vaccinated, total_living, total_deaths, self.total_vaxxed, total_infected)
        self._infect_newly_infected()
        self.total_interactions += self.healthy_interactions
        self.healthy_interactions = 0


    def interaction(self, random_person):
        if random_person.is_vaccinated or random_person.infection is not None or random_person in self.newly_infected:
            pass
        else:
            self.healthy_interactions +=1
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)


    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus
        self.newly_infected = []

    def find_reason(self):
        living = []
        vaccinated = []
        dead = []
        for person in self.person_instances:
            if person.is_alive: 
                living.append(person)
                if person.is_vaccinated:
                    vaccinated.append(person)
                else: 
                    return "ERROR"
            else:
                dead.append(person)
        if len(living) == 0:
            return "Everyone is dead"
        elif len(vaccinated) == len(living):
            return "Everyone is vaccinated"
        else: 
            return "No healthy humans remain."
            
            


# if __name__ == "__main__":
#     # Test your simulation here
#     virus_name = "Sniffles"
#     repro_num = 0.5
#     mortality_rate = 0.12
#     virus = Virus(virus_name, repro_num, mortality_rate)

#     # Set some values used by the simulation
#     pop_size = 1000
#     vacc_percentage = 0.1
#     initial_infected = 10

#     # Make a new instance of the imulation
#     virus = Virus(virus_name, repro_num, mortality_rate)
#     sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)

    # sim.run()
parser = argparse.ArgumentParser(description="Virus Simulator")

parser.add_argument('population', type=int, help="The size of the population for the simulation")
parser.add_argument('vacc_percentage', type=float, help="The percentage of the population that is vaccinated")
parser.add_argument('virus_name', type=str, help="The name of the virus for the simulation")
parser.add_argument('mortality_rate', type=float, help="The mortality rate of the virus for the simulation")
parser.add_argument('repro_rate', type=float, help="The reproduction rate of the virus for the simulation")
parser.add_argument('initial_infected', type=int, help="The number of people initially infected with the virus")

args = parser.parse_args()

virus = Virus(args.virus_name, args.repro_rate, args.mortality_rate)
simulation = Simulation(virus, args.population, args.vacc_percentage, args.initial_infected)

simulation.run()