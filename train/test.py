# # check null value
# import pandas as pd

# # Load clean dataset
# df = pd.read_csv("kepler_clean_dataset.csv")

# # Check for missing values per column
# missing_counts = df.isnull().sum()

# print("❌ Missing values per column:\n")
# for col, count in missing_counts.items():
#     print(f"{col}: {count}")


# # make user csv
# import pandas as pd

# data = {
#     "orbital_period":[9.48803557,54.4183827,19.89913995,1.736952453,2.525591777,11.09432054,4.13443512,2.56658897,7.36178958,16.06864674],
#     "transit_duration":[2.9575,4.507,1.7822,2.40641,1.6545,4.5945,3.1402,2.429,5.022,3.5347],
#     "transit_depth":[615.8,874.8,10829.0,8079.2,603.3,1517.5,686.0,226.5,233.7,4914.3],
#     "planet_radius":[2.26,2.83,14.6,33.46,2.75,3.9,2.77,1.59,39.21,5.76],
#     "snr":[35.8,25.8,76.3,505.6,40.9,66.5,40.2,15.0,47.7,161.9],
#     "semi_major_axis":[0.0853,0.2734,0.1419,0.0267,0.0374,0.0992,0.0514,0.0374,0.082,0.1158],
#     "stellar_density":[3.20796,3.02368,7.29555,0.2208,1.98635,0.67324,0.37377,0.48909,0.00485,3.6659],
#     "equilibrium_temp":[793.0,443.0,638.0,1395.0,1406.0,835.0,1160.0,1360.0,1342.0,600.0],
#     "inclination":[89.66,89.57,88.96,67.09,85.41,88.11,83.72,82.17,60.92,89.92],
#     "stellar_radius":[0.927,0.927,0.868,0.791,1.046,0.972,0.972,0.972,1.958,0.848],
#     "stellar_mass":[0.919,0.919,0.961,0.836,1.095,1.053,1.053,1.053,1.358,0.801],
#     "impact_parameter":[0.146,0.586,0.969,1.276,0.701,0.538,0.762,0.755,1.169,0.052],
# }

# # Create DataFrame
# df = pd.DataFrame(data)

# # Prediction-ready CSV (12 features + optional label)
# prediction_df = df[[
#     "orbital_period",
#     "transit_duration",
#     "transit_depth",
#     "planet_radius",
#     "snr",
#     "semi_major_axis",
#     "stellar_density",
#     "equilibrium_temp",
#     "inclination",
#     "stellar_radius",
#     "stellar_mass",
#     "impact_parameter",
# ]]

# # Save CSV
# prediction_df.to_csv("sample_prediction_input.csv", index=False)
# print("✅ Sample prediction CSV saved as sample_prediction_input.csv")
