import pandas as pd
from selenium import webdriver

def get_data() :
    url = "https://www.worldometers.info/coronavirus/"
# driver path
    option = webdriver.ChromeOptions()
# Specifying incognito mode as you launch your browser[OPTIONAL]
    option.add_argument("--incognito")

# Create new Instance of Chrome in incognito mode
    browser = webdriver.Chrome(options=option)
# Initiate the browser and visit the link
    browser.get(url)
    right_table = browser.find_element_by_class_name('table')

    column_name = right_table.find_elements_by_tag_name('th')  # Give column name
    col_name = []
    for i in range(1, len(column_name) - 1):
        col_name.append(column_name[i].text)

    get_corona = browser.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[4]/div[1]/div/table/tbody[1]')
    right_table = get_corona.find_elements_by_tag_name('tr')

    data_list = []
    data_list2 = []
    for row in right_table:
        cells = row.find_elements_by_tag_name('td')
        for i in cells:
            data_list.append(i.text)
        data_list2.append(data_list)
        data_list = []
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










df.to_csv('covid_data.csv')