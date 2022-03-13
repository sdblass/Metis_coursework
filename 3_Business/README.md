# Where to put the next Tesla Dealership

## Abstract
The goal of this project was to identify geographical areas for new electric vehicle (EV) dealerships and target demographics by finding attributes common to areas with high rates of EV adoption. Areas with those attributes but low rates of EV adoption would be areas for more targeted research. Data visualizations from exploratory data analysis reveal sensitivity of EV demand to population density, income, and age. Future iterations will add feature complexity to make the model more accurate.

## Design
EV sales increasing exponentially will spur manufacturers to open new dealership locations to meet growing demand. Manufacturers will want to choose locations that maximize the the new dealerships’ prospects. This project’s scope centers around an iterative plan to identify such areas by finding relationships between demand for EVs and area demographic data. This project’s MVP indicated urban areas have highest demand for EVs. Later iterations added demographic data and generated more granularity about who in these urban areas is driving EV demand. Future iterations will augment the feature set to create a fuller picture of the target demographic.

## Data
The data set contains EV and demographic data for every zip code in NY, NJ, CT, and MD. These coastal states were chosen because they have more people than inland states and, therefore, likely more EVs. Later iterations can include data from other states.
*Sources*
* [Atlas EV Hub](https://www.atlasevhub.com/) is a repository of EV registration records
* [Maryland state government database](https://opendata.maryland.gov/Transportation/MD-MDOT-MVA-Electric-and-Plug-in-Hybrid-Vehicle-Re/tugr-unu9) also contains EV registration records for MD
* [Alternative Fuels Data Center](https://afdc.energy.gov/stations/#/analyze) contains downloadable spreadsheets for alternative fuel stations including EV charging stations by zip code
* https://www.unitedstateszipcodes.org/ for zip code demographic info

*Features*
* Population
* **Population density**
* **Number of electric vehicles registered**
* Number of electric charging stations
* **Median household income**
* **Median age**
* Educational levels

Bold features indicate those that were included in the initial exploratory data analysis.

## Algorithms
*Feature Engineering*

The EV data contained the number of EVs registered in each zip code. For this project, EV demand was calculated as follows:

* EV demand = Number of EVs registered (in 2019) / Total number of drivers
* Tot num drivers = Pop * % of pop that drives

The number of EV registrations is only a snapshot in time for a particular year and is not a measure of the total number of EVs on the road at any given time. Therefore, analysis errors can occur if a particular area has high demand for EVs but just not that particular year.

*Data visualizations*

Visualizations showed demand for EVs increased gradually with median income in areas with low to medium population density (<15,000 people per mi) which makes sense considering EVs are more expensive than gasoline cars. In high population density areas, demand for EV grew more rapidly with increasing income, indicating that other factors in urban areas is influencing EV demand not accounted for by population density or income alone. Additional visualizations suggest **the target demographic most likely to adopt EVs is high income people under 30 living in cities**.

## Tools
* Python for data acquisition
* Google Sheets for cleaning, feature engineering, and visualizations
* Tableau for feature engineering and visualizations (see link for interactive data)

## Communication
* Slides, visuals, write-up, recorded presentation



