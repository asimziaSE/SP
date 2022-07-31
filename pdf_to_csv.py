import tabula


df = tabula.read_pdf("C:/Users/asimz/OneDrive/Desktop/Data Engineering/GDP_table.pdf", pages='all')[0]

tabula.io.convert_into("C:/Users/asimz/OneDrive/Desktop/Data Engineering/GDP_table.pdf", "GDP_table.csv", output_format = "csv", pages='all')

print(df)
