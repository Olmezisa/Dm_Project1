import matplotlib.pyplot as plt
import numpy as np
from sympy import primerange


def prime_counting_function(x):
    return len(list(primerange(1, x+1)))


x_values = np.arange(2, 1000, 10)
pi_values = [prime_counting_function(x) for x in x_values]
approximation = x_values / np.log(x_values)


plt.figure(figsize=(10, 6))
plt.plot(x_values, pi_values, label="π(x) (Prime Number Counting Function)", color="blue")
plt.plot(x_values, approximation, label="x / ln(x) (Approach)", linestyle="dashed", color="orange")
plt.xlabel("x")
plt.ylabel("Number of Prime Numbers")
plt.title("Distribution and Approximation of Prime Numbers")
plt.legend()
plt.grid()
plt.savefig("Prime_Numbers_Distrubtion.png", dpi=300)
plt.show()