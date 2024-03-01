# WaterJugChallenge

## Overview

This project provides a solution to the classic Water Jug Riddle using a FastAPI application. The challenge involves using two jugs with different capacities to measure a specific amount of water. The application allows users to input the capacities of the jugs and the desired amount of water to measure, and it provides a step-by-step solution if one exists.

## Installation

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd water-jug-challenge-solver
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the FastAPI Application

1. Navigate to the project directory.

2. Run the FastAPI application using Uvicorn:

    ```bash
    py -m uvicorn main:app --reload
    ```

3. Access the API at `http://localhost:8000/water_jug_solution/` and provide values for `x`, `y`, and `z` as query parameters to get the solution or the message indicating no solution.

### Running the Tests

1. Make sure you have installed the project dependencies, including pytest.

2. Navigate to the project directory.

3. Run the tests using pytest:

    ```bash
    pytest
    ```

## Implementation

### Problem Solving

The solution to the Water Jug problem is implemented using breadth-first search (BFS). The algorithm explores all possible states of the jugs, considering actions such as filling, emptying, and transferring water between the jugs. If a state is encountered where one of the jugs contains the desired amount of water, the algorithm terminates and returns the step-by-step solution. If no solution is possible, it returns a message indicating so.

### FastAPI Application

The FastAPI application provides a user-friendly interface for solving the Water Jug problem. It exposes a single GET endpoint `/water_jug_solution/` where users can input the capacities of the jugs (`x` and `y`) and the desired amount of water (`z`). The application then returns a JSON response containing the step-by-step solution if one exists or a message indicating no solution possible.
