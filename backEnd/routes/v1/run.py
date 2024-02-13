from . import create_app
from os import getenv

if __name__ == "__main__":
    app = create_app()
    app.run(
        host=getenv('CN_HOST', '0.0.0.0'),
        port=int(getenv('CN_PORT', 5000)),
        debug=True,
 )

