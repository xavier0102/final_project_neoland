
En este proyecto intentaremos predecir en qué país un nuevo usuario hará su primera reserva.En nuestro caso, agruparemos solo en si un usuario reserva y no resserva, para hacer el ejercicio dicotomico, mas sensillo, ya qeu es nuestros primer proyecto independiente.

En este Ejercicio, se nos proporciona una lista de usuarios junto con sus datos demográficos, registros de sesiones web y algunas estadísticas resumidas. Se le pide que prediga de qué país será el primer destino de reserva de un nuevo usuario. Todos los usuarios en este conjunto de datos son de los EE. UU.

Hay 12 posibles resultados del país de destino: 'EE. UU.', 'FR', 'CA', 'GB', 'ES', 'IT', 'PT', 'NL', 'DE', 'AU', 'NDF' (no encontró ningún destino) y 'otro'. Tenga en cuenta que 'NDF' es diferente de 'otro' porque 'otro' significa que hubo una reserva, pero es para un país no incluido en la lista, mientras que 'NDF' significa que no hubo una reserva. 

Descripciones de archivo

train_users.csv  : el conjunto de formación de usuarios

test_users.csv : el conjunto de prueba de usuarios
id: id de usuario

date_account_created: la fecha de creación de la cuenta

timestamp_first_active: marca de tiempo de la primera 
actividad, tenga en cuenta que puede ser anterior a date_account_created o date_first_booking porque un usuario puede buscar antes de registrarse
date_first_booking: fecha de la primera reserva
género
años
método_registro
signup_flow: la página desde la que llegó un usuario para registrarse
idioma: preferencia de idioma internacional
affiliate_channel: qué tipo de marketing pagado
affiliate_provider: donde el marketing es, por ejemplo, google, craigslist, otro
first_affiliate_tracked: cuál es el primer marketing con el que el usuario interactuó antes de registrarse
signup_app
primer_dispositivo_tipo
primer_buscador
country_destination: esta es la variable objetivo que debe predecir
sessions.csv - registro de sesiones web para usuarios
user_id: se unirá con la columna 'id' en la tabla de usuarios
acción
tipo de acción
detalle_acción
tipo de dispositivo
segundos_elapsados
country.csv  : resumen de estadísticas de países de destino en este conjunto de datos y sus ubicaciones
age_gender_bkts.csv : estadísticas resumidas del grupo de edad, sexo y país de destino de los usuarios
sample_submission.csv : formato correcto para enviar sus predicciones
