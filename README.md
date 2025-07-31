# Shark Attack Data Analysis

This project analyzes a dataset of shark attacks to identify patterns and trends. The analysis is performed using Python with the pandas, numpy, and fuzzywuzzy libraries. The data is cleaned and then visualized to answer several key questions about shark attacks.

## Project Structure

- `shark-attack.ipynb`: A Jupyter Notebook containing the main analysis and visualizations.
- `cleaning.py`: A Python script with functions for cleaning the raw data.
- `test_species_cleaning.py`: A script for testing the species cleaning function.
- `GSAF5.xls`: The raw data file containing shark attack records.
- `.gitignore`: A file specifying which files and directories to ignore in version control.

## Key Questions and Findings

The analysis in the notebook addresses the following questions:

1.  **Where do the most attacks happen?**
    - The top 5 countries for shark attacks are the USA, Australia, South Africa, New Zealand, and the Bahamas. These five countries account for approximately 70% of all recorded attacks.

2.  **What are the most dangerous activities?**
    - The top 5 most dangerous activities are:
        1. Surfing
        2. Swimming
        3. Fishing
        4. Diving
        5. Other

3.  **Is there a "shark season"?**
    - Yes, the summer months of June, July, and August see the highest number of attacks, with a peak in July. These three months account for 38% of all attacks.

4.  **What body parts do sharks target most often?**
    - The most commonly targeted body parts are:
        1. Leg / Foot
        2. Arm
        3. Hand / Fingers
        4. Body / Abdomen
        5. Shoulder

5.  **Who are the most common victims?**
    - **Sex:** 82% of victims are male, 17% are female, and 1% are unknown.
    - **Age:** The median age of victims is 24 years.

6.  **What are the most dangerous shark species?**
    - The top 5 most dangerous shark species are:
        1. Great White Shark
        2. Tiger Shark
        3. Bull Shark
        4. Oceanic Whitetip Shark
        5. Nurse Shark

## How to Run the Analysis

1.  **Install dependencies:**
    ```bash
    pip install pandas numpy fuzzywuzzy python-Levenshtein
    ```
2.  **Run the Jupyter Notebook:**
    ```bash
    jupyter notebook shark-attack.ipynb
    ```

## Data Cleaning

The `cleaning.py` script performs the following data cleaning steps:

- **Type:** Standardizes the `Type` column to consistent values like "Unprovoked", "Provoked", and "Unconfirmed".
- **Sex:** Cleans the `Sex` column, standardizing it to "M" for male and "F" for female.
- **Age:** Converts the `Age` column to a numeric type.
- **Date:** Extracts the month and year from the `Date` column.
- **Country and State:** Uses fuzzy matching to standardize country and state names.
- **Activity:** Categorizes activities into a predefined set of categories.
- **Species:** Standardizes shark species names using a predefined list and fuzzy matching.
- **Injury:** Categorizes injuries into body parts.
- **Fatal (Y/N):** Standardizes the `Fatal Y/N` column to "Yes" and "No".
