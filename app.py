import streamlit as st
from preprocessing import load_model

model = 'models/classifier-01-2020-11-09 05:48:03.552051.sav'
vec = 'models/classifier-01-2020-11-09 05:48:03.552051-vec.sav'

model,vec = load_model(model,vec)


def inference(text,model,vec):
    lst = [text]
    vectorizer = vec.transform(lst).toarray()
    pred = model.predict(vectorizer)[0]
    return pred

def app():
    st.title("Basic Spam Filter")

    sentence = st.text_area('Input your sentence here:') 
    submit = st.button('Is it Spam?')

    if sentence != '':
        prediction = inference(sentence,model,vec)
        print(prediction)

    print(sentence)


  
    if submit:
        if prediction == 1:
            st.error('SPAM!')
        elif prediction == 0:
            st.success('Not Spam!')
        


if __name__ == '__main__':
    app()