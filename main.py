from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pandas as pd
import database as db

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

DF = pd.read_sql(f'SELECT * FROM stats', db.cnx)
D = DF.to_dict(orient="records")
templates = Jinja2Templates(directory="static")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("root.html", {"request": request})


@app.get("/all")
def get_all():
    return DF.to_dict(orient="records")


@app.get("/division/{division}")
def search_by_division(division):
    selected_division = pd.DataFrame(DF.loc[DF['division'] == division.upper()])
    return selected_division.to_dict(orient="records")


@app.get("/organization/{organization}")
def search_by_organization(organization):
    selected_organization = pd.DataFrame(DF.loc[DF['organization'] == organization.upper()])
    return selected_organization.to_dict(orient="records")


@app.get("/nationality/{nationality}")
def search_by_nationality(nationality):
    selected_nationality = pd.DataFrame(DF.loc[DF['nationality'] == nationality.upper()])
    return selected_nationality.to_dict(orient="records")


@app.get("/name/{name}")
def search_by_name(name):
    selected_name = pd.DataFrame(DF.loc[DF['name'] == name.upper()])
    return selected_name.to_dict(orient="records")

