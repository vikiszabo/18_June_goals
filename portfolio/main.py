from flask import Flask, render_template, url_for

app = Flask('weiliya_advanced_module_profile', static_url_path='/static')


@app.route('/')
def index():
    return render_template('main.html',  mimetype="text/html")


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()