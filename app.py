import streamlit as st
import google.generativeai as genai
from PIL import Image

# Streamlit Secrets ကနေ Gemini API Key ကို ခေါ်သုံးခြင်း
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("ကျေးဇူးပြု၍ Streamlit Settings ထဲမှာ GOOGLE_API_KEY ထည့်ပေးပါ!")
    st.stop()

st.set_page_config(page_title="Suomi-Myanmar Grammar AI (Gemini)", layout="wide")
st.title("🇫🇮 Suomi-Myanmar သဒ္ဒါလက်ထောက် (Gemini AI)")

# Photo input
img_file = st.camera_input("ဖင်လန်စာပါတဲ့ စာမျက်နှာကို ဓာတ်ပုံရိုက်ပါ")

if img_file:
    with st.spinner('Gemini AI က ဇယားဆွဲပေးနေပါတယ်...'):
        # Load image
        img = Image.open(img_file)
        
        # Model configuration
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Instruction prompt
        prompt = """
        မင်းက ဖင်လန်-မြန်မာ သဒ္ဒါပညာရှင်တစ်ယောက်ပါ။ 
        ဓာတ်ပုံထဲက ဖင်လန်စကားလုံးတွေကို ရှာဖွေပြီး စကားလုံးတစ်လုံးချင်းစီအတွက် အောက်ပါအတိုင်း ဇယားနဲ့ ပြပေးပါ-
        ၁။ အခြေခံပုံစံ ၄ မျိုး (Infinitive, Noun, Genitive, Passive/Let's)
        ၂။ ကတ္တားအလိုက် (Minä, Sinä, Hän, Me, Te, He) ရုပ်ပြောင်းပုံများ။
        မြန်မာလိုပြန်ဆိုတဲ့အခါ ကြိယာဆိုလျှင် 'သည်'၊ နာမ်ဆိုလျှင် 'ခြင်း/၏' နောက်ဆက်တွဲများကို အသုံးပြုပါ။
        ဇယားကို Markdown table ပုံစံနဲ့ သေသေချာချာ ပြပေးပါ။
        """
        
        # Generate content
        response = model.generate_content([prompt, img])
        
        st.markdown(response.text)
