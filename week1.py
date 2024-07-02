import io
import csv

num_attributes=6
a=[]
print("The given Dataset is")
with open('climate.csv','r') as csvfile:
  reader=csv.reader(csvfile)
  for row in reader:
    a.append(row)
    print(row)
    print("The initial hypothesis is")
hypothesis=['0']*num_attributes
print(hypothesis)
for j in range(0,num_attributes):
  hypothesis[j]=a[1][j]

print(hypothesis)
print("Find S: Finding maximal Specific Hypothesis")
for i in range(1,len(a)):
  if a[i][num_attributes]=='Yes' or a[i][num_attributes]=='Yes':
    for j in range(0,num_attributes):
      if a[i][j]!=hypothesis[j]:
        hypothesis[j]='?'
      else:
        hypothesis[j]=a[i][j]
  print("For Training instances No: {0} the hypothesis is". format(i),hypothesis)

