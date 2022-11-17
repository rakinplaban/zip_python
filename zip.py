import zipfile

with zipfile.ZipFile('filex.zip','w') as my_zip:
    my_zip.write('text1.txt')
    my_zip.write('text2.txt')
    my_zip.write('Snap.png')

