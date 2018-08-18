from termcolor import colored

#Get file path from user
given_path = input("File path of the file you want to read: ")

#Make Filehandler
try:
  fhandler = open(given_path)
except:
  print('The filepath given was not found. Filepath =', given_path)
  quit()

#Display text from file in alternating colors
color = 'green'
for line in fhandler:
  if(line.strip == ""):
    print(line.rstrip())
    continue
  
  print(colored(line.rstrip(), color))

  if(color == 'green'):
    color = 'yellow'
  else:
    color = 'green'
