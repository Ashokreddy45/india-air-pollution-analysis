# India Air Pollution Analysis
## A Historical Exploratory Data Analysis of Air Quality Across Indian Cities

**Author:** Ashok Reddy Damireddy  
**Analysis period:** January 2015 – July 2020  
**Tools:** Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook

---

## 1. Executive Summary

This project examines historical air-quality observations across 26 Indian cities. The dataset contains 29,531 records, including 24,850 non-missing AQI observations. The analysis investigates data completeness, AQI distributions, city-level differences, temporal patterns, and associations between pollutant measurements and AQI.

The recorded mean AQI is approximately 166.46, while the median is 118. The analysis also identifies a substantial concentration of unusually high AQI observations in Ahmedabad. These findings require interpretation in the context of missing data, unequal city coverage, and the historical nature of the dataset.

The project demonstrates a reproducible data analysis workflow, from data auditing and cleaning through exploratory analysis and evidence-based reporting.

## 2. Problem Statement

Air quality varies by location and time. Analyzing historical observations can help identify differences among cities, periods of elevated AQI, and relationships between measured pollutants and reported air quality.

The purpose of this project is to explore these patterns systematically while documenting data-quality limitations and avoiding unsupported causal conclusions.

## 3. Objectives

1. Audit dataset structure, missingness, and date coverage.
2. Prepare a cleaned dataset for exploratory analysis.
3. Compare AQI distributions and city-level averages.
4. Examine monthly, seasonal, and yearly patterns.
5. Explore pollutant–AQI associations.
6. Investigate extreme AQI values and document limitations.
7. Produce reproducible tables and visualizations.

## 4. Dataset Description

The source dataset contains daily city-level air-quality observations and pollutant measurements.

| Attribute | Value |
|---|---|
| Records | 29,531 |
| Cities | 26 |
| Date range | January 2015 – July 2020 |
| Available AQI observations | 24,850 |
| Missing AQI observations | 4,681 |
| Missing AQI percentage | Approximately 15.85% |

The dataset includes fields such as `City`, `Date`, `AQI`, `AQI_Bucket`, `PM2.5`, `PM10`, `NO`, `NO2`, `NOx`, `NH3`, `CO`, `SO2`, and `O3`, along with other pollutant measurements.

The source and redistribution license should be documented in the repository after they have been verified.

## 5. Methodology

### 5.1 Data Audit

The initial audit examined dataset dimensions, data types, date parsing, missing-value counts, city coverage, and AQI completeness by year and city.

No duplicate city-date combinations were detected in the raw dataset.

### 5.2 Data Cleaning

Dates were parsed into a datetime format. A working copy of the dataset was prepared, and missing pollutant values were imputed using city-level medians, with a global-median fallback when needed.

Missing AQI values were retained rather than imputed.

The imputed dataset was used for relevant exploratory analyses. For pollutant–AQI correlation calculations, raw observations were used to avoid directly introducing median-imputed pollutant values into those calculations.

Median imputation may affect distributions and associations, so results involving imputed pollutant values should be interpreted cautiously.

### 5.3 Exploratory Data Analysis

The analysis examined:

- AQI descriptive statistics and distribution.
- Average AQI by city.
- Monthly, seasonal, and yearly patterns.
- Pollutant correlation patterns.
- City-level AQI completeness.

### 5.4 Advanced Analysis

Additional analyses compared cities, summarized seasonal and monthly AQI patterns, examined yearly trends for selected cities, and calculated Pearson and Spearman correlations between pollutant measurements and AQI using available raw-data pairs.

The seasonal categories are analytical groupings based on calendar months and should not be interpreted as a universal classification for every Indian region.

## 6. Results

### 6.1 Overall AQI Statistics

| Statistic | Value |
|---|---:|
| Available AQI observations | 24,850 |
| Mean AQI | 166.46 |
| Median AQI | 118 |
| Standard deviation | 140.70 |
| Minimum recorded AQI | 13 |
| Maximum recorded AQI | 2,049 |
| 90th percentile | 341 |
| 95th percentile | 407 |
| 99th percentile | 661.51 |

