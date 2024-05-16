import streamlit as st
from streamlit.logger import get_logger
from PIL import Image 
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu


st.set_page_config(page_title='⛽T1 Gases', layout='centered', initial_sidebar_state="expanded")

st.title("⛽T1 Gases")
st.divider()
st.text("Mobile Online Shop")

with st.sidebar:
    selected = option_menu(
    menu_title = "Navigate Here:",
    options = ["🏡Home","⛽Services Offered"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "vertical"
    )
    
if selected == "🏡Home":
    st.subheader("Welcome, to our online shopping platform", divider=True)
    img=Image.open("t1_gases/img/logo.png")
    st.image(
        img,
        caption="T1 Gases Trademark Logo",
        width=310,
        channels="RGB")
    st.divider()
    with st.container(border=True):
        st.write("Visit our services offered page to learn more about our business")
    st.divider()
if selected == "⛽Services Offered":
    with st.container(border=True):
        st.subheader("Gas Sales")
        st.info("We have L.P Gas available at USD1.90/kg")
        st.info("For home deliveries we charge USD$2.00 a delivery around Gwabalanda")
        st.divider()
        img=Image.open("t1_gases/img/0b3025dea653bbd4b2a1198afdbbc654.jpg")
        st.image(
            img,
            caption="L.P Gas Available ",
            width=280,
            channels="RGB")
    with st.container(border=True):
        st.subheader("Gas Handling")
        st.info("We also fix leaking gas tanks and gas stoves also starting for only USD$3.00")
        img=Image.open("t1_gases/img/ed31393a4a210d2db696b1c0e4094571.jpg")
        st.image(
            img,
            caption="Gas repair servives available",
            width=310,
            channels="RGB")
        st.divider()
        st.subheader("Why get your gas tank fixed?")
        st.info("""We are also dedicated to providing exceptional services and quality to your LP Gas tank systems. Our team understands the importance
        of a properly functioning gas system for your residential and commercial needs. Whether you require installation, maintanace or repairs,
        we have the expertise to ensure your LP gas tank operates safely and efficiently.""")
        img=Image.open("t1_gases/img/55953cb71a95e3b3d7c94e5e6f7dd2f8.jpg")
        st.image(
            img,
            caption="We also offer gas installation services",
            width=310,
            channels="RGB")
        st.divider()
        st.subheader("A quick tip for our customers")
        st.write("View the image bewlow to get a free tip from us to you on how to care for your gas stoves.")
        img=Image.open("t1_gases/img/82c3a5dbdb2e7c79f4ccbc58f8526c0d.jpg")
        st.image(
            img,
            #caption="We also offer gas installation services",
            width=310,
            channels="RGB")
    
with st.sidebar:
    st.subheader("Contact us now")
    with st.container(border=True):
        st.write("Click on the button below in order to make your order or enquiry")
        st.link_button("Contact Bukhosi", "https://wa.me/263788679282")
        st.link_button("Contact T1", "https://wa.me/263771978987")
        st.link_button("Contact Mbizo", "https://wa.me/263784256710")
    st.info("Our business is located at the Gwabalanda Carpark next to Maplanka Shopping Centre📍")
    with st.form("my_form", clear_on_submit=True):
        st.write("**Rate my website**")
        slider_val = st.slider("How do you rate this website", help="Slide to the desired precentage(%)")
        checkbox_val = st.checkbox("Did you find this site useful?", help="Check the box if True")
        submitted = st.form_submit_button("Submit")
        if submitted: st.write("Rating", slider_val, "Helpful", checkbox_val)
        
