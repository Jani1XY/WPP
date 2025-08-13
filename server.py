from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from bs4 import BeautifulSoup
from datetime import date
import requests

wiki = "https://bluearchive.wiki/wiki/Main_Page"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}


class DivResponse(BaseModel):
    message: str
    div: str



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Mount static files (CSS, JS, images)
# The first "/static" is the URL path, the second "static" is the directory name
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse(name="index.html", request=request)


@app.get("/banners")
def getBanners():

    try:
        response = requests.get(wiki, headers=headers)

        # Check if the request was successful (status code 200)
        response.raise_for_status()

        # Print the status code and the content of the response
        print(f"Status Code: {response.status_code}")
        soup = BeautifulSoup(response.text, 'html.parser')
        bannersDiv = soup.select('div.tabs-content.tabs-content-2')
        print(f"div COUNT: {len(bannersDiv)}")
        print(bannersDiv)

        if not bannersDiv:
            print("Div with both classes not found.")
            raise HTTPException(404, "Banners not found")

        for i in bannersDiv:
            print("Div with classes found")
            print(i.prettify())
            print("-----------")
            

            return DivResponse(message="Successfully received banners", div=str(bannersDiv))


    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Something went wrong: {err}")


def getDayDiff(early:str, late:str):

    earlydates = early.split("/")
    latedates = late.split("/")

    e = date(date.today().year, int(earlydates[0]), int(earlydates[1]))
    l = date(date.today().year, int(earlydates[0]), int(latedates[1]))
    
    time_difference = l - e

    # The time_difference object contains the number of days, seconds, microseconds, etc.
    print(f"The difference between {e} and {l} is: {time_difference}")

    # To get the difference in days as a simple integer,
    # you can access the '.days' attribute of the timedelta object.
    day_difference = time_difference.days
    print(f"The difference in days is: {day_difference}")

    # You can also use the timedelta object to perform further calculations.
    # For example, to find a date 5 days in the future
    # from datetime import timedelta
    # future_date = date1 + timedelta(days=5)
    # print(f"5 days after {date1} will be: {future_date}")

    return time_difference


getDayDiff("2/2","2/12")