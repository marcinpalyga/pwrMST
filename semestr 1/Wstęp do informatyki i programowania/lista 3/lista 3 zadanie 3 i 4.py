def rot13(text):
    result = ""                #zmienna w której przechowujemy przetworzony tekst

    for i in text:
        c = ord(i)

        if c >= ord('a') and c <= ord('z'):      #pętla dla małych liter która w zależności od miejsca litery w alfabecie zmienia ją o +13 lub -13
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):   #taka sama pętla dla dużych liter
            if c > ord('M'):
                c -= 13
            else:
                c += 13

        result += chr(c)

    return result

print(rot13("""N PBQR BS RGUVPNY ORUNIVBE SBE CNGVRAGF:
1. QB ABG RKCRPG LBHE QBPGBE GB FUNER LBHE QVFPBZSBEG. Vaibyirzrag
jvgu gur cngvrag’f fhssrevat zvtug pnhfr uvz gb ybfr inyhnoyr
fpvragvsvp bowrpgvivgl.
2. OR PURRESHY NG NYY GVZRF. Lbhe qbpgbe yrnqf n ohfl naq gelvat
yvsr naq erdhverf nyy gur tragyrarff naq ernffhenapr ur pna trg
.
3. GEL GB FHSSRE SEBZ GUR QVFRNFR SBE JUVPU LBH NER ORVAT GERNGRQ.
Erzrzore gung lbhe qbpgbe unf n cebsrffvbany erchgngvba gb
hcubyq."""))
print(rot13(rot13("""N PBQR BS RGUVPNY ORUNIVBE SBE CNGVRAGF:
1. QB ABG RKCRPG LBHE QBPGBE GB FUNER LBHE QVFPBZSBEG. Vaibyirzrag
jvgu gur cngvrag’f fhssrevat zvtug pnhfr uvz gb ybfr inyhnoyr
fpvragvsvp bowrpgvivgl.
2. OR PURRESHY NG NYY GVZRF. Lbhe qbpgbe yrnqf n ohfl naq gelvat
yvsr naq erdhverf nyy gur tragyrarff naq ernffhenapr ur pna trg
.
3. GEL GB FHSSRE SEBZ GUR QVFRNFR SBE JUVPU LBH NER ORVAT GERNGRQ.
Erzrzore gung lbhe qbpgbe unf n cebsrffvbany erchgngvba gb
hcubyq.""")))
