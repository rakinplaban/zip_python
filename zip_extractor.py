import zipfile

with zipfile.ZipFile('filex.zip','r') as my_zip:
    my_zip.extractall('filex')
    my_zip.extract('Snap.png')