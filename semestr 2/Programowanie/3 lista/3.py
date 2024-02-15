from PyPDF2 import PdfFileMerger

def pdf(pliki: list, zapis):
    
    for plik in pliki:
        PdfFileMerger().append(plik) #w pętli dodajemy do siebie kazdy podany plik i zapisujemy w jednym
    PdfFileMerger().write(zapis)
    PdfFileMerger().close()

pdf(['sciezka1.pdf', 'sciezka2.pdf'], "zapis.pdf")