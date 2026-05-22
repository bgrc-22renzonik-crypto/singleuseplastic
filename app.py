from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>

    <head>
        <title>Single Use Plastics</title>

        <style>

            body{
                font-family: Arial, sans-serif;
                background-color: lightblue;
                padding: 20px;
            }

            h1{
                color: darkblue;
            }

            section{
                background: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 10px;
            }

            button{
                padding: 10px;
                background-color: darkblue;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }

        </style>

    </head>

    <body>

        <h1>Single Use Plastics</h1>

        <section>

            <h2>What Are Single Use Plastics?</h2>

            <p>
                Single use plastics are products designed to be utilised once before disposal.
                Examples include plastic bottles, carrier bags and takeaway packaging.
            </p>

        </section>

        <section>

            <h2>The Consequences</h2>

            <p>
                Plastic pollution devastates ecosystems and threatens marine organisms.
                Numerous animals mistakenly consume plastic, causing injury and death.
            </p>

        </section>

        <section>

            <h2>How To Reduce Them</h2>

            <ul>
                <li>Use reusable water bottles.</li>
                <li>Carry fabric shopping bags.</li>
                <li>Avoid disposable straws.</li>
                <li>Recycle conscientiously.</li>
            </ul>

            <button onclick="showFact()">
                Click For A Fact
            </button>

            <p id="fact"></p>

        </section>

        <script>

            function showFact(){

                let facts = [

                    "A plastic bottle can take centuries to decompose.",

                    "Millions of tonnes of plastic enter oceans annually.",

                    "Microplastics have been discovered in drinking water.",

                    "Marine creatures frequently mistake plastic for food."

                ];

                let randomFact =
                    facts[Math.floor(Math.random() * facts.length)];

                document.getElementById("fact").innerHTML = randomFact;
            }

        </script>

    </body>

    </html>
    """

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
