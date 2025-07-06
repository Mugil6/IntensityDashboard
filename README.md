# Emission Intensity Dashboard

This project tracks and visualizes the **emission intensity of power generation across Indian states** using data from the [Indian Climate and Energy Dashboard (ICED)](https://iced.niti.gov.in/).

---

## Objective

To monitor how much CO₂ (in grams) is emitted per kilowatt-hour (g/kWh) of electricity generation in India over the years, and enable insights on **decarbonization trends**.

---

## Data Source

- Downloaded from **https://iced.energy.gov.in/**
- Two datasets used:
  - **CO₂ Emissions by Fuel Type (Coal, Oil & Gas)** – state-wise, yearly
  - **Electricity Generation by Source** – state-wise, yearly

---

## Methodology

1. **Data Preprocessing (Python)**:
   - Restructured raw Excel sheets into a normalized schema (`State`, `Year`, `Fuel Type` or `Source`, `Value`)
   - Grouped and aggregated data using `pandas`
   - Computed **emission intensity** as:

     \[
     \text{Intensity (g/kWh)} = \frac{\text{CO₂ Emissions (MT)} \times 1000}{\text{Generation (GWh)}}
     \]

2. **Cloud Platform (Google Cloud Platform)**:
   - Uploaded final CSV to **BigQuery** using Python
   - Dataset: `emissions_ds`
   - Table: `emission_intensity`

3. **Visualization (Looker Studio)**:
   - Built an interactive dashboard with:
     - State & Year filters
     - Trend chart and bar comparison
     - KPI tiles for total generation and emissions

---

## Tech Stack

- Python (pandas, google-cloud-bigquery)
- Google Cloud Platform (BigQuery, Cloud Shell)
- Looker Studio for dashboarding
- Git & GitHub for version control

---
