import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("time_series_covid19_confirmed_global.csv")

print(data.shape)

dates = data.columns[4:]

covid_data = data[dates].apply(pd.to_numeric, errors="coerce")

country_totals = covid_data.groupby(data["Country/Region"]).sum()

daily_cases = country_totals.diff(axis=1)

top_countries = country_totals.sum(axis=1).nlargest(5)

print(top_countries)

plt.figure(figsize=(10, 5))

for country in top_countries.index:
    plt.plot(dates, daily_cases.loc[country], label=country)

plt.title("Daily COVID-19 Cases - Top 5 Countries")
plt.xlabel("Date")
plt.ylabel("Daily Cases")
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("7_day_rolling_average.png", dpi=300, bbox_inches="tight")
plt.show()

top_country = top_countries.index[0]

rolling_average = daily_cases.loc[top_country].rolling(window=7).mean()

plt.figure(figsize=(10, 5))
plt.plot(dates, rolling_average)
plt.title(f"7-Day Rolling Average - {top_country}")
plt.xlabel("Date")
plt.ylabel("7-Day Average Cases")
plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()
plt.savefig("7_day_rolling_average.png", dpi=300, bbox_inches="tight")
plt.show()

peak_date = daily_cases.loc[top_country].idxmax()
peak_cases = daily_cases.loc[top_country].max()

print("Peak Country:", top_country)
print("Peak Date:", peak_date)
print("Peak Daily Cases:", peak_cases)