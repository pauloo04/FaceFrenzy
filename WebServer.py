from flask import Flask, jsonify
import threading

class WebServer(threading.Thread):
    def __init__(self, exporter, port=5000):
        super().__init__(daemon=True)
        self.exporter = exporter
        self.port = port
        self.app = Flask(__name__)
        self._setup_routes()

    def _setup_routes(self):
        @self.app.route('/api/state', methods=['GET'])
        def get_state():
            return jsonify(self.exporter.export())

    def run(self):
        self.app.run(host='0.0.0.0', port=self.port, use_reloader=False)