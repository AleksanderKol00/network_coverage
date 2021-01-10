# Network coverage project

## Getting Started
### Settings
To run project required is to add json with settings (template in `settings_template.json`) and add file path to
env variable `NETWORK_COVERAGE_SETTINGS`

### Installing
1. Install Python3.8 
2. Install packages by pip
```
 pip install -r requirements.txt
```

### Run dev server
```
python3 manage.py runserver
```

### Running api tests
```angular2html
 python3 manage.py test api.tests
```