#!/usr/bin/env python2

# Alfonso Saera Vila
#
# V 1.0
# 10/10/2018
# Back end script with the functions to power the GUI coded in frontend.py

# import custom made matparser() function from matparser.py
from matparser import *

################
# set variables#
################
INS = 4 # insertion penalty
DEL = 2 # deletion penalty

#############
# FUNCTIONS #
#############

# define backtrace_matrix() to choose pathway in dynamic programming matrix and
# return CIGAR (MDIMM...)
def backtrace_matrix(pattern, text, dp_matrix):
  i, j, CIGAR = len(pattern), len(text), []
  while i>0 and j>0:
    if dp_matrix[i][j] == dp_matrix[i-1][j] - DEL: #Deletion
      i -= 1
      CIGAR.insert(0, "D")
    elif dp_matrix[i][j] == dp_matrix[i][j-1] - INS: #Insertion
      j -= 1
      CIGAR.insert(0,'I')
    else:
      i -= 1
      j -= 1
      if pattern[i] == text[j]:
        CIGAR.insert(0, "M") #Match
      else:
        CIGAR.insert(0, "X") #Substitution
  if i > 0:
    for _ in range(i): CIGAR.insert(0, "D")
  if j > 0:
    for _ in range(j): CIGAR.insert(0, "I")
  return CIGAR

# define score_match() function to read substitution matrix when
# edit_distance_dp() function gets match-missmatch
def score_match(pair, matrix):
  if pair in matrix:
    return matrix[pair]
  else:
    return matrix[tuple(reversed(pair))]

# define edit_distance_dp() function to calculate the dynamic programming matrix
# with the edit distance between pattern and text. Returns the score and CIGAR
def edit_distance_dp(pattern,text, substitution_matrix):
  # Init dynamic programming matrix
  dp_matrix = [[0 for i in range(len(text)+1)] for j in range(len(pattern)+1)]
  for i in range(len(pattern)+1):
    dp_matrix[i][0] = -DEL*i
  for j in range(len(text)+1):
    dp_matrix[0][j] = -INS*j
  # Compute cells
  for i in range(1,len(pattern)+1):
    for j in range(1, len(text)+1):
      dp_matrix[i][j] = max(
        dp_matrix[i-1][j-1] + (score_match((pattern[i-1], text[j-1]), substitution_matrix)),
        dp_matrix[i][j-1] - INS, #insertion
        dp_matrix[i-1][j] - DEL) #deletion
  score = dp_matrix[i][j]
  CIGAR = backtrace_matrix(pattern, text, dp_matrix)
  return score, CIGAR

# define pretty_alignment() to add gaps in sequences to generate alignment
# creating a line with | marking identities between the sequences. Returns the
# alignment and its score
def pretty_alignment(pattern,text,substitution_matrix):
  score, CIGAR = edit_distance_dp(pattern,text,substitution_matrix)
  line1, line2, line3 = "", "", ""
  pattern_index, text_index = 0, 0
  for i in CIGAR:
    if i == "M": # match
      line1 += pattern[pattern_index]
      line2 += "|"
      line3 += text[text_index]
      pattern_index += 1
      text_index += 1
    if i == "I": # insertion
      line1 += "-"
      line2 += " "
      line3 += text[text_index]
      text_index += 1
    if i == "D": # deletion
      line1 += pattern[pattern_index]
      line2 += " "
      line3 += "-"
      pattern_index += 1
    if i == "X": # missmatch
      line1 += pattern[pattern_index]
      line2 += " "
      line3 += text[text_index]
      pattern_index += 1
      text_index += 1
  return line1, line2, line3, score

# define read_fasta() function to read a fasta file and return a list of lists
# with name and seq
def read_fasta(file):
  list = []
  f = open(file, 'r')
  header = f.readline()
  while len(header) != 0:
    seq = []
    seq.append(header[1:-1])
    r = ""
    while True:
      s = f.readline()
      if len(s) == 0 or s[0] == ">":
        header = s
        break
      r = r + s [:-1]
    seq.append(r)
    list.append(seq)
  return list

# define print_alignment() function to get the first 2 seq names and seqs from
# input file and return a "paper-like" alignment and its score
def print_alignment(fasta_file, substitution_matrix, block_size):
  # Get sequences
  pattern, text = read_fasta(fasta_file)[0][1], read_fasta(fasta_file)[1][1]
  # Get names
  pattern_name, text_name = read_fasta(fasta_file)[0][0], read_fasta(fasta_file)[1][0]
  # Get alignment and score
  line1, line2, line3, score = pretty_alignment(pattern,text,substitution_matrix)
  # Generate paper like alignment
  aa1_len, aa2_len, result = 0, 0, ""
  for index in range(0, len(line1), block_size):
    aa1 = line1[index : index + block_size]
    aa2 = line3[index : index + block_size]
    aa1_len += len(aa1.replace("-",""))
    aa2_len += len(aa2.replace("-",""))
    result = result + "\n" +\
    pattern_name + "\t" + aa1 + "  " + str(aa1_len) + "\n" +\
    "\t" + line2[index : index + block_size] + "\n" +\
    text_name + "\t" + aa2 + "  " + str(aa2_len) + "\n"
    if (index + block_size) > len(line1):
      break
  return score, result

# define nw_protein() function to print the alignment of the first 2 sequences
# in input file.fasta with the selected options in the GUI and the score
def nw_protein(fasta_file, substitution_matrix = "blosum62", block_size = 65):
  # choose substitution matrix depending on passed argument
  from Bio.SubsMat import MatrixInfo # get matrices using biopython
  if substitution_matrix == "blosum62":
    matrix = MatrixInfo.blosum62
  elif substitution_matrix == "blosum45":
    matrix = MatrixInfo.blosum45
  elif substitution_matrix == "blosum80":
    matrix = MatrixInfo.blosum80
  else:
    matrix = matparser(substitution_matrix)

  score, alignment = print_alignment(fasta_file, matrix, block_size)
  res = "\nFile: "+fasta_file+"    Substiturion matrix: "+substitution_matrix+\
  "\nAlignment score: " + str(score) + "\n" + alignment
  return res
