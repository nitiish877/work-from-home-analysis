import pandas as pd
import numpy as np

df=pd.read_csv("D:\\downloads\\nitishh\\pandas_project\\kaggle\\work_from_home_burnout_dataset.csv")

burnout=np.corrcoef(df["work_hours"],df["burnout_score"])

weekand_harmful1=df.groupby("day_type")["burnout_score"].sum()

df1=df.select_dtypes(include=["int","float"])


for col in df1.columns:
    correlation=np.corrcoef(df1[col],df1["burnout_score"])
    # print(col,correlation,"\n")

Df=df1.corr()["burnout_score"].sort_values(ascending=False)

high_screen=df[(df["screen_time_hours"]>df["screen_time_hours"].mean()) & (df["sleep_hours"]>df["sleep_hours"].mean())]

# userwise_burnout=high_screen.groupby("user_id")["burnout_score"].sum().sort_values(ascending=False)
a1=np.corrcoef(high_screen["screen_time_hours"],high_screen["burnout_score"])
a2=np.corrcoef(high_screen["sleep_hours"],high_screen["burnout_score"])

a=["work_hours","meetings_count","after_hours_work"]
for col1 in a:
    cor=np.corrcoef(df[col1],df["screen_time_hours"])
    # print(cor)


import matplotlib.pyplot as plt
# task_rate=df.groupby("user_id")["task_completion_rate","burnout_score"].sum()
task_rate=np.corrcoef(df["task_completion_rate"],df["burnout_score"])

# plt.plot(df["task_completion_rate"],df["burnout_score"])
# plt.show()
print(task_rate)

low_sleep=df[(df["sleep_hours"]<df["sleep_hours"].mean()) & (df["screen_time_hours"]>df["screen_time_hours"].mean())]
highscreen_burnout=np.corrcoef(low_sleep["screen_time_hours"],low_sleep["burnout_score"])

high_after_work=df[(df["after_hours_work"]>df['after_hours_work'].mean()) & df["breaks_taken"]<df["breaks_taken"].mean()]
high_after_work_burnout=np.corrcoef(high_after_work["after_hours_work"],high_after_work["breaks_taken"])

print(Df)