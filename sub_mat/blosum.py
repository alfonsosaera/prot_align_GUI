import ftplib

path = 'blast/matrices/'
filename = 'GONNET'

ftp = ftplib.FTP("ftp.ncbi.nih.gov")
ftp.login('anonymous', 'password')
ftp.cwd(path)
ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
ftp.quit()

BlossumFile = open(filename, "r")
temp = BlossumFile.read()
BlossumFile.close()
print (temp)
