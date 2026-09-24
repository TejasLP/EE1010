import matplotlib.pyplot as plt
import numpy as np

# Define range for x values
x = np.linspace(-5, 10, 400)

# Equation 1: 2x + 3y = 6  =>  y = (6 - 2x) / 3
y1 = (6 - 2 * x) / 3

# Equation 2 with k = 3: 4x + 6y = 9  =>  y = (9 - 4x) / 6
y2_k3 = (9 - 4 * x) / 6

# Equation 2 with k = 5: 4x + 6y = 15 =>  y = (15 - 4x) / 6
y2_k5 = (15 - 4 * x) / 6

plt.figure(figsize=(9, 6))

# Plot lines
plt.plot(x, y1, label=r"$2x + 3y = 6$ (Base Line)", color="black", linewidth=2.5)
plt.plot(
    x,
    y2_k3,
    label=r"$4x + 6y = 9\ (k=3)$",
    color="crimson",
    linestyle="--",
    linewidth=2,
)
plt.plot(
    x,
    y2_k5,
    label=r"$4x + 6y = 15\ (k=5)$",
    color="darkgreen",
    linestyle="-.",
    linewidth=2,
)

# Graph formatting
plt.axhline(0, color="gray", linewidth=0.8, linestyle=":")
plt.axvline(0, color="gray", linewidth=0.8, linestyle=":")
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"Parallel Lines for $k=3$ and $k=5$ vs $2x + 3y = 6$")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.7)

# Save the plot as a PDF
plt.savefig("parallel_lines_plot.pdf", format="pdf", bbox_inches="tight")
    
