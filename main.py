import streamlit as st
import newspaper
import nltk

nltk.download('punkt')


st.title('Article Summarizer')

url = st.text_input('', placeholder='Paste the URL of the article amd press Enter')

if url:
    try:
        article = newspaper.Article(url)

        article.download()
        # article.html
        article.parse()

        img = article.top_image
        st.image(img)
        

        title = article.title
        st.subheader(title)
        

        authors = article.authors
        st.text(','.join(authors))
        
        article.nlp()

        keywords = article.keywords
        st.subheader('Keywords:')
        st.write(', '.join(keywords))
        
        tab1, tab2= st.tabs(["Full Text", "Summary"])
        with tab1:
            txt = article.text
            txt = txt.replace('Advertisement', '')
            st.write(txt)
        
        with tab2:
            st.subheader('Summary')
            summary = article.summary
            summary = summary.replace('Advertisement', '')
            st.write(summary)
        
        
    except:
        st.error('Sorry something went wrong')





import streamlit as st


st.set_page_config(page_title="Your Web App", page_icon="https://www.shutterstock.com/image-vector/bird-logo-600nw-662212243.jpg", layout="wide")


col1, col2, col3, col4 ,col5 = st.columns([1, 7, 2, 1, 1])
with col1:
    st.image("https://www.shutterstock.com/image-vector/bird-logo-600nw-662212243.jpg", use_column_width=True)
with col2:
    st.title("Your Web App")
with col3:
    st.write("")  
with col4:
    signup = st.button("Sign Up")  
with col5:
    signin = st.button("Sign In")

if signup:
    st.write("Sign Up functionality goes here...")
elif signin:
    st.write("Sign In functionality goes here...")
else:
    col1, col2, col3, col4 = st.columns([1, 2, 1, 1])
    
    with col1:
        st.write("")
   
    with col2:
        if st.button("Article Summarizer"):
            st.header("Article Summarizer functionality goes here...")

    with col3:
        if st.button("Video Summarizer"):
            st.header("Video Summarizer functionality goes here...")
    with col4:
        st.write("")
