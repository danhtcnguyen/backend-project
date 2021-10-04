0. have django installed
1. navigate to project directory
2. start app with 'python manage.py runserver'
3. server now running on 'http://127.0.0.1:8000'
4. run 'python manage.py migrate'

Endpoints:

return all factory data: 'get-all-factories/'

return a specific factory: 'get-all-factories/<int:id>/

return a specifc sprocket: 'get-sprocket/<int:id>/'

create a new sprocket: 'create-sprocket/<int:teeth>/<int:pitch_diameter>/<int:outside_diameter>/<int:pitch>/'

update an existing sprocket: 'update-sprocket/<int:id>/<int:teeth>/<int:pitch_diameter>/<int:outside_diameter>/<int:pitch>/'
