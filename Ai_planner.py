import streamlit as sp
from langchain_google_genai import ChatGoogleGenerativeAI

sp.image('https://png.pngtree.com/background/20230401/original/pngtree-travel-around-the-world-background-picture-image_2253108.jpg', use_container_width=True)

sp.title('AI powerd Travel Assistant')


source = sp.text_input('Source ',placeholder='E.g. Mumbai')
destination = sp.text_input('Destination city',placeholder='E.g. goa')
travel_date = sp.date_input('Traveling date')
mode = sp.selectbox('Mode',['Any', 'Flight', 'CAB', 'Train', 'Bus'])



def travel_option(source,destination,mode,travel_date):
    system_prompt = 'You are an AI-powered travel assistant. Provide multiple travel options (cab, train, bus, flight) with estimated costs, duration, and relevant travel tip and give summry table and keep it short, suggest which will be better '
    user_prommpt = f"I am traveling from {source} to {destination}, Preferred mode: {mode}. Suggest travel options with estimated cost, duration, and important details and summery table with diffrent mode prices."
    
    # Initializing Model
    model = ChatGoogleGenerativeAI(api_key = 'AIzaSyBb78vgrSXypIr4YYjkoozC5DGAwwYU0TM',model='gemini-2.0-flash-lite')
    
    try :
        respoce = model.invoke([user_prommpt,system_prompt])
        respoce.content if respoce else 'No Responce'
    except Exception as e:
        print(f'error: {str(e)}')



# finding travel options 
if sp.button('Find Traveling options'):
    if source.strip() and destination.strip():
        travel_option(source,destination,mode,travel_date)
        sp.markdown(travel_option())
    else:
        sp.warning('Please enter Sources')
