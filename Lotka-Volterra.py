import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def lotka_volterra(population, t, alpha, beta, delta, gamma):
    prey, predator = population
    dprey_dt = alpha * prey - beta * prey * predator
    dpredator_dt = delta * prey * predator - gamma * predator
    return [dprey_dt, dpredator_dt]

def simulate_lotka_volterra():
    initial_population = [40, 9]  # Initial prey and predator populations
    alpha, beta, delta, gamma = 0.1, 0.02, 0.01, 0.1  # Parameters
    t = np.linspace(0, 200, 1000)

    population = odeint(lotka_volterra, initial_population, t, args=(alpha, beta, delta, gamma))

    prey, predator = population.T

    plt.plot(t, prey, label="Prey")
    plt.plot(t, predator, label="Predator")
    plt.legend()
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.title("Lotka-Volterra Predator-Prey Model")
    plt.show()

simulate_lotka_volterra()
