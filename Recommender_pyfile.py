import pandas as pd #import Libraries

#Sample Dataset
data_sets={
    'ID':['I1','I1','I2','I2','I3','I3','I4','I4'],
    'Product':['Phone','Laptop','Phone','Keyboard','Laptop','Headset','Phone','Laptop'],
    'Rating':[5,4,4,3,5,4,2,3]
}
dframe = pd.DataFrame(data_sets)

dframe.to_csv('data_ratings.csv',index=False)

dframe


from sklearn.preprocessing import LabelEncoder #data Encoding

dframe = pd.read_csv('data_ratings.csv')

user_encoder = LabelEncoder()
product_encoder = LabelEncoder()

dframe['User'] = user_encoder.fit_transform(dframe['ID'])
dframe['Items'] = product_encoder.fit_transform(dframe['Product'])

dframe

user_item_matrix = dframe.pivot_table(values='Rating',index='User',columns='Items').fillna(0)

from sklearn.metrics.pairwise import cosine_similarity

item_similarity = cosine_similarity(user_item_matrix.T)

import numpy as np 

item_similarity_dframe = pd.DataFrame(item_similarity,index=user_item_matrix.columns,columns=user_item_matrix.columns)

item_similarity_dframe



#Recommendation Function
data_set={
    'Products':['Phone','Laptop','Keyboard','Headset']
}
dframe = pd.DataFrame(data_set)
dframe
print(dframe)

product_name = input("Enter the Product")
def recommend(product_name,top_n=3):
    try:
        product_id = product_encoder.transform([product_name])[0]
        scores = list(enumerate(item_similarity_dframe[product_id]))
        scores = sorted(scores,key=lambda x: x[1],reverse=True)[1:top_n+1]

        print(f"\nTop {top_n} products similar to '{product_name}':")
        for i,score in scores:
            similar_product = product_encoder.inverse_transform([i])[0]
            print(f"- {similar_product}(similarity Score : {score:.2f})")
    except:
        print(f"'{product_name}' not found in product list.")

recommend(product_name,top_n=3)