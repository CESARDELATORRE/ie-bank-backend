import os
from iebank_api import app

# OLD/Original code (Uses port 5000 by default)
# if __name__ == '__main__':
#     app.run(debug=True)

# Get the port from the PORT environment variable
if __name__ == '__main__':
    port = int(os.environ.get('FLASK_RUN_PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)