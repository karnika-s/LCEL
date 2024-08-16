import requests
import streamlit as st


def get_groq_response(input_text): #, input_language, output_language):
    json_body={
  "input": {
    "language": "French",
    "text": f"{input_text}"
  },
  "config": {},
  "kwargs": {}
}

#     json_body={
#   "input": {
#     "language": "English",
#     "text": f"{input_text}"
#   },
#   "config": {},
#   "kwargs": {}
#     }


    # json_body = {
    #     "input": {
    #         "language": input_language,
    #         "text": input_text
    #     },
    #     "config": {},
    #     "kwargs": {}
    # }
    
    response=requests.post("http://localhost:8000/chain/invoke",json=json_body)

    try:
        response_data=response.json()

        output = response_data.get("output","no result field in response")
        return output
    except ValueError:
        return "Error : Invalid JSON response"
    
# the get functions ends here 

## Streamlit app
st.title("My French Translator😎 ")
input_text=st.text_input("Enter the text you want to convert")

# language_option = st.selectbox(
#     "Select input language",
#     ("English to French", "French to English")
# )
# Determine input and output languages based on selection
# if language_option == "English to French":
#     input_language = "English"
#     output_language = "French"
# else:
#     input_language = "French"
#     output_language = "English"


# input_text = st.text_input(f"Enter the text you want to convert ({input_language} to {output_language})")

# if input_text:
#     st.write(get_groq_response(input_text, input_language, output_language))


if input_text:
    st.write(get_groq_response(input_text))
    