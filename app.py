from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Single Use Plastics</title>

        <style>
            body{
                font-family: Arial;
                background-color: lightblue;
                padding: 20px;
            }

            h1{
                color: darkblue;
            }

            section{
                background: white;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
            }

            button{
                padding: 10px;
                background: darkblue;
                color: white;
                border: none;
                cursor: pointer;
            }
        </style>

    </head>

    <body>

        <h1>Single Use Plastics</h1>

        <section>
            <h2>What Are Single Use Plastics?</h2>

            <p>
                Single use plastics are items designed to be utilised once before disposal.
                These include plastic bottles, carrier bags and straws.
            </p>
        </section>

        <section>
            <h2>The Consequences</h2>

            <p>
                Plastic pollution devastates ecosystems and harms marine organisms.
                Many creatures consume plastic accidentally, causing injury and death.
            </p>
        </section>

        <section>
            <h2>How To Reduce Them</h2>

            <ul>
                <li>Use reusable bottles</li>
                <li>Recycle properly</li>
                <li>Avoid plastic straws</li>
                <li>Use fabric shopping bags</li>
            </ul>

            <button onclick="showMessage()">
                Click Me
            </button>

            <p id="message"></p>
        </section>

        <script>
            function showMessage(){
                document.getElementById("message").innerHTML =
                "Small decisions can create substantial environmental improvement.";
            }
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
