from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def scrape_movies():

    url = "https://www.imdb.com/chart/top/"

    driver = webdriver.Chrome()

    driver.get(url)

    time.sleep(5)

    titles = driver.find_elements(By.CSS_SELECTOR, "h4.ipc-title__text")
    ratings = driver.find_elements(By.CSS_SELECTOR, "span.ipc-rating-star--rating")

    movies = []

    for title, rating in zip(titles, ratings):

        movies.append({
            "title": title.text,
            "rating": rating.text
        })

    driver.quit()
    print("Movies fetched:", len(movies))

    return movies