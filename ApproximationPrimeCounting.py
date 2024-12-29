import matplotlib.pyplot as plt
import numpy as np

def li_function(x):
    """Approximation of the logarithmic integral function."""
    result = []
    for xi in x:
        if xi > 1:
            integral = 0
            dx = 0.01  
            t = 2  
            while t <= xi:
                integral += dx / np.log(t)
                t += dx
            result.append(integral)
        else:
            result.append(0)
    return np.array(result)

def prime_counting_function(x):
    """Approximation of the prime-counting function π(x)."""
    result = []
    for xi in x:
        count = 0
        for i in range(2, int(xi) + 1):
            is_prime = True
            for j in range(2, int(np.sqrt(i)) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
        result.append(count)
    return np.array(result)

def x_log_x_function(x):
    """Compute x / log(x)."""
    return x / np.log(x)


x = np.arange(2, 201)  
li_x = li_function(x)  
pi_x = prime_counting_function(x)  
x_log_x = x_log_x_function(x)  


plt.figure(figsize=(12, 6))  


plt.plot(x, li_x, 'k-', label='Li(X) (Upper Bound)')  
plt.step(x, pi_x, 'r-', label='π(X) (Prime Counting)', where='post')  
plt.plot(x, x_log_x, 'b-', label='X/log(X) (Lower Bound)')  

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plots of Li(X), π(X), and X/log(X)')
plt.legend()


plt.xlim(0, 200)
plt.ylim(0, 50) 


plt.grid()
plt.show()