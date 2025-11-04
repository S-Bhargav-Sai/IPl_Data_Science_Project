-- schema.sql

-- Table for batting averages (from batting_avgs.csv)
CREATE TABLE IF NOT EXISTS batting_averages (
    player_names TEXT,
    ipl_timeline TEXT,
    matches INTEGER,
    innings INTEGER,
    runs INTEGER,
    averages REAL
);

-- Table for batting strike rates (from batting_sr.csv)
CREATE TABLE IF NOT EXISTS batting_strike_rates (
    player_names TEXT,
    matches INTEGER,
    innings INTEGER,
    runs INTEGER,
    sr REAL
);

-- Table for bowling economy (from bowling_econ.csv)
CREATE TABLE IF NOT EXISTS bowling_economy (
    player_names TEXT,
    overs REAL,
    econ REAL
);

-- Table for ball-by-ball data (from ipl_ball_by_ball_clean.csv)
CREATE TABLE IF NOT EXISTS ipl_ball_by_ball (
    match_id INTEGER,
    batting_team TEXT,
    over INTEGER,
    ball_in_over INTEGER,
    batsman TEXT,
    bowler TEXT,
    non_striker TEXT,
    runs_batsman INTEGER,
    runs_extras INTEGER,
    runs_total INTEGER,
    inning INTEGER
);

-- Table for total wickets by bowlers (from ipl_bowlers_total_wickets_final.csv)
CREATE TABLE IF NOT EXISTS bowlers_total_wickets (
    player_name TEXT,
    total_wickets INTEGER
);

-- Table for match details (from ipl_matches_clean.csv)
CREATE TABLE IF NOT EXISTS ipl_matches (
    match_id INTEGER PRIMARY KEY,
    season INTEGER,
    date TEXT,
    venue TEXT,
    city TEXT,
    teams TEXT,
    toss_winner TEXT,
    toss_decision TEXT,
    winner TEXT,
    result_type TEXT,
    player_of_match TEXT
);

-- Table for team performance (from ipl_teams_wins_and_loss.csv)
CREATE TABLE IF NOT EXISTS team_performance (
    teams TEXT,
    ipl_seasons TEXT,
    matches INTEGER,
    won INTEGER,
    lost INTEGER,
    tie INTEGER,
    NR INTEGER,
    w_l REAL,
    w_pct REAL,
    l_pct REAL
);

-- Table for most catches (from most_catches.csv)
CREATE TABLE IF NOT EXISTS most_catches (
    player_name TEXT,
    ipl_season TEXT,
    mat INTEGER,
    inn INTEGER,
    catches INTEGER,
    ct_inn REAL
);

-- Table for most dismissals (wicket-keepers) (from most_dismissals_wk.csv)
CREATE TABLE IF NOT EXISTS most_dismissals_wk (
    player_name TEXT,
    timeline TEXT,
    matches INTEGER,
    innings INTEGER,
    dismissed INTEGER,
    catches INTEGER,
    stumping INTEGER,
    dis_inn REAL
);

-- Table for most runs (from most_runs.csv)
CREATE TABLE IF NOT EXISTS most_runs (
    player_name TEXT,
    timeline TEXT,
    matches INTEGER,
    innings INTEGER,
    runs INTEGER
);

-- Table for most wickets (from most_wickets.csv)
CREATE TABLE IF NOT EXISTS most_wickets (
    player_name TEXT,
    timeline TEXT,
    matches INTEGER,
    innings INTEGER,
    overs REAL,
    wickets INTEGER
);

-- Table for player details (from Players_details.csv)
CREATE TABLE IF NOT EXISTS player_details (
    name TEXT,
    playing_role TEXT,
    batting_style TEXT,
    bowling_style TEXT
);

-- Table for season winners (from seasonwise_winners.csv)
CREATE TABLE IF NOT EXISTS season_winners (
    year INTEGER,
    champions TEXT
);

-- Table for unique players (from unique_players.csv)
CREATE TABLE IF NOT EXISTS unique_players (
    name TEXT PRIMARY KEY,
    url TEXT
);

-- Table for venue intelligence (from venue_intelligence_final.csv)
CREATE TABLE IF NOT EXISTS venue_intelligence (
    venue TEXT PRIMARY KEY,
    matches_played INTEGER,
    avg_1st_innings_score INTEGER,
    avg_2nd_innings_score INTEGER,
    win_pct_batting_first REAL,
    win_pct_bowling_first REAL
);