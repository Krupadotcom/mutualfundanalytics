import matplotlib.pyplot as plt
import os

os.makedirs("reports", exist_ok=True)

plt.plot([1, 2, 3], [10, 20, 30])
plt.title("Test Graph")

plt.savefig("reports/test_graph.png")

print("Graph saved in reports folder")