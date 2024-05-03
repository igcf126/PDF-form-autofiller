% Ruta del archivo PDF original y destino
archivo_pdf_original = 'FTO model.pdf';
archivo_pdf_destino = 'filled_MatL.pdf';


% Datos para rellenar los campos del formulario
datos_para_rellenar = struct(...
    'Nombre/Marca', 'John Doe', ...
    'Presentación', 'john.doe@example.com', ...
    'Envase Primario', '123-456-7890');


% Leer el archivo PDF original
pdf_data = pdfrw_read(archivo_pdf_original);


% Iterar sobre las páginas del PDF
for pagina_num = 1:numel(pdf_data.pages)
    pagina = pdf_data.pages(pagina_num);
    
    % Obtener los campos de la página
    campos = pagina.Annots;
    
    if ~isempty(campos)
        % Iterar sobre los campos de la página
        for campo_num = 1:numel(campos)
            campo = campos(campo_num);
            campo_nombre = campo.T;
            
            % Verificar si el campo está en los datos para rellenar
            if isfield(datos_para_rellenar, campo_nombre)
                campo.V = pdf_string(datos_para_rellenar.(campo_nombre));
            end
        end
    end
end

% Guardar el PDF rellenado en un nuevo archivo
pdfrw_write(archivo_pdf_destino, pdf_data);
