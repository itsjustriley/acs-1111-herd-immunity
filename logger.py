class Logger(object):
    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, 
                        basic_repro_num):
        f = open(self.file_name, "w")
        f.write("METADATA\n")
        f.write(f"Population size\t{pop_size}\n")
        f.write(f"Vaccination percentage\t{vacc_percentage}\n")
        f.write(f"Virus name\t{virus_name}\n")
        f.write(f"Mortality rate\t{mortality_rate}\n")
        f.write(f"Basic reproduction number\t{basic_repro_num}\n")
        f.write("------\n")
        f.close()


    def log_interactions(self, num_infected, number_of_interactions, number_of_new_infections):
        f = open(self.file_name, "a")
        f.write(f"{num_infected} infected people had {number_of_interactions} interactions with healthy people, resulting in {number_of_new_infections} new infections\n")
        f.close()

    def log_infection_survival(self, number_of_new_fatalities, number_of_new_vaccinations, total_alive, total_dead, total_vaccinated, total_infections):
        f = open(self.file_name, "a")
        f.write(f"{number_of_new_fatalities} people died from the infection\n")
        f.write(f"{number_of_new_vaccinations} people were vaccinated\n")
        f.write(f"{total_alive} people are alive\n")
        f.write(f"{total_vaccinated} people are vaccinated\n")
        f.write(f"{total_infections} infected remain.\n")
        f.write(f"{total_dead} people are dead\n")
        f.close()

    def log_time_step(self, time_step_number):
        f = open(self.file_name, "a")
        f.write("------\n")
        f.write(f"TIME STEP NUMBER: \t{time_step_number}\n")
        f.write("------\n")
        f.close()


    def final(self, time_step_number, total_alive, total_dead, reason):
        survival_rate = (total_alive / (total_alive + total_dead)) * 100
        f = open(self.file_name, "a")
        f.write("------\n")
        f.write(f"TOTAL TIME STEPS: \t{time_step_number}\n")
        f.write(f"REASON FOR ENDING: \t{reason}\n")
        f.write(f"Survivors: \t{total_alive}\n")
        f.write(f"Deaths: \t{total_dead}\n")
        f.write(f"Survival rate: {survival_rate}%\n")
        f.write("------\n")
        f.write("SIMULATION COMPLETE\n")
        f.write("------\n")
        f.close()

