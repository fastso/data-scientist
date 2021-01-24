# Matplotlib入門

## Matplotlib入門

Matplotlibはデータの可視化とカスタマイズに最も柔軟性のあるインターフェースpyplotを提供します。  
pyplotの簡単な使用方法は以下：

```python
import pandas as pd

df01 = pd.DataFrame(
    {'time': ['1s', '2s', '3s', '4s', '5s'],
     'value': [1, 2, 3, 4, 5]})
df02 = pd.DataFrame(
    {'time': ['1s', '2s', '3s', '4s', '5s'],
     'value': [5, 4, 3, 2, 1]}
)
```

```python
# matplotlib.pyplotをインポート
import matplotlib.pyplot as plt

# FigureとAxesオブジェクトを作成
fig, ax = plt.subplots()

# df01のvalueをtimeに対してプロット
ax.plot(df01["time"], df01['value'])

# df02のvalueをtimeに対してプロット
ax.plot(df02['time'], df02['value'])

# プロット表示
plt.show()
```

### プロットのカスタマイズ

```python
# Plot Seattle data, setting data appearance
ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-PRCP-NORMAL"], color='b',
        marker='o', linestyle='--')

# Plot Austin data, setting data appearance
ax.plot(austin_weather["MONTH"], austin_weather["MLY-PRCP-NORMAL"], color='r', marker='v',
        linestyle='--')

# Customize the x-axis label
ax.set_xlabel('Time (months)')

# Customize the y-axis label
ax.set_ylabel('Precipitation (inches)')

# Add the title
ax.set_title('Weather patterns in Austin and Seattle')

# Call show to display the resulting plot
plt.show()
```

# Create a Figure and an array of subplots with 2 rows and 2 columns

fig, ax = plt.subplots(2, 2)

# Addressing the top left Axes as index 0, 0, plot month and Seattle precipitation

ax[0, 0].plot(seattle_weather['MONTH'], seattle_weather['MLY-PRCP-NORMAL'])

# In the top right (index 0,1), plot month and Seattle temperatures

ax[0, 1].plot(seattle_weather['MONTH'], seattle_weather['MLY-TAVG-NORMAL'])

# In the bottom left (1, 0) plot month and Austin precipitations

ax[1, 0].plot(austin_weather['MONTH'], austin_weather['MLY-PRCP-NORMAL'])

# In the bottom right (1, 1) plot month and Austin temperatures

ax[1, 1].plot(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'])
plt.show()

