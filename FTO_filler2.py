
from pdfrw import PdfReader, PdfWriter, PdfDict, PdfObject, objects
import xml.sax.saxutils
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def escape_accents(text):
    return ''.join(c if unicodedata.category(c) not in ['Mn', 'Me'] else f'\\{ord(c)}' for c in text)


def fillFTO(input_pdf, output_pdf, field_data):
    pdf = PdfReader(input_pdf)
    # print(pdf.keys())
    # print(pdf.Info)
    #print(pdf.Root.keys())
    # print('PDF has {} pages'.format(len(pdf.pages)))
    # print('\n')

    #print(field_data[2])

    for page in pdf.pages: 
        i = 0 
        j=0
        # for key in field_data.keys():
        #     print(key)
        if '/Annots' in page:
            for annot in page['/Annots']:
                i = i+1
                if '/T' in annot and '/V' in annot:
                    field_name = annot['/T'][1:]

                    field_name2 = annot['/V'][1:]
                    field_name3 = annot['/RV']
                    print(field_name)
                    # print(field_name2)
                    #print(field_name3)
                    print(i)
                    
                    

                    if field_name in field_data:# or (i in [1, 8, 10, 11, 12, 13, 14, 15, 16, 18]):  # Check if the field is in your provided data                 
                        
                        annot.update(PdfDict(V=field_data[field_name]))
                        j+j+1
                        # annot.update(PdfDict(RV=showin))
                        print(i)
                        # print(PdfDict(RV=showin))
                        ##pdf.Root.AcroForm.update( PdfDict(NeedAppearances=PdfObject('true')))
                    
                    print('\n')

        pdf.Root.AcroForm.update( PdfDict(NeedAppearances=PdfObject('true')))
    PdfWriter().write(output_pdf, pdf)


inpdf = 'FTO model.pdf'
outpdf = 'filled_form3.pdf'
f_data = {'NombreMarca)': 'El pepe', 'Presentaci\\363n)': 'john.doe@example.com', 'Envase Primario)': 'john.doe@example.com', 'Especificaciones del Envase Primario)': 'john.doe@example.com', 'Contenido del Envase Primario)': 'john.doe@example.com', 'Envase Secundario)': 'john.doe@example.com', 'Finalidad del Producto)': 'john.doe@example.com', 'Modo de uso)': 'john.doe@example.com', 'Advertencias y Precauciones)': 'john.doe@example.com', 'Per\\355odo de validez)': 'john.doe@example.com'}
# Update dictionary values to include escape codes for accents
# field_data = {key: escape_accents(value) for key, value in field_data.items()}

fillFTO(inpdf, outpdf, f_data)

#field_data = ['El pepe', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com']
