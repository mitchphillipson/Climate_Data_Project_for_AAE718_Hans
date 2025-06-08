# Wisconsin Snowfall and Extreme Temperature Analysis

## Project Description

This project analyzes the relationship between snowfall and extreme temperatures across four regions in Wisconsin, using weather data from January 2015 to June 2025. The goal is to examine trends in extreme weather events and to explore the relationship between snow depth and temperature departure.

The four weather stations included in the study are:

- Chippewa Valley Regional Airport
- La Crosse Regional Airport
- Madison Dane County Regional Airport
- Milwaukee Mitchell International Airport

The project generates time series plots, scatter plots, and regression trendlines to visualize the evolving patterns of snowfall and extreme temperatures in Wisconsin. You can also use the Report.md file to chceck the report based on the visulized data.

## How to Run the Project

### 1. Environment Setup

You will need Python (>=3.8) and the following Python libraries:

- pandas
- matplotlib
- seaborn
- numpy
- scikit-learn (optional, if used for regression fitting)

Install the required libraries using:

```bash
pip install pandas matplotlib seaborn numpy scikit-learn


### 2. Prepare Data

Before running the analysis script, **download the `data/` folder and all files it contains**, and place it in the project directory.

The `data/` folder contains the necessary weather data used for the analysis.

### 3. Running the Analysis

Run the provided Python script to generate the figures:

```bash
python Graphs_generation.py



