import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyse():
    heart = pd.read_csv("heart.csv") #importation des données

    plt.figure()
    sns.histplot(x='Age', data=heart)
    plt.title('Age distribution')
    plt.show()

    plt.figure()
    sns.histplot(x='Sex', data=heart)
    plt.title('Sex distribution')
    plt.show()

    plt.figure()
    sns.histplot(x='Cholesterol', data=heart)
    plt.title('Cholesterol distribution')
    plt.show()

    plt.figure()
    sns.histplot(x='ChestPainType', data=heart)
    plt.title('Chest pain type distribution')
    plt.show()


analyse()