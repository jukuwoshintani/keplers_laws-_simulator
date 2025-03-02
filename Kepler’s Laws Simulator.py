import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры орбиты
a = 1.0         # большая полуось
e = 0.5         # эксцентриситет
b = a * np.sqrt(1 - e**2)  # малая полуось

# Настройка фигуры и осей
fig, ax = plt.subplots(figsize=(8, 8))
fig.patch.set_facecolor('black')  # фон всей фигуры
ax.set_facecolor('black')           # фон осей
ax.set_aspect('equal')
ax.set_xlim(-1.5 * a, 1.5 * a)
ax.set_ylim(-1.5 * a, 1.5 * a)
ax.axis('off')

# Рисуем орбиту (эллипс) с правильным сдвигом, чтобы звезда (фокус) была в (0,0)
theta = np.linspace(0, 2*np.pi, 300)
x_orbit = a * np.cos(theta) - a * e
y_orbit = b * np.sin(theta)
ax.plot(x_orbit, y_orbit, color='gray', linestyle='--', linewidth=1.5, zorder=1)

# Рисуем звезду (фокус) в точке (0,0)
star, = ax.plot(0, 0, marker='o', markersize=16, color='yellow', zorder=2)

# Рисуем планету; изначально пустой график
planet, = ax.plot([], [], marker='o', markersize=8,
                  markerfacecolor='white', markeredgecolor='red', zorder=3)

def update(t):
    # Вычисляем координаты планеты по эллипсу: x = a*cos(t) - a*e, y = b*sin(t)
    x = a * np.cos(t) - a * e
    y = b * np.sin(t)
    planet.set_data([x], [y])
    return planet,

# Создаем анимацию; blit=False для корректного обновления
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 200),
                    interval=50, repeat=True, blit=False)

plt.title("Kepler's Laws Simulator", color='white')
plt.show()
