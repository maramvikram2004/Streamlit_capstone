# Urban Metro Station Site Predictor

Welcome to the **Urban Metro Station Site Predictor** Streamlit site! This platform provides an interactive and data-driven approach to analyze and predict optimal metro stop locations across Indian cities. The tool leverages advanced machine learning algorithms to aid urban planning and development.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Data Sources](#data-sources)
- [Model Details](#model-details)

## Overview
The **Urban Metro Station Site Predictor** is designed to assist city planners and stakeholders in identifying optimal locations for metro stations based on:
- Population density
- Proximity to buildings, schools, and hospitals
- Traffic congestion levels
- Rental costs
- Existing railway lines

The model was trained and tested using data from Hyderabad, Bangalore, and Chennai, achieving an impressive accuracy of **86%** using XGBoost.

## Features
- Interactive map visualization of metro station predictions
- Dynamic filtering based on user-defined parameters
- Display of predicted station locations with relevant attributes
- Comparison of predicted locations with existing metro lines


## Data Sources
The model is built using datasets that include attributes such as:
- Population density
- Building count
- Proximity to schools and hospitals
- Traffic data
- Rental costs

City-specific data was manually compiled and scraped for Chennai, Bangalore, and Hyderabad. Additional data collection is ongoing for Chandigarh.

## Model Details
- **Algorithms Used:**
  - Random Forest
  - XGBoost (current best model with **F1 score of 91** and **accuracy of 86%**)

- **Training and Testing:**
  - Data from Hyderabad and Bangalore was used for training.
  - Model tested on Chennai and compared with existing metro lines for validation.

