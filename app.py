from flask import Flask
import os
import random

app = Flask(__name__)

facts = [
    "A plastic bottle can take hundreds of years to decompose.",
    "Millions of tonnes of plastic enter oceans every year.",
    "Microplastics have been discovered in drinking water.",
    "Marine animals often mistake plastic for food."
]

@app.route("/")
def home():

    random_fact = random.choice(facts)

    return f"""

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Single Use Plastics</title>

<style>

body{{
    font-family: Arial, sans-serif;
    background-color: #d9f5ff;
    margin: 0;
    padding: 20px;
}}

h1{{
    color: darkblue;
}}

section{{
    background-color: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
}}

</style>

</head>

<body>

<h1>Single Use Plastics</h1>

<section>

<h2>What Are Single Use Plastics?</h2>

<p>
Single use plastics are products designed to be utilised once before disposal.
Examples include bottles, straws, wrappers and carrier bags.
</p>

</section>

<section>

<h2>The Consequences</h2>

<p>
Plastic pollution devastates ecosystems and threatens marine wildlife.
Many animals accidentally consume plastic, causing severe injury.
</p>

</section>

<section>

<h2>How To Reduce Plastic Usage</h2>

<ul>
<li>Use reusable water bottles.</li>
<li>Carry fabric shopping bags.</li>
<li>Avoid disposable straws.</li>
<li>Recycle conscientiously.</li>
</ul>

</section>

<section>

<h2>Random Fact</h2>

<p>{random_fact}</p>

</section>

</body>
</html>

"""

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 10000))

    app.run(host="0.0.0.0", port=port)
