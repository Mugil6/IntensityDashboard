import pandas as pd
from google.cloud import bigquery

# Load data
emissions = pd.read_csv("cleaned_emissions_data.csv")
generation = pd.read_csv("cleaned_generation_data.csv")

# Clean column names
emissions.columns = emissions.columns.str.strip()
generation.columns = generation.columns.str.strip()

# Convert emission and generation columns to numeric
emissions["CO2 Emissions (MT)"] = pd.to_numeric(emissions["CO2 Emissions (MT)"], errors="coerce")
generation["Generation (GWh)"] = pd.to_numeric(generation["Generation (GWh)"], errors="coerce")

# Group by State and Year to get total values
emissions_grouped = emissions.groupby(["State", "Year"], as_index=False)["CO2 Emissions (MT)"].sum()
generation_grouped = generation.groupby(["State", "Year"], as_index=False)["Generation (GWh)"].sum()

# Merge the grouped data
df = pd.merge(emissions_grouped, generation_grouped, on=["State", "Year"], how="inner")

# Drop any rows where generation is zero or NaN to avoid divide-by-zero
df = df.dropna(subset=["CO2 Emissions (MT)", "Generation (GWh)"])
df = df[df["Generation (GWh)"] > 0]

# Calculate intensity
df["Intensity_g_per_kWh"] = (df["CO2 Emissions (MT)"] * 1000) / df["Generation (GWh)"]

# Rename columns for BigQuery compatibility
df.rename(columns={
    "CO2 Emissions (MT)": "Emissions_MT",
    "Generation (GWh)": "Generation_GWh"
}, inplace=True)

client = bigquery.Client()
table_id = "emissionstracker-465105.emissions_ds.emission_intensity"