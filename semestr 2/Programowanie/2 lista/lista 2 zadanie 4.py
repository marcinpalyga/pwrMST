from PyPDF2 import PdfFileWriter, PdfFileReader


def pdf(sciezka, numer_strony):
    pdf_czytnik = PdfFileReader(open(sciezka, "rb"), strict=False)
    pdf.zapis = PdfFileWriter()        
    strona_początkowa = 0
    ilosc_stron = pdf_czytnik.numPages
    if max(numer_strony) <= ilosc_stron:                   #warunek sprawdzający czy podane strony na których plik ma zostać rodzielony istnieją
        numer_strony.append(ilosc_stron)
        for i in range(len(numer_strony)):                   #podwójną pętlą rozdzielamy plik pdf na kilka plików zapisując je z nazwą zawierająca strony
            for k in range(strona_początkowa, numer_strony[i]):
                pdf.zapis.addPage(pdf_czytnik.getPage(k))
                nazwa = str(strona_początkowa) + '-' + str(numer_strony[i])
            with open("pages(%s).pdf" % nazwa, 'wb') as plik:
                pdf.zapis.write(plik)
                strona_początkowa = numer_strony[i]
    else:
        print("Podana strona nie istnieje")


pdf('sciezka', [1,3,5])