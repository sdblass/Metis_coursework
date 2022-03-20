# Predicting Poverty in Ecuador

## Abstract
Addressing poverty in the developing world requires identifying those who need assistance the most. However, poverty can manifest itself in many different ways and be caused by many different factors. Therefore, the goal of this project is to build a classification model that can predict an individual's vulnerability to poverty as well as identify the factors that are most influential in contributing to poverty. Feature engineering combined with model tuning take the first few steps in addressing this important problem.

## Design
The data come from the Costa Rica Poverty Prediction competition on [Kaggle](https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/San_Jos%C3%A9_desde_el_Monte_de_la_Cruz%2C_Alajuelita%2C_Costa_Rica._-_panoramio.jpg/1280px-San_Jos%C3%A9_desde_el_Monte_de_la_Cruz%2C_Alajuelita%2C_Costa_Rica._-_panoramio.jpg). The goal of the competition was to prioritize those who need aid the most by creating a multiclass classification model that predicts poverty given a set of objective descriptions of an individual's personal and household qualities. For example, the model needed to determine if the number of people in a household significantly affected the household's poverty level. 

## Data
### Features
The data set contains 142 features that can broadly be categorized by individual, household, and geographical attributes. Some columns were binary indicating features such as presence of a computer tablet. Other features were discrete such as years of education. Still other features were continuous such as monthly rent. Example features include:
* **Individual:** Age, years of education, gender
* **Household:** Number of household members, dwelling's building material and condition, presence of electricity
* **Geography:** Six geographical regions of Costa Rica

### Target variable

* 1 = extreme poverty
* 2 = moderate poverty
* 3 = vulnerable households
* 4 = non vulnerable households 

Each row corresponds to one individual. Each invidual also gets a household id number to indicate which individuals live together. The data also indicate which individuals are heads of household which Kaggle uses to compute a score.

## Algorithms
### Exploratory Data Analysis and Data Cleaning
Individuals in the same household should have the same feature data for household, geography, and poverty. Data cleaning involved correcting for discrepancies between individual and household data. Cleaning also corrected for mixed data types in the "Dependency" feature which turns out to rank highly in feature importance.

The comparatively low numbers of vulnerable individudals compared to non-vulnerable ones indicate a potential class imbalance.


### Feature Engineering
Data were scaled by geographical area to correct for regional differences in factors such as cost of living. For example, a poor individual in a high cost of living area may not be considered as poor in a lower cost of living area. Such a nuance would not be captured in a model without that feature engineering.

### Modeling

#### Model selection
Random Forest and Logistic Regression models were fitted to the processed data because they are algorithms that can handle large complicated data sets where interpretation is less important than predictability. 

#### Train-test-split and cross validation
Model testing was done on an 80-20 train-test-split on the data with 5-fold cross validation. Cross-validation scores agreed well with one another. Members of the same household must not be in both the training and testing data to prevent data leakage. Otherwise, the model will predict scores with overly high accuracy because members of the same household have the same features in common, including poverty score.

#### Classification Metric
Recall was chosen due to the high priority of minimizing false negatives. Flagging a household for assistance it does not need aid is less important than missing a household that does. The final score is a macrorecall that consists of a weighted average of scores for each poverty category's recall score. This metric penalizes the model for incorrectly predicting poverty the further from the correct answer it gets.

#### Hyperparameter tuning
Several hyperparameters were tested using an exhaustive grid search for both Random Forest and Logistic Regression. Model performance measured by AUC indicate the default settings produce the highest scores.


## Tools
* Data acquisition: Kaggle 
* Cleaning: Pandas
* Visualizations: Matplotlib and Seaborn
* Modeling: Scikit-learn

## Communication
* Slides, visuals, write-up, recorded presentation
* Recorded presentation can be viewed [here](https://drive.google.com/file/d/1UsS1bhE_9lbAlyNAw5csjLtGir6jFhFu/view?usp=sharing).

![feature importance](https://github.com/sdblass/Metis_coursework/blob/master/4_Classification/images/feature_importance.png)

![auc](https://github.com/sdblass/Metis_coursework/blob/master/4_Classification/images/auc.png)

![roc](https://github.com/sdblass/Metis_coursework/blob/master/4_Classification/images/roc.png)

