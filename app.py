import streamlit as st

st.set_page_config(page_title="Single Use Plastics", layout="centered")

st.title("Single Use Plastics Awareness 🌍")

st.header("What are single use plastics?")
st.write(
    """
    Single use plastics are items designed to be used once before being thrown away.
    Examples include plastic bottles, straws, carrier bags and food packaging.
    """
)

st.header("Consequences")
st.write(
    """
    These plastics pollute oceans, harm wildlife, and break down into microplastics
    that enter the food chain and even drinking water.
    """
)

st.header("How to reduce them")
st.write(
    """
    - Use reusable bottles  
    - Carry fabric shopping bags  
    - Avoid plastic straws  
    - Recycle properly  
    """
)

st.header("Random Fact")

facts = [
    "A plastic bottle can take hundreds of years to decompose.",
    "Millions of tonnes of plastic enter the oceans every year.",
    "Microplastics have been found in human drinking water.",
    "Sea animals often mistake plastic for food."
]

if st.button("Show a fact"):
    st.success(facts[0])
