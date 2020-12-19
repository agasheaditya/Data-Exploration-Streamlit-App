import pandas as pd
import streamlit as st
import numpy as np
#import sklearn
import io
#import plotly.graph_objects as go


st.set_option('deprecation.showfileUploaderEncoding', False)


def showSampleData(DataFrame, size):
    st.subheader('Quick table look of your sample data: ')
    return st.dataframe(DataFrame.sample(size))

def showHeadData(DataFrame, size):
    st.subheader('Quick table look of your head data: ')
    return st.dataframe(DataFrame.head(size))

def showTailData(DataFrame, size):
    st.subheader('Quick table look of your tail data: ')
    return st.dataframe(DataFrame.tail(size))

def sortValsBy(df,cols):
    return df.sort_values(by=cols,ascending=True).head()

def colMean(df):
    columns = ['Column name', 'Mean']
    frame = pd.DataFrame(columns=columns)
    cols = df.select_dtypes(include=np.number).columns.tolist()
    for i in cols:
        Mean = df[i].mean()
        frame = frame.append({'Column name': i, 'Mean': Mean}, ignore_index=True) 
    return frame

def main():
    st.title("Data Exploration 📒 and Analysis 📑")
    st.sidebar.title("Menu")
    st.subheader("👨‍💻 Explore your data here 👨‍🏫")
    st.write('- - -')

    file_buffer = st.file_uploader(label="Upload your Dataset", type=['csv', 'xlsx', 'xlsm'])
        
    if file_buffer:
        df = pd.read_excel(file_buffer)
        if st.sidebar.checkbox('Show Data'):
            
            chosen = st.radio('Quick look', ("Head", "Tail", "Sample"))
            if chosen == "Head":
                size = st.slider("No. of rows: ", min_value=6,
                                max_value=40, step=5, format=None, key="Disp_data")
                showHeadData(df, size)
            if chosen == "Tail":
                size = st.slider("No. of rows: ", min_value=6,
                                max_value=40, step=5, format=None, key="Disp_data")
                showTailData(df, size)
            if chosen == "Sample":
                size = st.slider("No. of rows: ", min_value=6,
                                max_value=40, step=5, format=None, key="Disp_data")
                showSampleData(df, size)
        
        if st.sidebar.checkbox("Show Stats"):
            value = st.radio('Select stats', ("Shape", "Columns", "Numerical Data Description", "Non-numerical Data Description"))
            st.write('- - - ')
            if value == 'Shape':
                st.markdown("Rows, Columns : "+str(df.shape))
            if value == "Columns":
                st.markdown("Name of Columns: \n")
                st.markdown(df.columns)
            if value == 'Numerical Data Description':
                st.markdown('Shows basic statistical characteristics of each numerical feature (int64 and float64 types): number of non-missing values, mean, standard deviation, range, median, 0.25 and 0.75 quartiles.')
                st.table(df.describe())
            if value == 'Non-numerical Data Description':
                st.markdown('Statistics on non-numerical features')
                st.dataframe(df.describe(include=['object', 'bool']))
        st.sidebar.markdown('- - -')
        if st.sidebar.checkbox('Column-wise operations'):
            st.markdown('A DataFrame can be sorted by the value of one of the variables (i.e columns).')
            sel_cols = st.multiselect('Select columns name/names', df.columns)
            st.write(sel_cols)
            if sel_cols:
                st.dataframe(sortValsBy(df,sel_cols))
            if st.checkbox("Show Mean"):
                st.table(colMean(df))
            #cols = df.select_dtypes(include=np.number).columns.tolist()
            #col_names = st.radio('Select stats', (cols))
            #if col_names == cols[]:
            #    st.markdown(df[])


if __name__ == '__main__':
    main()
