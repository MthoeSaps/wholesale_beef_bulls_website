import streamlit as st
from streamlit.logger import get_logger
from PIL import Image 
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu

LOGGER = get_logger(__name__)

def run():
   st.set_page_config(page_title='🏏Wholesale Beef Bulls Cricket Club', layout='centered')

   selected = option_menu(
    menu_title = "Main Menu",
    options = ["🏡Home","📺Player Interviews & Profiles","🕹Player Practice sessions","📽Live Games & Fixtures"],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal"
    )
    
   if selected == "🏡Home":
      st.header(':yellow[Wholesale Beef Bulls Cricket Club]',divider=True)
      st.markdown(
         """
         ### Welcome

         yellow[Welcome to the official Wholesale Beef Bulls online cricket platform. Here you can check all the team stats, watch all the live WBBCC games and get updates on the Club fixtures, tours and tounaments]

        
        :yellow[Access more data and infomation about WBBCC on our Panel] """
        )
      with st.sidebar.container(border=True):
          img = Image.open("wbbcapp/images/beefbulls.jpg")
          st.image(img)
      with st.sidebar.container(border=True):    
         st.header("Wholesale Beef Bulls Cricket Club")
      with st.sidebar.container(border=True):   
         st.subheader("Follow our social media pages")
         st.link_button("Instagram account", "https://www.instagram.com/wholesalebeefbulls_cricketclub?igsh=YzljTk1ODg3Zg")
         st.link_button("Facebook account", "https://www.facebook.com/profile.php?id=61553393035248&sfnsn=wa&mibextid=RUbZ1f")
         st.link_button("Whatsapp Channel", "https://whatsapp.com/channel/0029Va8jh94ATRSwgXfpVS1B")
         st.link_button("Email us here", "https://")
      with st.sidebar.container(border=True):
          st.subheader("WBBCC Organogram/ About")
          st.write("Here is our organisational setup")
      with st.sidebar.container(border=True):
          st.subheader("Directors")
          st.write("D. Saudan")
          st.write("N. Saudan")
      with st.sidebar.container(border=True):
          st.subheader("Administration")
          st.write("J. Dzimati")
          st.write("Contact Administator on:")
          st.write("Cell: +263 773 737 466")
          st.write("WhatsApp: +263 732 737 466")
      with st.sidebar.container(border=True):
          st.subheader("Coaches")
          st.write("S. Kusano")
          st.write("S. Chigumbura")
          st.write("T. Moyo")
      with st.sidebar.container(border=True):
          st.subheader("Wholesale Beef Profile")   
          st.subheader("Click on the link below to get see Wholesale Beef meat promos")    
      with st.sidebar.container(border=True):    
          st.link_button("Wholesale Beef Facebook Page", "https://www.facebook.com/share/3Gwq26vWm5EYupSi/?mibextid=qi2Omg") #__updsate this link button    
      with st.sidebar.container(border=True):
          st.subheader("Location")
          st.write("Our Club HQ is found at Factory A, N0 10, Bessborough road, Belmont, Bulawayo")

      left_column,right_column = st.columns(2)
      with left_column:
         with st.container(border=True):
            st.header('Wholesale Beef Bulls Teamlist')
            st.write('Checkout our current season teamlist and view our player stats on this page')
            st.link_button('View Team List',"https://cricheroes.in/tournament/905559/2023-24-BMCA-2nd-League-Pro40" )
      with right_column:
         with st.container(border=True):
            url = ("https://www.example.com") #__update this feature
            st.video(url)
          
          
   if selected == "📺Player Interviews & Profiles":    
      with st.container(border=True):
         st.header('Watch our player interviews and Player Profiles here')
         st.write('A story about our rising stars')
         with st.container(border=True):
            url = ('https://192.168.191.235:8080')#update link
            st.video(url)
            with st.container(border=False):
               st.header('Player profiles')
               st.write(':red[Player name: Sharmar]')
               st.write("Role: Opening Batsman")
               st.write("Batting style: Right handed batsman")
               st.write("Age: 20 years old")
               st.write("Watch Player Profile Video")
               with st.container():
                  url = ('https://192.168.191.235:8080')#update link
                  st.video(url) #__player 1
                  with st.container():
                     st.write(':red[Player name: Shane Chigumbura]')
                     st.write("Role: Allrounder")
                     st.write("Bowling style: Right arm medium seamer")
                     st.write("Batting style: Right handed batsman")
                     st.write("Age: 26 years old")
                     st.write("Watch Player Profile Video")
                     with st.container():
                        url = ('https://192.168.191.235:8080')#update link
                        st.video(url) #__player 2
                        with st.container():
                           st.write(':red[Player name: Glen]')
                           st.write("Role: Bowler")
                           st.write("Bowling style: Right arm medium")
                           st.write("Age: 26 years old")
                           st.write("Watch Player Profile Video")
                           with st.container():
                              url = ('https://192.168.191.235:8080')#update link
                              st.video(url) #__player3
                              with st.container():
                                 st.write(':red[Player name: Bona Mjuru]')
                                 st.write("Role: All rounder")
                                 st.write("Bowling style: Right arm leg break")
                                 st.write("Batting style:Right handed batsman ")
                                 st.write("Age: 32 years old")
                                 st.write("Watch Player Profile Video")
                                 with st.container():
                                    url = ('https://192.168.191.235:8080')#update link
                                    st.video(url) #__player 4
                                    with st.container():
                                       st.write(':red[Player name: Mthokozisi T. Sapuwa]')
                                       st.write("Role: Batsman")
                                       st.write("Batting styel: Right handed batsman")
                                       st.write("Age: 23 years old")
                                       st.write("Watch Player Profile Video")
                                       with st.container():
                                          url = ('https://192.168.191.235:8080')#update link
                                          st.video(url) #__player 5
                                          with st.container():
                                             st.write(':red[Player name: Kevin]')
                                             st.write("Role: All rounder")
                                             st.write("Bowling style: Right arm medium pacer")
                                             st.write("Right handed batsman")
                                             st.write("Age: 22 years old")
                                             st.write("Watch Player Profile Video")
                                             with st.container():
                                                url = ('https://192.168.191.235:8080')#update link
                                                st.video(url) #__player 6
                                                with st.container():
                                                   st.write(':red[Player name: William] ')
                                                   st.write("Role: Bowler")
                                                   st.write("Bowling style: Right arm  seamer")
                                                   st.write("Age:  years old")
                                                   st.write("Watch Player Profile Video")
                                                   with st.container():
                                                      url = ('https://192.168.191.235:8080')#update link
                                                      st.video(url) #__player 7
                                                      with st.container():
                                                         st.write(':red[Player name: Lawrence]')
                                                         st.write("Role: Bowling Allrounder")
                                                         st.write("Bowling style: Right arm offspin")
                                                         st.write("Batting style: Right Handed Batsman ")
                                                         st.write("Age: 21 years old")
                                                         st.write("Watch Player Profile Video")
                                                         with st.container():
                                                            url = ('https://192.168.191.235:8080')#update link
                                                            st.video(url) #__player 8
                                                            with st.container():
                                                               st.write(':red[Player name: Gerald]')
                                                               st.write("Role:Wicket keeper/Batsman")
                                                               st.write("Batting style: Right handed batsman")
                                                               st.write("Age: 23 years old")
                                                               st.write("Watch Player Profile Video")
   if selected == "🕹Player Practice sessions":
      with st.container(border=True):
         st.title('Watch our training practice sessions here')
         st.write("""Our Friday practice session was feeling nice and crisp, stay tuned for our weekend game.""")
      with st.container(border=True):
         url = ('https://www.example.com') #update link
         st.video(url)#__vid 1
         
      with st.container(border=True):
         st.subheader("Crisp batting by our batsmen sharpenig up for our next fixture")
         url = ('https://192.168.191.235:8080') #update link
         st.video(url) #__vid 2
         
      with st.container(border=True):
         st.subheader("Engergies on our fielding sessions")
         st.write("Good fielding prep put up by the boys today, like they always say, catches win matches")
         url = ('https://192.168.191.235:8080') #update link
         st.video(url)#__vid 3
         
      with st.container(border=True):
         st.subheader("Management speaks")
         st.write("Check out a couple of interview from our team management and hear a bit more of what they think")
         url = ('https://192.168.191.235:8080') #update link
         st.video(url)#__vid 4
         
    
   if selected == "📽Live Games & Fixtures":
      st.header('Checkout our season fixtures',divider = True)
      st.subheader('Click on the link below to view our upcoming season fixtures')
      st.link_button('View Upcoming WBBCC fixtures',"https://cricheroes.in/tournament/905559/2023-24-BMCA-2nd-League-Pro40" )
      with st.container(border=True):
         st.subheader('WBBCC vs Champions Cricket Club',divider = True)
         st.write('This game is streaming live ')
         
               
if __name__ == "__main__":
   run()
        
