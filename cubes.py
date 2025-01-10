import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

ax.set_title("Cubes", fontsize=32)
ax.set_xlabel("Value", fontsize=16)
ax.set_ylabel("Cube", fontsize=16)

ax.tick_params(labelsize=16)

ax.axis([0, 5100, 0, 130_000_000_000])
ax.ticklabel_format(style='plain')

plt.savefig('cubes_plot.png', bbox_inches='tight')

