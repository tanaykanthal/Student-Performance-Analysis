import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("student.csv")
#Student_ID,Study_Hours,Attendance_Percentage,Parental_Education,Internet_Access,Sleep_Hours,Previous_Grade,Final_Score
# print(df.head())
avg_study_hour=df['Study_Hours'].mean()
avg_final_score=df['Final_Score'].mean()
prev_avg_final_score=df['Previous_Grade'].mean()
max_final_score=df['Final_Score'].max()
min_final_score=df['Final_Score'].min()
prev_max_final_score=df['Final_Score'].max()
prev_min_final_score=df['Final_Score'].min()
def getrange(x,y):
    start_y = (int(x) // 10) * 10
    end_y = ((int(y) // 10) + 1) * 10
    coord=[start_y,end_y]
    return coord

#------------------------------------------------------------------------------------------------------------------------------
# student marks to studytime


# planning to remove and add something new






#--------------------------------------------------------------------------------------------------------------------
# #student marks to studytime



plt.figure(figsize=(8,6))
print(df.head())
sns.set_context("talk")

sns.set_style("whitegrid")
sns.regplot(data=df,x="Study_Hours",y="Final_Score",) 

plt.axhline(avg_final_score,color="red",linestyle="--",label="Avg_score")
plt.axhline(prev_avg_final_score,color="blue",linestyle="--",label="previous_Avg_score")
sns.despine()
start_y = (int(min_final_score) // 10) * 10
end_y = ((int(df["Final_Score"].max()) // 10) + 1) * 10
plt.yticks(range(start_y, end_y, 5))

plt.xlabel("Study Hours per Day")
plt.ylabel("Final Score")
plt.title("Study Time vs Final score")
plt.legend()
plt.tight_layout()
plt.savefig(
    "uploads/Studytime_performance1.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

  

#boxplot for student marks to studytime
plt.figure(figsize=(8,6))
sns.boxplot(data=df, x="Study_Hours", y="Final_Score")

plt.title("Distribution of Final Scores by Study Hours")
plt.tight_layout()
plt.savefig(
    "uploads/Studytime_performance2.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()



#--------------------------------------------------------------------------------------------------------------
# attendance vs performance

plt.figure(figsize=(8,6))
sns.set_style("whitegrid")
sns.scatterplot( data=df,x="Attendance_Percentage", y="Final_Score",)
plt.yticks(range(35, 101, 5))
df["Score_Category"] = pd.cut(
    df["Final_Score"],
    bins=[0, 60, 80, 100],
    labels=["Below 60", "60-79", "80+"]
)


sns.scatterplot(
    data=df,
    x="Attendance_Percentage",
    y="Final_Score",
    hue="Score_Category",
    palette=["red", "orange", "green"]
)

# Regression line (single color)
sns.regplot(
    data=df,
    x="Attendance_Percentage",
    y="Final_Score",
    scatter=False,
    color="black"
)
sns.despine()
plt.ylabel("MarksObtain")
plt.xlabel("Attendance")
plt.title("Attendance (%) vs Final Score Density")
plt.savefig(
    "uploads/attendance_vs_performance.png",
    dpi=300,
    bbox_inches="tight"
)
plt.tight_layout()
plt.show()


#----------------------------------------------------------------------------------------------------
# parental education vs marks obtains


plt.figure(figsize=(8,6))

sns.set_context("talk")
order = ["High School", "Graduate", "Postgraduate"]

sns.set_theme(style="darkgrid", font_scale=1.1)
#sns.barplot(data=df,x="Parental_Education",y="Final_Score",palette = ["#9ecae1", "#3182bd", "#08519c"],order=order,errorbar="sd") 
sns.boxplot(
    data=df,
    x="Parental_Education",
    y="Final_Score",
    order=order,
    palette="Blues"
)

plt.axhline(
    avg_final_score,
  color="#e76f51",
    linestyle="--",
    linewidth=2,
    label="Overall Average"
)
plt.legend()
sns.despine()
medians=df.groupby("Parental_Education")["Final_Score"].median()

for i,category in enumerate(order):
    median=medians[category]
    plt.text(i,median+1, f'{median}',ha="center",fontsize="10",color="#ffffff",fontweight="bold")
   

plt.xlabel("parental education ")
plt.ylabel("Final Score")
plt.title("Final Score by Parental Education Level", weight="bold")



start, end = getrange(min_final_score, max_final_score)

plt.yticks(range(start, end + 1, 10))
# plt.yticks(range(start,end+ 1, 10))
plt.tight_layout()
plt.savefig(
    "uploads/parentaleducation_performance.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

#--------------------------------------------------------------------------------------------
sns.countplot(data=df,x="Internet_Access",hue="Internet_Access")
plt.legend(title="Internet")

plt.xlabel("Student internet Access ")
plt.ylabel("no of student")
plt.title("Student Internet Access ", weight="bold")
plt.tight_layout()
plt.savefig(
    "uploads/internetaccess_performance1.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()



#_____________________________________________________________________________

plt.figure(figsize=(8,6))

sns.set_context("talk")


sns.set_theme(style="darkgrid")
sns.stripplot(x="Internet_Access", y="Final_Score", data=df,size=10 ,jitter=True,hue="Parental_Education")
plt.xlabel("Student internet Access ")
plt.ylabel(" Marks of student")
plt.title("Student  Scores by Internet Access ",size=30, weight="bold")
start_y = (int(min_final_score) // 10) * 10
end_y = ((int(df["Final_Score"].max()) // 10) + 1) * 10
plt.yticks(range(start_y, end_y, 5))
plt.tight_layout()
plt.savefig(
    "uploads/internetaccess_performance2.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
#----------------------------------------------------------------------------------------------------------------------

sns.set_theme(style="darkgrid", font_scale=1.1)
sns.set_context("talk")

sns.despine()
# KDE curves

sns.histplot(df["Previous_Grade"], kde=True, label="Previous Grade", alpha=0.5)
sns.histplot(df["Final_Score"], kde=True, label="Final Score", alpha=0.5)

plt.axvline(df["Previous_Grade"].mean(), linestyle="--",color="red",label="Previous average")
plt.axvline(df["Final_Score"].mean(), linestyle="--",label="Current average")

plt.title("Score Distribution: Previous vs Final")
plt.xlabel("Score")
plt.ylabel("Count")
plt.legend()
plt.savefig(
    "uploads/prev_performance1.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()