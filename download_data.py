import zipfile, urllib.request, shutil

url = 'https://github.com/Akashkunwar/Datathon2022/blob/main/data/Given_Datathon_data.zip?raw=true'

with urllib.request.urlopen(url) as response, open('Given_Datathon_data.zip', 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
    with zipfile.ZipFile('Given_Datathon_data.zip') as zf:
        zf.extractall()