#%%
import plotly.express as px

df = px.data.tips()
fig = px.violin(df, y="total_bill")
fig.show()
# %%
px.histogram(df, y="total_bill")
# %%
