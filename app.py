import streamlit as st

st.title("Carbon Emissions Prediction")

with st.form("carbon_emissions_form"):
    col1, col2 = st.columns(2)

    st.selectbox("Make", ["ACURA", "ALFA ROMEO","ASTON MARTIN","AUDI","BENTLEY","BMW","BUICK",
 "CADILLAC","CHEVROLET","CHRYSLER","DODGE","FIAT","FORD","GMC","HONDA",
 "HYUNDAI","INFINITI","JAGUAR","JEEP","KIA","LAMBORGHINI","LAND ROVER",
 "LEXUS","LINCOLN","MASERATI","MAZDA","MERCEDES-BENZ","MINI","MITSUBISHI",
 "NISSAN","PORSCHE","RAM","ROLLS-ROYCE","SCION","SMART","SRT","SUBARU",
 "TOYOTA","VOLKSWAGEN","VOLVO","GENESIS","BUGATTI"])
    
    submitted = st.form_submit_button("Submit")