"""
Ramp Signal Simulation
Signals and Systems Project

Ramp signal definition:
    x(t) = t   for t >= 0
    x(t) = 0   for t <  0
"""

# ---------------------------------------------------------
# Step 1: Import required libraries
# ---------------------------------------------------------
import numpy as np                  # For numerical calculations
import matplotlib.pyplot as plt     # For plotting graphs

# ---------------------------------------------------------
# Step 2: Create the time axis (-5 s to 10 s)
# ---------------------------------------------------------
# 2000 points make the curve look smooth
t = np.linspace(-5, 10, 2000)

# ---------------------------------------------------------
# Step 3: Generate the ramp signal
# ---------------------------------------------------------
# np.where(condition, value_if_true, value_if_false)
# If t >= 0 -> x(t) = t, otherwise x(t) = 0
x = np.where(t >= 0, t, 0)

# ---------------------------------------------------------
# Step 4: Create the figure
# ---------------------------------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

# Part of the signal before t = 0 (value is zero)
ax.plot(t[t < 0], x[t < 0], color="#d62728", linewidth=2.5,
        label="x(t) = 0 for t < 0")

# Part of the signal after t = 0 (increasing ramp)
ax.plot(t[t >= 0], x[t >= 0], color="#1f77b4", linewidth=2.5,
        label="x(t) = t for t ≥ 0")

# Light shading under the ramp to show growth clearly
ax.fill_between(t[t >= 0], x[t >= 0], color="#1f77b4", alpha=0.12)

# ---------------------------------------------------------
# Step 5: Highlight the zero (origin) point
# ---------------------------------------------------------
ax.plot(0, 0, "o", color="black", markersize=9, zorder=5,
        label="Origin (t = 0, x = 0)")
ax.annotate("Origin (0, 0)", xy=(0, 0), xytext=(-3.8, 2),
            fontsize=11, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="black", lw=1.5))

# Show the slope (unit slope = 1) with a marked point at t = 6
ax.plot(6, 6, "s", color="green", markersize=8, zorder=5)
ax.annotate("Slope = 1\nx(6) = 6", xy=(6, 6), xytext=(3.2, 8),
            fontsize=11, color="green", fontweight="bold",
            arrowprops=dict(arrowstyle="->", color="green", lw=1.5))

# ---------------------------------------------------------
# Step 6: Axis lines, labels, title, grid
# ---------------------------------------------------------
ax.axhline(0, color="black", linewidth=1)   # horizontal axis line
ax.axvline(0, color="black", linewidth=1)   # vertical axis line

ax.set_title("Ramp Signal:  x(t) = t · u(t)", fontsize=16, fontweight="bold")
ax.set_xlabel("Time, t (seconds)", fontsize=13)
ax.set_ylabel("Amplitude, x(t)", fontsize=13)

# Axis ticks and limits
ax.set_xticks(np.arange(-5, 11, 1))
ax.set_yticks(np.arange(-1, 12, 1))
ax.set_xlim(-5, 10)
ax.set_ylim(-1, 11)

# Grid for better readability
ax.grid(True, linestyle="--", alpha=0.6)

# Legend
ax.legend(loc="upper left", fontsize=11, frameon=True, shadow=True)

# ---------------------------------------------------------
# Step 7: Display the graph
# ---------------------------------------------------------
plt.tight_layout()
plt.savefig("ramp_signal.png", dpi=300)   # Save as image for the report/PPT
plt.show()                                # Show the graph on screen
