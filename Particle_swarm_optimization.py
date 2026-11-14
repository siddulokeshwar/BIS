{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMYnL/gVb4pOJFXjsQ2eNHr"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "71628a21",
        "outputId": "7dbb6a96-06ea-475a-d2d4-9fd7b9cc6a9d"
      },
      "source": [
        "import numpy as np\n",
        "\n",
        "\n",
        "def fitness(x):\n",
        "    return np.power(x, 2)\n",
        "\n",
        "population_size = 10\n",
        "iterations = 50\n",
        "inertia = 0.5\n",
        "cognitive, social = 1.5, 1.5\n",
        "\n",
        "\n",
        "\n",
        "positions = np.random.uniform(0 , 50, size=population_size)\n",
        "velocities = np.random.uniform(0, 1, size=population_size)\n",
        "\n",
        "p_best_positions = np.copy(positions)\n",
        "p_best_fitnesses = fitness(p_best_positions)\n",
        "\n",
        "g_best_idx = np.argmin(p_best_fitnesses)\n",
        "g_best_position = p_best_positions[g_best_idx]\n",
        "g_best_fitness = p_best_fitnesses[g_best_idx]\n",
        "\n",
        "\n",
        "print(f\"Initial Global Best Position: {g_best_position:.4f}, Fitness: {g_best_fitness:.4f}\\n\")\n",
        "\n",
        "for i in range(iterations):\n",
        "    r1 = np.random.uniform(0, 1, size=population_size)\n",
        "    r2 = np.random.uniform(0, 1, size=population_size)\n",
        "\n",
        "\n",
        "    velocities = (inertia * velocities +\n",
        "                  cognitive * r1 * (p_best_positions - positions) +\n",
        "                  social * r2 * (g_best_position - positions))\n",
        "\n",
        "\n",
        "    positions = positions + velocities\n",
        "\n",
        "\n",
        "    current_fitnesses = fitness(positions)\n",
        "\n",
        "    improved_mask = current_fitnesses < p_best_fitnesses\n",
        "    p_best_positions[improved_mask] = positions[improved_mask]\n",
        "    p_best_fitnesses[improved_mask] = current_fitnesses[improved_mask]\n",
        "\n",
        "    min_current_idx = np.argmin(p_best_fitnesses)\n",
        "    if p_best_fitnesses[min_current_idx] < g_best_fitness:\n",
        "        g_best_position = p_best_positions[min_current_idx]\n",
        "        g_best_fitness = p_best_fitnesses[min_current_idx]\n",
        "\n",
        "    if (i + 1) % 10 == 0 or i == 0:\n",
        "        print(f\"Iteration {i+1:02d}/{iterations}: Best Position = {g_best_position:.6f}, Best Fitness = {g_best_fitness:.6f}\")\n",
        "\n",
        "print(f\"\\nOptimization complete.\\nFinal Best Position: {g_best_position:.6f}\\nFinal Best Fitness: {g_best_fitness:.6e}\")"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Initial Global Best Position: 0.0616, Fitness: 0.0038\n",
            "\n",
            "Iteration 01/50: Best Position = 0.061556, Best Fitness = 0.003789\n",
            "Iteration 10/50: Best Position = 0.003445, Best Fitness = 0.000012\n",
            "Iteration 20/50: Best Position = 0.000426, Best Fitness = 0.000000\n",
            "Iteration 30/50: Best Position = 0.000002, Best Fitness = 0.000000\n",
            "Iteration 40/50: Best Position = -0.000001, Best Fitness = 0.000000\n",
            "Iteration 50/50: Best Position = 0.000000, Best Fitness = 0.000000\n",
            "\n",
            "Optimization complete.\n",
            "Final Best Position: 0.000000\n",
            "Final Best Fitness: 9.707163e-14\n"
          ]
        }
      ]
    }
  ]
}