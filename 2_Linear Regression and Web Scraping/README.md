#  Predicting Book Demand on Overdrive
## Abstract

The goal of this project was to predict the demand for books on the library ebook-hosting service Overdrive using popularity data from Goodreads.  To meet the needs of their customers, libraries must be able to predict demand for titles so they can purchase the appropriate number of licenses to minimize wait times and keep their customers happy. I scraped data, identified high-demand genres using exploratory data analysis, and fit a multiple linear regression to the data. The model can predict 13% of demand. The model fails to predict demand, likely due to missing time-dependency popularity data.

## Abstract
The goal of this project was to predict the demand for books on the library ebook-hosting service Overdrive using popularity data from Goodreads.  To meet the needs of their customers, libraries must be able to predict demand for titles so they can purchase the appropriate number of licenses to minimize wait times and keep their customers happy. I scraped data, identified high-demand genres using exploratory data analysis, and fit a multiple linear regression to the data. The model can predict 13% of demand. The model fails to predict demand, likely due to missing time-dependency popularity data.

## Design
My hypothesis was that the more highly rated a book and its author are on Goodreads, the greater the demand would be on Overdrive. I scraped data for 1600 books from a Goodreads list entitled [Best Books Ever](https://www.goodreads.com/list/show/1.Best_Books_Ever?page=1). I then searched for each title on the New York Public Library’s Overdrive page, one of the largest collections in the country, and collected demand info for the top two search results.

## Data
The final data set contained 3200 rows. By calculating Levenshtein ratios, I eliminated books whose Overdrive and Goodreads titles did not match. I gathered price and page counts using Google searches and searched for the titles on IMDB to see if they had been made into movies. Matching books to movies on IMDB proved too unreliable for modeling purposes. After eliminating books with missing demand data and outliers, the final data set for modeling contained information for 1772 books. 

## Algorithms
*Feature Engineering*
* Created dummy variables for 125 genres and calculated demand for each genre.
* Normalized the demand by the number of books in each genre to correct demand inflation due to some genres containing more books as well as other genres.
* Created dummy variables to indicate if the book is part of a series
* Calculated a book’s popularity by multiplying the number of stars a book has by the number of users who rated the book divided by the number of years the book has been in print. Normalizing by year corrects for the tendency of a book’s popularity to increase with time due to users having had more time to rate. Normalizing also assumes popularity increases linearly with time which is likely inaccurate. The trend is more likely logarithmic than linear.

*Modeling*
* Correlation table to identify predictive features. 
* Multiple linear regression using standard scaled values.
* Single linear and polynomial regression for book popularity data.
* Regularization + cross-validation was ineffective due to low R-squared. 




## Tools
* Numpy and Pandas for data handling
* Statsmodels and Scikit-learn for modeling
* Matplotlib and Seaborn for visualization
* Python requests, Selenium, and WebScrapingAPI proxy service for web scraping
* BeautifulSoup for html parsing.

## Communication
* Slides, visuals, write-up




