import pandas as pd

def get_poverty_data():
    file_url = "https://77.rosstat.gov.ru/storage/mediabank/Доля%20населения%20с%20денежными%20доходами%20ниже%20прожиточного%20минимума%20и%20границы%20бедности%20за%202011-2024%20гг.(1).xlsx"  
    df = pd.read_excel(file_url)
    df.to_csv("data/raw/poverty.csv", index=False)
    return df

if __name__ == "__main__":
    data = get_poverty_data()
    print(data.head())