import seaborn as sns
import matplotlib.pyplot as plt
def nettoyage1(df):
    print("Number of Duplicates:", df.duplicated().sum(), "\n") #nombre de doublon
    print("Nombre de NaN : \n" , df.isna().sum()) #nombre de données manquantes
    

    num_df = df.select_dtypes(include=['int64', 'float64'])

    min_values = num_df.describe().loc['min']

    print("Minimums des colonnes numeriques : ")
    print(min_values)

    cat_df = df.select_dtypes(include=['object'])

    print("Valeurs uniques des variables catégorielles : \n")
    for col in cat_df.columns :
        unique_value = cat_df[col].unique()
        print(unique_value)

    sns.boxplot(y=df['Age'])
    plt.title("Boxplot de l'âge")
    plt.show()
    
    
    