"""App start point"""

from site_package import create_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
