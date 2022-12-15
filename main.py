from src.app import create_app
#bruh
# Shut down the scheduler when exiting the app

if __name__ == '__main__':
    napp = create_app()
    napp.run(debug=True, port=5000)