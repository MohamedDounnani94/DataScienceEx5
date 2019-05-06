 # -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt

"""
Valore atteso di una variabile casuale definisce il valore medio
di una lungua sequenza di campioni ripetuti della variabile casuale
"""

# Esempio variabile casuale di un lancio di dadi -> media variabile casuale
def random_variable_of_dice_roll():
    return random.randint(1, 7)

num_trials = range(100, 10000, 10)
avgs = []
for num_trial in num_trials:
    trials = []
    for trial in range(1, num_trial):
        trials.append( random_variable_of_dice_roll() )
    avgs.append(sum(trials) / float(num_trial))
    
plt.plot(num_trials, avgs)
plt.xlabel("Number of trials")
plt.ylabel("Average")
plt.show()