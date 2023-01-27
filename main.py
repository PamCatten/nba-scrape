import os
import scrape

SEASONS = list(range(2016, 2023))
DATA_DIR = "data"
STANDINGS_DIR = os.path.join(DATA_DIR, "standings")
SCORES_DIR = os.path.join(DATA_DIR, "scores")

standings_files = os.listdir(STANDINGS_DIR)
standings_files = [s for s in standings_files if ".html" in s]

for f in standings_files:
    filepath = os.path.join(STANDINGS_DIR, f)
    scrape.scrape_game(filepath)
