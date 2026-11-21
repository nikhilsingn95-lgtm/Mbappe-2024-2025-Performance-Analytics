# Kylian Mbappe 2024-25 Performance Analysis

## Project scope
This beginner-level Python project analyses Kylian Mbappe's Real Madrid performance by competition in the 2024-25 season. The dataset includes six Real Madrid competitions and excludes the 2025 FIFA Club World Cup. It does not include France national-team matches.

## Files
- `main.py` — Python analysis and chart generation
- `mbappe_2024_25.csv` — competition-level dataset
- `requirements.txt` — Python libraries needed
- `Documentation.docx` — project report
- `outputs/` — generated charts and calculated results (created after running the script)

## Run the project
1. Install Python.
2. Open this folder in VS Code.
3. Open the VS Code terminal in this folder.
4. Run: `python -m pip install -r requirements.txt`
5. Run: `python main.py`

If the command `python` does not work on Windows, try `py main.py`.

## Data notes
Competition-level appearance, goal, assist and minute figures are transcribed from the cited 2024/25 player statistics table. Totals in this dataset are 56 appearances, 43 goals and 4 assists. Real Madrid's official article independently confirms 43 goals in all competitions at the end of the campaign before the Club World Cup. The club later reported 44 goals after the Club World Cup; that later total is outside this dataset's defined scope.

## Sources
- SportPremi, Kylian Mbappe 2024/25 statistics: https://sportpremi.com/player/kylian-mbappe-278/stats/season/2024
- Real Madrid, “Mbappé: Golden Boot 2024-25” (25 May 2025): https://www.realmadrid.com/en-US/news/football/first-team/latest-news/mbappe-bota-de-oro-2024-25-25-05-2025
- FBref, Real Madrid 2024-25 all-competitions statistics: https://fbref.com/en/squads/53a2f082/2024-2025/all_comps/Real-Madrid-Stats-All-Competitions

## Limitations
This is a small descriptive dataset. It compares competition totals; it does not measure the quality of opponents, match difficulty, expected goals, or the player's full contribution. Different statistical providers may classify assists or competition scope differently.
