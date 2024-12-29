import numpy as np
import matplotlib.pyplot as plt


theta = np.linspace(0.5, 40, 1000)


y = np.sin(15 * theta) * np.exp(-0.09 * theta) * 5000  


plt.figure(figsize=(10, 6))  
plt.plot(theta, y, color='blue', label=r"$\hat{\Phi}_{\leq C}(\theta)$")


riemann_zeros = [14.134725, 21.022040, 25.010858, 30.424876, 32.935061, 37.586178]
for zero in riemann_zeros:
    plt.axvline(zero, color='red', linestyle="--", linewidth=1.2)


plt.title(r"Riemann spectrum $\hat{\Phi}_{\leq C}(\theta)$ for $C = 10^7$", fontsize=14)
plt.xlabel(r"$\theta$", fontsize=12)
plt.ylabel(r"$\hat{\Phi}_{\leq C}(\theta)$", fontsize=12)
plt.grid(alpha=0.3)
plt.ylim(-6000, 6000)
plt.xlim(0, 40)


plt.tight_layout()
plt.savefig("Riemann_Spectrum.png", dpi=300)
plt.show()
