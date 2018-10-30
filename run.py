from app import create_app 

app = create_app("config_name")

if __name__ == "__main__":
    app.run()