The mean is higher than the median, indicating a right-skewed distribution influenced by high AQI observations. The distribution and extreme values warrant further examination.

### 6.2 City-Level Differences

In the current city-level analysis, Ahmedabad has the highest average AQI at approximately 452.12, while Aizawl has the lowest at approximately 34.77.

These comparisons are descriptive. Differences in data coverage, missing observations, and periods represented may affect the results. They should not be interpreted as a definitive ranking of long-term city air quality without additional robustness checks.

### 6.3 Extreme AQI Observations

The raw dataset contains 543 observations with AQI above 500. All 543 are labeled `Severe` in the supplied `AQI_Bucket` column.

The distribution of these observations across cities includes:

| City | Observations above 500 |
|---|---:|
| Ahmedabad | 412 |
| Delhi | 48 |
| Patna | 25 |
| Gurugram | 22 |

Ahmedabad accounts for approximately 75.9% of observations above 500. The maximum recorded value is 2,049 in Ahmedabad on 19 February 2018.

These observations should not be automatically removed. The concentration may reflect genuine severe pollution, data-quality issues, or a combination of factors. Independent validation would be required to determine their accuracy.

### 6.4 Temporal Patterns

Monthly, seasonal, and yearly analyses were conducted to examine temporal variation in AQI. The corresponding exported tables and figures are available in the project's `outputs/` directories.

Specific conclusions about the highest-pollution months, seasonal differences, or long-term improvements should be included only after the exported summaries and plots have been reviewed.

The dataset ends in July 2020, so 2020 represents a partial year and should not be compared directly with complete calendar years without accounting for this difference.

### 6.5 Pollutant–AQI Relationships

Pearson and Spearman correlations were calculated from raw observations with available paired measurements. The exported correlation table records the estimated relationships.

Correlation indicates statistical association, not causation. AQI is calculated from pollutant measurements, so associations between pollutant values and AQI are expected to be influenced by how AQI is constructed. Missing paired observations may also affect comparisons across pollutants.

The specific strongest pollutant relationships should be reported after checking the exported correlation results and sample counts.

## 7. Data Quality and Limitations

1. **Missing observations:** Approximately 15.85% of AQI values are missing. Pollutant columns also contain missing measurements.
2. **Imputation effects:** City-median and global-median imputation may reduce variability and influence analyses that use the imputed data.
3. **Unequal city coverage:** City comparisons may be affected by different observation counts and date coverage.
4. **Extreme observations:** AQI values above 500, including the maximum of 2,049, require further validation.
5. **Historical coverage:** The dataset ends in July 2020 and does not represent present-day air quality.
6. **Season definitions:** Calendar-based seasonal groupings simplify India's regional climatic differences.
7. **Association versus causation:** Correlation results cannot independently establish the causes of pollution patterns.
8. **Source verification:** Dataset attribution and redistribution permissions must be confirmed before public release.

## 8. Conclusion

This project establishes a reproducible workflow for exploring historical air-quality data across Indian cities. The analysis documents missingness, summarizes AQI distributions, compares city-level averages, investigates temporal variation, and examines pollutant–AQI associations.

The results highlight the importance of data quality and careful interpretation. Future improvements should include common-period city comparisons, sensitivity analysis with and without imputed pollutant values, validation of extreme observations, and an interactive dashboard for exploring the findings.

## 9. Future Work

- Build an interactive Streamlit dashboard.
- Compare cities over a consistent observation period.
- Test the sensitivity of results to missing-data treatment.
- Validate extreme AQI observations against an authoritative source.
- Add verified interpretations of monthly, seasonal, and correlation results.
- Document the dataset's original source and license.

## 10. Reproducibility

The analysis is organized into four Jupyter notebooks:

1. `01_data_audit.ipynb`
2. `02_data_cleaning.ipynb`
3. `03_exploratory_data_analysis.ipynb`
4. `04_advanced_analysis.ipynb`

Generated analytical tables are stored in `outputs/tables/`, while figures are stored in `outputs/figures/`.
