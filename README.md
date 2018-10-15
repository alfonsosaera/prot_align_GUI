# prot_align_GUI

Graphic user interface that aligns two protein sequences with the selected substitution matrix using a simplified version of the needleman-wunsch algorithm. It is written in `Python` using the `tkinter` module and based on my [prot_align script](https://github.com/alfonsosaera/prot_align).

<p align="center">
<img src=img/app_empty.png height="500">
</p>

# Usage

To launch the application in __windows__, open a Command prompt window in the folder of the `frontend.py` file and type:
```shell
py frontend.py
```
To lauch the application in __linux__, open a terminal in the folder of the `frontend.py` file and type:
```shell
python3 frontend.py
```
or (make sure you made `frontend_unix.py` executable with `chmod`)

```shell
./frontend_unix.py
```
Then write the path of Multi-FASTA file (the first 2 sequences will be used)

<p align="center">
<img src=img/app_file.png height="500">
</p>

and click on the desired Blosum matrix to align the protiens

<p align="center">
<img src=img/app_b45.png height="500">
</p>

You can use any substitution matrix by writing the path to the substitution matrix file and clicking `Custom:` button.

<p align="center">
<img src=img/app_custom.png height="500">
</p>

Custom substitution matrices must be in genbank format (or similar enough for the `matparser` function). The following python code can be used to download and visualize alternative substitution matrices.

```python
import ftplib

path = 'blast/matrices/'
filename = 'BLOSUM62'

ftp = ftplib.FTP("ftp.ncbi.nih.gov")
ftp.login('anonymous', 'password')
ftp.cwd(path)
ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
ftp.quit()

BlossumFile = open("BLOSUM62", "r")
temp = BlossumFile.read()
BlossumFile.close()
print (temp)
```
To visualize long alignments you can scroll down

<p align="center">
<img src=img/app_down.png height="500">
</p>

or enlarge the window

<p align="center">
<img src=img/app_large.png height="500">
</p>

# Installation

The `biopython` module is required to use the predefined substitution matrices. Download the repository from [github](https://github.com/alfonsosaera/prot_align_GUI) or clone it by typing in the terminal

```shell
git clone https://github.com/alfonsosaera/prot_align_GUI.git
```
