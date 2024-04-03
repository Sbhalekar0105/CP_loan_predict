# Importing necessary libraries
import pickle
import streamlit as st
import yfinance as yf
import pandas as pd
import altair as alt
import plotly.express as px
import numpy as np
from streamlit_option_menu import option_menu
import openai
import json
from streamlit_lottie import st_lottie
from streamlit_feedback import streamlit_feedback
from tensorflow.keras.models import load_model
import warnings
warnings.filterwarnings(action='ignore')

st.set_page_config(page_title="Loan_Predict_App", 
                   page_icon=":money_with_wings:",
                   layout="wide",
                   initial_sidebar_state="expanded")
alt.themes.enable("dark")

st.markdown("""
    <style>
        body {
          background-color: #f0f2f5;  /* Light background */
          color: #333;             /* Text color */
        }
        .stTitle {
          color: #2e8b57;           /* Green for headings */
        }
        .stSubheading {
          color: #f9a825;          /* Orange for subheadings */
        }
        .prediction {
          font-size: 2em;
          color: #2e8b57;           /* Green for the prediction text */
        }
        /* ... add more styling for cards, buttons, etc. as needed ... */
    </style>
    """, unsafe_allow_html=True)
st.markdown("""
    <style>
        body {
          background-color: #f0f2f5;  /* Light background */
          color: #333;             /* Text color */
        }
        .stTitle {
          color: #2e8b57;           /* Green for headings */
        }
        .stSubheading {
          color: #f9a825;          /* Orange for subheadings */
        }
        .prediction {
          font-size: 2em;
          color: #2e8b57;           /* Green for the prediction text */
        }
        /* ... add more styling for cards, buttons, etc. as needed ... */
    </style>
    """, unsafe_allow_html=True)

# Importing the models
df = pickle.load(open('model/dataset.pkl','rb'))
model = load_model('model/my_model.h5')

# Initialize the session state variable
if 'loan_details' not in st.session_state:
    st.session_state['loan_details'] = {
        'loan_amnt': 2400,
        'term': 36,
        'int_rate': 15.96,
        'installment': 84.33,
        'grade': 'B',
        'sub_grade': 'C5',
        'last_pymnt_amnt': 649.91,
    }

# Initialize the session state variable
if 'borrower_details' not in st.session_state:
    st.session_state['borrower_details'] = {
        'emp_length': '10+',
        'home_ownership': 'RENT',
        'annual_inc': 12252.0,
        'verification_status': 'Verified',
        'purpose': 'small_business',
        'dti': 8.72,
        'delinq_2yrs': 0.0,
        'inq_last_6mths': 2.0,
        'open_acc': 2.0,
        'pub_rec': 0.0,
        'revol_bal': 2956.0	,
        'revol_util': 98.5,
        'total_acc': 10.0
    }
    st.markdown("""
    <style>
        body {
          background-color: #f0f2f5;  /* Light background */
          color: #333;             /* Text color */
        }
        .stTitle {
          color: #2e8b57;           /* Green for headings */
        }
        .stSubheading {
          color: #f9a825;          /* Orange for subheadings */
        }
        .prediction {
          font-size: 2em;
          color: #2e8b57;           /* Green for the prediction text */
        }
        /* ... add more styling for cards, buttons, etc. as needed ... */
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
        body {
          background-color: #f0f2f5;  /* Light background */
          color: #333;             /* Text color */
        }
        .stTitle {
          color: #2e8b57;           /* Green for headings */
        }
        .stSubheading {
          color: #f9a825;          /* Orange for subheadings */
        }
        .prediction {
          font-size: 2em;
          color: #2e8b57;           /* Green for the prediction text */
        }
        /* ... add more styling for cards, buttons, etc. as needed ... */
    </style>
    """, unsafe_allow_html=True)

# Create a container for the sidebar
sidebar = st.sidebar.container()

# Add widgets to the sidebar
def load_lottiefile(filepath : str):
    with open("C:\\Users\\shubh\\Desktop\\CP\\loan.json","r", encoding="utf-8") as f:
        return   json.load(f)
