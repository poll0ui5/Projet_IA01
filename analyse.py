import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyse1(df):

    plt.figure()
    sns.histplot(x='Sex', data=df)
    plt.title('Sex distribution')
    plt.show()

    plt.figure()
    sns.histplot(x='ChestPainType', data=df)
    plt.title('ChestPainType distribution')
    plt.show()

    plt.figure()
    sns.histplot(x='RestingECG', data=df)
    plt.title('RestingECG distribution')
    plt.show()

    plt.figure()
    sns.histplot(x='RestingECG', data=df)
    plt.title('RestingECG distribution')
    plt.show()

    plt.figure()
    sns.histplot(x='ExerciseAngina', data=df)
    plt.title('ExerciseAngina distribution')
    plt.show()

    plt.figure()
    sns.histplot(x='ST_Slope', data=df)
    plt.title('ST Slope distribution')
    plt.show()


  


def analyse2(df):

    matrice_corr = df.corr(numeric_only=True)
    sns.heatmap(matrice_corr, annot=True)
    plt.show()

    sns.countplot(x=df['Sex'], hue=df['HeartDisease'])
    plt.show()

    sns.countplot(x=df['ChestPainType'], hue=df['HeartDisease'])
    plt.show()

    sns.countplot(x=df['RestingECG'], hue=df['HeartDisease'])
    plt.show()

    sns.countplot(x=df['ExerciseAngina'], hue=df['HeartDisease'])
    plt.show()

    sns.countplot(x=df['ST_Slope'], hue=df['HeartDisease'])
    plt.show()
    

   