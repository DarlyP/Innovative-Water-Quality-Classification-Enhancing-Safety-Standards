import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

#Load All files
#Load model

with open('best_pipe.pkl', 'rb') as file_1:
    best_pipe = pickle.load(file_1)
with open('num_col.txt', 'r') as file_2: 
    num_col = json.load(file_2)

def run():
    st.title('Water Quality Data Input Form')

    # Membuat form
    with st.form('Water_Quality'):
        aluminium = st.number_input('Aluminium', value=0.0, min_value=0.0)
        ammonia = st.number_input('Ammonia', value=0.0, min_value=0.0)
        arsenic = st.number_input('Arsenic', value=0.0, min_value=0.0)
        cadmium = st.number_input('Cadmium', value=0.0, min_value=0.0)
        chloramine = st.number_input('Chloramine', value=0.0, min_value=0.0)
        copper = st.number_input('Copper', value=0.0, min_value=0.0)
        bacteria = st.number_input('Bacteria', value=0.0, min_value=0.0)
        viruses = st.number_input('Viruses', value=0.0, min_value=0.0)
        lead = st.number_input('Lead', value=0.0, min_value=0.0)
        nitrites = st.number_input('Nitrites', value=0.0, min_value=0.0)
        perchlorate = st.number_input('Perchlorate', value=0.0, min_value=0.0)
        radium = st.number_input('Radium', value=0.0, min_value=0.0)
        selenium = st.number_input('Selenium', value=0.0, min_value=0.0)
        silver = st.number_input('Silver', value=0.0, min_value=0.0)
        uranium = st.number_input('Uranium', value=0.0, min_value=0.0)

        # Membuat tombol submit
        submitted = st.form_submit_button('Submit')

    # Mengumpulkan data inputan ke dalam dictionary
    data_inf = {
        'aluminium': aluminium,
        'ammonia': ammonia,
        'arsenic': arsenic,
        'cadmium': cadmium,
        'chloramine': chloramine,
        'copper': copper,
        'bacteria': bacteria,
        'viruses': viruses,
        'lead': lead,
        'nitrites': nitrites,
        'perchlorate': perchlorate,
        'radium': radium,
        'selenium': selenium,
        'silver': silver,
        'uranium': uranium
    }

    # Mengubah dictionary menjadi DataFrame
    data_inf = pd.DataFrame([data_inf])

    # Menampilkan DataFrame
    st.dataframe(data_inf)

    # Memproses data setelah tombol submit ditekan
    if submitted:
        # Prediksi menggunakan model 
        y_pred_inf = best_pipe.predict(data_inf)
        
        if y_pred_inf == 0:
            st.write('## Rating : Dangerous')
        else:
            st.write('## Rating : Safe')

# Menjalankan aplikasi
if __name__ == "__main__":
    main()


