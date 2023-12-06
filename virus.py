class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your your virus
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    virus2 = Virus("Bubonic Plague", 0.1, 0.6)
    assert virus2.name == "Bubonic Plague"
    assert virus2.repro_rate == 0.1
    assert virus2.mortality_rate == 0.6

    virus3 = Virus("Ebola", 0.5, 0.8)
    assert virus3.name == "Ebola"
    assert virus3.repro_rate == 0.5
    assert virus3.mortality_rate == 0.8

    virus4 = Virus("Smallpox", 0.3, 0.5)
    assert virus4.name == "Smallpox"
    assert virus4.repro_rate == 0.3
    assert virus4.mortality_rate == 0.5

    
