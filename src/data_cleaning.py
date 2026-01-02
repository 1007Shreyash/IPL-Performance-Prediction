import pandas as pd
import os

# Define file paths relative to the project root
RAW_PATH = os.path.join('data', 'raw')
PROCESSED_PATH = os.path.join('data', 'processed')

def load_and_clean_data():
    # Ensure processed directory exists
    os.makedirs(PROCESSED_PATH, exist_ok=True)
    
    print("Loading data...")
    matches = pd.read_csv(os.path.join(RAW_PATH, 'matches.csv'))
    deliveries = pd.read_csv(os.path.join(RAW_PATH, 'deliveries.csv'))
    
    print(f"Matches shape: {matches.shape}")
    print(f"Deliveries shape: {deliveries.shape}")

    # --- 1. Fix Date Formats ---
    if 'date' in matches.columns:
        matches['date'] = pd.to_datetime(matches['date'], errors='coerce')

    # --- 2. Standardize Team Names ---
    # Map old names to current names
    team_mapping = {
        'Delhi Daredevils': 'Delhi Capitals',
        'Kings XI Punjab': 'Punjab Kings',
        'Rising Pune Supergiants': 'Rising Pune Supergiant',
        'Royal Challengers Bangalore': 'Royal Challengers Bengaluru',
        'Deccan Chargers': 'Sunrisers Hyderabad', # Optional: historic mapping
        'Pune Warriors': 'Rising Pune Supergiant', # Simplification for legacy
        'Gujarat Lions': 'Gujarat Titans' # Note: Be careful with completely different franchises
    }
    
    # Apply mapping
    matches.replace(team_mapping, inplace=True)
    deliveries.replace(team_mapping, inplace=True)

    # --- 3. Handle Missing Values ---
    matches['city'] = matches['city'].fillna('Unknown')
    matches['winner'] = matches['winner'].fillna('No Result')
    matches['player_of_match'] = matches['player_of_match'].fillna('None')

    # --- 4. Fix Venue Names ---
    # Remove dots and standardize common duplicates
    matches['venue'] = matches['venue'].str.replace('.', '', regex=False)
    matches['venue'] = matches['venue'].str.replace('M Chinnaswamy Stadium', 'M. Chinnaswamy Stadium')

    print("Saving cleaned data...")
    matches.to_csv(os.path.join(PROCESSED_PATH, 'matches_cleaned.csv'), index=False)
    deliveries.to_csv(os.path.join(PROCESSED_PATH, 'deliveries_cleaned.csv'), index=False)
    print("Success! Data saved to data/processed/")

if __name__ == "__main__":
    load_and_clean_data()