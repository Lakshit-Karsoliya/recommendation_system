import streamlit as st
import pickle
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import random

st.set_page_config(page_title='I M GR8',layout='wide')
with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
quotes=['“फैशन सपने की तरह है, खुद देखने और दूसरों को दिखाने की तरह।” – डोनाटेल वरसाचे',
        '“जो महिला ब्लैक पहनती हैं, उनकी ज़िंदगी कलरफुल रहती है।” – नईमन मार्कस',
        '“फैशन आर्ट है और आप कैनवस।” – वेलवेट पैपर',
        '“जिंदगी छोटी है, आपकी हील्स छोटी नहीं होनी चाहिए।” – ब्रेन एटवुड',
        '“जुराबें छेद होने के लिए ही बनी हैं।” – एंथनी टी. हिंक्स',
        '“खूबसूरत दिखने के लिए परफेक्ट होना जरूरी नहीं।” – कार्सन क्रेसले',
        '“हमेशा ऐसे ड्रेस्ड होकर निकलिए, जैसे आप अपने दुश्मन से मिलने जा रहे हैं।“ – किमोरा ली   ',
        '“फैशन खाने की तरह है, एक ही मेन्यू पर टिके न रहें।” – केन्ज़ो टकाडा',
        ]
st.markdown("""
<center>
  <h1>नमस्कार</h1>
  <h1>Productcart :)</h1>
  <p>product recommendation system<p>
</center>
""",unsafe_allow_html=True)


def index_of_product(id):
  res=[]
  index = df[df['id']==id].index[0]
  dis,idx = neighbors.kneighbors([vectors[index]])
  for i in idx[0]:
    res.append(df['id'][i])
  return res

df = pickle.load(open('df.pkl','rb'))
df = pd.DataFrame(df)
vectors = pickle.load(open('vectors.pkl','rb'))

cola,colb = st.columns([5,1])
with cola:
  selected_product_name = st.selectbox("",df['productDisplayName'].values)
with colb:
  st.write('')
  st.write('')
  btn = st.button('Search Product')
    
if btn:
  neighbors = NearestNeighbors(n_neighbors=21,algorithm='brute',metric='euclidean')
  neighbors.fit(vectors)

  st.write('---')
  st.markdown('''
      <h3>Product Description</h3>
  ''',unsafe_allow_html=True)

  col1,col2 = st.columns([1,2])
  with col1:
      st.image(f"archive (1)/images/{df['id'][df[df['productDisplayName']==selected_product_name].index[0]]}.jpg",width=200)
  with col2:
      st.write(f'## {selected_product_name}')
      st.write('Product Rating 4.5/5')
      st.button('Buy Now')
      st.button('Add to Cart')
      st.write("note* product rating and buynow/addtocart button serves no purpose here")
  st.write('---')
  st.write("## Similar products :)")
  st.write('')
  st.write('')

  product_ids = index_of_product(df['id'][df[df['productDisplayName']==selected_product_name].index[0]])

  for product in range(1,len(product_ids),2):
      col1,col2 = st.columns(2)
      with col1:
        st.image(f"archive (1)/images/{product_ids[product]}.jpg",width=200)
        st.write(f"{df['productDisplayName'][df[df['id']==product_ids[product]].index[0]]}")
      product = product+1
      with col2:
        st.image(f"archive (1)/images/{product_ids[product]}.jpg",width=200)
        st.write(f"{df['productDisplayName'][df[df['id']==product_ids[product]].index[0]]}")
  st.write('---')
  st.write('')
  st.markdown(f"<center><h4 >{random.choice(quotes)}</h4></center>",unsafe_allow_html=True)
  st.write('')
  st.write('')

