import pdftotext

# Load your PDF
with open("Get_Started_With_Smallpdf.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)

print("\n\n".join(pdf))

# Save all text to a txt file.
with open('output.txt', 'w') as f:
    f.write("\n\n".join(pdf)) 

content = ''
with open('new.txt', 'r') as f:
    content = f.read() 

print(">" * 10)
print('After reading..')
print(">" * 10)
print(content)