with st.sidebar:
    with st.container():
        l,r = st.columns((1,1))
        with l:
            st.empty()
        with r:
            st.empty()
    
    selected = option_menu("App Navigation",["Home", "Borrower Details", "Loan Details", "Insights", "Chat Bot",],
        icons=['house','pencil', 'pen','book', 'chat'],menu_icon='globe',default_index=0) 
    styles={
        "container": {"padding": "0!important", "background-color": " #0E1117"},
        "icon": {"color": "white", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#53CCDC"},
        "nav-link-selected": {"background-color": "#000000"},
    }
    lottie = load_lottiefile("C:\\Users\\shubh\\Desktop\\CP\\loan.json")
    st_lottie(lottie,key='loc')
# Create a container for the main content
content = st.container()

# Add content to the main container
def load_lottiefile1(filepath : str):
    with open("C:\\Users\\shubh\\Desktop\\CP\\place2.json","r", encoding="utf-8") as g:
        return   json.load(g)
with content:
    if selected == "Home":
      # st.title('Loan Prediction App')
      st.markdown("<h1 style='color: #FAFAFA; text-align: center;'>MODERNIZED LOAN APPROVAL SYSTEM</h1>", unsafe_allow_html=True)
      st.markdown("<h3 style='color: #FAFAFA; text-align: center;'>Using the power of Artificial Neural Networks to make informed financial decisions</h3>", unsafe_allow_html=True)
      st.divider()

      st.markdown("<h4 style='color: #FAFAFA; text-align: center;'>Welcome to the Modernized Loan Status Predictor App</h4>",unsafe_allow_html=True)
      col1,col2=st.columns(2)
      with col1:
            st.header('Use Cases')
            st.markdown(
                """
                - _Looking for a new loan?_
                - _Conducting research for loan?_
                - _Curious about your loan eligibility?_
                - _Find out your instant predictions with our loan prediction app?_
                """
                )
      with col2:
            lottie2 = load_lottiefile1("C:\\Users\\shubh\\Desktop\\CP\\place2.json")
            st_lottie(lottie2,key='place',height=250,width=300)
      home_container = st.container()
      home_container.markdown(
                """
                <style>
                .home-container {
                    background-color: #3FB0E8;
                    padding: 20px;
                    border-radius: 20px;
                }

                h1, h3, subheader, header {
                    text-align: center;
                }
                .text{
                background-color: #192841;
                  color: #F9F9F9;
                }

                </style>
               
                <div class="home-container"; background-color: "#3FB0E8"; padding:"20px"; border-radius: "0px">

                <div style="display: flex; justify-content: space-between; color: #192841; background-color: #3FB0E8">
                    <div class="feature-column"; background-color: "#3FB0E8">
                        <h3 class="text">Machine Learning Model</h3>
                        <p style="justify-content: space-between;background-color: #192841;color: #F9F9F9">- Trained on a large dataset of Lending loans</p>
                    </div>
                    <div class="feature-column">
                        <h3 class="text">User-friendly Interface</h3>
                        <p style="justify-content: space-between;background-color: #192841;color: #F9F9F9">- Easily input loan and borrower details</p>
                    </div>
                    <div class="feature-column">
                        <h3 class="text">Customizable  Input's</h3>
                        <p style="justify-content: space-between;background-color: #192841;color: #F9F9F9">- Adjust inputs to see how they affect prediction</p>
                    </div>
                    <div class="feature-column">
                        <h3 class="text">Instant Predictions</h3>
                        <p style="justify-content: space-between;background-color: #192841;color: #F9F9F9">- Get loan status predictions in seconds</p>
                    </div>
                </div>

                """, unsafe_allow_html=True)
      st.divider()
      with st.expander('Modernized Loan Approval System Advantages', expanded=True):
           tab1, tab2, tab3, tab4 = st.tabs(["Improved Financial Planning","Reduced Risk of Default","Enhanced Risk Assessment", "Increased Transparency"])

      with tab1:
         st.header("Improved Financial Planning")
         st.write("Gain insights for informed borrowing and budgeting.")

      with tab2:
         st.header("Reduced Risk of Default")
         st.write("Make data-driven decisions to lower loan default risks.")

      with tab3:
         st.header("Enhanced Risk Assessment")
         st.write("Streamline loan applications by identifying potentially risky borrowers.")
      
      with tab4:
         st.header("Increased Transparency")
         st.write("Gain a deeper understanding of factors influencing loan outcomes.")

            # Create four columns with background color and border radius using CSS
      col1, col2, col3, col4 = st.columns(4)
      for col in [col1, col2, col3, col4]:
        col.markdown("""
                <style>
                .feature-column {
                    background-color: #e0e0e0;   Light gray   
                    padding: 10px;
                    border-radius: 5px;
                    margin: 5px;
                }
                </style>
                """, unsafe_allow_html=True)
      textcontainer = st.container()
      textcontainer.markdown(
                """
                <style>
                .textcontainer {
                   /* background-color: #f5f5f5;   Light blue */
                    padding: 20px;
                    border-radius: 10px;
                }

                h1, h3 {
                    text-align: center;
                }

                .animated-text {
                    font-size: 1.2rem;
                    animation: typing 3.5s steps(40, end) forwards;
                }

                @keyframes typing {
                    from { width: 0 }
                    to { width: 100% }
                }
                </style>

                <div class="textcontainer">
                <div class="animated-text">Thank you for using our Loan Status Predictor App!</div>
          """, unsafe_allow_html=True)
      
    elif selected == "Loan Details":
      st.title('Loan Details')
      st.write('Enter Loan details here.')
      
      loan_amnt = st.number_input('Loan Amount', min_value=0)
      term = st.selectbox('Term', [36,60])
      int_rate = st.number_input('Interest Rate', min_value=0.0, step=5.0, format="%.2f")
      installment = st.number_input('Monthly Payment', min_value=0.0, step=50.0, format="%.2f")
      grade = st.selectbox('Grade', np.sort(df['grade'].unique(), kind='mergesort'))
      sub_grade = st.selectbox('Sub-Grade', np.sort(df['sub_grade'].unique(), kind='mergesort'))
      last_pymnt_amnt = st.number_input('Loan Payment Amount', min_value=0.0, step=100.0, format="%.2f")
      
      st.session_state['loan_details'] = {
        'loan_amnt': loan_amnt,
        'term': term,
        'int_rate': int_rate,
        'installment': installment,
        'grade': grade,
        'sub_grade': sub_grade,
        'last_pymnt_amnt': last_pymnt_amnt,
        }


    elif selected == "Borrower Details":
      st.title('Borrower Details')
      st.write('Enter Borrower details here.')
      
      emp_length = st.selectbox('Employment Length(in year)', ['<1', '1', '2', '3',
                                                '4', '5', '6', '7',
                                                '8', '9', '10+'])
      home_ownership = st.selectbox('Home Ownership', np.sort(df['home_ownership'].unique(),kind='mergesort'))
      # Preprocess input to match format used in model
      home_ownership = home_ownership.replace(" ", "_")
      annual_inc = st.number_input('Annual Income', min_value=0.0, step=1000.0)
      verification_status = st.selectbox('Income Verification Status', np.sort(df['verification_status'].unique(),kind='mergesort'))
      purpose = st.selectbox('Purpose for the loan',np.sort(df['purpose'].unique(),kind='mergesort'))
      
      dti = st.number_input('Debt-to-Income Ratio (DTI)', min_value=0.0, step=5.0)
      delinq_2yrs = st.number_input('Delinquency count in the past 2 years', min_value=0.0, step=1.0, max_value=50.0)
      inq_last_6mths = st.number_input('Credit inquiry count in the last 6 months:', min_value=0.0, step=1.0, max_value=30.0)
      open_acc = st.number_input('Open credit account count', min_value=0.0, step=1.0, max_value=500.0)
      pub_rec = st.number_input('Derogatory public record count', min_value=0.0, step=1.0, max_value=30.0)
      revol_bal = st.number_input('Revolving balance', min_value=0.0, step=1000.0)
      revol_util = st.number_input("Revolving credit utilization(%):", min_value=0.0, step=5.0)
      total_acc = st.number_input("Enter your total number of credit accounts:", min_value=0.0, value=0.0, step=1.0)
      
      st.session_state['borrower_details'] = {
        'emp_length': emp_length,
        'home_ownership': home_ownership,
        'annual_inc': annual_inc,
        'verification_status': verification_status,
        'purpose': purpose,
        'dti': dti,
        'delinq_2yrs': delinq_2yrs,
        'inq_last_6mths': inq_last_6mths,
        'open_acc': open_acc,
        'pub_rec': pub_rec,
        'revol_bal': revol_bal,
        'revol_util': revol_util,
        'total_acc': total_acc
        }
    elif selected == "Insights":
      st.write("""
      # Shown are the insights of Loan Prediction App.
      """)
      # CSS styling
      st.markdown("""
      <style>

      [data-testid="block-container"] {
      padding-left: 2rem;
      padding-right: 2rem;
      padding-top: 1rem;
      padding-bottom: 0rem;
      margin-bottom: -7rem;
      }

      [data-testid="stVerticalBlock"] {
      padding-left: 0rem;
      padding-right: 0rem;
      }

      [data-testid="stMetric"] {
      background-color: #393939;
      text-align: center;
      padding: 15px 0;
      }

      [data-testid="stMetricLabel"] {
      display: flex;
      justify-content: center;
      align-items: center;
      }

      [data-testid="stMetricDeltaIcon-Up"] {
      position: relative;
      left: 38%;
      -webkit-transform: translateX(-50%);
      -ms-transform: translateX(-50%);
      transform: translateX(-50%);
      }

      [data-testid="stMetricDeltaIcon-Down"] {
      position: relative;
      left: 38%;
      -webkit-transform: translateX(-50%);
      -ms-transform: translateX(-50%);
      transform: translateX(-50%);
      }

      </style>
      """, unsafe_allow_html=True)


      #######################
      # Load data
      df_reshaped = pd.read_csv('C:\\Users\\shubh\\Desktop\\CP\\India_data.csv')


      #######################
      # Sidebar
      with st.sidebar:
           st.title('Loan Data Dashboard')
    
      year_list = list(df_reshaped.year.unique())[::-1]
    
      selected_year = st.selectbox('Select a year', year_list)
      df_selected_year = df_reshaped[df_reshaped.year == selected_year]
      df_selected_year_sorted = df_selected_year.sort_values(by="loans", ascending=False)

      color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
      selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
      hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """
      st.markdown(hide_table_row_index, unsafe_allow_html=True)


      #######################
      # Plots

      # Heatmap
      def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
          heatmap = alt.Chart(input_df).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=None,
                             scale=alt.Scale(scheme=input_color_theme)),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.25),
            ).properties(width=900
            ).configure_axis(
            labelFontSize=12,
            titleFontSize=12
            ) 
      # height=300
          return heatmap

      # Choropleth map
      df = pd.read_csv("./pending.csv")
      def make_choropleth(df):
          choropleth = px.choropleth(
          df,
          geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
          featureidkey='properties.ST_NM',
          locations='state',
          color='pending loans',
          color_continuous_scale='Reds'
          )
          choropleth.update_layout(
          template='plotly_dark',
          plot_bgcolor='rgba(0, 0, 255, 0)',
          paper_bgcolor='rgba(0, 0, 255, 0)',
          margin=dict(l=0, r=0, t=0, b=0),
          height=350
          )

          choropleth.update_geos(fitbounds="locations", visible=False)
          return choropleth


        # Donut chart
      def make_donut(input_response, input_text, input_color):
        if input_color == 'blue':
            chart_color = ['#29b5e8', '#155F7A']
        if input_color == 'green':
            chart_color = ['#27AE60', '#12783D']
        if input_color == 'orange':
            chart_color = ['#F39C12', '#875A12']
        if input_color == 'red':
            chart_color = ['#E74C3C', '#781F16']
    
        source = pd.DataFrame({
            "Topic": ['', input_text],
            "% value": [100-input_response, input_response]
        })
        source_bg = pd.DataFrame({
            "Topic": ['', input_text],
            "% value": [100, 0]
        })
    
        plot = alt.Chart(source).mark_arc(innerRadius=45, cornerRadius=25).encode(
        theta="% value",
        color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          #domain=['A', 'B'],
                          domain=[input_text, ''],
                          # range=['#29b5e8', '#155F7A']),  # 31333F
                          range=chart_color),
                      legend=None),
          ).properties(width=130, height=130)
    
        text = plot.mark_text(align='center', color="#29b5e8", font="Lato", fontSize=32, fontWeight=700, fontStyle="italic").encode(text=alt.value(f'{input_response} %'))
        plot_bg = alt.Chart(source_bg).mark_arc(innerRadius=45, cornerRadius=20).encode(
        theta="% value",
        color= alt.Color("Topic:N",
                      scale=alt.Scale(
                          # domain=['A', 'B'],
                          domain=[input_text, ''],
                          range=chart_color),  # 31333F
                      legend=None),
          ).properties(width=130, height=130)
        return plot_bg + plot + text

      # Convert population to text 
      def format_number(num):
          if num > 10000000:
              if not num % 10000000:
                  return f'{num // 10000000} K'
              return f'{round(num / 10000000, 1)} K'
          return f'{num // 100000} K'

      # Calculation year-over-year population
      def calculate_loans_difference(input_df, input_year):
        selected_year_data = input_df[input_df['year'] == input_year].reset_index()
        previous_year_data = input_df[input_df['year'] == input_year - 1].reset_index()
        selected_year_data['loans_difference'] = selected_year_data.loans.sub(previous_year_data.loans, fill_value=0)
        return pd.concat([selected_year_data.states, selected_year_data.id, selected_year_data.loans, selected_year_data.loans_difference], axis=1).sort_values(by="loans_difference", ascending=False)


      #######################
      # Dashboard Main Panel
      col = st.columns((1.5, 4.5, 2), gap='medium')

      with col[0]:
            st.markdown('#### Approved/Rejected')

            df_loans_difference_sorted = calculate_loans_difference(df_reshaped, selected_year)

            if selected_year > 2010:
                first_state_name = df_loans_difference_sorted.states.iloc[0]
                first_state_loans = format_number(df_loans_difference_sorted.loans.iloc[0])
                first_state_delta = format_number(df_loans_difference_sorted.loans_difference.iloc[0])
            else:
                first_state_name = '-'
                first_state_loans = '-'
                first_state_delta = ''
            st.metric(label=first_state_name, value=first_state_loans, delta=first_state_delta)

            if selected_year > 2010:
                last_state_name = df_loans_difference_sorted.states.iloc[-1]
                last_state_loans = format_number(df_loans_difference_sorted.loans.iloc[-1])   
                last_state_delta = format_number(df_loans_difference_sorted.loans_difference.iloc[-1])   
            else:
                last_state_name = '-'
                last_state_loans = '-'
                last_state_delta = ''
            st.metric(label=last_state_name, value=last_state_loans, delta=last_state_delta)

    
            st.markdown('#### States loans')

            if selected_year > 2010:
                df_greater_50000 = df_loans_difference_sorted[df_loans_difference_sorted.loans_difference > 50000]
                df_less_50000 = df_loans_difference_sorted[df_loans_difference_sorted.loans_difference < -50000]
        
                # % of States with population difference > 50000
                states_loan_greater = round((len(df_greater_50000)/df_loans_difference_sorted.states.nunique())*100)
                states_loan_less = round((len(df_less_50000)/df_loans_difference_sorted.states.nunique())*100)
                donut_chart_greater = make_donut(states_loan_greater, 'Approved', 'green')
                donut_chart_less = make_donut(states_loan_less, 'Rejected', 'red')
            else:
                states_loan_greater = 0
                states_loan_less = 0
                donut_chart_greater = make_donut(states_loan_greater, 'Approved', 'green')
                donut_chart_less = make_donut(states_loan_less, 'Rejected', 'red')

            loan_col = st.columns((0.2, 1, 0.2))
            with loan_col[1]:
                st.write('Approved')
                st.altair_chart(donut_chart_greater)
                st.write('Rejected')
                st.altair_chart(donut_chart_less)

      with col[1]:
          st.markdown("<h3 style='color: #FAFAFA; text-align: center;'>Total Loans</h3>", unsafe_allow_html=True)

    
          choropleth = make_choropleth(df)
          st.plotly_chart(choropleth, use_container_width=True)
    
          heatmap = make_heatmap(df_reshaped, 'year', 'states', 'loans', selected_color_theme)
          st.altair_chart(heatmap, use_container_width=True)
    

      with col[2]:
          st.markdown('#### Top States')

          st.dataframe(df_selected_year_sorted,
                 column_order=("states", "loans"),
                 hide_index=True,
                 width=None,
                 column_config={
                    "states": st.column_config.TextColumn(
                        "States",
                    ),
                    "loans": st.column_config.ProgressColumn(
                        "loans",
                        format="%f",
                        min_value=0,
                        max_value=max(df_selected_year_sorted.loans),
                     )}
                 )
    
      with st.expander('About', expanded=True):
        st.write('''
            - Data: [INDIA.DATA](https://www.kaggle.com/datasets/tanishaj225/loancsv)
            - :orange[**Approved/Rejected**]: states with high approved/ rejected loans for selected year
            - :orange[**States Loans**]: percentage of states with annual approved/ rejected loans > 50,000
            ''')
      
    elif selected == "Chat Bot":

      # app config
      st.title("Chat-Bot")

      openai.api_key = st.secrets["OPENAI_API_KEY"]

      # Set a default model
      if "openai_model" not in st.session_state:
          st.session_state["openai_model"] = "gpt-3.5-turbo"

      # Initialize chat history
      if "messages" not in st.session_state:
          st.session_state.messages = []

      # Display chat messages from history on app rerun
      for message in st.session_state.messages:
          with st.chat_message(message["role"]):
              st.markdown(message["content"])

      # Accept user input
      prompt = st.chat_input("What is up?")
      if prompt:
          with st.chat_message("user"):
            st.markdown(prompt)
          st.session_state.messages.append({"role": "user", "content": prompt})
    

      # Display assistant response in chat message container
      with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.chatCompletion.create(
         model=st.session_state["openai_model"],
         message=[
             {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
         ],
         stream=True,
         
     ):
          full_response += response.choices[0].delta.get("content","")
        message_placeholder.markdown(full_response + "")
      message_placeholder.markdown(full_response)
      st.session_state.messages.append({"role": "user", "content": full_response})

if st.button('Predict'):
    # Access loan details and borrower details from session state
    loan_details = st.session_state.get('loan_details')
    borrower_details = st.session_state.get('borrower_details')
    
    loan_amnt = loan_details['loan_amnt']
    term = loan_details['term']
    int_rate = loan_details['int_rate']
    installment = loan_details['installment']
    grade = loan_details['grade']
    # Create a dictionary that maps each grade to its corresponding number
    grade_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
    # Map the selected grade to its corresponding number
    grade = grade_map.get(grade, -1)
    
    sub_grade = loan_details['sub_grade']
    # Create a dictionary that maps each sub_grade to its corresponding number
    sub_grade_map= {'A1': 0, 'A2': 1, 'A3': 2, 'A4': 3, 'A5': 4, 
                    'B1': 5, 'B2': 6, 'B3': 7, 'B4': 8, 'B5': 9, 
                    'C1': 10, 'C2': 11, 'C3': 12, 'C4': 13, 'C5': 14, 
                    'D1': 15, 'D2': 16, 'D3': 17, 'D4': 18, 'D5': 19, 
                    'E1': 20, 'E2': 21, 'E3': 22, 'E4': 23, 'E5': 24, 
                    'F1': 25, 'F2': 26, 'F3': 27, 'F4': 28, 'F5': 29, 
                    'G1': 30, 'G2': 31, 'G3': 32, 'G4': 33, 'G5': 34}
    # Map the selected sub_grade to its corresponding number
    sub_grade = sub_grade_map.get(sub_grade, -1)
    
    last_pymnt_amnt = float(loan_details['last_pymnt_amnt'])
    
    emp_length = borrower_details['emp_length']
    # Create a dictionary that maps each emp_length to its corresponding number
    emp_length_map= {'<1': 0,'1': 1,'2': 2,'3': 3,
                    '4': 4, '5': 5,'6': 6,'7': 7,
                    '8': 8,'9': 9, '10+': 10}
    # Map the selected sub_grade to its corresponding number
    emp_length = emp_length_map.get(emp_length, -1)
    
    home_ownership = borrower_details['home_ownership']
    annual_inc = borrower_details['annual_inc']
    verification_status = borrower_details['verification_status']
    purpose = borrower_details['purpose']
    dti = borrower_details['dti']
    delinq_2yrs = borrower_details['delinq_2yrs']
    inq_last_6mths = borrower_details['inq_last_6mths']
    open_acc = borrower_details['open_acc']
    pub_rec = borrower_details['pub_rec']
    revol_bal = borrower_details['revol_bal']
    revol_util = borrower_details['revol_util']
    total_acc = borrower_details['total_acc']
    
    if home_ownership =='MORTGAGE':
      home_ownership_MORTGAGE=1
      home_ownership_NONE=0
      home_ownership_OTHER=0
      home_ownership_OWN=0
      home_ownership_RENT=0
    elif home_ownership =='NONE':
      home_ownership_MORTGAGE=0
      home_ownership_NONE=1
      home_ownership_OTHER=0
      home_ownership_OWN=0
      home_ownership_RENT=0
    elif home_ownership =='OTHER':
      home_ownership_MORTGAGE=0
      home_ownership_NONE=0
      home_ownership_OTHER=1
      home_ownership_OWN=0
      home_ownership_RENT=0
    elif home_ownership =='OWN':
      home_ownership_MORTGAGE=0
      home_ownership_NONE=0
      home_ownership_OTHER=0
      home_ownership_OWN=1
      home_ownership_RENT=0
    elif home_ownership =='RENT':
      home_ownership_MORTGAGE=0
      home_ownership_NONE=0
      home_ownership_OTHER=0
      home_ownership_OWN=0
      home_ownership_RENT=1
    else:
      home_ownership_MORTGAGE=0
      home_ownership_NONE=0
      home_ownership_OTHER=0
      home_ownership_OWN=0
      home_ownership_RENT=0
      
    if verification_status =='Source Verified':
      verification_status_Source_Verified=1
      verification_status_Verified=0
    elif verification_status =='Verified':
      verification_status_Source_Verified=0
      verification_status_Verified=1
    else:
      verification_status_Source_Verified=0
      verification_status_Verified=0
    
    if purpose =='credit_card':
      purpose_credit_card=1
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=0
    elif purpose =='debt_consolidation':
      purpose_credit_card=0
      purpose_debt_consolidation=1
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=0
    elif purpose =='educational':
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=1
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=0
    elif purpose =='home_improvement':
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=1
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=0
    elif purpose =='house':
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=1
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=0
    elif purpose =='major_purchase':
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=1
      purpose_medical=0
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=0
    elif purpose =='medical':
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=1
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=0
    elif purpose =='moving':
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=1
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=0
    elif purpose =='other':
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=0
      purpose_other=1
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=0
    elif purpose =='renewable_energy':
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=1
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=0
    elif purpose =='small_business':
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=1
      purpose_vacation=0
      purpose_wedding=0
    elif purpose =='vacation':
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=1
      purpose_wedding=0
    elif purpose =='wedding':
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=1
    else:
      purpose_credit_card=0
      purpose_debt_consolidation=0
      purpose_educational=0
      purpose_home_improvement=0
      purpose_house=0
      purpose_major_purchase=0
      purpose_medical=0
      purpose_moving=0
      purpose_other=0
      purpose_renewable_energy=0
      purpose_small_business=0
      purpose_vacation=0
      purpose_wedding=0
    
    query = np.array([[loan_amnt, term, int_rate, installment, grade, sub_grade, emp_length, annual_inc, dti, delinq_2yrs,
              inq_last_6mths, open_acc,	pub_rec, revol_bal,	revol_util,	total_acc, last_pymnt_amnt, home_ownership_MORTGAGE,
              home_ownership_NONE,	home_ownership_OTHER, home_ownership_OWN, home_ownership_RENT, verification_status_Source_Verified,
              verification_status_Verified,	purpose_credit_card, purpose_debt_consolidation, purpose_educational,
              purpose_home_improvement,	purpose_house, purpose_major_purchase, purpose_medical,	purpose_moving,
              purpose_other, purpose_renewable_energy, purpose_small_business, purpose_vacation, purpose_wedding]])
    query = query.reshape(1,37)
    
    prediction=int(model.predict(query)[0])
    st.title("Prediction:")
    if prediction ==0:
      st.subheader("APPROVED")
    else:
      st.subheader("REJECTED")  
