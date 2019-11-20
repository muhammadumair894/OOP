from sklearn.feature_extraction.text import CountVectorizer
path = r'C:\Users\muham\PycharmProjects\stopwords\NB format data\Acta Informatica.csv'
f = open(path, "r")
line = f.readline()

str_file = list()
i=1

while line:

    line = f.readline()
    print (line)
    str_file.append(line)
    i = i+1

text = ["this is a sample code ", "this code will helps us to understand the concept behinde TF-IDF", "coding is not much complex", "understand the concept "]
vector = CountVectorizer(max_features = 2000)
#print(str_file)
#print(text)
vector.fit(str_file)
#vector.fit(f)
print("Vacoblary"+ str(vector.vocabulary) + '\n\n')
vector.get_feature_names()
print("Feature Names"+ str(vector.get_feature_names()) + '\n')
#count = vector.transform(f)
count = vector.transform(str_file)
#count = vector.transform(f)
print("Shap of count" + str(count.shape)+ '\n')
print("Printing count" + '\n'+ str(count.toarray()))
y= f.iloc[:,1].values
f.close()

