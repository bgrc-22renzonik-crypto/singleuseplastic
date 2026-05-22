from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Single Use Plastics Awareness</title>

<style>

body{
    font-family: Arial, sans-serif;
    background-color: #d9f5ff;
    margin: 0;
    padding: 0;
    color: #222;
}

header{
    background-color: #0088aa;
    color: white;
    text-align: center;
    padding: 30px;
}

section{
    background-color: white;
    margin: 20px;
    padding: 20px;
    border-radius: 10px;
}

h2{
    color: #006d86;
}

button{
    background-color: #0088aa;
    color: white;
    border: none;
    padding: 12px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover{
    background-color: #005f73;
}

#fact{
    margin-top: 15px;
    font-weight: bold;
    color: darkred;
}

footer{
    background-color: #0088aa;
    color: white;
    text-align: center;
    padding: 15px;
    margin-top: 20px;
}

</style>

</head>

<body>

<header>

<h1>Single Use Plastics</h1>

<p>
Raising awareness about environmental preservation
</p>

</header>

<section>

<h2>What Are Single Use Plastics?</h2>

<p>
Single use plastics are products manufactured to be utilised once before disposal.
Examples include plastic bottles, carrier bags, takeaway containers and straws.
</p>

<p>
These materials persist within the environment for centuries and contribute
to substantial pollution across ecosystems.
</p>

</section>

<section>

<h2>The Consequences</h2>

<p>
Plastic pollution devastates marine environments and threatens biodiversity.
Many animals mistakenly consume plastic, causing severe injury and death.
</p>

<button onclick="showFact()">
Click For A Fact
</button>

<p id="fact"></p>

</section>

<section>

<h2>How To Reduce Plastic Usage</h2>

<ul>
<li>Use reusable bottles.</li>
<li>Carry fabric shopping bags.</li>
<li>Avoid disposable cutlery and straws.</li>
<li>Recycle conscientiously.</li>
<li>Choose products with minimal packaging.</li>
</ul>

</section>

<footer>

<p>
Protect oceans • Preserve wildlife 🌍
</p>

</footer>

<script>

function showFact(){

    let facts = [

        "A plastic bottle may require centuries to decompose.",

        "Millions of tonnes of plastic enter oceans annually.",

        "Microplastics have been found in drinking water.",

        "Marine animals frequently mistake plastic for food."

    ];

    let randomFact = facts[Math.floor(Math.random() * facts.length)];

    document.getElementById("fact").innerHTML = randomFact;
}

</script>

</body>

</html>

"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=0)
