import streamlit as st
from streamlit.logger import get_logger
from PIL import Image 
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu


st.set_page_config(page_title='🔧Welding Shop', layout='centered', initial_sidebar_state="expanded")

st.title("Gwabalanda Caarpark Welding Shop")
st.divider()
st.text("Mobile and PC Compartible.")

with st.sidebar:
    selected = option_menu(
    menu_title = "Navigate Here:",
    options = ["🏡Home","🔧Services Offered"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "vertical"
    )
    
if selected == "🏡Home":
    img=Image.open("wbbcapp/welding_shop/img/Screenshot_20240515_120913_Canva.jpg")
    st.image(
        img,
        caption="Gwabalanda Steel Fabrications Trademark Logo",
        width=310,
        channels="RGB")
    st.header(':yellow[Welcome, to our official online shop]',divider=True)
    st.divider()
    st.write("Use this platform in order to view our readily available products and get custom fabricated windows and door frames from us.")
    st.info("Navigate the site and see what we have in store for you. ")
    
if selected == "🔧Services Offered":
    with st.container(border=True):
        st.title('Here are available door and window frames')
        with st.container(border=True):
            st.write("All Window Frame prices are stacked at USD$100.00, Door Frames at USD$200.00")
    img=Image.open("wbbcapp/welding_shop/img/02d42c42b7da5584ccf6461fcaea06bb.jpg")
    st.image(
        img,
        caption="Windown frames available 2m x 1m measuring for your perfect window finishing",
        width=310,
        channels="RGB")
    img=Image.open("wbbcapp/welding_shop/img/7760e0a2822ffc7b733f045291df1aa3.jpg")
    st.image(
        img,
        caption="Custom steel and aluminium fabricated window frames available",
        width=310,
        channels="RGB")
    img=Image.open("wbbcapp/welding_shop/img/32f9bbabc96665397e71046c25eeda45.jpg")
    st.image(
        img,
        caption="Aluminium doors & door frames also available",
        width=310,
        channels="RGB")
    img=Image.open("wbbcapp/welding_shop/img/4f798501fff0cbd31866a76e4621091a.jpg")
    st.image(
        img,
        caption="Custom steel and aluminium fabricated door frames available",
        width=310,
        channels="RGB")
    with st.container(border=True):
        st.title("We also offer sliding gates for steel fabrication")
        st.info("Sliding gates available at USD$300.00")
    img=Image.open("wbbcapp/welding_shop/img/3d9359473ee55b5ec5d4095a005d5c16.jpg")
    st.image(
        img,
        caption="Custom steel sliding gates",
        width=310,
        channels="RGB")
    img=Image.open("wbbcapp/welding_shop/img/47e8f834924645f32d8b11fdbe2a46cc.jpg")
    st.image(
        img,
        caption="Custom steel sliding gates tailored to your desugn and fit",
        width=310,
        channels="RGB")
    img=Image.open("wbbcapp/welding_shop/img/517497f0711e7d736bd8697ece17e0c4.jpg")
    st.image(
        img,
        caption="Custom steel sliding gates tailored to your desugn and fit",
        width=310,
        channels="RGB")
    with st.container(border=True):
        st.title("We also cater for other Steel Works")
        st.info("JoJo/ Water Tank stands Available @ USD$450.00")
    img=Image.open("wbbcapp/welding_shop/img/a0cc7ebec88b891f95995ead11e588b9.jpg")
    st.image(
        img,
        caption="Custom Jojo Tank Stands",
        width=310,
        channels="RGB")
    img=Image.open("wbbcapp/welding_shop/img/a36fe84c231d3815f7e67b2cb0ff6079.jpg")
    st.image(
        img,
        caption="Custom Jojo Tank Stands fabricated for any use and any size",
        width=310,
        channels="RGB")
    img=Image.open("wbbcapp/welding_shop/img/0ab596492203d2083e481eaa1192a50f.jpg")
    st.image(
        img,
        caption="Custom designed stands to fit your exact needs",
        width=310,
        channels="RGB")
    
    
    st.divider()
    st.write("**Contact us now for a quotation and get your business or home a propert aesthetic finish**")

with st.sidebar:
    st.title("☎Contact us")
    with st.container(border=True):
        st.write("Click on the button below and make your order with us today and get an immediate quote from us")
        st.link_button("WhatsApp me here", "https://wa.me/263777399511")
        
    st.title("Location📍")
    st.info("Our business is located next to the Maplanka Supermaket Shops at the Gwabalanda Carpark")
   
