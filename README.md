# Drone-Delivery-Service

## Drone Delivery Project

This project is a console application that simulates the delivery of packages using drones. The goal is to distribute the packages among the drones and highlighting the most efficient deliveries for each drone to make on each trip.

## Instructions
An **input.txt** file must be provided to execute this project. The file should have the following structure:

```
Line 1: [Drone #1 Name], [#1 Maximum Weight], [Drone #2 Name], [#2 Maximum Weight], etc.
Line 2: [Location #1 Name], [Location #1 Package Weight]
Line 3: [Location #2 Name], [Location #2 Package Weight]
Line 4: [Location #3 Name], [Location #3 Package Weight]
Etc.
```

To execute the code make sure to have Python installed. Then, run the command:

```
python drone.py
```

An **output.txt** should be created containing the following structured based on the input provided:

```
[Drone #1 Name]
Trip #1
[Location #2 Name], [Location #3 Name]
Trip #2
[Location #1 Name]
[Drone #2 Name]
Trip #1
[Location #4 Name], [Location #7 Name]
Trip #2
[Location #5 Name], [Location #6 Name]
```

## Algorithm

This code is implementing a version of the Greedy Algorithm for the Knapsack Problem. The Knapsack Problem is a problem in combinatorial optimization: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. This algorithm is effective in this case because it ensures that the drones are utilized as much as possible.

## Walk Through Solution

The drones and locations are sorted in descending order based on their maximum weight and delivery weight respectively. Then, deliveries are assigned to each drone by iterating over the list of locations and for each location, it checks if the drone has enough remaining capacity to carry the delivery. If it does, the location is added to the drone’s current trip and removed from the list of locations. This process continues until there are no more locations left or none of the drones can carry the remaining locations.

## Technical Dependencies and Libraries

This project uses Python and was developed using VIsual Studio Code as the code editor.


