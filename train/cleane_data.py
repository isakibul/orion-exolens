import pandas as pd

# Load Kepler CSV (ignore comment lines)
df = pd.read_csv("kepler_data.csv", comment='#')

# Generalized features mapping
feature_map = {
    "orbital_period": "koi_period",
    "transit_duration": "koi_duration",
    "transit_depth": "koi_depth",
    "planet_radius": "koi_prad",
    "snr": "koi_model_snr",
    "semi_major_axis": "koi_sma",
    "stellar_density": "koi_srho",
    "equilibrium_temp": "koi_teq",
    "inclination": "koi_incl",
    "stellar_radius": "koi_srad",
    "stellar_mass": "koi_smass",
    "impact_parameter": "koi_impact"
}

# Select only important features + target
df_selected = df[list(feature_map.values()) + ["koi_disposition"]].copy()

# Handle missing values (drop for now)
df_selected.dropna(inplace=True)

# Rename columns to generalized names
df_selected.rename(columns={v: k for k, v in feature_map.items()}, inplace=True)

# Save clean dataset
df_selected.to_csv("kepler_clean_dataset.csv", index=False)

print("✅ Clean dataset saved as kepler_clean_dataset.csv")
