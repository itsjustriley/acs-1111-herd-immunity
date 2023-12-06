import random
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = None):
        # A person has an id, is_vaccinated and possibly an infection
        self._id = _id  
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.is_alive = True

    def did_survive_infection(self):
        if self.infection is not None:
            if random.random() < self.infection.mortality_rate:
                self.is_alive = False
                return False
            else:
                self.is_vaccinated = True
                self.infection = None
                return True

if __name__ == "__main__":
    # This section is incomplete finish it and use it to test your Person class
    # TODO Define a vaccinated person and check their attributes
    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    # TODO Test unvaccinated_person's attributes here...
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

    # Test an infected person. An infected person has an infection/virus
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    infected_person = Person(3, False, virus)
    # TODO: complete your own assert statements that test
    # the values of each attribute
    # assert ...
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus

    
    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people. 
    # Create a list to hold 100 people. Use the loop below to make 100 people
    people = []
    for i in range(0, 100):
        people.append(Person(i, False, virus))

    # Now that you have a list of 100 people. Resolve whether the Person 
    # survives the infection or not by looping over the people list. 

    did_survive = 0
    did_not_survive = 0
    for person in people:
        # For each person call that person's did_survive_infection method
        survived = person.did_survive_infection()
        if survived:
            did_survive += 1
        else:
            did_not_survive += 1

    print(f"Survived: {did_survive}")
    print(f"Did not survive: {did_not_survive}")



    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 
    # Generate a random number. If that number is less than the 
    # infection rate of the virus that person is now infected. 
    # Assign the virus to that person's infection attribute. 

    # this didn't actually require making a list of people
    # but if I'll leave a commented version underneath!
    infected_count = 0
    uninfected_count = 0
    for i in range(0, 100):
        if random.random() < virus.repro_rate:
            infected_count += 1
        else:
            uninfected_count += 1

    # people = []
    # for i in range(0, 100):
    #     people.append(Person(i, False))
    
    # for person in people:
    #     if random.random() < virus.repro_rate:
    #         person.infection = virus

    # infected_count = 0
    # uninfected_count = 0
    # for person in people:
    #     if person.infection is not None:
    #         infected_count += 1
    #     else:
    #         uninfected_count += 1


    
    print(f"Infected: {infected_count}")
    print(f"Uninfected: {uninfected_count}")