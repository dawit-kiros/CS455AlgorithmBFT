# Maze Problem Solver using Breadth-First Traversal

This repository contains a Python implementation and a technical report for solving the "Maze" problem using the Breadth-First Traversal (BFT) approach. The problem involves finding a path from a given starting point to a destination point in a maze represented by a 2D grid.

## Table of Contents

- [Introduction](#introduction)
- [Design](#design)
    - [Problem Understanding](#problem-understanding)
    - [Solution Investigation](#solution-investigation)
    - [Solution Selection](#solution-selection)
- [Implementation](#implementation)
- [Test](#test)
- [Enhancement Ideas](#enhancement-ideas)
- [Conclusion](#conclusion)

## Introduction

The "Maze" problem is a classic graph traversal problem where the objective is to determine if a path exists from a starting point to a destination point, navigating only through empty cells while avoiding walls. This repository presents a solution to the problem using the Breadth-First Traversal (BFT) algorithm.

## Design

### Problem Understanding

The problem requires finding a path in a maze represented as a 2D grid. Cells in the grid can be either walls or empty cells. The task is to navigate through the empty cells from the starting point to the destination point. The BFT algorithm is chosen due to its ability to find the shortest path.

### Solution Investigation

Two potential solutions were considered:
1. Depth-First Traversal (DFT)
2. Breadth-First Traversal (BFT)

While DFT explores as far as possible along each branch before backtracking, it does not guarantee the shortest path. BFT, on the other hand, explores all neighbors of a node before moving on to their child nodes, ensuring the shortest path is found.

### Solution Selection

Breadth-First Traversal (BFT) is selected as the solution due to its property of finding the shortest path. This aligns well with the problem's requirement to determine if a path exists and to find it efficiently.

## Implementation

The implementation uses a Python script that applies the BFT algorithm to the maze problem. It uses a queue to explore nodes level by level, navigating through empty cells and avoiding walls.

## Test

The implementation is tested using provided test data. An example test case and its expected output are provided in the code.

## Enhancement Ideas

Several enhancement ideas can be considered:

1. **Efficiency:** Optimize the algorithm by avoiding redundant visits to already explored cells.

## Conclusion

The Breadth-First Traversal approach effectively solves the Maze problem by finding the shortest path from a starting point to a destination point in a maze. The implementation showcases the power of graph traversal algorithms in solving real-world problems.

---


