from src.Utils.Loader import Loader

total_data = Loader.load_data("/Users/yigitbaser/Coronavirusmodel/Storage/RealData/02042020/TotalTable.csv")

print(total_data[total_data['Country,Other']== 'Germany'])