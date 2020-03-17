import pandas as pd
import matplotlib.pyplot as plt
import gathering

plt.close('all')


df = gathering.gather_total_data()
df.plot(kind='bar',x='name',y='age')