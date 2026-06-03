
# Job Scheduling Problem Optimization using Genetic Algorithm
This repository contains a Python project developed as a Final Term Project for the 1st Year Introduction to Programming school course. The project optimizes the sequence of multiple jobs in a single-machine production environment using Genetic Algorithm (GA) steps to minimize the total weighted lateness cost.

# Project Objectives
The algorithm combines heuristic approaches with logic to achieve the following pipeline:

Random Population: Generates initial random job sequences and evaluates the exact lateness cost for each sequence.
Selection: Identifies the top two best solutions with the lowest costs to use as parents.
Crossover: Combines the parent sequences using Single-Point Permutation Crossover to create new generations without creating duplicate job IDs (not in validation).
Mutation: Applies Swap Mutation (swapping two random indexes) to escape local optima and maintain diversity.
Result: Finds the most optimal job schedule at the end of the generations.

# Real-World Use Cases (Business Applications)
This optimization algorithm can be directly adapted to solve scheduling problems in various industries. For example; Manufacturing & Job-Shop Scheduling, E-commerce Logistics & Delivery,Cloud Computing & Data Processing.
