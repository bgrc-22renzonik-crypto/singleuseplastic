from flask import Flask
import random

app = Flask(__name__)

facts = [
    "A plastic bottle can take centuries to decompose.",
    "Millions of tonnes of plastic enter oceans annually.",
    "Microplastics have been discovered in drinking water.",
    "Marine wildlife frequently mistakes plastic for food."
]

@app.route("/")
def home():

    fact = random.choice(facts)

    return f"""

<!DOCTYPE html>
<html>

<head>

<title>Single Use Plastics</title>

<style>

body {{
    font-family: Arial, sans-serif;
    background-color: #d9f5ff;
    padding: 20px;
}}

section {{
    background-color: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 10px;
}}

h1 {{
    color: darkblue;
}}

</style>

</head>

<body>

<h1>Single Use Plastics</h1>

<section>

<h2>What Are Single Use Plastics?</h2>

<p>
Single use plastics are products designed to be utilised once before disposal.
Examples include bottles, wrappers, straws and carrier bags.
</p>

</section>

<section>

<h2>The Consequences</h2>

<p>
Plastic pollution devastates ecosystems and threatens biodiversity.
Marine organisms frequently consume plastic accidentally.
</p>

</section>

<section>

<h2>How To Reduce Them</h2>

<ul>
<li>Use reusable bottles.</li>
<li>Carry fabric shopping bags.</li>
<li>Avoid disposable straws.</li>
<li>Recycle conscientiously.</li>
</ul>

</section>

<section>

<h2>Random Fact</h2>

<p>{fact}</p>

</section>

</body>

</html>

"""

if __name__ == "__main__":
    app.run(port=0)
