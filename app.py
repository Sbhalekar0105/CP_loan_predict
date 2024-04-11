# Importing necessary libraries
import pickle
import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import numpy as np
from streamlit_option_menu import option_menu
from typing import Generator
import json
import matplotlib.pyplot as plt
import time
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
    lottie = load_lottiefile("loan.json")
    st_lottie(lottie,key='loc')
    selected = option_menu("App Navigation",["Home", "Borrower Details", "Loan Details","EMI Calculator","Check CIBIL Score", "Insights","Chat Bot"],
        icons=['house','pencil', 'pen','app-indicator','check','activity' ,'chat'],menu_icon='cast',default_index=0)
    st.markdown("<h2 style='text-align: center; color: white;'>Do You Like Our App?</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style='display: flex; justify-content: center;'>
        <button style='border: none; background-color: transparent; padding: 10px; border-radius: 5px; cursor: pointer; box-shadow: 0 0 5px 2px green;'>
            👍
        </button>
        <button style='border: none; background-color: transparent; padding: 10px; border-radius: 5px; cursor: pointer; box-shadow: 0 0 5px 2px red; margin-left: 10px;'>
            👎
        </button>
    </div>
    """, unsafe_allow_html=True)

# Styling for the sidebar
    st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #0E1117;
        }
        .sidebar .sidebar-content .stSelectbox {
            color: white;
        }
        .sidebar .sidebar-content .stSelectbox .stSelectbox-options {
            color: black;
        }
        .sidebar .sidebar-content h2 {
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
    styles={
        "container": {"padding": "0!important", "background-color": " #0E1117"},
        "icon": {"color": "white", "font-size": "20px"}, 
        "nav-link": {"font-size": "17px", "text-align": "left", "margin":"0px", "--hover-color": "#53CCDC"},
        "nav-link-selected": {"background-color": "#000000"},
    }
def load_lottiefile1(filepath : str):
    with open("place2.json","r", encoding="utf-8") as g:
        return   json.load(g)    
# Create a container for the main content
content = st.container()
# Add content to the main container
with content:
    if selected == "Home":
      # st.title('Loan Prediction App')
      st.markdown("<h1 style='color: #F9F9F9; text-align: center;'>MODERNIZED LOAN APPROVAL SYSTEM</h1>", unsafe_allow_html=True)
      st.markdown("<h3 style='color: #F9F9F9; text-align: center;'>Using the power of Artificial Neural Networks to make informed financial decisions</h3>", unsafe_allow_html=True)
      st.subheader("",divider="rainbow", anchor=False)

      st.markdown("<h4 style='color: #F9F9F9; text-align: center;'>Welcome to the Modernized Loan Status Predictor App</h4>",unsafe_allow_html=True)
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
            st_lottie(lottie2,key='place',height=180,width=300)
      st.subheader("",divider="rainbow", anchor=False)
      st.markdown("<h2 style='text-align: center; margin-bottom: -0.9em;'>Do you think a personal loan needs too much effort?</h2>", unsafe_allow_html=True)
      st.markdown("<h5 style='text-align: center; margin-bottom: 30px;'>Getting a personal loan was never this easy</h5>", unsafe_allow_html=True)
# Function to display markdown content with image
      def display_image_with_text(image_path, title, content):
       st.image(image=image_path,width=80, caption=title)
       st.write(content)
# Display images using display_image_with_text function
      col1, col2, col3 = st.columns(3)

      with col1:
       display_image_with_text("1.png", "Instant personal loans", "Get instant personal loans from 5000 to 5 lakh to fit all your needs and dreams")
       display_image_with_text("2.jpg", "Quick Approvals & Disbursals", "Get prompt loan approval and money in your account")

      with col2:
       display_image_with_text("3.jpg", "Paperless Documentation", "Upload pictures of your KYC documents and sign your loan application digitally")
       display_image_with_text("4.jpg", "ZERO Affordable EMI plans", "Easy to manage EMI plans with reminders and auto-debit features so that you don't miss out on timely payments")

      with col3:
       display_image_with_text("5.jpg", "One-click subsequent personal loans", "Need another loan from PaySense? With one-time documentation, it's just a click away.")
       display_image_with_text("6.jpg", "Zero Credit History", "Never taken a personal loan previously? It's okay - we serve the users who are new to the credit and lending system.")     
      st.subheader("",divider="rainbow", anchor=False)
      box1_style = """
        padding: 14px;
        border-radius: 10px;
        background-color: #3FB0E8;
        color: white;
        margin-bottom: 1px;
        """
      box2_style = """
        padding: 3px;
        border-radius: 10px;
        background-color: #3FB0E8;
        color: white;
        """
      eligibility_criteria = """
        ### Are you eligible for a personal loan?
        To be eligible to get a personal loan from,you should fulfill the following eligibility criteria:
        - **Resident of India**
        - **Age: 21 years to 60 years**
        - **Employment Type: Salaried and Self-employed**
        """
      documents_required = """
      ### What are required documents?
      To get a personal loan instantly, you should keep some documents handy before you start applying.

      - **Proof of Identity:**
      PAN Card & Selfie\n
      - **Proof of Address:**
      Aadhaar card, Voter ID, Passport or Driving License\n
      - **Proof of Income:**
      Net-Banking or last 3 months bank e-statements\n
      """

# Splitting the content into two columns
      col1, col2 = st.columns(2)

# Displaying the content in the first column
      with col1:
        st.markdown(
        f"""
        <div style="{box1_style}">
            {eligibility_criteria}
        </div>
        """,
        unsafe_allow_html=True
    )

# Displaying the content in the second column
      with col2:
        st.markdown(
        f"""
        <div style="{box2_style}">
            {documents_required}
        </div>
        """,
        unsafe_allow_html=True
    )
      st.subheader("",divider="rainbow", anchor=False)

      with st.expander('### **Modernized Loan Approval System Advantages**', expanded=True):
           tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Improved Financial Planning","Reduced Risk of Default","Enhanced Risk Assessment", "Increased Transparency","Faster Decision Making","Cost Reduction"])

      def load_lottiefile3(filepath : str):
        with open("ani1.json","r", encoding="utf-8") as g:
         return   json.load(g) 
      def load_lottiefile4(filepath : str):
        with open("ani2.json","r", encoding="utf-8") as g:
         return   json.load(g) 
      def load_lottiefile5(filepath : str):
        with open("ani3.json","r", encoding="utf-8") as g:
         return   json.load(g)
      def load_lottiefile6(filepath : str):
        with open("ani4.json","r", encoding="utf-8") as g:
         return   json.load(g)
      def load_lottiefile7(filepath : str):
        with open("ani5.json","r", encoding="utf-8") as g:
         return   json.load(g) 
      def load_lottiefile8(filepath : str):
        with open("ani6.json","r", encoding="utf-8") as g:
         return   json.load(g) 
      with tab1:
         st.markdown("<h2 style='text-align: center;'>Improved Financial Planning</h2>",unsafe_allow_html=True)
         st.subheader("",divider="", anchor=False)
         col1, col2 = st.columns(2)
         with col1:
          st.write("• _Plan future expenses effectively_.")
          st.write("• _Analyze historical data for better financial decisions_.")
          st.write("• _Gain insights for informed borrowing and budgeting_.")
          st.write("• _Incorporate goal-setting frameworks to align financial decisions_.")
          st.write("• _Employ forecasting techniques to anticipate future financial needs_.")
         with col2:
          lottie2 = load_lottiefile3("ani1.json")
          st_lottie(lottie2,key='new',height=180,width=300,)
      
      with tab2:
         st.markdown("<h2 style='text-align: center;'>Reduced Risk of Default</h2>",unsafe_allow_html=True)
         st.subheader("",divider="", anchor=False)
         col1, col2 = st.columns(2)
         with col1:
          st.write("• _Identify early warning signs of potential defaults_.")
          st.write("• _Identify warning signs of potential defaults early on_.")
          st.write("• _Make data-driven decisions to lower loan default risks_.")
          st.write("• _Implement predictive models to assess default likelihood_.")
          st.write("• _Implement risk scoring models to assess default probability_.")
         with col2:
           lottie2 = load_lottiefile4("ani2.json")
           st_lottie(lottie2,key='new5',height=180,width=300,)
      with tab3:
         st.markdown("<h2 style='text-align: center;'>Enhanced Risk Assessment</h2>",unsafe_allow_html=True)
         st.subheader("",divider="", anchor=False)
         col1, col2 = st.columns(2)
         with col1:
          st.write("• _Automate creditworthiness evaluation processes_.")
          st.write("• _Utilize machine learning algorithms for risk profiling_.") 
          st.write("• _Streamline loan applications by identifying potentially risky borrowers_.")
          st.write("• _Implement real-time monitoring to promptly detect changes in borrower risk profiles_.")
          st.write("• _Leverage machine learning to develop comprehensive risk profiles for more accurate assessments_.")
         with col2:
          lottie2 = load_lottiefile5("ani3.json")
          st_lottie(lottie2,key='new1',height=180,width=350,)
      
      with tab4:
         st.markdown("<h2 style='text-align: center;'> Increased Transparency</h2>",unsafe_allow_html=True)
         st.subheader("",divider="", anchor=False)
         col1, col2 = st.columns(2)
         with col1:
          st.write("• _Enhance regulatory compliance through transparent processes_.")
          st.write("• _Gain a deeper understanding of factors influencing loan outcomes_.")
          st.write("• _Provide borrowers with clear explanations of loan terms and conditions_.")
          st.write("•_Improve regulatory compliance by ensuring transparent processes and clear communication_.")
          st.write("• _Utilize technology to provide easily accessible information on loan terms and conditions_.")
         with col2:
          lottie2 = load_lottiefile6("ani4.json")
          st_lottie(lottie2,key='new2',height=180,width=350,)  

      with tab5:
         st.markdown("<h2 style='text-align: center;'>Faster Decision Making</h2>",unsafe_allow_html=True)
         st.subheader("",divider="", anchor=False)
         col1, col2 = st.columns(2)
         with col1:
          st.write("• _Enhance customer experience with prompt responses_.") 
          st.write("• _Reduce processing time through automated workflows_.")
          st.write("• _Make quicker loan approval decisions to improve customer satisfaction_.")
          st.write("• _Implement efficient automated workflows to streamline processing time_.")
          st.write("• _Utilize data-driven insights to expedite loan approval processes, boosting customer satisfaction_ .") 
         with col2:
          lottie2 = load_lottiefile7("ani5.json")
          st_lottie(lottie2,key='new3',height=150,width=300,)

      with tab6:
         st.markdown("<h2 style='text-align: center;'>Cost Reduction</h2>",unsafe_allow_html=True)
         st.subheader("",divider="", anchor=False)
         col1, col2 = st.columns(2)
         with col1:
          st.write("• _Minimize paperwork and administrative overhead_.")
          st.write("• _Optimize resource allocation for improved efficiency_.")
          st.write("• _Streamline processes to minimize paperwork and administrative burdens_.")
          st.write("• _Lower operational costs associated with manual loan processing methods_.")  
          st.write("• _Implement digital solutions to reduce operational costs linked to manual loan processing_.")
         with col2:
          lottie2 = load_lottiefile8("ani6.json")
          st_lottie(lottie2,key='new4',height=220,width=450,)
      # Create four columns with background color and border radius using CSS
      col1, col2, col3, col4,col5, col6 = st.columns(6)
      for col in [col1, col2, col3, col4, col5, col6]:
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
      st.markdown("<h3 style='text-align: left;'>Personal loan comparison index :</h3>",unsafe_allow_html=True)
      st.subheader("",divider="rainbow", anchor=False)
      data = {
    "Bank/NBFC": ["Lending Kart", "Axis Finance", "ICICI", "NIRA", "Muthoot Finance", "Home credit", "Bajaj Finserv", "Fullerton"],
    "Interest rate": ["(18 - 30)%", "(12 - 18)%", "(10.5 - 19)%", "-", "14.5 - 25%", "0% - 5%", "13%", "(11.99 - 36)%"],
    "Loan amount": ["50,000 - 1 Cr", "50,000 max 50L", "50,000 - 25 Lacs", "5,000 - 100,000 INR", "1 Lakh metro , 50 k Non metro - Max 10 Lakhs", "25,000 - 200,000 INR", "-", "-"],
    "Processing fee": ["At 2%", "2% on loan amount + GST", "Upto 2.25% of loan amount plus GST", "350-750 depending on the loan amount", "1.75% Per disbursal", "0% - 5%", "upto 4.13% on loan amount + Taxes", "0-6% Loan Amount"],
    "Tenure": ["-", "Upto 60 Months", "12 to 72 months", "3-12 months", "12-60 months", "-", "3-36 months", "upto 60 Months"],
    "Target age group": ["18-65", "21-60", "23-58", "21-55", "23-60", "19+", "23-55", "21-60"],
    "Serviceable location": ["Pan India", "Pan India", "-", "Pan India", "Pan India", "-", "Pan India", "-"],
    "Salary bracket": ["12 lakhs annual turnover and above", "Tier 1: 25K, Tier 2: 20k, Tier 3: 15k", "30K+", "12000+", "20K - 25K", "INR 10,000 +", "Tier 1: 25K +,Tier 2: 35K +", "Tier 1: 20K, Tier 2: 20K +"],
    "Commercials offered": ["Slab wise, 50L - 3CR: 1-2%", "1.5%", "1.1% Per disbursal", "1500", "-", "1.4 % CPD", "650+", "750+"],
    "Credit score": ["660 (560-660 will could be considered on case to case basis) + NTC", "650 min , actual >720 (V3), CIBIL>750", "750+", "660+", "750 & -1 & NTC", "670+ credit score", "650+", "750+"],
    "Employment type": ["Self employed", "Salaried", "Salaried", "Salaried", "Salaried", "Salaried and self employed", "Salaried and self employed", "Salaried"],
    "Product type": ["working capital loans and business loans", "Personal Loan", "PL", "Short term loan", "Personal Loan", "-", "PL/BL", "PL"]
}
      # Creating DataFrame
      df = pd.DataFrame(data)
      df.insert(0, "Sr. No.", range(1, len(df) + 1))
      df.set_index("Sr. No.", inplace=True)
      # Change header color
      header_html = """
      <style>
      div.row-widget.stRadio>div{flex-direction:column;}
      th {
      background-color: #3FB0E8;
      color: #F9F9F9; 
      }
      </style>
      """
      st.markdown(header_html, unsafe_allow_html=True)
      # Displaying the table
      st.table(df.style.set_table_styles([{'selector': 'th', 'props': [('background-color', '#3FB0E8')]}]))
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
      if st.button('Save'):
          st.write('### Borrower Details has saved proceed to Loan Details.')
          st.session_state['Loan Details'] = True
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
      
    elif selected == "EMI Calculator":
      st.title('EMI Calculator')
      st.write('Enter EMI details here.')
      def calculate_emi(principal, annual_interest_rate, loan_term):
          monthly_interest_rate = annual_interest_rate / 12 / 100
          number_of_payments = loan_term * 12
          emi = (principal * monthly_interest_rate * ((1 + monthly_interest_rate) ** number_of_payments)) / (((1 + monthly_interest_rate) ** number_of_payments) - 1)
          total_payment = emi * number_of_payments
          total_interest = total_payment - principal
          return emi, total_interest, total_payment

      def main():
          st.title("EMI Calculator")
    
      principal = st.number_input("Loan Amount", value=0.00)
      annual_interest_rate = st.number_input("Annual Interest Rate (%)", value=0.0, step=0.1)
      loan_term = st.number_input("Loan Term (years)", value=0)
    
      if st.button("Calculate"):
        emi, total_interest, total_payment = calculate_emi(principal, annual_interest_rate, loan_term)
        
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.subheader("EMI:")
            st.write(f"{emi:.2f} INR")
            st.subheader("Total Interest Payable:")
            st.write(f"{total_interest:.2f} INR")
            st.subheader("Total Payment Payable:")
            st.write(f"{total_payment:.2f} INR")
        
        with col2:
            # Pie Chart
            fig, ax = plt.subplots(facecolor='#192841')
            labels = ['Principal', 'Interest']
            sizes = [principal, total_interest]
            colors = ['#2E8B57', '#FF6347']
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, labeldistance=1.05, textprops={'color': 'white'})
            ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax.set_facecolor('#192841')
            ax.legend(facecolor='#192841', edgecolor='white', labelcolor='white')
            st.pyplot(fig)
        
        # Amortization Schedule
        fig, ax = plt.subplots(figsize=(5, 3), facecolor='#192841')
        fig.__sizeof__=('0,2')
        months = np.arange(1, loan_term * 12 + 1)
        principal_remaining = principal
        interest_paid = 0
        principal_paid = 0
        principal_schedule = []
        interest_schedule = []
        
        for month in months:
            interest_this_month = principal_remaining * (annual_interest_rate / 12 / 100)
            principal_this_month = emi - interest_this_month
            principal_remaining -= principal_this_month
            interest_paid += interest_this_month
            principal_paid += principal_this_month
            principal_schedule.append(principal_remaining)
            interest_schedule.append(interest_this_month)
        
        ax.plot(months, principal_schedule, label='Principal Remaining', color='#2E8B57')
        ax.plot(months, interest_schedule, label='Interest Paid', color='#FF6347')
        ax.set_xlabel('Months', color='white')
        ax.set_ylabel('Amount (INR)', color='white')
        ax.set_title('Amortization Schedule', color='white')
        ax.legend()
        ax.grid(color='lightgray', linestyle='--', linewidth=0.5)
        ax.set_facecolor('#192841')
        plt.xticks(color='white')
        plt.yticks(color='white')
        st.pyplot(fig)
        
        # Animation
        progress_bar = st.progress(0)
        status_text = st.empty()
        for i in range(101):
            progress_bar.progress(i)
            status_text.text(f'Calculating... {i}%')
            time.sleep(0.05)
        progress_bar.empty()
        status_text.text('Calculation Complete!')

    elif selected == "Check CIBIL Score":
      st.title('CIBIL Score Calculator')
      st.write('Enter details here.')
      def calculate_cibil_score(age, income, loan_amount, loan_tenure, existing_loan_emi, credit_card_balance, 
                          dependents, employment_years, recent_credit_inquiries, late_payments, total_accounts,
                          credit_utilization_ratio):
    # Calculate CIBIL score
          cibil_score = 700 + (age * 5) + (income / 100000) - (loan_amount / 1000000) - (loan_tenure / 2) - \
                  (existing_loan_emi / 10000) - (credit_card_balance / 10000) + (dependents * 10) - \
                  (employment_years * 5) - (recent_credit_inquiries * 20) - (late_payments * 30) + \
                  (total_accounts * 20) - (credit_utilization_ratio * 10)
    
          return int(cibil_score)

# Function to display CIBIL score category
      def get_score_category(cibil_score):
        if cibil_score >= 800:
          return "Excellent"
        elif 750 <= cibil_score < 800:
          return "Good"
        elif 700 <= cibil_score < 750:
          return "Average"
        else:
          return "Bad"

    # Creating two columns for arranging inputs side by side
      col1, col2 = st.columns(2)

    # User inputs
      with col1:
        age = st.number_input("Your Age:", min_value=0, max_value=100, value=0)
        loan_amount = st.number_input("Loan Amount Requested (INR):", value=0)
        existing_loan_emi = st.number_input("Existing Loan EMI (INR):", value=0)
        dependents = st.number_input("Number of Dependents:", min_value=0, value=0)
        recent_credit_inquiries = st.number_input("Recent Credit Inquiries (6 months):", min_value=0, value=0)
        credit_utilization_ratio = st.number_input("Credit Utilization Ratio:", min_value=0, value=0)

      with col2:
        income = st.number_input("Your Annual Income (INR):", value=0)
        loan_tenure = st.number_input("Loan Tenure (Years):", min_value=0, value=0)
        credit_card_balance = st.number_input("Credit Card Balance (INR):", value=0)
        employment_years = st.number_input("Years in Current Employment:", min_value=0, value=0)
        late_payments = st.number_input("Late Payments (2 years):", min_value=0, value=0)
        total_accounts = st.number_input("Total Number of Accounts:", min_value=0, value=0)

      if st.button("Calculate CIBIL Score"):
        # Calculate CIBIL score
        cibil_score = calculate_cibil_score(age, income, loan_amount, loan_tenure, existing_loan_emi, credit_card_balance, 
                                            dependents, employment_years, recent_credit_inquiries, late_payments, total_accounts,
                                            credit_utilization_ratio)

        # Display CIBIL score and category
        st.subheader("Your CIBIL Score:")
        st.write(f"**{cibil_score}**")

        score_category = get_score_category(cibil_score)
        st.subheader("Score Category:")
        st.write(score_category)

        # Display score category with animation
        if score_category == "Excellent":
            st.success("Congratulations! You have an excellent score.")
        elif score_category == "Good":
            st.info("Your score is good. Keep it up!")
        elif score_category == "Average":
            st.warning("Your score is average. Work on improving it.")
        else:
            st.error("Your score is bad. Take steps to improve it.")

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
      def make_choropleth(df,input_column,input_color_theme):
          choropleth = px.choropleth(df,color=input_column,color_continuous_scale=input_color_theme,
          geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
          featureidkey='properties.ST_NM',
          locations='state',
          )
          choropleth.update_layout(
          template='plotly_dark',
          plot_bgcolor='#192841',
          paper_bgcolor='#192841',
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
          if num > 1000:
              if not num % 1000:
                  return f'{num // 1000} K'
              return f'{round(num / 1000, 1)} K'
          return f'{num // 1000} K'

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
                df_greater_50000 = df_loans_difference_sorted[df_loans_difference_sorted.loans_difference > 50]
                df_less_50000 = df_loans_difference_sorted[df_loans_difference_sorted.loans_difference < -5]
        
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
          st.markdown("<h3 style='color: #FAFAFA; text-align: center;'>States</h3>", unsafe_allow_html=True)

    
          choropleth = make_choropleth(df,'pending loans',selected_color_theme)
          st.plotly_chart(choropleth, use_container_width=True)
    
          heatmap = make_heatmap(df_reshaped, 'year', 'states', 'loans', selected_color_theme)
          st.altair_chart(heatmap, use_container_width=True)
    

      with col[2]:
          st.markdown('#### Total loans')

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
            - :orange[**States Loans**]: percentage of states with annual approved/ rejected loans > 15,000
            ''')
      
    elif selected == "Chat Bot":

      # app config
      def load_lottiefile2(filepath : str):
        with open("C:\\Users\\shubh\\Desktop\\CP\\new.json","r", encoding="utf-8") as g:
         return   json.load(g)
      lottie = load_lottiefile2("C:\\Users\\shubh\\Desktop\\CP\\loan.json") 
      st.title("Chat-Bot")
      st_lottie(lottie,key='loc1',height=120,width=170)
      st.subheader("",divider="rainbow", anchor=False)

      
