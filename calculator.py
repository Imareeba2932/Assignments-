import streamlit as st
import math

st.image("assets/IMG (1).jpg", use_column_width=True)
st.write("---------------")

def math_operations(n1,n2,operations):
    if operations=='Add':
        return n1+n2
    elif operations=='Subtract':
        return n1-n2
    elif operations=='Multiply':
        return n1*n2
    elif operations=='Division':
        return n1/n2

def scientific_math_operations(n1,operations):
    if operations=='Log':
        return math.log10(n1)
    elif operations=='Sin':
        return math.sin(n1)
    elif operations=='Cosine':
        return math.cos(n1)
    elif operations=='Tangent':
        return math.tan(n1)

def main():
    
    if operations in ['Add','Subtract','Mutipliply','Division']:
        n1=st.number_input("Enter First Value")
        n2=st.number_input("Enter Second Value")
        result=math_operations(n1,n2,operations) 
        st.success(f'result={result}')
    elif operations in ['Log','Sin','Cosine','Tangent']:
        n1=st.number_input("Enter the Value")
        result=scientific_math_operations(n1,operations)
        st.success(f'result={result}')

operations=st.radio("Select an operation",['Add','Subtract','Multiply','Division','Log','Sin','Cosine','Tangent'])


if __name__=='__main__':
    main()

 