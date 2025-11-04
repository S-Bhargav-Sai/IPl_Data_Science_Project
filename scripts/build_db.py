# build_db.py (located in the scripts folder)
import sqlite3
import pandas as pd
import os

# --- Configuration ---
DATABASE_NAME = '../db/ipl_stats.db'  # Output DB path: Go up one level (..), then into the 'db' folder.
SCHEMA_FILE = 'schema.sql'         # schema.sql is in the same directory (scripts)
DATA_DIR = '../data/final_clean_data' # Data path: Go up one level (..), then into 'data/final_clean_data' folder

# Map CSV files to their corresponding table names (remains the same)
FILE_TO_TABLE_MAP = {
    'batting_avgs.csv': 'batting_averages',
    'batting_sr.csv': 'batting_strike_rates',
    'bowling_econ.csv': 'bowling_economy',
    'ipl_ball_by_ball_clean.csv': 'ipl_ball_by_ball',
    'ipl_bowlers_total_wickets_final.csv': 'bowlers_total_wickets',
    'ipl_matches_clean.csv': 'ipl_matches',
    'ipl_teams_wins_and_loss.csv': 'team_performance',
    'most_catches.csv': 'most_catches',
    'most_dismissals_wk.csv': 'most_dismissals_wk',
    'most_runs.csv': 'most_runs',
    'most_wickets.csv': 'most_wickets',
    'Players_details.csv': 'player_details',
    'seasonwise_winners.csv': 'season_winners',
    'unique_players.csv': 'unique_players',
    'venue_intelligence_final.csv': 'venue_intelligence'
}

def setup_database(db_name, schema_file):
    """Connects to the DB and creates tables using the schema file."""
    try:
        # Ensure the target directory for the DB exists
        db_dir = os.path.dirname(db_name)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)
            print(f"Created directory: {db_dir}")

        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # schema_file is correctly read from the current directory (scripts)
        with open(schema_file, 'r') as f:
            sql_script = f.read()
        
        cursor.executescript(sql_script)
        conn.commit()
        print(f"Database '{db_name}' created and schema applied successfully.")
        return conn
    except Exception as e:
        print(f"Error setting up database: {e}")
        return None

def load_data(conn, data_dir, file_to_table_map):
    """Reads CSVs and loads data into the corresponding SQLite tables."""
    print("--- Starting data loading ---")
    
    if not os.path.isdir(data_dir):
        print(f"Error: Data directory not found at {data_dir}. Please check the path.")
        return

    for filename, table_name in file_to_table_map.items():
        file_path = os.path.join(data_dir, filename)
        
        if not os.path.exists(file_path):
            print(f"Skipping: File not found at {file_path}")
            continue

        try:
            df = pd.read_csv(file_path)
            
            # Load data into SQLite
            df.to_sql(table_name, conn, if_exists='append', index=False)
            
            print(f"SUCCESS: Loaded {len(df)} rows from {filename} into table '{table_name}'.")

        except Exception as e:
            print(f"FAILED to load data from {filename} into table '{table_name}'. Error: {e}")

if __name__ == '__main__':
    # 1. Setup the database and create tables
    db_connection = setup_database(DATABASE_NAME, SCHEMA_FILE)
    
    if db_connection:
        # 2. Load the data from CSVs
        load_data(db_connection, DATA_DIR, FILE_TO_TABLE_MAP)
        
        # 3. Close the connection
        db_connection.close()
        print("\nDatabase build process complete.")