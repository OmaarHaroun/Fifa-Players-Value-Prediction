import streamlit as st
import pandas as pd
import joblib
import numpy as np
import plotly.express as px
inputs = joblib.load('INPUTS.pkl')
model = joblib.load('Model.pkl')


#-----------------------------------------------------------------------------------------------------------------------

def Prediction_Page():
    def pred(Age, Nationality, Overall, International_Reputation, Work_Rate, Position):
        test_df = pd.DataFrame(columns = inputs)
        test_df.at[0, 'Age'] = Age 
        test_df.at[0, 'Nationality'] = Nationality 
        test_df.at[0, 'Overall'] =Overall 
        test_df.at[0, 'International Reputation'] = International_Reputation
        test_df.at[0, 'Work Rate'] = Work_Rate
        test_df.at[0, 'Position'] = Position
        result = model.predict(test_df)[0]
        return result

    
    def main():
        st.title ('Time To Predict')
        Age = st.slider('Indicate the age', min_value= 15, max_value= 44, value=0, step=1 )
    
        Nationality = st.selectbox('Select Nationality',['England' ,'Argentina', 'others', 'Brazil', 'Italy', 'Uruguay',
                                                'Republic of Ireland' ,'Turkey', 'Romania' ,'United States' ,'France'
                                                'Netherlands' ,'Germany', 'Sweden', 'Spain', 'Paraguay' ,'Poland', 'Japan',
                                                'Ecuador', 'China PR', 'Venezuela'] )
    
        Overall = st.slider('State player overall', min_value= 44, max_value= 81, value=0, step=1 )
        International_Reputation = st.slider('Reputation', min_value=1, max_value= 4, value=0, step=1)
    
    
        Work_Rate = st.selectbox('State Work Rate', ['Medium/ Medium', 'High/ Low', 'Medium/ Low', 'High/ Medium', 'Medium/ High',
                                                 'High/ High' ,'Low/ Medium', 'Low/ High', 'Low/ Low'])
    
        Position = st.selectbox('State the Position',['RES', 'RB' ,'RCM' ,'SUB' ,'LDM' ,'RM' ,'LCB' ,'LCM', 'LM', 'CDM', 'LB', 'ST' 'RDM'
                                                  'CAM', 'RS', 'RWB' ,'RF', 'LS', 'LW' ,'RCB' ,'LWB', 'RW', 'CB' ,'LF' ,'CM', 'LAM'
                                                  'CF' ,'RAM' ,'GK'])

    
    
        if st.button('Predict'):
            result = pred(Age, Nationality, Overall, International_Reputation, Work_Rate, Position)
            st.text(f'The Player Value is will be {result}')         
                
    if __name__ == '__main__':
        main()
        
# -----------------------------------------------------------------------------------------------------------------


def mainpage():
    
    st.title("FIFA PLAYERS VALUE PREDICTION")

    
    
    st.image("360_F_431188076_ZJ6XwNhJDUIG7ZwWnR3cfUg0vpGLyDEN.jpg")
    
    
    
# --------------------------------------------------------------------------------------------------------------------    
       
def aboutpage():
    
    st.title('About The Dataset')
    st.write('This Dataset collect information about the players in FIFA game to predict the Value of any player in the future')
    
    df = pd.read_csv('FOOTBALL.csv')
    if st.button('Data Sample'):
        st.success('Here is a sample from the original dataset')
        st.write(df.head(5))
    if st.button('Data Features'):
        st.success('The Features of the Data are')
        st.write('''
        
        Age: The Age of the player
        
        Nationality: The Country where each player is from 
        
        Position: The main position of each player in his club 
        
        International Reputation: Scale from 0 to 4 , to indicate the player's International reupuatation
        
        Work Rate: It is a feature to indicate the attack and defense skills for each player (Attack/Defense)
        
        Overall: Value to indicate the total performance of the player
         ''')

#------------------------------------------------------------------------------------------------------------------
def Data_analysis():
    df = pd.read_csv('FOOTBALL.csv')
    st.title('Data Analysis Page')
    st.write('''This Page will help you in visualizing the data you want for using in data analysis:
    Univariante analysis to see the plot of the feature
    Bivariante analysis to see the plots between features with each others or with target
    ''')
    if st.checkbox('Univariante Analysis'):
        fig1=px.histogram(data_frame=df,x='Age',text_auto=True,marginal='box')
        fig2=px.pie(data_frame=df,names='Age')
        fig3=px.histogram(data_frame=df,x='Nationality',text_auto=True,marginal='box')
        fig4=px.histogram(data_frame=df,x='Overall',text_auto=True,marginal='box')
        fig5=px.histogram(data_frame=df,x='Club',text_auto=True,marginal='box')
        fig6=px.histogram(data_frame=df,x='Value',text_auto=True,marginal='box')
        fig7=px.histogram(data_frame=df,x='Preferred Foot',text_auto=True,marginal='box')
        fig8=px.histogram(data_frame=df,x='International Reputation',text_auto=True,marginal='box')
        fig9=px.histogram(data_frame=df,x='Weak Foot',text_auto=True,marginal='box')
        fig10=px.histogram(data_frame=df,x='Skill Moves',text_auto=True,marginal='box')
        fig11=px.pie(data_frame=df,names='Skill Moves')
        fig12=px.histogram(data_frame=df,x='Work Rate',text_auto=True,marginal='box')
        fig13=px.histogram(data_frame=df,x='Position',text_auto=True,marginal='box')
        st.plotly_chart(fig1)
        st.plotly_chart(fig2)
        st.plotly_chart(fig3)
        st.plotly_chart(fig4)
        st.plotly_chart(fig5)
        st.plotly_chart(fig6)
        st.plotly_chart(fig7)
        st.plotly_chart(fig8)
        st.plotly_chart(fig9)
        st.plotly_chart(fig10)
        st.plotly_chart(fig11)
        st.plotly_chart(fig12)
        st.plotly_chart(fig13)
    elif st.checkbox('Bivariante Analysis'):
        selected=st.selectbox('Choose the plot to see a feature with the target',('Player age with value','Overall rate with value','Preffered foot with value','Weak foot with value','Nationality with value'))
        if selected=='Player age with value':
            f1=px.scatter(data_frame=df,x='Age',y='Value',color='Value')
            st.plotly_chart(f1)
        elif selected== 'Overall rate with value':   
            f2=px.scatter(data_frame=df,x='Overall',y='Value',color='Value')
            st.plotly_chart(f2)
        elif selected=='Preffered foot with value':
            f3=px.scatter(data_frame=df,x='Preferred Foot',y='Value',color='Value')
            st.plotly_chart(f3)
        elif selected=='Weak foot with Value':
            f4=px.scatter(data_frame=df,x='Weak Foot',y='Value',color='Value')
            st.plotly_chart(f4)
        elif selected=='Nationality with value':
            f5=px.scatter(data_frame=df,x='Nationality',y='Value',color='Value')
            st.plotly_chart(f5)  
            
    
    elif st.checkbox('Correlation between numerical features'):
        correlation=px.imshow(df.select_dtypes('number').corr(),text_auto=True)
        st.plotly_chart(correlation) 

#---------------------------------------------------------------------------------------------------------------------
page_names_to_funcs = {
    "Main Page": mainpage,
    "About": aboutpage,
    "Data Analysis": Data_analysis,
    "Let's Predict": Prediction_Page
    
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
