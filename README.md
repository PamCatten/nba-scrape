# nba-scrape
### Introduction
nba-scrape was a machine-learning project developed as part of an open-ended assignment to demonstrate mastery of several model archetypes and techniques taught in DS: Predictive Analysis and Modeling. The project aimed to predict the outcome of games for the 2021 - 2022 NBA regular season by leveraging raw box score data from the prior eight seasons scraped from the sports analytics website [Basketball Reference](https://www.basketball-reference.com/). The entire project was written entirely in Python, in addition to several different packages and libraries.

### Data Collection
* The dataset consisted of over 9,000 games of raw box score data scraped from Basketball Reference
* To avoid being flagged as malicious, each retrieval attempt was delayed by 5 seconds, taking around 16 hours non-stop to collect the dataset in its entirety
* The retrieval script was written in Python, using the package Playwright to download, categorize, and save browser HTML information to local files
* While the scope of the testing dataset was originally set to be two seasons, I made the decision to limit it to the most recent fully played regular season 2021 - 2022, as the prior season was shortened by COVID 19 lockdowns, and likely wouldn't be much help in assuaging potential variance
* The training dataset consistuted the remaining eight seasons of collected data, from 2013 - 2014 to 2019 - 2020

### Preprocessing & Transformation
* The package BeautifulSoup was used to parse and wrangle downloaded HTML files into dataframes from the Pandas libary
* Once in dataframes, the data still required extensive cleaning and wrangling
* Specific metric columns, such as blocks-per-minute (BPM) or points-per-36 (PER 36) had to be removed because stadiums scorekeepers report them somewhat inconsistently to the league
* Similarly stats generated in overtime (OT) had to be removed due to noticable deviations in expected behavior from the dataframes when included with non-OT games
* Individual player stats had to be aggregated to create team-level features such as total points, rebounds, assists, etc
* Duplicated columns, such as opponent field goal percentage had to be flattened to maintain data integrity
* To help more directly compare teams, additional metrics such as team win streaks, home/away game records, and average player performance were calculated
* Finally, the dataframes were converted into .CSVs to be fed to the training model
  
### Training & Results
* Because of the large number of highly correlated variables in the dataset, and the project limitation of using linear regression models, I elected to use Ridge Regression, a technique to regularize model results
* Ridge Regression reduces the risk of overfitting the model to the training data by identifying variables that share collinearity with another, discarding one of the variables as excess
* Using the modeling library Scikit-learn, I was able to fit Ridge regression models to the dataset, achieving an average accuracy of 57.8% on the testing data across the models
* I realized that because of the nature of the sports season, with teams naturally building or losing momentum as rosters begin to gel or players became injured, I opted to implement another technique, time series splits, to sort the folds of the data when cross validating by time, meaning that future games were always being validated against games from the past, improving classification
* Implementing both of these techniques increased average prediction accuracy to 64.3%; Additionally, it earned me an A-, so hey, pretty cool!
