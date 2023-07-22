# About

Final project in data science in HIT. <br>
We (@Omer-5, @smooth3x) set out to explore the possibility of predicting year-over-year growth in demand for various services on the website [Midrag](www.midrag.co.il) it was an interesting journey, this is what we achieved:
1. Data Acquisition: used `selenium` to web scrape the reviews in chosen fields
    * Modular approach: developed 3 crawlers to handle different part of the process.
    * Stop-Resume feature
    * Chain automation: each crawler feed the next crawler with tasks and the final crawler output the data.
    <br><br>
2. Data Cleaning: used several methods to examine the raw data and process it to a workable dataset:
    * Remove duplication: removing reviews that appear in more than one sub-field
    * Handle confidential reviews and missing data
    * Feature extraction: computed several new columns
    <br><br>
3. EDA: visualized the data in several ways to gain insight about the data:
    * Plot the data by year to reveal inconsistent data because of covid-19.
    * Plot the data by  region to illustrate growth was not even across the country.
    * Used `Vincent`, `Folium` and [OpenStreetMap's](www.openstreetmap.org) API to create a map showing growth for the top 10 cities with most reviews.
    * Analyze the difference between confidential and non-confidential reviews using word cloud and bar graphs - confidential reviews made up a significant portion of negative scores, vastly out weighting they proportion of total reviews
    <br><br>
4. Machine Learning:

    We trained a linear regression model until the year 2018 and tried to predict the growth of 2019-2021. <br>
    Unfortunately our model couldn't predict the outcome, indicated by the negative R-squared value. <br>
    This result can be explained by the lake of data points, the 327K reviews were only across 17 years and we needed to split the data to validate our modal. we tried to train the model based on months, increasing the data points, however it didn't fix the model.
    <br>
    Another reason is the huge jump in demand due to covid-19 making the data behave in an  unpredictable manner. This has taught us an important lesson regarding ML.

    ## Video Presentation
    https://www.youtube.com/watch?v=I-aDGSpyvzs

    [![video presentation](http://img.youtube.com/vi/I-aDGSpyvzs/0.jpg)](http://www.youtube.com/watch?v=I-aDGSpyvzs)


# Installation

Create python virtual environment:
```
$ python -m venv venv
```

Activate virtual environment (in powershell):
```
$ .\venv\Scripts\Activate.ps1
```

Install requirements file:
```
pip install -r requirements-BASE.txt
pip install -r requirements-CRAWLING.txt

```

[Installation guide for Geckodriver- only for scrapping](https://github.com/mozilla/geckodriver/releases/tag/v0.32.0)



