import zipfile

my_zip = zipfile.ZipFile('filex.zip','w')


my_zip.write('text1.txt')
my_zip.write('text2.txt')
my_zip.write('Snap.png')

my_zip.close()