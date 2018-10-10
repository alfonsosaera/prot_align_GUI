# Alfonso Saera Vila
# 9/10/2018

# Function to parse a matrix downloaded from genbank
# https://ftp.ncbi.nih.gov/blast/matrices
# returns a dictionary in the form dict[('A','A')] = INT

def matparser(filename):
    f = open(filename, 'r')
    mat_list = []
    for line in f.readlines():
      if line[0] == "#": # avoid comment lines
        continue
      line = " ".join(line.split()) # remove multiple white spaces and \n
      mat_list.append(line.split(" "))

    mat_dict = {}
    for i in range(1, len(mat_list)):
      for j in range(i, len(mat_list[i])):
        mat_dict[(mat_list[0][j-1], mat_list[i][0])] = int(mat_list[i][j])
    return mat_dict
