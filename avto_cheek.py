def avto_raqam_tekshir(raqam):
    natija=False
    if (
        type(raqam)==str and
        len(raqam)==8 and
        raqam[:2].isdigit() and
        raqam[2].isupper() and
        raqam[3:6].isdigit() and
        raqam[6:].isupper()
    ):
        natija=True
    return natija
print(avto_raqam_tekshir("60A123AA"))