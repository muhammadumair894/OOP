filepath =r'C:\Users\muham\Documents\MPhill (CS) NTU\3rd Semester\Data Scrap\shahzad\untitled5\abstract scraping\Data\Networking Science.csv'
#with open(filepath) as fp:

fp = open(filepath, 'r')
line = fp.readline()
cnt = 1
while line:
       #print("Line {}: {}".format(cnt, line.strip()))
       print(line.strip())
       line = fp.readline()
       cnt += 1

fp.close()