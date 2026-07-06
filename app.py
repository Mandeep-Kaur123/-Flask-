from flask import Flask, render_template
app= Flask(__name__)

print(__name__)
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/learn_more")
def learn_more():
    return render_template("learn_more.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/minor_projects")
def minor_projects():
    return render_template("minor_projects.html")


@app.route("/major_projects")
def major_projects():
    return render_template("major_projects.html")

@app.route("/webscrapping")
def webscrapping():
    return render_template("webscrapping.html")

#@app.route("/static_scrapping")
#def static_scrapping():
#    return render_template("static_scrapping.html")


@app.route("/dynamic_scrapping")
def dynamic_scrapping():
    return render_template("dynamic_scrapping.html")


@app.route("/api_scrapping")
def api_scrapping():
    return render_template("api_scrapping.html")

@app.route('/web_scraping')
def web_scraping():
    return render_template('web_scraping.html')

from Scraper.static_scraper import scrape_quotes
from Scraper.dynamic_imdb_films import scrape_movies

@app.route("/static_scrapping")
def static_scrapping():

    quotes = scrape_quotes()

    return render_template(
        "static_scrapping.html",
        quotes=quotes
    )
    
@app.route('/api_projects')
def api_projects():
    return render_template('api_projects.html')

@app.route('/api1')
def api1():
    return render_template('api1.html')

@app.route('/api2')
def api2():
    return render_template('api2.html')

@app.route('/api3')
def api3():
    return render_template('api3.html')

@app.route('/api4')
def api4():
    return render_template('api4.html')

@app.route('/api5')
def api5():
    return render_template('api5.html')

@app.route('/dynamic_projects')
def dynamic_projects():
    return render_template('dynamic_projects.html')

@app.route('/states_capital')
def states_capital():
    return render_template('states_capital.html')


@app.route('/dynamic_quotes')
def dynamic_quotes():
    return render_template('dynamic_quotes.html')


@app.route('/imdb_films')
def imdb_films():

    movies = scrape_movies()

    return render_template(
        'imdb_films.html',
        movies=movies
    )


@app.route('/imdb_cartoons')
def imdb_cartoons():
    return render_template('imdb_cartoons.html')


@app.route('/dynamic_books')
def dynamic_books():
    return render_template('dynamic_books.html')


if (__name__=="__main__"):
    app.run(debug=True)