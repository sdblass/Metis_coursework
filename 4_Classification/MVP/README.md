# Predicting Poverty in Ecuador

Addressing poverty in the developing world requires identifying who needs assistance the most. Simple indicators such as salary are not always reliable because some families may have low salaries but may not necessarily need aid. Others with higher salaries may still need aid depending on the number of people in a household and living conditions. A classification algorithm that accounts for many factors such as years of education or condition of living space may help identify those needing aid the most, thus reducing the effort needed to classify new aid applicants.

## Project Goal

The goal of this project is to use feature engineering and model testing to predict poverty for the most vulnerable population. This will be done by feature engineering and writing functions to enable rapid testing of multiple models. Functions to measure model performance will measure the models' ability to predict extreme poverty at the expense of a high false positive rate (maximize recall).

## Process

The data set comes from the Ecuador Poverty competition on [Kaggle](https://www.kaggle.com/c/costa-rican-household-poverty-prediction/data). There are about 9500 observations and about 140 features. The raw data is a mixture of boolean and continuous columns. Presumably, it is more important to minimize the number of poor households that are missed (false negatives) than it is to provide aid to households that need it less than predicted. Therefore we will evaluate models by their **recall**. However, this is a multiclass classification problem so we will use a custom recall function that will serve as a weighted average of recalls for each class with the class of interest (poverty category 1) being of the most interest. 


## Preliminary Conclusions

* Initial EDA does not show much affect of household size on poverty.
* Some basic feature engineering shows the proportion of adults in a household affects a random forest model more than most of the other original features, however, the model is most strongly affected by only a few variables so adding this feature in only had marginal improvement on model performance.
* Age and dependency (number of adults per number of children and eldery) are among the strongest predictors of poverty. A possible explanation is the older someone is, the less likely they are to be poor because the more resources they probably have. Similarly, the greater the dependency, the more demand on resources, the more likely they are to be poor.
* Scaling data by geographic area is complete but analysis remains to be done.
* Curse of dimensionality may be a factor. Initial results show extremely high AUC for random forest. Data are not shown in the MVP.

## Future Work

* Determine which scaled features should be included in the final analysis
* Ranking features by importance and running models on those
* Corrections for class imbalance
* Hyperparameter tuning for multiple models and selection of best model

