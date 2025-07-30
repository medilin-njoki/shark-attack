import numpy as np
import pandas as pd
from pycountry import countries
from fuzzywuzzy import process

# clean the colunm 'Type' in df
def clean_type(raw_shark_attack_df):
    shark_attack_df = raw_shark_attack_df.copy()
    shark_attack_df['Type'] = shark_attack_df['Type'].replace({'?': 'Unconfirmed', 
                                                          'Unverified': 'Unconfirmed', 
                                                          'Invalid': 'Unconfirmed',
                                                          'Questionable': 'Unconfirmed',
                                                          pd.NA: 'Unconfirmed',
                                                          'unprovoked': 'Unprovoked',
                                                          ' Provoked': 'Provoked',
                                                          'Boat': 'Watercraft'})
    return shark_attack_df

def clean_sex(raw_shark_attack_df):
    shark_attack_df = raw_shark_attack_df.copy()
    shark_attack_df['Sex'] = shark_attack_df['Sex'].str.strip()
    shark_attack_df['Sex'] = shark_attack_df['Sex'].str.upper()
    shark_attack_df['Sex'] = shark_attack_df['Sex'].replace('.', np.nan)
    shark_attack_df['Sex'] = shark_attack_df['Sex'].replace({'LLI': 'M', 
                                                          'M X 2': 'M', 
                                                          'N': 'M',
                                                          '.': np.nan,})
    return shark_attack_df

def clean_age(raw_shark_attack_df):
    shark_attack_df = raw_shark_attack_df.copy()
    shark_attack_df['Age'] = pd.to_numeric(shark_attack_df['Age'], errors='coerce').astype('Int64')
    return shark_attack_df

def drop_useless_columns(raw_shark_attack_df):
    return raw_shark_attack_df.drop(columns=['Case Number'
                                                    , 'Name'
                                                    , 'Source'
                                                    , 'pdf'
                                                    , 'href formula'
                                                    , 'href', 'Case Number.1'
                                                    , 'original order'
                                                    ,'Unnamed: 21','Unnamed: 22'
                                                    ], errors='ignore')

def clean_date(raw_shark_attack_df):
    shark_attack_df = raw_shark_attack_df.copy()
    
    # Extract month from Date column
    shark_attack_df['Month'] = shark_attack_df['Date'].str.extract(r'(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)', expand=False)
    
    # Map abbreviated months to full names
    month_map = {'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April', 
                 'Jun': 'June', 'Jul': 'July', 'Aug': 'August', 'Sep': 'September', 
                 'Oct': 'October', 'Nov': 'November', 'Dec': 'December'}
    shark_attack_df['Month'] = shark_attack_df['Month'].replace(month_map)
    
    # Clean Year column - convert to integer, handle 0 values
    shark_attack_df['Fixed Year'] = pd.to_numeric(shark_attack_df['Year'], errors='coerce')
    shark_attack_df.loc[shark_attack_df['Fixed Year'] == 0, 'Fixed Year'] = np.nan
    
    # Extract year from Date column when Fixed Year is missing
    date_year = shark_attack_df['Date'].str.extract(r'(\d{4})', expand=False)
    shark_attack_df['Fixed Year'] = shark_attack_df['Fixed Year'].fillna(pd.to_numeric(date_year, errors='coerce')).astype('Int64')

    # drop column 'Year' and 'Date'
    shark_attack_df = shark_attack_df.drop(columns=['Year', 'Date'], errors='ignore')

    # rename 'Fixed Year' to 'Year'
    shark_attack_df = shark_attack_df.rename(columns={'Fixed Year': 'Year'})
    
    return shark_attack_df

def clean_country(raw_shark_attack_df):
    shark_attack_df = raw_shark_attack_df.copy()
    
    # Get list of all country names
    country_names = [country.name for country in countries]
    
    def match_country(name):
        if pd.isna(name):
            return name
        name = str(name).strip()
        if not name:
            return name
        
        # Direct replacements for common cases
        replacements = {
            'USA': 'United States',
            'AUSTRALIA': 'Australia',
            'CEYLON (SRI LANKA)': 'Sri Lanka',
            'SOUTH AFRICA': 'South Africa'
        }
        
        if name in replacements:
            return replacements[name]
        
        # Use fuzzy matching for other cases
        match = process.extractOne(name, country_names, score_cutoff=70)
        return match[0] if match else name
    
    shark_attack_df['Country'] = shark_attack_df['Country'].apply(match_country)
    # title 'Country'
    shark_attack_df['Country'] = shark_attack_df['Country'].str.title()
    return shark_attack_df

def clean_data(raw_shark_attack_df):
    shark_attack_df = drop_useless_columns(raw_shark_attack_df)
    shark_attack_df = clean_date(shark_attack_df)
    shark_attack_df = clean_sex(shark_attack_df)
    shark_attack_df = clean_age(shark_attack_df)
    shark_attack_df = clean_type(shark_attack_df)
    shark_attack_df = clean_country(shark_attack_df)
    return shark_attack_df