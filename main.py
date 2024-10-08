from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
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

    # Tworzenie footera -  278 oznacza ilość mm od napisu w headerze
    # pdf.ln(265)
    # pdf.set_font(family="Times", style='I', size=8)
    # pdf.set_text_color(0, 0, 0)
    # pdf.cell(w=0, h=10, txt=row["Topic"], align='R')

    # dodawanie okreslonej ilości stron z pliku csv
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        # set of the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style='I', size=8)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=10, txt=row["Topic"], align='R')

pdf.output('output.pdf')
