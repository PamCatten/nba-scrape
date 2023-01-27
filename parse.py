from bs4 import BeautifulSoup
import pandas as pd
import os 

def parse_html(box_score):
    """Parses and cleans the html for further processing"""
    with open(box_score, encoding="utf-8", errors="ignore") as f:
        try:
            html = f.read()
        except (OSError, ValueError):
            print(box_score)

    soup = BeautifulSoup(html, "html.parser")
    # Decomposing unwanted table assets, the dataframe gets messy otherwise
    [s.decompose() for s in soup.select("tr.over_header")]
    [s.decompose() for s in soup.select("tr.thead")]
    return soup

def read_line_score(soup):
    line_score = pd.read_html(str(soup), attrs={"id": "line_score"})[0]
    cols = list(line_score.columns)
    cols[0] = "team"
    cols[-1] = "total"
    line_score.columns = cols
    # Removed quarterly score totals because pandas gets weird with OT
    # TODO: find efficient way to store OT data without messing with the dataframe
    line_score = line_score[["team", "total"]]
    return line_score

def read_stats(soup, team, stat):
    df = pd.read_html(str(soup), attrs = {'id': f'box-{team}-game-{stat}'}, index_col=0)[0]
    df = df.apply(pd.to_numeric, errors="coerce")
    return df

def read_season_info(soup):
    nav = soup.select("#bottom_nav_container")[0]
    hrefs = [a["href"] for a in nav.find_all("a")]
    season = os.path.basename(hrefs[1]).split("_")[0]
    return season
