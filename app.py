from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_tno6cg2w.json")
img_child_form = Image.open("images/yt_child_form.png.jpg")
img_monkey_form = Image.open("images/yt_monkey_form.png.jpg")
img_lion_form = Image.open("images/yt_lion_form.png.jpg")
img_bobmarle_form = Image.open("images/yt_bobmarle_form.png.jpg")
img_jazz_form = Image.open("images/yt_jazz_form.png.jpg")
img_sing_form = Image.open("images/yt_sing_form.png.jpg")
st.set_page_config(page_title="web app",page_icon=":tada:",layout="wide")
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)
local_css("style/style.css")


st.subheader('Hi :wave: my name is BROOK')
st.title("A material science and enginering student from adama science and technology university")
st.write("I am passionate about finding ways to use material science and enginering to be more efficient and effective in business setting.")
st.write("-------")
st.write("##")

st.subheader("personal information")
st.write("##")
left_column,right_column = st.columns(2)



with left_column:


            st.write("- age=20")
            st.write("- sex = MALE")
            st.write("- plcae of birth= ADDIS ABABA")
            st.write("- nationality=ETHIOPIAN")
            st.write("- personal address= ADAMA,ASTU,BLOCK 365")
            st.write("- telephone no= +251976035455")
            st.write("- id number=UGR/23553/13")




st.write("------------")
st.write("##")
left_column,right_column = st.columns(2)
with left_column:
      st.header("work experiance")
      st.write("##")
      st.write("- I have assisted on a wood work at a friends construction  place ")
      st.write("- I have done some art work on walls for charity for a place called dolacol")
      st.write("- I have worked as assistance for a company called omega as testing materials ")
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")
st.write("---------")
st.write("##")
st.header("Education background")
st.write("##")
st.write("- Currently Under graduated at Adama Science and technology")
st.write("- learned highschool from grade 9 to 12 at Elshaday holy saviour school")
st.write("- learn elementary and kindergarden at schoola Italiana di Addis Ababa ")
st.write("-------")
st.write("##")
left_column,right_column = st.columns(2)
with left_column:
    st.header("other skills")
    st.write("- I have a driving licence ")
    st.write("- I do so many kinds of arts like sketching, painting , wall art,digital painting ")
with right_column:
    st.header("Languges ")
    st.write("- Amharic ")
    st.write("- English ")
    st.write("- Italian")
st.write("##")
st.subheader("my preferance on work of the future ")
st.write("- I would like to work more on the art skill")
st.write("- I might learn some other studies like human psychology and behaviour")
st.write("------")
st.write("##")
st.header("my projects")
image_column,text_column = st.columns((1,2))
with image_column:
    st.image(img_monkey_form)
with text_column:
    st.header("NFT art painting on a flat wood :wink: ")
    st.write("This is NFT monkey which  is actually funny starring at his weird friend :smiley: :smiley: :smiley:")
image_column,text_column = st.columns((1,2))
with image_column:
    st.image(img_bobmarle_form)
with text_column:
    st.header("Famous musician BOOB MARLY")
    st.write("This is a famous musican bobmarly painted by me on the wall  ")
image_column,text_column = st.columns((1,2))
with image_column:
    st.image(img_lion_form)
with text_column:
    st.header("The strongest animal on earth ")
    st.write("This is a lion roring while protecting his teritory and it is painted on the wall by me ")
image_column,text_column = st.columns((1,2))
with image_column:
    st.image(img_jazz_form)
with text_column:
    st.header("The Famous jazz Ethioian musican  ")
    st.write("This is the greatest of all times in the ethiopian jazz history and it is painted on a wall by me ")
image_column,text_column = st.columns((1,2))
with image_column:
    st.image(img_sing_form)
with text_column:
    st.header("The hand ")
    st.write("This is a sketching made in pc by me while i am bored. just kidding :smiley: :smiley: :smiley: ")
st.write("##")
st.write("--------")

st.subheader("My family")
image_column,text_column = st.columns((1,2))
with image_column:
    st.image(img_child_form)
with text_column:
    st.header("my son")
    st.write("This is me holding my baby,the love of my life and my every thing ")
st.write("--------")
st.write("##")
st.header("Get in touch with me!")
contact_form = """
                        
                        <form action="https://formsubmit.co/brookayalew06@gmail.com" method="POST">
                        <input type="hidden" name="_captcha value="false">
                        <input type="text" name="name" placeholder="your name" required>
                         <input type="email" name="email" placeholder="your email" required>
                           <button type="submit">Send</button>
</form>
               """
left_column,right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()









