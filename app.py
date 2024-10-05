import streamlit as st
import os 
import random
from PIL import Image 

qsns=os.listdir()

def show_next_question():
    st.session_state['next_qsn']=1

if 'disp_qsns' not in st.session_state:
    st.session_state['disp_qsns']=[]
if 'correct_answers' not in st.session_state:
    st.session_state['correct_answers']=0
    
if list(set(st.session_state['disp_qsns']))==list(set(qsns)):
    st.success('You have attempted all questions. No more questions left. Please reload the browser window to restart the test')
    st.success(f'Correct answers : {st.session_state['correct_answers']}') 
    st.stop()

if 'first_qsn' not in st.session_state:
    st.session_state['first_qsn']=1

if 'next_qsn' not in st.session_state:
    st.session_state['next_qsn']=0

if 'current_qsn' not in st.session_state:
    st.session_state['current_qsn']='A'

if st.session_state['first_qsn']==1:
    qsn=random.choice([j for j in qsns if j not in st.session_state['disp_qsns']])
    st.session_state['current_qsn']=qsn
    st.session_state['disp_qsns'].append(qsn)
    st.session_state['first_qsn']=0

if st.session_state['next_qsn']==1:
    qsn=random.choice([j for j in qsns if j not in st.session_state['disp_qsns']])
    st.session_state['current_qsn']=qsn
    st.session_state['disp_qsns'].append(qsn)
    st.session_state['next_qsn']=0



if 'py' not in st.session_state['current_qsn']:
    st.header('Question : ')
    image_file = Image.open(st.session_state['current_qsn'])
    image_file = image_file.convert('1')
    st.image(image_file)
    selected_answers=[]
    st.subheader('Choose an answer : ')
    if st.checkbox('A'):
        selected_answers.append('A')
    if st.checkbox('B'):
        selected_answers.append('B')
    if st.checkbox('C'):
        selected_answers.append('C')
    if st.checkbox('D'):
        selected_answers.append('D')
    if st.checkbox('E'):
        selected_answers.append('E')
    if st.button('Submit'):
        correct_answers=[i.strip() for i in st.session_state['current_qsn'].strip().split('_')[1].strip().split('.')[0]]
        if list(set(correct_answers))==list(set(selected_answers)):
            st.success('Your Answer is Correct')
            st.session_state['correct_answers']=st.session_state['correct_answers']+1
        else:
            st.error(f'Your selected answer is not correct. The correct answers are : {",".join(correct_answers)}')
    

    st.button('Next Question',on_click=show_next_question)

    
