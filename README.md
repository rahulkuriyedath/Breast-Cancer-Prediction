# Relationship between Crop growth and Population growth in Asia

This is the repo for the group project for DSCI 522 (group 16)

- Author: DSCI 522 GROUP 16
- Contributors: Aditya, Ifeanyi Anene, Rahul Kuriyedath, Saule Atymtayeva

A data analysis project for DSCI 522; a course in the Master of Data Science program at the University of British Columbia.

# About 
At the current stage of this project, we are trying to answer the question: Given the population of people in Asia, and the wheat and paddy production in Asia, How has production in paddy and wheat in Asia varied over time with change in population? Answering this question is important because food insecurity is one of the major causes of high child mortality rates, slow economic development rates and low human development index in the developing world. 

To answer the inferential question proposed above, the current plan is to use a linear regression model to see if the increase in crop production would be able to keep up with the increase in Asian population growth. Before developing this model, we will perform a succinct but relevant exploratory data analysis on the data sets available. Given that this is a time series analysis, a locally estimated scatter plot smoothening (loess) regression model can be explored here to get started. 


A markdown report of the exploratory data analysis performed thus far can be found [here](src/EDA0.md), however, if that is not rendering properly on your end, you can also find it [here](src/EDA0.ipynb).


# Usage
To replicate the analysis, clone this GitHub repository, install the [dependencies](#dependencies) listed below, and run the following commands at the command line/terminal from the root directory of this project:

1. Create a conda envrioment using the `group16.yml`

```bash
conda env create -f group16.yml
conda activate group16
```

2. Download population and crop datasets in the data directory





# Dependencies

To run this project, please install the required dependencies [here](https://github.com/UBC-MDS/dsci522-group16/blob/main/group16.yml)



# License 

The Crop growth and Population growth material are licensed under the Creative Commons Attribution 2.5 Canada License (CC BY 2.5 CA). If re-using/re-mixing please provide attribution and link to this webpage.



# References 

Data.worldbank.org. 2020. Population, Total | Data. [online] Available at: <https://data.worldbank.org/indicator/SP.POP.TOTL> [Accessed 19 November 2020].

Fao.org. 2020. FAOSTAT. [online] Available at: <http://www.fao.org/faostat/en/#data/QC> [Accessed 19 November 2020].