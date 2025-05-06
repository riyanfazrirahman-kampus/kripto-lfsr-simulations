import streamlit as st
import pandas as pd
from lfsr_functions import validate_name, char_to_ascii, decimal_to_binary, lfsr_simulation

def main():
    st.title("LFSR Simulation")

    # Input form
    with st.form(key="lfsr_form"):
        name = st.text_input("Enter your name:", value="Riyan")
        bits = st.selectbox("Select bit length:", [4, 5, 6, 7, 8], index=3)
        steps = st.number_input("Number of LFSR steps:", min_value=1, max_value=100, value=14, step=1)
        submit_button = st.form_submit_button(label="Run Simulation")

    if submit_button:
        try:
            # Get first character
            first_char = validate_name(name)
            
            # Convert to ASCII
            ascii_value = char_to_ascii(first_char)
            
            # Convert ASCII to binary
            initial_state = decimal_to_binary(ascii_value, bits)
            
            # Run LFSR simulation
            output_sequence, history = lfsr_simulation(initial_state, steps)

            # Create Pandas DataFrame
            df = pd.DataFrame(history)
            
            # Reorder columns to move Output to the far right
            df = df[['Iteration', 'State', 'Feedback', 'New State', 'Output']]
            df.set_index('Iteration', inplace=True)

            # Display results
            st.write(f"**Name:** {name}")
            st.write(f"**First Character:** {first_char}")
            st.write(f"**ASCII Value:** {ascii_value}")
            st.write(f"**Initial State (Binary, {bits}-bit):** {initial_state}")
            st.write("**LFSR Process Table:**")
            st.dataframe(df, use_container_width=True)
            st.write(f"**Random Output Sequence:** {''.join(output_sequence)}")

        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()