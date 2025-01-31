

#---------------------------------------------------------#
# 				ENTORNO VIRTUAL
#---------------------------------------------------------#

#Verificar versión del Python
python3.11 --version

#Crear entorno virtual llamado venv
python -m venv venv

#Activar el entorno virtual
source venv/bin/activate

#---------------------------------------------------------#
# 				SUBIR LA CARPETA spam_server
#Contiene el modelo entrenado y el api de consulta
#---------------------------------------------------------#


#---------------------------------------------------------#
# 				INSTALAR LAS LIBRERIAS
#---------------------------------------------------------#
pip install flask
pip install torch
pip install transformers
pip install flask_cors

#---------------------------------------------------------#
# 				EJECUTAR EL SERVICE
#---------------------------------------------------------#

#En la carpeta spam_server y ejecutar el service
python service.py


