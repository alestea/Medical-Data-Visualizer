import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = None

# 3
# 3.1 overweight
bmi = df['weight']/((df['height']/100)**2)
y = 0
for x in bmi:
    if x > 25: 
        df.loc[y,'overweight'] = 1

    else:
        df.loc[y,'overweight'] = 0

    y = y + 1

# 3.2 cholesterol/ gluc
for indx, values in df['cholesterol'].items():
    if values == 1: 
        df.loc[indx, 'cholesterol'] = 0

    else:
        df.loc[indx, 'cholesterol'] = 1


for indx, values in df['gluc'].items():
    if values == 1: 
        df.loc[indx, 'gluc'] = 0

    else:
        df.loc[indx, 'gluc'] = 1
        
# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])

    # 6    
    df_cat['total'] = 1
    df_cat = df_cat.groupby( ['cardio', 'variable', 'value'], as_index=False).count()
   
    # 7
    plot = sns.catplot(data=df_cat, x='variable', y='total', hue = 'value', col='cardio', kind= 'bar', legend='auto')
    
    # 8
    fig = plot.fig

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) & 
        (df['height'] <= df['height'].quantile(0.975)) & 
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots()

    # 15
    sns.heatmap(corr, mask = mask, annot=True, fmt=".1f", linewidth=.2)


    # 16
    fig.savefig('heatmap.png')
    return fig
