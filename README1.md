# Movies Database Query Tool
This project implements a Python program to query a SQLite database containing information about movies, directors, actors, and ratings. The tool allows users to extract insights from the database using SQL queries.

## Features
- Connects to a SQLite database containing movies and related metadata.
- Allows users to execute custom SQL queries to retrieve data.
- Provides pre-defined query examples to:
  - List movies by a specific director or starring a specific actor.
  - Retrieve the top-rated movies or those released in a specific year.
  - Count the number of movies in each genre.
  - Search for movies by keywords in their titles.
- Outputs query results in a clear and readable format.

## Problem Addressed
Manually analyzing large datasets of movies can be inefficient and time-consuming. This tool automates the process, enabling users to efficiently explore, filter, and analyze movie data using SQL queries.

## How to Use
1. **Run the Program**: Execute the Python script to load the SQLite database:
   ```bash
   python movies.py
   ```
2. **Interact with the Tool**:
   - Use the pre-defined query options to explore the database.
   - Enter custom SQL queries for advanced analysis.
3. **View Results**: The program will display query results in a user-friendly format.

## Why This Project?
This project was part of my Harvard CS50x coursework, designed to deepen understanding of database management, SQL query writing, and Python programming while exploring practical applications in data analysis.
