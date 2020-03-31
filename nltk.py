import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import textblob
from textblob import TextBlob
from nltk.stem import PorterStemmer
st = PorterStemmer()
from sklearn.feature_extraction.text import CountVectorizer
vc = CountVectorizer()
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv("n11data.csv")


#Büyük-küçük harf dönüüşümü

data1 = data["Ürünler"].apply(lambda x: " ".join(x.lower() for x in x.split()))
data2 = data["Satıcılar"].apply(lambda y: " ".join(y.lower() for y in y.split()))


#Noktalama İşaretlerinin silinmesi

data1 = data1.str.replace("[^\w\s]", "")
data2 = data2.str.replace("[^\w\s]", "")
data3 = data["Yeni_Fiyatlar"].str.replace("[\nTL]", "")
data3 = data3.str.replace(" ", "")
data4 = data["Yapılan Oylamalar"].str.replace("[^\w\s]", "")
data4 = data4.str.replace("[\n]", "")
data3 = data3.str.replace(',', '').astype(float)

#Stemmer İşlemini yaptığımız kısım
data1 =  data1.apply(lambda x: " ".join([st.stem(i) for i in x.split()]))
data2 =  data2.apply(lambda x: " ".join([st.stem(i) for i in x.split()]))

#Özellik çıkarımı yaptğımız bölümdeyiz

data1_tf = vc.fit_transform(data1).toarray()
data2_tf = vc.fit_transform(data2).toarray()
rdt = np.concatenate((data1_tf, data2_tf), axis = 1)
print(data3.dtypes)

x_train, x_test, y_train, y_test = train_test_split(data1_tf, data3)
y_test = y_test.astype('int')
y_train = y_train.astype('int')

from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()

gnb.fit(x_train, y_train)
y_pred = gnb.predict(x_test)
plt.plot(y_pred, y_test)


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()

rf.fit(x_train, y_train)
y_pred2 = gnb.predict(x_test)
plt.plot(y_pred, y_test)
