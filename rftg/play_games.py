import rftg
import matplotlib.pyplot as plt

# Parameters
n = 1000

# Run n games
score_record = []
for game in range(n):
    score_record.append(rftg.run_game())

print(score_record)

# Plot results
bins = 15
plt.hist(score_record, bins, density=1)
plt.show()