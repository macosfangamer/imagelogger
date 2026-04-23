from flask import Flask, request, send_file
from io import BytesIO
from datetime import datetime
import base64

app = Flask(__name__)

# PNG transparente 1x1
PIXEL = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR4nGNgYAAAAAMAASsJTYQAAAAASUVORK5CYII="
)

@app.get("/pixel")
def pixel():
    msg_id = request.args.get("msg_id", "unknown")
    event = {
        "msg_id": msg_id,
        "time": datetime.utcnow().isoformat() + "Z",
        "ua": request.headers.get("User-Agent"),
        # Evita almacenar IPs salvo que tengas base legal/consentimiento
        # "ip": request.remote_addr,
    }
    print(event)  # o guarda en DB

    return send_file(BytesIO(PIXEL), mimetype="image/png")

if __name__ == "__main__":
    app.run()
