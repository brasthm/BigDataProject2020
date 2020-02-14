
# coding: utf-8

# In[ ]:


from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle

file_in = sys.argv[1]
file_out = sys.argv[2]

columns_of_train = ['Product_Info_1', 'Product_Info_2', 'Product_Info_4', 'Product_Info_6',
       'Product_Info_7', 'Ins_Age', 'Ht', 'Wt', 'BMI', 'Employment_Info_1',
       'Employment_Info_6', 'InsuredInfo_1', 'InsuredInfo_3', 'InsuredInfo_4',
       'InsuredInfo_5', 'InsuredInfo_6', 'Insurance_History_1',
       'Insurance_History_2', 'Insurance_History_3', 'Insurance_History_4',
       'Insurance_History_5', 'Insurance_History_8', 'Family_Hist_1',
       'Family_Hist_2', 'Family_Hist_4', 'Medical_History_1',
       'Medical_History_2', 'Medical_History_3', 'Medical_History_4',
       'Medical_History_6', 'Medical_History_7', 'Medical_History_8',
       'Medical_History_9', 'Medical_History_11', 'Medical_History_12',
       'Medical_History_13', 'Medical_History_14', 'Medical_History_16',
       'Medical_History_17', 'Medical_History_18', 'Medical_History_19',
       'Medical_History_20', 'Medical_History_21', 'Medical_History_22',
       'Medical_History_23', 'Medical_History_25', 'Medical_History_28',
       'Medical_History_29', 'Medical_History_30', 'Medical_History_33',
       'Medical_History_34', 'Medical_History_37', 'Medical_History_39',
       'Medical_History_40', 'Medical_History_41', 'Medical_Keyword_1',
       'Medical_Keyword_3', 'Medical_Keyword_4', 'Medical_Keyword_6',
       'Medical_Keyword_7', 'Medical_Keyword_8', 'Medical_Keyword_10',
       'Medical_Keyword_15', 'Medical_Keyword_16', 'Medical_Keyword_21',
       'Medical_Keyword_22', 'Medical_Keyword_24', 'Medical_Keyword_25',
       'Medical_Keyword_26', 'Medical_Keyword_28', 'Medical_Keyword_29',
       'Medical_Keyword_30', 'Medical_Keyword_32', 'Medical_Keyword_33',
       'Medical_Keyword_34', 'Medical_Keyword_37', 'Medical_Keyword_39',
       'Medical_Keyword_40', 'Medical_Keyword_42', 'Medical_Keyword_45',
       'Medical_Keyword_47']
DATA_test = file_in
df_test = pd.read_csv(DATA_test, na_values='NAN')
dataframe_test = pd.DataFrame(df_test)
df_test = df_test[columns_of_train] 

columns_na = df_test.columns[df_test.isna().any()].tolist()
#Fill in the null values with the mean because there is just a little Null values
for i in columns_na:
    df_test[i] = df_test[i].fillna(value=df_test[i].mean())


df_test = df_test.apply(preprocessing.LabelEncoder().fit_transform)

scaler_standard = StandardScaler()
scaler_standard.fit(df_test)

X_scaled_real = scaler_standard.transform(df_test)


loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
result = loaded_model.predict(X_scaled_real)
df_test["Response"] = result
df_test.to_csv(file_out)

