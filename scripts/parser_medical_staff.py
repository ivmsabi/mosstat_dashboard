import pandas as pd

def get_medstaff_data():
    file_url = "https://77.rosstat.gov.ru/storage/mediabank/Численность%20медицинских%20кадров%20за%202020-2024%20гг(1).xlsx"  
    df = pd.read_excel(file_url)
    df.to_csv("data/raw/medstaff.csv", index=False)
    return df

if __name__ == "__main__":
    data = get_medstaff_data()
    print(data.head())