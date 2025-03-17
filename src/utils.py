"""
utils.py

This module provides utility functions for handling job data, 
including saving job listings to a CSV file.

Main functionalities:
1. Saves job data to a CSV file in a structured format.
2. Supports both **append mode** and **overwrite mode**.
3. Ensures UTF-8 encoding and proper CSV handling.

"""

import csv
import os

def save_to_csv(job_list, filename="scraped_jobs.csv", overwrite=False):
    """
    Saves job listings to a CSV file.

    :param job_list: List of job dictionaries to save.
    :param filename: Name of the CSV file (default: "scraped_jobs.csv").
    :param overwrite: If True, creates a new file instead of appending.
    """
    if not job_list:
        print("⚠️ No job data to save.")
        return

    # Determine mode: 'w' (overwrite) or 'a' (append)
    mode = 'w' if overwrite or not os.path.isfile(filename) else 'a'

    with open(filename, mode=mode, newline="", encoding="utf-8") as file:
        fieldnames = ["Company Name", "Required Skills", "Experience", "Salary", "Location", "More Info"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write headers only in 'w' mode (new file)
        if mode == 'w':
            writer.writeheader()

        # Write job data
        writer.writerows(job_list)

    print(f"Data successfully saved to {filename}")
