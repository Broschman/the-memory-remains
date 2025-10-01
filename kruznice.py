import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titulek aplikace
st.title("Body na kružnici")

# Vstupní parametry
st.sidebar.header("Parametry")
x0 = st.sidebar.number_input("Souřadnice středu X", value=0.0)
y0 = st.sidebar.number_input("Souřadnice středu Y", value=0.0)
r = st.sidebar.number_input("Poloměr kružnice (m)", value=1.0, min_value=0.1)
n = st.sidebar.slider("Počet bodů", min_value=3, max_value=500, value=20)
barva = st.sidebar.color_picker("Barva bodů", "#ff0000")
velikost = st.sidebar.slider("Velikost bodů", min_value=1, max_value=50, value=20)

# Výpočet bodů
angles = np.linspace(0, 2*np.pi, n, endpoint=False)
x = x0 + r * np.cos(angles)
y = y0 + r * np.sin(angles)

# Vykreslení grafu
fig, ax = plt.subplots()

# body
ax.scatter(x, y, c=barva, s=velikost, label="Body")

# stejné měřítko os
ax.set_aspect("equal", adjustable="box")

# popisky
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

# tenká šedá mřížka
ax.grid(True, color="lightgray", linewidth=0.5)

# osy x=0 a y=0 černé tenké
ax.axhline(0, color="black", linewidth=0.8)
ax.axvline(0, color="black", linewidth=0.8)

ax.legend()
st.pyplot(fig)


# Informace o autorovi a technologiích
st.sidebar.markdown("### Info")
st.sidebar.write("Autor: [Ondřej Brosch]")
st.sidebar.write("Kontakt: 277700@vutbr.cz")
st.sidebar.write("Technologie: Python, Streamlit, Matplotlib, NumPy")

# Export do PDF (zatím jen jednoduchý text)
from fpdf import FPDF

if st.button("Uložit parametry do PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Body na kružnici", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Střed: ({x0}, {y0})", ln=True)
    pdf.cell(200, 10, txt=f"Poloměr: {r} m", ln=True)
    pdf.cell(200, 10, txt=f"Počet bodů: {n}", ln=True)
    pdf.cell(200, 10, txt=f"Barva: {barva}", ln=True)
    pdf.cell(200, 10, txt="Autor: Tvoje jméno, kontakt", ln=True)
    pdf.output("parametry.pdf")
    st.success("PDF bylo vygenerováno (parametry.pdf)")
