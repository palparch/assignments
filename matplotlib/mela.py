import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("melasale.csv")

#df.plot(kind='line', color=['red', 'blue', 'brown'], marker='*', markersize=10, linewidth=3, linestyle='--')

df.plot(kind='barh', color=['red', 'yellow', 'purple'], edgecolor='green', linewidth=2, linestyle='--', x='Day')

plt.title('Mela sales')

plt.xlabel('Days')
plt.ylabel('Sales in Rs')

plt.show()
