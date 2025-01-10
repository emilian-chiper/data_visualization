import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

cubes = [1, 8, 27, 64, 125]

fig, ax = plt.subplots()
ax.plot(cubes)

plt.show()
