# India Air Pollution Analysis (2015–2020)

An exploratory data analysis project investigating air quality across Indian cities using historical Air Quality Index (AQI) and pollutant measurements.

## Project Overview

Air pollution is a major environmental challenge, and understanding how air quality varies across locations and time can help reveal patterns that deserve further investigation.

This project analyzes historical air-quality data from Indian cities to examine AQI distributions, city-level differences, seasonal and monthly patterns, year-wise trends, missing data, and relationships between recorded pollutant concentrations and AQI.

**Project period:** January 2015 – July 2020  
**Dataset size:** 29,531 records  
**Cities represented:** 26  
**Available AQI observations:** 24,850

## Objectives

- Examine data quality, completeness, and missing values.
- Clean and prepare the dataset for exploratory analysis.
- Compare recorded AQI levels across cities.
- Explore monthly, seasonal, and yearly AQI patterns.
- Investigate associations between pollutant measurements and AQI.
- Produce reproducible visualizations and analytical tables.

## Technology Stack

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Jupyter Notebook
- VS Code

## Project Structure

```text
india-air-pollution-analysis/
├── data/
│   ├── raw/
│   │   └── archive-3/
│   └── processed/
├── notebooks/
│   ├── 01_data_audit.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   └── 04_advanced_analysis.ipynb
├── outputs/
│   ├── figures/
│   └── tables/
├── reports/
├── src/
├── requirements.txt
└── README.md
```

## Analysis Workflow

### 1. Data Audit

- Inspected dataset dimensions, data types, and date coverage.
- Measured missing values in AQI and pollutant columns.
- Examined city-level and year-level AQI completeness.
- Checked for duplicate city-date combinations.

### 2. Data Cleaning

- Parsed dates and prepared a working copy of the dataset.
- Imputed missing pollutant measurements using city-level medians, with a global-median fallback where required.
- Preserved missing AQI values rather than imputing them.

### 3. Exploratory Data Analysis

- Examined the AQI distribution and summary statistics.
- Compared average AQI across cities.
- Explored monthly, seasonal, and annual patterns.
- Examined pollutant relationships using correlation analysis.

### 4. Advanced Analysis

- Compared city-level AQI coverage and averages.
- Investigated seasonal and monthly variation.
- Analyzed yearly trends for selected cities.
- Calculated Pearson and Spearman correlations using raw observations and available pollutant–AQI pairs.
- Investigated unusually high AQI observations.

## Preliminary Findings

- The dataset contains 29,531 records, of which 24,850 have recorded AQI values.
- The overall mean AQI in the available observations is approximately 166.46, while the median is 118.
- Ahmedabad has the highest average AQI in the current city-level analysis, approximately 452.12. This comparison should be interpreted alongside differences in data coverage.
- Aizawl has the lowest average AQI in the current city-level analysis, approximately 34.77.
- There are 543 observations with AQI above 500. All are labeled `Severe` in the supplied dataset, and 412 of these observations are from Ahmedabad.
- No duplicate city-date combinations were detected in the raw dataset.

These are descriptive findings from the dataset, not evidence that a particular source caused the observed pollution levels. The extreme AQI values require careful interpretation and should not automatically be treated as errors or as independently validated measurements.

## Outputs

The `outputs/tables/` directory contains exported analytical tables, including missing-value audits, city coverage summaries, AQI statistics, seasonal and monthly analyses, and pollutant correlation results.

The `outputs/figures/` directory contains visualizations of AQI distributions, city comparisons, time trends, and pollutant relationships.

## Limitations

- The data is historical and ends in July 2020; it does not describe current air quality.
- AQI and pollutant data contain missing observations.
- Median imputation can affect pollutant distributions and relationships. Correlation analysis therefore uses raw observations rather than the imputed pollutant dataset.
- City comparisons can be affected by differences in observation counts, time coverage, and missingness.
- Correlation does not establish causation. AQI is itself derived from pollutant measurements.
- Extreme values require further validation against an authoritative reference before being interpreted as confirmed measurements.

## Running the Project

Clone or download the repository and create a Python virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Open the project in VS Code, select the `.venv` Python interpreter, and run the notebooks in numerical order from `01_data_audit.ipynb` through `04_advanced_analysis.ipynb`.

Ensure the raw dataset is placed in the expected `data/raw/archive-3/` directory before running the notebooks.

## Future Improvements

- Develop an interactive Streamlit dashboard.
- Add robustness checks using a common observation period for city comparisons.
- Investigate extreme AQI observations and pollutant-data quality.
- Improve documentation with additional verified findings and chart annotations.

## Author

**Ashok Reddy Damireddy**

Data Science | Python | Exploratory Data Analysis | Data Visualization
