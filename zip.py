import zipfile

with zipfile.ZipFile('filex.zip','w',compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('text1.txt')
    my_zip.write('text2.txt')
    my_zip.write('Snap.png')

