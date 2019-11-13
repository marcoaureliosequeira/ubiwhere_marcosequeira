# Instalação

- Postgres
    - brew services start postgresql
    - createdb database_name
    - psql database_name
    - Configurar setings.py
    - django-admin startapp ubiwhere_app
    - python manage.py createsuperuser
        - Marcosequeira
        - Ubiwhere12345
    - pip install djangorestframework
    - Registar ubiwhere_app no ficheiro settings.py
    - Registar rest_framework no ficheiro settings.py
    - Criar a classe do modelo
    - python manage.py makemigrations
    - python manage.py migrate
    
    Nota: Desenvolvi o exercício em Mac e associei o utilizador do computador ao Postgres, contudo, depois criei um outro:
    	- su - (utilizador)
	- createuser --interactive --pwprompt
	- username: marcosequeira
	- password: 123456
	- Shall the new role be a superuser? y
    
- Silk
    - pip install django-silk
    - settings.py
    - MIDDLEWARE = […
   		 'silk.middleware.SilkyMiddleware',
	     …]
    - INSTALLED_APPS = [ …
		‘silk’
	     …]
    - 
        - 

# Endpoints
    - Criar registo
        - POST
        - http://localhost:8000/sensorData/create/
            - Form data
                - description (descrição do registo)
                - geo_location (localização do registo)
                - created_by (quem está a inserir o registo)
                - state (0-Não validado; 1- Validado; 2- Resolvido)
                - category (CONSTRUCTION, SPECIAL_EVENT, INCIDENT, WEATHER_CONDITION, ROAD_CONDITION) 
                - created_at (data em que o registo está a ser criado)
                - updated_at (data em que o registo é alterado)

    - Listar por autor
        - GET
        - http://localhost:8000/sensorData/list/author/{nome do autor}/

    - Listar por localização
        - GET
        - http://localhost:8000/sensorData/list/location/{valor da localização}/

    - Listar por categoria
        - GET
        - http://localhost:8000/sensorData/list/category/{valor da categoria}/

- Validar
    - PUT
		- http://localhost:8000/sensorData/validate/{id do registo}/


# Modelo de dados
Dado o exercício tentei simplificar ao máximo e daí resumi tudo a uma única entidade - DataFromSensor. Contudo seria possível separar os estados, o autor (caso estivesse associado a um utilizador na plataforma) e as categorias em entidades separadas e fazer o respetivo relacionamento à entidade DataFromSensor.

- DataFromSensor - tabela “data_from_sensors”
    - description: varchar (255)
    - geo_location: varchar (255)
    - created_by: text
    - category: varchar (255)
    - created_at: datetime
    - updated_at: datetime
