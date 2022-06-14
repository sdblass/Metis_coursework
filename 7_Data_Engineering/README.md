# New Apartment Finder - Balancing Commute Time with Rent
## Summary
The objective of this project is to create a webapp that allows a user searching for apartment rentals to retrieve a list of options that accounts for the user’s commute time. The further the user must travel to work, the more time the user must spend on the road. That commute is time not spent generating income and must be accounted for in the rent. This tool would allow a user to retrieve listings for apartment rentals with the rent adjusted for the commuting time to work. 

## Data Pipeline
![](https://github.com/sdblass/streamlit/blob/main/images/final_pipeline.png)
### Deployment
The pipeline is [hosted on streamlit](https://share.streamlit.io/sdblass/streamlit/main/apartments_streamlit_isochrone.py). The prototype only contains data for the Arlington, VA area but the user can input any address in the US. A future version will work anywhere in the US.

### User Data Input
The user puts in an address for a work location. The user also specifies mode of transportation such as car/bike/walk, the range of rents, and types of apartments (studios, 1 bedroom, 2 bedrooms). The user also inputs an hourly wage. This is the amount at which the user values his or her time. A higher hourly rate means time spent commuting has an even higher cost in terms of lost productivity.

### Bulk Data Ingestion
The prototype version scrapes a sampling of actual apartment listings from apartments.com and combines it with randomly generated points within 25 miles of the Arlington, VA area. The pipeline stores the data in a SQLite database. The full version will contain a database containing real listings pulled from a real estate website like [apartments.com](https://www.apartments.com). When a user inputs an address, the algorithm geocodes the address using the Mapbox Geocode API and queries the database for listings in the vicinity of the address.

### Data Processing
The pipeline queries the Mapbox Isochrone API for 10, 20, 30, and 40 minutes for the user's address and plots the resulting polygons on a map. All points within a given polygon can be reached within a certain amount of time. For example, all points within the 10 minute polygon can be reached from the user's address within 10 minutes. The pipeline then determines which polygon contains each apartment listing and adjusts the rent accordingly. The pipeline adjusts the rent with the following formula:

* New Rent = Old Rent + Commute Time * 2 * 20 / 60 * Hourly Rate

The new rent is the old rent plus roundtrip time spent commuting in hours per month multiplied by the user's hourly salary.

### Data Visualization
The pipeline plots each apartment on a map overlaid with polygons containing commuting information. The user can hover over any point to see the rent and type of apartment. The map will also display the commute length and whether the data is a real data point or a randomly generated one.

The pipeline then finds the lowest-rent apartments for each commuting length and lists the top three cheapest ones in a table. Apartments far from the user's address show a correspondingly higher adjusted rent.

![](https://github.com/sdblass/streamlit/blob/main/images/visual.png)


## Tools
* *Data Ingestion:* Webautomation.io predefined extractor for apartments.com, SQL
* *Data Processing:* Pandas
* *Data Visualization:* Plotly
* *Web App Deployment:* Streamlit

## Communication
* Slides, visuals, write-up


