import numpy as np
import matplotlib.pyplot as plt


def riemann_zeta(s, terms=100):
    """Approximate the Riemann Zeta Function using a series expansion."""
    if s <= 1:
        return float('inf') 
    return sum(1 / (n ** s) for n in range(1, terms + 1))


s_values = np.linspace(0.1, 10, 500)  
zeta_values = [riemann_zeta(s) for s in s_values]


plt.figure(figsize=(10, 6))
plt.plot(s_values, zeta_values, label=r'$\zeta(s)$', color='blue')
plt.axvline(1, color='red', linestyle="--", label="s = 1 (Divergence Point)")
plt.title("Riemann Zeta Function", fontsize=16)
plt.xlabel("s (Real part)", fontsize=12)
plt.ylabel(r'$\zeta(s)$', fontsize=12)
plt.grid(alpha=0.4)
plt.legend()
plt.savefig("Zeta_Funtion.png", dpi=300)
plt.show()