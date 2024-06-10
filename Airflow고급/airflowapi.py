import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8080/api/v1/dags"

dags = requests.get(url, auth=HTTPBasicAuth("airflow", "airflow")).json()

paused_dags = [dag for dag in dags['dags'] if dag['is_paused'] is False]

print(paused_dags)