import streamlit as st
from facrotial import fact 

def main():
  st.title('Factorial Calculator')
  number = st.number_input('Enter a number: ',
                           min_value = 0,
                           max_value = 900)
  
  if st.button('Calculate'):
    result = fact(number)
    st.write(f'The factorial is {number} is {result}')
if __name__ == "__main__":
  main()