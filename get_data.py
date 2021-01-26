import pandas as pd
from selenium import webdriver

def get_data() :
    # définir le site web à scraper
    url = "https://www.worldometers.info/coronavirus/"

    # driver path : chromedriver
    option = webdriver.ChromeOptions()

    # Spécifier le mode navigation privée [OPTIONAL]
    option.add_argument("--incognito")

    # Creer nouvelle instance de Chrome en nav privée

    browser = webdriver.Chrome(options=option)

    # Initier le navigateur et visiter le lien
    browser.get(url)

    # Récuperer l'ensemble de la table. Son classname est "table"
    right_table = browser.find_element_by_class_name('table')
    # Récuperer les colonnes. Ils se trouvent dans le tag "th"
    column_name = right_table.find_elements_by_tag_name('th')  # Donner le nom de la colonne
    col_name = []
    for i in range(1, len(column_name) - 1):
        col_name.append(column_name[i].text)

    get_corona = browser.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]')
    right_table = get_corona.find_elements_by_tag_name('tr')

    data_list = []
    data_list2 = []
    for row in right_table:
        # Récuperer les lignes. Chaque ligne représente un pays et ses infos.
        # Elles se trouvent dans le tag "td"
        cells = row.find_elements_by_tag_name('td')
        for i in cells:
            data_list.append(i.text)
        #On stocke dans le dataframe data_list2
        data_list2.append(data_list)
        data_list = []


    #Stocker dans dataframe

    df = pd.DataFrame(data_list2)
    df = df.iloc[:, 1:14]
    df.columns = col_name
    print(df)

    browser.quit()

    #df = pd.read_csv('covid19_world_data.csv')
    new_df = df.dropna(axis=0, how='all')

    new_df = new_df.dropna(axis=1, thresh=30)
    print(new_df)
    print(df.columns)
    print(new_df.shape)

    return new_df
df = get_data()
#print(get_data())


#Sauvegarder en csv
df.to_csv('covid_data.csv')