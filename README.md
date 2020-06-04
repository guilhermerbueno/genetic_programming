# genetic_programming
Learning genetic algorithm and genetic programming

# What is genetic algorithm (GA)
It's a kind of evolutionary algorithm to solve optimization problems.

The GA is composite by:

1. Population: What is the size of population?
2. Individuals

There are some steps well defined on GA:

**1. Initial population:** Represents the elements that starts the algorithm.
**2. Cross over:** The process of two selected parents generated descendants. For instance: P1 and P2 are the parents with the following chromossomes P1 = (0,1,0,0,1,1,0,1) and P2 = (1,1,1,0,0,0,1,0). The crossover could be n-points or uniform. Analyzing a 1-point crossover on 3 chromossome these parents will generate the following offsprings D1 = (0,1,0,0,0,0,1,0) and D2 = (1,1,1,0,1,1,0,1).
**3. Mutation:** In nature mutation is a kind of error on 'copy' genes and we try to reproduce it on GA. This step ends the reproduce phases.
**4. Merge:** Merging the parents with the descendants to generate a new population with the right size. The worst members are discarted.
**5. Selection:** It's the process to select parents to create the next generations of individuals. This process could be done:
    **5.1. Random:** Select the parents randomly is not effective because weak parents could be selected
    **5.2. Tournament:** Selecting few elements (like 5) and do a tournament between them, the winner will be selected
    **5.3. Roulette wheel:** It's a kind of probability selection
