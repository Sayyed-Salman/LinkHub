from LinkHub import init_app, db

app = init_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
