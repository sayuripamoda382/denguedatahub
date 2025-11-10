import pydenguedatahub as dh
from pydenguedatahub import load_dataset
from pydenguedatahub.preprocessing import preprocess_srilanka_weekly
from pydenguedatahub.visualization import plot_srilanka_weekly, plot_srilanka_weekly_facet

# 1. List datasets
print("Available datasets:")
print(dh.list_datasets())
print()

# 2. Load dataset
df = load_dataset("srilanka_weekly_data")
print(df.head())
print(df.columns)
print(df.shape)
print()

# 3. Preprocess
national_weekly, district_weekly, national_yearly, district_yearly = preprocess_srilanka_weekly(df)

# 4. Plot
plot_srilanka_weekly(national_weekly)
plot_srilanka_weekly_facet(district_weekly)


# Try with another country data
america_df = load_dataset("americas_annual_data")
print(america_df.head())
print(america_df.columns)
print(america_df.shape)
print()

# filter regions in world annual data
world_annual = load_dataset("world_annual")
print(world_annual.head())
