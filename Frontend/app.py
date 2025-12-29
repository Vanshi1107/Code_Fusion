import streamlit as st
import requests
st.set_page_config(
    page_title="AI-Driven Expense Tracker For Indian Students",
    layout="centered"
)
st.title("AI Expense Tracker For Indian Students")
st.write("Upload bill/UPI screenshots or enter expense text.")
options=st.radio("Choose input method:",["Text","Image"])
if options=="Text":
    text_input=st.text_input("enter your expense details",placeholder="paid \u20B9250 to zomato via UPI")
elif options=="Image":
    image_input=st.file_uploader("upload UPI screenshot or Bill")
    if image_input:
        st.image(image_input,caption="Uploaded Image",use_column_width=True)
if st.button("Extract Expense"):
    if options == "Text" and text_input:
        backend_url = "http://localhost:8000/parse-expense"

        response = requests.post(
            backend_url,
            data={"text": text_input}   # send as Form
        )

        if response.status_code == 200:
            st.subheader("Extracted Expense")
            st.json(response.json())
        else:
            st.error("Backend error")

    else:
        st.warning("Please enter expense text")
