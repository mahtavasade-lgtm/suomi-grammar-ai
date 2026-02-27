import streamlit as st
import google.generativeai as genai
from PIL import Image

# Page setting
st.set_page_config(page_title="Suomi-Myanmar Grammar AI", layout="wide")
st.title("🇫🇮 Suomi-Myanmar သဒ္ဒါလက်ထောက်")

# API Key စစ်ဆေးခြင်း
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("ကျေးဇူးပြု၍ Streamlit Settings (Secrets) ထဲမှာ GOOGLE_API_KEY ကို ထည့်ပေးပါ!")
    st.stop()

# နည်းလမ်း ၂ မျိုးလုံးထည့်ပေးထားပါတယ်
source = st.radio("ပုံယူမည့် နည်းလမ်းကို ရွေးပါ:", ("ပုံတင်မည် (နောက်ကင်မရာ သုံးနိုင်သည်)", "ဓာတ်ပုံရိုက်မည် (Selfie သာရနိုင်)"))

if source == "ဓာတ်ပုံရိုက်မည် (Selfie သာရနိုင်)":
    img_file = st.camera_input("စာမျက်နှာကို ရိုက်ပါ")
else:
    img_file = st.file_uploader("ပုံရွေးပါ သို့မဟုတ် နောက်ကင်မရာဖြင့် ရိုက်ပါ", type=['jpg', 'jpeg', 'png'])

if img_file:
    with st.spinner('Gemini AI က စာသားတွေကို ဖတ်ပြီး သဒ္ဒါဇယားတွေ ဆွဲပေးနေပါတယ်...'):
        try:
            img = Image.open(img_file)
            
            # Model selection
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            # ပိုမိုတိကျသော ညွှန်ကြားချက် (Prompt)
            prompt = """
            မင်းက ဖင်လန်-မြန်မာ သဒ္ဒါပညာရှင်တစ်ယောက်ပါ။ 
            ဓာတ်ပုံထဲက ဖင်လန်စကားလုံးတွေကို ရှာဖွေပြီး စကားလုံးတစ်လုံးချင်းစီအတွက် အောက်ပါအတိုင်း ဇယားနဲ့ ပြပေးပါ-
            ၁။ ကြိယာ (Verbs) ဖြစ်လျှင်: Perusmuoto, Minä, Sinä, Hän, Me, Te, He ပုံစံများ နှင့် မြန်မာလို အဓိပ္ပာယ်။
            ၂။ နာမ် (Nouns) ဖြစ်လျှင်: Nominatiivi, Genetiivi (-n), Partitiivi နှင့် မြန်မာလို အဓိပ္ပာယ်။
            ဇယားကို Markdown table ပုံစံနဲ့ သေသေချာချာ ပြပေးပါ။
            """
            
            response = model.generate_content([prompt, img])
            
            if response.text:
                st.success("ခွဲခြမ်းစိတ်ဖြာမှု ပြီးစီးပါပြီ!")
                st.markdown(response.text)
            else:
                st.warning("စာသားများကို ဖတ်မရပါ။ ကျေးဇူးပြု၍ ပုံကို ပိုမိုကြည်လင်အောင် ပြန်ရိုက်ပေးပါ။")
                
        except Exception as e:
            st.error(f"Error တက်သွားပါတယ်: {str(e)}")
            st.info("အကြံပြုချက်: requirements.txt ထဲမှာ google-generativeai version ကို အဆင့်မြှင့်ထားသလား ပြန်စစ်ပေးပါ။")
