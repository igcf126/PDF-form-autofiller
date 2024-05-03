## VERSIÓN 100 % FUNCIONAL
# TENER APLICACIONES DE LECTURA PDF CERRADAS, ESPECIALMENTE ADOBE


import pandas as pd
from pdfrw import PdfReader, PdfWriter, PdfDict, PdfObject, objects
import xml.sax.saxutils
import unicodedata

# Load data from Excel sheet
excel_file = 'AdoptPrueba.xlsx'
sheet_name = 'Datos para FTO definitivo'
data = pd.read_excel(excel_file, sheet_name)

# Create a dictionary to store data
product_dict = {}
inpdf = 'ADOPT FTO model.pdf'
outpdf = 'filled_form3.pdf'

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
                    print(remove_accents(field_name))
                    #print(field_data)
                    #print(field_name3)
                    # print(i)
                    
                    

                    if remove_accents(field_name) in field_data:# or (i in [1, 8, 10, 11, 12, 13, 14, 15, 16, 18, 17]):  # Check if the field is in your provided data                 
                        
                        annot.update(PdfDict(V=field_data[remove_accents(field_name)]))
                        j+j+1
                        # annot.update(PdfDict(RV=showin))
                        print(i)
                        # print(PdfDict(RV=showin))
                        ##pdf.Root.AcroForm.update( PdfDict(NeedAppearances=PdfObject('true')))
                    
                    # print('\n')

        pdf.Root.AcroForm.update( PdfDict(NeedAppearances=PdfObject('true')))
    PdfWriter().write(output_pdf, pdf)


# inpdf = 'FTO model.pdf'
# outpdf = 'filled_form3.pdf'
# f_data = {'NombreMarca)': 'El pepe', 'Presentaci\\363n)': 'john.doe@example.com', 'Envase Primario)': 'john.doe@example.com', 'Especificaciones del Envase Primario)': 'john.doe@example.com', 'Contenido del Envase Primario)': 'john.doe@example.com', 'Envase Secundario)': 'john.doe@example.com', 'Finalidad del Producto)': 'john.doe@example.com', 'Modo de uso)': 'john.doe@example.com', 'Advertencias y Precauciones)': 'john.doe@example.com', 'Per\\355odo de validez)': 'john.doe@example.com'}
# # Update dictionary values to include escape codes for accents
# # field_data = {key: escape_accents(value) for key, value in field_data.items()}

# fillFTO(inpdf, outpdf, f_data)

# #field_data = ['El pepe', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com', 'john.doe@example.com']



# Iterate through rows in the DataFrame
for index, row in data.iterrows():
    # Extract product information from the DataFrame
    product_name = row['Num']
    solicitud = row['Solicitud']

    field1_value = row['NombreCVL']
    field2_value = row['Presentaciones']
    field3_value = row['EnvasePrimario']
    field4_value = row['Especificaciones']
    field5_value = row['Contenido']
    field6_value = row['EnvaseSecundario']
    field7_value = row['Finalidad']
    field8_value = row['ModoDeUso']
    field9_value = row['Advertencias']
    field10_value = row['Validez']
    #field11_value = row['Conserva']
    # ... Add more fields as needed

    # Create a dictionary for the product
    product_data = {
        # 'NombreMarca)': field1_value, 
        # 'Presentaci\\363n)': field2_value, 
        # 'Envase Primario)': field3_value, 
        # 'Especificaciones del Envase Primario)': field4_value, 
        # 'Contenido del Envase Primario)': field5_value, 
        # 'Envase Secundario)': field6_value, 
        # 'Finalidad del Producto)': field7_value, 
        # 'Modo de uso)': field8_value, 
        # 'Advertencias y Precauciones)': field9_value, 
        # 'Per\\355odo de validez)': field10_value,
        # 'Condiciones de conservaci\\363n)': field11_value         
        
        'NombreMarca)': field1_value, 
        'Presentacion)': field2_value, 
        'Envase Primario)': field3_value, 
        'Especificaciones del Envase Primario)': field4_value, 
        'Contenido del Envase Primario)': field5_value, 
        'Envase Secundario)': field6_value, 
        'Finalidad del Producto)': field7_value, 
        'Modo de uso)': field8_value, 
        'Advertencias y Precauciones)': field9_value, 
        'Periodo de validez)': field10_value,
        #'Condiciones de conservacion)': field11_value         
        
        # 'NombreMarca)': field1_value, 
        # 'Presentaci�n)': field2_value, 
        # 'Envase Primario)': field3_value, 
        # 'Especificaciones del Envase Primario)': field4_value, 
        # 'Contenido del Envase Primario)': field5_value, 
        # 'Envase Secundario)': field6_value, 
        # 'Finalidad del Producto)': field7_value, 
        # 'Modo de uso)': field8_value, 
        # 'Advertencias y Precauciones)': field9_value, 
        # 'Per�5odo de validez)': field10_value,
        # 'Condiciones de conservaci�n)': field11_value         
        }
    
    # Add the product to the dictionary
    product_dict[solicitud] = product_data

# Call a function for each product
for solicitud, product_data in product_dict.items():
    # Call your function with the product data and name
    #print(inpdf)
    output_pdf = f"./ADOPT_FTOs/{solicitud} FTO.pdf"
    
    #print(output_pdf)
    #print(product_data)
    #print("\n")
    fillFTO(inpdf, output_pdf, product_data)
    
