# Matplotlib時系列プロット

## 時系列データのプロット

実世界のデータの多くは時系列で整理されています。可視化は時系列データのパターンを見出すための優れた方法です。 Matplotlibを使用した時系列データのプロットを試みます。

サンプルデータとして以下を使用します。

```csv
date,value01,value02
2021-01-01,1,100
2021-01-02,3,500
2021-01-03,2,200
2021-01-04,4,600
2021-01-05,3,300
2021-01-06,5,700
2021-01-07,4,400
2021-01-08,6,800
2021-01-09,5,500
2021-01-10,7,900
2021-01-11,6,600
2021-01-12,8,1000
2021-01-13,7,700
2021-01-14,9,1100
2021-01-15,8,800
2021-01-16,10,1200
```

まずはサンプルデータをインポートします。（日付をインデックスとして）[pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)

```python
import pandas as pd

df = pd.read_csv('df.csv', parse_dates=['date'], index_col='date')
```

時系列データの全体をプロットします。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(df.index, df['value01'])
ax.set_xlabel('Date')
ax.set_ylabel('Value01')
plt.show()
```

[図]

時系列データのズームインをし、プロットします。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# ズームイン
df_zoom_in = df['2021-01-01':'2021-01-05']

ax.plot(df_zoom_in.index, df_zoom_in["value01"])
plt.show()
```

[図]

## 複数変数の時系列プロット

2つの変数value01とvalue02を同時にプロットしてみると、下記のようにvalue01の特徴を見出すことができなくなります。
理由はvalue01の測定値スケールが1～10まで、value02の100～1200よりずっと小さいから。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(df.index, df['value01'])
ax.plot(df.index, df['value02'])
plt.show()
```

[図]

この場合、双軸を使用します。2つの異なるy軸スケールを使用して、同じサブプロットにプロットします。

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(df.index, df['value01'], color='b')

# X軸を共有する双軸
ax2 = ax.twinx()

ax2.plot(df.index, df['value02'], color='r')
plt.show()
```

[図]

時系列データを多数プロットする場合、プロット用関数を定義してみます。
[matplotlib.axes.Axes.tick_params](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.axes.Axes.tick_params.html)

```python
def plot_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params('y', colors=color)
```

[図]

定義した関数を使ってみます。

```python
fig, ax = plt.subplots()
plot_timeseries(ax, df.index, df['value01'], 'blue', 'Date', 'Value01')
ax2 = ax.twinx()
plot_timeseries(ax2, df.index, df['value02'], 'red', 'Date', 'Value02')
plt.show()
```

[図]

## 時系列データの注釈

注釈を付けることは、可視化を強化する重要な方法です。特定の部分を参照するテキストでデータのいくつかの特徴を強調でき、その特徴を説明します。

```python
fig, ax = plt.subplots()
plot_timeseries(ax, df.index, df['value01'], 'blue', 'Date', 'Value01')
ax2 = ax.twinx()
plot_timeseries(ax2, df.index, df['value02'], 'red', 'Date', 'Value02')

ax2.annotate('annotate day', xy=(pd.Timestamp('2021-01-10'), 900),
             xytext=(pd.Timestamp('2021-01-10'), 200),
             arrowprops={'arrowstyle': '->', 'color': 'gray'})

plt.show()
```

[図]