import matplotlib.pyplot as plt
import pandas as pd

def plot_srilanka_weekly(weekly_df):
    """
    Plot national weekly dengue cases over time.
    weekly_df should contain columns: start.date, cases
    """
    plt.figure(figsize=(12, 6))
    plt.plot(weekly_df["start.date"], weekly_df["cases"])
    plt.title("Weekly Dengue Cases in Sri Lanka (National Level)")
    plt.xlabel("Date")
    plt.ylabel("Number of Cases")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_srilanka_weekly_facet(district_weekly_df):
    """
    Faceted line plots for each district.
    district_weekly_df should contain: district, start.date, cases
    """
    districts = district_weekly_df["district"].unique()
    n = len(districts)

    cols = 4  # number of columns in the subplot grid
    rows = (n + cols - 1) // cols  # calculate number of rows needed

    fig, axes = plt.subplots(rows, cols, figsize=(16, rows * 3), sharey=False)
    axes = axes.flatten()  # flatten axis array for easier indexing

    for i, district in enumerate(districts):
        ax = axes[i]
        data = district_weekly_df[district_weekly_df["district"] == district]
        ax.plot(data["start.date"], data["cases"])
        ax.set_title(district)
        ax.set_xlabel("Date")
        ax.set_ylabel("Cases")
        ax.tick_params(axis="x", rotation=90)  # rotate x-axis labels

    # Turn off unused subplots
    for j in range(i + 1, len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    plt.show()
