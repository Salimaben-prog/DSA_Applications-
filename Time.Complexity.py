import time
import matplotlib.pyplot as plt

def quadratic_example_1(n):
    """Simple O(n²) algorithm with nested loops"""
    total_operations = 0

    for i in range(n):  # O(n)
        for j in range(n):  # O(n) × O(n) = O(n²)
            total_operations += 1  # Constant operation

    return total_operations


# Example usage
print("Operations:", quadratic_example_1(5))

T=[]
for n in range(600):
    t=time.time()
    quadratic_example_1(n)
    t=time.time()-t
    T.append(t)
    print(n,t)

plt.plot(T)
plt.show()
