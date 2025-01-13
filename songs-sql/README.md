# Songs Database Query Tool
This project implements a Python program to query a SQLite database containing information about songs, artists, albums, and genres. The tool enables users to extract meaningful insights from the database using SQL queries.

## Features
- Connects to a SQLite database containing songs and related metadata.
- Allows users to execute custom SQL queries to retrieve data.
- Provides pre-defined query examples to:
  - List songs by a specific artist or album.
  - Count the number of songs in each genre.
  - Retrieve the longest or shortest songs.
  - Search for songs by keywords in their titles.
- Outputs query results in a clear and readable format.

## Problem Addressed
Analyzing music metadata manually can be cumbersome and inefficient. This tool automates the process, allowing users to explore, filter, and analyze song data with SQL queries.

## How to Use
1. **Run the Program**: Execute the Python script to load the SQLite database:
   ```bash
   python songs.py
   ```
2. **Interact with the Tool**:
   - Use the pre-defined query options to explore the database.
   - Enter custom SQL queries to perform advanced analysis.
3. **View Results**: The program will display query results in a user-friendly format.

## Why This Project?
This project was part of my Harvard CS50x coursework, designed to introduce database management and SQL query writing, as well as reinforce Python programming skills.
