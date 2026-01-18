
# NBA Player Performance Analysis

Python • NumPy • Data Analytics

## Overview

This project analyzes NBA player performance across multiple games using
Python and NumPy. It demonstrates data cleaning, reshaping, aggregation,
metric creation, ranking, and basic statistical analysis, targeted for a
Junior Data Analyst role.

## Dataset Description

Each row represents one player's performance in one game.

Columns: - Team ID - Points - Rebounds - Assists - Minutes - Win (0 =
Loss, 1 = Win)

The dataset includes 5 players across 3 games.

## Key Steps

### Data Cleaning

Removed team_id as it is categorical and not relevant for numerical
analysis.

### Data Reshaping

Reshaped the data into a 3D array: (games, players, statistics) to
enable clean aggregation.

### Aggregation

Calculated totals and averages for points, minutes, and wins using
vectorized NumPy operations.

### Efficiency Metric

Defined a simple efficiency score: Efficiency = Points + Rebounds +
Assists

### Ranking

Ranked players by points per game and efficiency using NumPy sorting.

### Statistical Insight

Calculated correlation between points scored and game outcomes.

## Technologies Used

-   Python
-   NumPy

## Purpose

Created to demonstrate foundational data analytics skills for a Junior
Data Analyst position.
