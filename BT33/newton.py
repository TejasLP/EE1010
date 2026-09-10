import numpy as np
import matplotlib.pyplot as plt

# 1. Generate x and y arrays
x = np.linspace(-2, 3, 400)
y = np.exp(x) - 2

# 2. Use NumPy interpolation to find the root numerically
# By asking for the x-value where y=0, we extract the root from the arrays
root_x = np.interp(0, y, x)
root_y = 0
print("Root:",root_x)
# 3. Set up the figure
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r'$f(x) = e^x - 2$', color='blue', linewidth=2)

# 4. Highlight the numerically derived root
plt.scatter([root_x], [root_y], color='red', zorder=5, s=60, label=f'Root (x ≈ {root_x:.3f})')
plt.text(root_x - 0.5, root_y + 0.5, f'({root_x:.3f}, 0)', fontsize=11, color='black')

# 5. Add axes and grid
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.7)

# 6. Labels and title
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Graph of $e^x - 2$ ', fontsize=14)
plt.legend(fontsize=11)

# 7. Save the figure
plt.savefig('exp_root_interp.pdf', dpi=300, bbox_inches='tight')

# 8. Display the plot
plt.show()

