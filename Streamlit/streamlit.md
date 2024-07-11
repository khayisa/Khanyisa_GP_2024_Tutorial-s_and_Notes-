# StreamLit Tutorial 
```
import streamlit as st
import time 
```

#### session states 
```
if "photo" not in st.session_state:
    st.session_state["photo"]= "not done"

```
#### columns component 
```
col1, col2, col3 = st.columns([1,2,1])
```
#### markdown
```
col1.markdown(" # welcome to my app ")
col1.markdown(" Here is some info on the app. ")
```
#### callback function
```
def change_photo_state():
    st.session_state["photo"] = "done"
```

#### file uploader component 
```
uploaded_photo = col2.file_uploader("upload a photo", on_change=change_photo_state)
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)


if st.session_state["photo"] == "done":
    
    progress_bar = col2.progress(0)

    #feedback comoponent 
    # conditional statement for the streamlit 
    for perc_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc_completed+1)

    col2.success("Photo uploaded sucessfilly!")

    #metrics
    col3.metric(label= "Temperature", value= "60", delta= "3")

    #Expanders
    with st.expander("Click to read more"):
        st.write("hello, here are more details on this topic that you were intrested in.")

        if uploaded_photo is None:
            st.image(camera_photo)
        else:
            st.image(uploaded_photo)

     


