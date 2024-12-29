import numpy as np
import matplotlib.pyplot as plt
from mpmath import zeta, mp


mp.dps = 20  


t_values = np.linspace(0, 50, 1000)  
zeta_values = [zeta(0.5 + 1j * t) for t in t_values]
zeta_magnitude = [abs(z) for z in zeta_values]  


plt.figure(figsize=(12, 6))
plt.plot(t_values, zeta_magnitude, color='blue', label="|ζ(1/2 + it)|")
plt.axhline(0, color='black', linewidth=0.8, linestyle='dashed')  
plt.xlabel("t (Imaginary Part)")
plt.ylabel("|ζ(1/2 + it)| (Size)")
plt.title("Size of the Riemann Zeta Function in the Critical Strip")
plt.legend()
plt.grid()
plt.savefig("zetafunction_Critical_Strip1.png", dpi=300)
plt.show()