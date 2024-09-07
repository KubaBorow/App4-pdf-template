from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit="mm", format="A4")
# df - data frame
df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style='B', size=24)
    # set color text paleta RGB
    pdf.set_text_color(0, 128, 255)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    # poczaątek linii x1,y1 koniec linii x2,y2
    # x1 odleglosc od lewej krawędzi y od lewej gornej krawędzi
    pdf.line(10, 21, 200, 21)

pdf.output('output.pdf')
