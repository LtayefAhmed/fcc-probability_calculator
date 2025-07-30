# Probability Calculator - Final freeCodeCamp Certification Project

This repository contains my solution for the "Probability Calculator" project. This is the fifth and final project required to earn the "Scientific Computing with Python" certification from freeCodeCamp.

## Project Overview

This project is a Python program that calculates the approximate probability of drawing a specific set of balls from a hat containing a random assortment of colored balls. It utilizes a Monte Carlo simulation method to run a large number of experiments and estimate the probability based on the outcomes.

The project consists of two main parts:
1.  A `Hat` class that can be initialized with a variable number of balls of different colors and has a `draw` method to randomly pull a specified number of balls.
2.  An `experiment` function that takes a `Hat` object, the expected balls, the number of balls to draw, and the number of experiments to run. It then performs the simulation and returns the calculated probability.

## Key Skills & Concepts Demonstrated

*   **Object-Oriented Programming:** The `Hat` class encapsulates the state and behavior of the main object in the simulation.
*   **Monte Carlo Simulation:** The core of the project is a statistical simulation method used to approximate probabilities that would be difficult to calculate theoretically.
*   **Deep Copying Objects:** Correctly using `copy.deepcopy()` to ensure that each experiment in the simulation is independent and starts with an identical state.
*   **Data Structures:** Effective use of lists and dictionaries to manage the contents of the hat and to count the outcomes of the random draws.
*   **Python Standard Library:** Proficient use of the `random` module for the core drawing logic and the `copy` module for state management.

---

This project marks the successful completion of the "Scientific Computing with Python" curriculum, demonstrating a solid foundation in Python programming, object-oriented principles, and algorithmic problem-solving.
