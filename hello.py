import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 400)
plt.figure(figsize=(8, 4))
plt.plot(x, np.sin(x))
plt.title("My first plot")
plt.savefig("test_sin.png", dpi=150)
print("done")