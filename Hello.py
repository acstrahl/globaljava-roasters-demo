import streamlit as st
import random

class ChatManager:
    def __init__(self):
        self.chat_history = []

    def add_message(self, sender, message):
        self.chat_history.append({"sender": sender, "message": message})

    def get_chat_history(self):
        return self.chat_history

    def clear_chat_history(self):
        self.chat_history = []

def chatbot():
    if 'chat_manager' not in st.session_state:
        st.session_state['chat_manager'] = ChatManager()

    chat_manager = st.session_state['chat_manager']

    user_input = st.chat_input("Send a message")
    if user_input:
        chat_manager.add_message("user", user_input)
        bot_response = random.choice([
            "Sure, let me check that for you.",
            "I'm not quite sure. Let me find out.",
            "Hmm, I need to think about that.",
            "Interesting question! Give me a moment."
        ])
        chat_manager.add_message("bot", bot_response)

    for chat in chat_manager.get_chat_history():
        with st.chat_message(chat["sender"]):
            st.write(chat["message"])

    st.button("Clear chat history", on_click=chat_manager.clear_chat_history)

def general_faqs():
    bean_source_expander = st.expander('Where do you source your coffee beans?')
    with bean_source_expander:
        st.write('Our coffee beans are ethically sourced from family-owned farms and cooperatives across various coffee-growing regions, ensuring quality and sustainability in every cup.')
        
    roast_expander = st.expander('How do you roast your beans?')
    with roast_expander:
        st.write('We employ a combination of traditional and modern roasting techniques, meticulously adjusting the roast profile for each batch to bring out the unique flavors and aromas of the beans.')

def recipe_faqs():
    cold_brew_expander = st.expander('What is your recommended recipe for a classic cold brew coffee?')
    with cold_brew_expander:
        st.write("For a smooth and robust cold brew, mix coarsely ground coffee beans with cold water in a 1:8 ratio, steep for 12-18 hours, and then filter. Serve over ice and customize with milk or sweeteners to taste.")
        
    dessert_expander = st.expander('Do you have a signature coffee-based dessert recipe?')
    with dessert_expander:
        st.write("Yes, our signature dessert is the 'GlobalJava Mocha Brownies.' Blend melted dark chocolate with your favorite GlobalJava espresso shot, add to your brownie mix, and bake. These rich, coffee-infused brownies are a coffee lover's delight and perfect for any occasion.")

def submit_feedback():
    st.header("Customer Feedback Form")
    st.write("Your input helps us brew a better experience. Please share your thoughts about our coffee and service.")

    st.write("Did you enjoy your coffee?")
    enjoyed_coffee = st.button("Yes, it was great!")
    not_enjoyed_coffee = st.button("No, it could be better.")

    if enjoyed_coffee:
        st.write("Glad you enjoyed it!")
    elif not_enjoyed_coffee:
        st.write("We're sorry to hear that. We'll strive to improve.")

    st.write("On a scale of 1 to 10, how would you rate our coffee today?")
    coffee_rating = st.slider("Rate our coffee", 1, 10, 5)

    st.write("What type of service did you experience?")
    service_type = st.selectbox("Choose service type", ["In-store Purchase", "Online Order", "Phone Order"])

    st.write(f"You rated our coffee a {coffee_rating} and experienced {service_type} service.")

    st.write("We're always looking to improve. Please tell us more about your experience.")
    name = st.text_input("Name")
    feedback = st.text_area("Your Feedback")
    st.write(f"Thank you, {name}, for your feedback: {feedback}")

def about_us():
    st.header('About Us')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image('Elizabeth_Bennet.png')
        st.markdown('#### Elizabeth Bennet')
        st.write('Founder and CEO, Elizabeth is passionate about bringing customers flavorful and delicious coffee.')
    with col2:
        st.image('Charles_Bingley.png')
        st.markdown('#### Charles Bingley')
        st.write('Marketing Director and Social Media Expert, Charles helps the world know about our great new flavors!')
    
    with col3:
        st.image('Georgiana_Darcy.png')
        st.markdown('#### Georgiana Darcy')
        st.write('Georgiana is the creative genius behind the scenes!')

st.title("GlobalJava Roasters :coffee:")

st.sidebar.title('Navigation')
page = st.sidebar.selectbox('Choose a page', ['About Us', 'FAQs', 'Submit Feedback', 'Chat with Us!'])
       
if page == 'FAQs':
    st.header('FAQs')
    tabs = st.tabs(['General', 'Recipes'])
    with tabs[0]:
        general_faqs()
    with tabs[1]:
        recipe_faqs()

elif page == 'Submit Feedback':
    submit_feedback()

elif page == 'About Us':
    about_us()

elif page == 'Chat with Us!':
    chatbot()