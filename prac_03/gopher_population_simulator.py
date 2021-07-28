"""
Simulate the population of gopher
"""
import random

MIN_BIRTH_RATE = 0.1
MAX_BIRTH_RATE = 0.2
MIN_DEATH_RATE = 0.05
MAX_DEATH_RATE = 0.25
STARTING_POPULATION = 1000
NUM_OF_YEARS = 10


def gopher_populate(population, min_rate, max_rate):
    """Populate gophers within a range from a population of gopher"""
    return int(population * random.uniform(min_rate, max_rate))


def main():
    """Generate a gopher population for a number of years"""
    print("Welcome to Gopher Population Simulator")
    population = STARTING_POPULATION
    print("Initial population: {0}".format(population))
    for i in range(0, NUM_OF_YEARS):
        if population <= 0:
            print("All gophers have died")
            break

        print("\nYear {0}".format((i + 1)))

        gopher_born = gopher_populate(population, MIN_BIRTH_RATE, MAX_BIRTH_RATE)
        gopher_died = gopher_populate(population, MIN_DEATH_RATE, MAX_DEATH_RATE)
        print("{0} gophers are born, {1} gophers died".format(gopher_born, gopher_died))

        population = population + gopher_born - gopher_died
        population = population if population > 0 else 0
        print("Current population: {0}".format(population))


if __name__ == "__main__":
    main()
