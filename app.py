import streamlit as st
import google.generativeai as genai
from PIL import Image

# API Key စစ်ဆေးခြင်း
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("GOOGLE_API_KEY မရှိသေးပါ။")
    st.stop()

st.set_page_config(page_title="Suomi-Myanmar Grammar AI", layout="wide")
st.title("🇫🇮 Suomi-Myanmar သဒ္ဒါလက်ထောက်")

# နည်းလမ်း ၂ မျိုးလုံးထည့်ပေးထားပါတယ်
source = st.radio("ပုံယူမည့် နည်းလမ်းကို ရွေးပါ:", ("ဓာတ်ပုံရိုက်မည် (Selfie သာရနိုင်)", "ပုံတင်မည် (နောက်ကင်မရာ သုံးနိုင်သည်)"))

if source == "ဓာတ်ပုံရိုက်မည် (Selfie သာရနိုင်)":
    img_file = st.camera_input("စာမျက်နှာကို ရိုက်ပါ")
else:
    # ဒီနည်းလမ်းက နောက်ကင်မရာသုံးဖို့ ပိုအဆင်ပြေပါတယ်
    img_file = st.file_uploader("ပုံရွေးပါ သို့မဟုတ် နောက်ကင်မရာဖြင့် ရိုက်ပါ", type=['jpg', 'jpeg', 'png'])

if img_file:
    with st.spinner('AI က စာသားတွေကို ဖတ်နေပါတယ်...'):
        img = Image.open(img_file)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = "ဓာတ်ပုံထဲက ဖင်လန်စကားလုံးတွေကို ရှာပြီး B1 Level သဒ္ဒါဇယားတွေနဲ့ မြန်မာလို ဘာသာပြန်ပေးပါ။"
        
        response = model.generate_content([prompt, img])
        st.markdown(response.text)
