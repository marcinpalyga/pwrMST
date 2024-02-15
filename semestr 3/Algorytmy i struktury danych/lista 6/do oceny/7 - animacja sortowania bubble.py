import random

def bubblesort(S):
    n = len(S)
    stages_S = [S.copy()]

    for i in range(n-1):
        for j in range(0, n-i-1):
            if S[j] > S[j+1]:
                S[j], S[j+1] = S[j+1], S[j]
                stages_S.append(S.copy())

    return S, stages_S

S = [random.randint(-50, 50) for i in range(30)]
S, stages_S = bubblesort(S)




import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(facecolor='black')

def animate(i):
    ax.clear()
    plt.xlim(0, len(stages_S[i]))
    plt.ylim(min(stages_S[i]), max(stages_S[i])) 
    
    for (n,el) in enumerate(stages_S[i]):
        ax.add_patch(Rectangle((n+1e-1, 0-1e-1), 1-1e-1, el, color='w'))

ani = FuncAnimation(fig, animate, frames=len(stages_S), interval=50, repeat=False)
ax.set_facecolor("black")
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.grid(False)
plt.show()