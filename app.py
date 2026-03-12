import streamlit as st
import requests
 
Title = st.title("Rhyming Word")
pexels_api = "PMfEge6mJ962e5D6H5CAwbE7aAIC7VXtNSPxkV6u729FBsyJt2afkTct"
word = st.text_input("Enter word")
is_clicked = st.button("Click Here" ,use_container_width=True , type = "secondary")
if is_clicked :
    res = requests.get(url=f"https://api.datamuse.com/words?ml={word}" )
    if res.status_code == 200:
        data =res.json()
        if not data:
            st.write("no related word found")
        else:
            st.write("Related word and images")
            count =1
            for item in data [:5]:
                related_word = item.get("word")
                st.write(f"{count}.{related_word}")
                img_res = requests.get(url=f"https://api.pexels.com/v1/search?query={related_word}&per_page=1",
                                        headers={"Authorization": pexels_api})
                if img_res.status_code ==200 :
                    img_res_data =img_res.json()
                    photos =img_res_data.get("photos", [])
                    if photos:
                        image_url = photos[0]["src"]["medium"]
                        st.image(image_url)
                st.write("-" * 50)
                count +=1
    else:
        st.write("Error:", res.status_code)