# Final Project

### Team: Paramount Predictors
### Members: Michaela Giandello and Rebecca Melo

## [Website](add html to heroku here)

This repo houses a [website](add html to heroku here) that visualizes and predicts the Box Office revenue and IMDb ratings of upcoming films based on historical movie releases from 1980 to 2022. 

### The Data

* [OMDb API](http://www.omdbapi.com)
* [Kaggle](https://www.kaggle.com/danielgrijalvas/movies)
* [The-Numbers](https://www.the-numbers.com/box-office-records/domestic/all-movies/cumulative/all-time)
* [IMDb](https://www.imdb.com/calendar/?ref_=nv_mv_cal)

The team gathered data from Kaggle, IMDB, OMDB, and The Numbers. The information obtained included movie budget data, upcoming movies, genres, actors, etc.
The collected data was then cleaned and saved to csv files and the database was created.
PostgreSQL was used to host the database.

## Process

### Project Proposal

The goal of this project was to create a website containing a model to predict a films box office success and IMDb ratings, based on the historical movie data the team gathered.

### Website Scraping
Example of code used to scrape from one of the data sources is shown below.

<img width="1154" alt="web_scrape" src="https://user-images.githubusercontent.com/88587843/157091117-c2035a34-ba82-48d9-9287-12bc97b20677.png">

We used the available data we had from web scrapping IMDb to pull the recent 2021 and 2022 missing data from our orginal Kaggle data set.
Then, we scraped the IMDb website for upcoming movie lists, to then save that list and search through our API.

### API

<img width="1021" alt="API" src="https://user-images.githubusercontent.com/88587843/157091340-79682598-3bb6-4602-bd42-59894970025c.png">

From the movie list from Kaggle, srapped data from the-numbers.com and IMBd for upcoming movies, 

### ETL

* Extract using an API calls to obtain list of movies by year from OMDb.
* Transform using Python/Pandas to merge dataframes, replace null values with ‘NA’ or ‘0’ as appropriate, remove duplicates, normalize all headers
* Load the final final output to CSV and our SQL database.

### Preprocessing
* Create labels based on IMDb rating and Box Office.
* Select beneficial columns for the model and drop those that we don't need, like language, country, and release date.
* Convert categorical data to numerical.
* Additional cleanup of null and missing values.
* Reduce number of distributions of some features like genre, director, writer, actor, and rating (i.e. PG vs. R, etc.).
* Binning the IMDb rating into 3 distinct groups of <5, between 5 and 7, and >7.
* Binning the Box Office revenues into 59 groups ranging starting from 0 - 100,000 and ending in the range of 2,000,000,000 - 2,500,000,000
* Encode the rest of categorical data using `get_dummies`.
* Merge all features into a single dataframe and save into PostreSQL. 

Our final dataset uses the following features: movie id, title, runtime (mins), IMDb ratings, Meta-Score ratings, Box Office (USD), Movie Ratings, Director, Writer, Actors.

### Building the Models

Our team created 3 Jupyter Notebook files containing the our machine learning models for Random Forest Classifer (for Box office only) and Logstic Regression(for Box Office and IMDb ratings). Both models were used to predict box office success and IMDb ratings based on the historical movie data.


### The Models - Results 

Initially, we tried multiple models and target data binning methods to see which ones would yield the best result. Linear regression and SVM models didn’t seem suitable for the dataset that we assembled, so we moved on to random forests, and logstic regression. These 2 models yielded different accuracy scores:

<ins><b> Random Forest Model: Box Office </b></ins>
* <b>Training Score:</b> 1.0
* <b>Testing Score:</b> 0.223

These testing scores are very low, in which predicting the Box Office revenue was very inaccurate from Prediction vs. Actual just on the Histroical Movie Data alone. This is when we decided Random Forest was not the best choice.

<ins><b> Logistic Regression Model: Box Office </b></ins>
* <b>Training Score:</b> 0.698
* <b>Testing Score:</b> 0.716

<img width="791" alt="box_office_Log" src="https://user-images.githubusercontent.com/88587843/157096590-c7eadd20-948b-43ec-9a79-bbd3dc9992bd.png">

These testing scores are better than Random Forest, but still low in the low 70% accurarcy. Therefore, Box Office revenue was still inaccurate from Prediction vs. Actual on Historical Move Data and Upcoming Movie Data.

<ins><b> Logistic Regression Model: IMDb Ratings </b></ins>
* <b>Training Score:</b> 0.702
* <b>Testing Score:</b> 0.712

<img width="793" alt="imdb_score" src="https://user-images.githubusercontent.com/88587843/157097949-a79c7492-8db3-4a69-bbce-bc0d060cf417.png">


These testing scores are better than Random Forest as well, but still low in the low 70% accurarcy. IMDB ratings was better, but still inaccurate from Prediction vs. Actual on Historical Move Data and Upcoming Movie Data.

### Final Thoughts

In the end, Logsitc Regression seems like the better mmodel to use between the two machine learning models. However, we still need more features to get a higher accuracry score use Logsitc Regression properly.


### The Webpage / Deploying the App

The webpage is deployed and hosted on Heroku, so it is able to be viewed publically. It references this repository's root directory to build a public application.

### Presentation

[Our Presentation](https://docs.google.com/presentation/d/1IDqEru0ikBrq68DJWKZhHUyVnVfSFYV5xCU27yGUBNA/edit#slide=id.g107e079d02a_0_54)

