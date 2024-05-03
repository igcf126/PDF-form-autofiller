import pandas as pd

# Load data from Excel sheet
excel_file = 'AdoptPrueba.xlsx'
sheet_name = 'Datos para FTO'
data = pd.read_excel(excel_file, sheet_name)

# Create a dictionary to store data
product_dict = {}
inpdf = 'FTO model.pdf'
outpdf = 'filled_form3.pdf'


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
    # ... Add more fields as needed

    # Create a dictionary for the product
    product_data = {
        'NombreMarca)': field1_value, 
        'Presentaci\\363n)': field2_value, 
        'Envase Primario)': field3_value, 
        'Especificaciones del Envase Primario)': field4_value, 
        'Contenido del Envase Primario)': field5_value, 
        'Envase Secundario)': field6_value, 
        'Finalidad del Producto)': field7_value, 
        'Modo de uso)': field8_value, 
        'Advertencias y Precauciones)': field9_value, 
        'Per\\355odo de validez)': field10_value
        }
    
    # Add the product to the dictionary
    product_dict[solicitud] = product_data

# Call a function for each product
for solicitud, product_data in product_dict.items():
    # Call your function with the product data and name
    print(inpdf)
    output_pdf = f"{solicitud} FTO.pdf"
    
    print(output_pdf)
    print(product_data)
    print("\n")
    fillFTO(inpdf, output_pdf, product_data)
    
