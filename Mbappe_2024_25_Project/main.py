"""
Kylian Mbappe 2024-25 Real Madrid Performance Analysis
Dataset scope: Real Madrid competitive matches, excluding the 2025 FIFA Club World Cup.
Run: python main.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "mbappe_2024_25.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

df = pd.read_csv(DATA_FILE)

# Calculate useful performance measures.
df["Goals_Per_Appearance"] = (df["Goals"] / df["Appearances"]).round(2)
df["Goal_Contributions"] = df["Goals"] + df["Assists"]

print("=" * 58)
print("KYLIAN MBAPPE — 2024-25 REAL MADRID PERFORMANCE ANALYSIS")
print("=" * 58)
print(df.to_string(index=False))

total_apps = int(df["Appearances"].sum())
total_goals = int(df["Goals"].sum())
total_assists = int(df["Assists"].sum())
total_minutes = int(df["Minutes"].sum())
overall_rate = total_goals / total_apps

print("\nSUMMARY")
print(f"Total appearances: {total_apps}")
print(f"Total goals: {total_goals}")
print(f"Total assists: {total_assists}")
print(f"Total goal contributions: {total_goals + total_assists}")
print(f"Total minutes: {total_minutes}")
print(f"Goals per appearance: {overall_rate:.2f}")
print(f"Top-scoring competition: {df.loc[df['Goals'].idxmax(), 'Competition']}")

# Chart 1: goals by competition.
plt.figure(figsize=(10, 5))
plt.bar(df["Competition"], df["Goals"])
plt.title("Mbappe's Goals by Competition (2024-25)")
plt.xlabel("Competition")
plt.ylabel("Goals")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "goals_by_competition.png", dpi=150)
plt.close()

# Chart 2: appearances by competition.
plt.figure(figsize=(10, 5))
plt.bar(df["Competition"], df["Appearances"])
plt.title("Mbappe's Appearances by Competition (2024-25)")
plt.xlabel("Competition")
plt.ylabel("Appearances")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "appearances_by_competition.png", dpi=150)
plt.close()

# Chart 3: goals and assists by competition.
plot_df = df.set_index("Competition")[["Goals", "Assists"]]
plot_df.plot(kind="bar", figsize=(10, 5))
plt.title("Goals and Assists by Competition (2024-25)")
plt.xlabel("Competition")
plt.ylabel("Number")
plt.xticks(rotation=25, ha="right")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "goals_and_assists.png", dpi=150)
plt.close()

# Save calculated analysis table.
df.to_csv(OUTPUT_DIR / "analysis_results.csv", index=False)
print(f"\nCharts and results saved in: {OUTPUT_DIR}")
