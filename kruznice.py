import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titulek aplikace
st.title("Bodový graf kružnice")

# Vstupní parametry
st.sidebar.header("Parametry")
x0 = st.sidebar.number_input("Souřadnice středu X", value=0)
y0 = st.sidebar.number_input("Souřadnice středu Y", value=0)
r = st.sidebar.number_input("Poloměr kružnice (m)", value=1, min_value=1)
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
ax.scatter(x, y, c=barva, s=velikost, label="Body", zorder=5)

# stejné měřítko os
ax.set_aspect("equal", adjustable="box")

# popisky
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")

# tenká šedá mřížka
ax.grid(True, color="lightgray", linewidth=0.5, zorder=0)

# černé osy uprostřed kružnice
ax.axhline(y=y0, color="black", linewidth=0.8, zorder=1)
ax.axvline(x=x0, color="black", linewidth=0.8, zorder=1)

# napsání souřadnic u středu kružnice, odsazeno od os
offset = 0.02 * r  # odsazení 2 % poloměru
ax.text(x0 + offset, y0 + offset, f"[{x0}, {y0}]", color="black",
        fontsize=10, ha="left", va="bottom",
        bbox=dict(facecolor="white", alpha=0.5, edgecolor="none", pad=1))

ax.legend()
st.pyplot(fig)

# Informace o autorovi a technologiích
st.sidebar.markdown("### Info")
st.sidebar.write("Autor: Ondřej Brosch")
st.sidebar.write("Kontakt: 277700@vutbr.cz")
st.sidebar.write("Technologie: Python, Streamlit, Matplotlib, NumPy")

# pevně nastavené údaje o autorovi
autor = "Ondřej Brosch"
kontakt = "277700@vutbr.cz"
technologie = "Python, Streamlit, Matplotlib, NumPy"

import io
from fpdf import FPDF
import tempfile

# uložíme graf do PNG
tmpfile = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
fig.savefig(tmpfile.name, dpi=150, bbox_inches='tight')

# vytvoření PDF do BytesIO
pdf_bytes = io.BytesIO()
pdf = FPDF()
pdf.add_page()
pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
pdf.set_font("DejaVu", size=12)
pdf.image(tmpfile.name, x=10, y=20, w=100)
pdf.set_xy(120, 20)
text = (
    f"Body na kruznici - parametry\n\n"
    f"Střed: ({x0}, {y0})\n"
    f"Poloměr: {r} m\n"
    f"Počet bodů: {n}\n"
    f"Velikost bodů: {velikost}\n\n"
    f"Autor: Ondřej Brosch\n"
    f"Kontakt: 277700@vutbr.cz\n"
    f"Použité technologie: Python, Streamlit, Matplotlib, NumPy"
)
pdf.multi_cell(0, 8, text, align="L")
pdf.output(pdf_bytes)
pdf_bytes.seek(0)

# rovnou nabídne ke stažení
st.download_button(
    label="Stáhnout PDF",
    data=pdf_bytes,
    file_name="kruznice.pdf",
    mime="application/pdf"
)
