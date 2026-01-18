import numpy as np
from numpy.typing import NDArray
#0 → team_id
#1 → points
#2 → rebounds
#3 → assists
#4 → minutes
#5 → win
# 0= loss 1= win
games = np.array([
[ 1, 23, 7, 10, 34, 0],
[ 2, 43, 12, 9, 40, 0],
[ 2, 11, 3, 12, 29, 1],
[ 3, 31, 7, 1, 39, 1],
[ 4, 40, 15, 1, 29, 1],
[ 1, 21, 7, 9, 39, 1],
[ 2, 49, 11, 8, 34, 0],
[ 2, 17, 6, 8, 34, 1],
[ 3, 31, 4, 5, 34, 0],
[ 4, 29, 11, 2, 32, 1],
[ 1, 25, 3, 8, 37, 1],
[ 2, 44, 12, 6, 38, 1],
[ 2, 25, 6, 6, 32, 1],
[ 3, 5, 1, 0, 3, 1],
[ 4, 31, 14, 4, 26, 1]])

games_no_team = games[:, 1:]
games_reshaped = games_no_team.reshape(3, 5, 5)
player_totals = np.sum(games_reshaped, axis=0)
#0 → points
#1 → rebounds
#2 → assists
#3 → minutes
#4 → win
player_names = np.array(["Cade", "Luka", "LeBron", "Ant", "Wemby"])
games_played = games_reshaped.shape[0]

points_totals = player_totals[:, 0]
points_avgs = points_totals / games_played

print("Player Points Summary")
print("-" * 28)

for name, total, avg in zip(player_names, points_totals, points_avgs):
    print(f"{name:<8} | Total: {total:>3} | Avg: {avg:>5.2f}")

total_games = 3
wins_per_player = np.sum(games_reshaped[:, :, 4], axis=0)

print("-" * 28)
print("Player Win Summary")
print("-" * 28)

avg_minutes = np.mean(games_reshaped[:, :, 3], axis=0)

for i, (name, wins) in enumerate(zip(player_names, wins_per_player)):
    perc = (wins / total_games) * 100
    print(
        f"{name:<8} | Games: {total_games:>3} | Avg.Min: {avg_minutes[i]:>5.1f} | Wins: {wins:>3} | Percentage: {perc:>6.2f}%"
    )

# Efficiency per game = points + rebounds + assists
efficiency_per_game = (
    games_reshaped[:, :, 0] +
    games_reshaped[:, :, 1] +
    games_reshaped[:, :, 2]
)

efficiency_avg = np.mean(efficiency_per_game, axis=0)

points_rank = np.argsort(points_avgs)[::-1]
print("\nRanking by Points Per Game")
print("-" * 30)

for i in points_rank:
    print(f"{player_names[i]:<8} | PPG: {points_avgs[i]:>6.2f}")

eff_rank = np.argsort(efficiency_avg)[::-1]

print("\nRanking by Efficiency")
print("-" * 30)

for i in eff_rank:
    print(f"{player_names[i]:<8} | Eff: {efficiency_avg[i]:>6.2f}")

top_scorer = player_names[np.argmax(points_avgs)]
top_eff = player_names[np.argmax(efficiency_avg)]

print(f"\nTop scorer on average: {top_scorer}")
print(f"Most efficient player: {top_eff}")

points_all = games_reshaped[:, :, 0].flatten()
wins_all = games_reshaped[:, :, 4].flatten()
corr = np.corrcoef(points_all, wins_all)[0, 1]
print(f"\nCorrelation between points and winning: {corr:.2f}")









