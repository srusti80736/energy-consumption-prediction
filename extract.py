import zipfile
zip_path = r"C:\Users\srust\Energy Consumption\dataset\archive (3).zip"
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall("dataset")
print("Dataset extracted successfully")