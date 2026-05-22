from flask import Flask

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
    background-color: #cfefff;
    padding: 20px;
}

h1{
    color: darkblue;
}

section{
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    margin-bottom: 20px;
}

button{
    background-color: darkblue;
    color: white;
    padding: 10px;
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
Examples include plastic bottles, wrappers, straws and carrier bags.
</p>

<p>
Although they may appear convenient, they persist within the environment
for centuries and contribute to extensive pollution.
</p>

</section>

<section>

<h2>The Consequences</h2>

<p>
Plastic pollution devastates ecosystems and threatens biodiversity.
Marine organisms frequently mistake plastic for nourishment,
causing injury and death.
</p>

<p>
Furthermore, plastics gradually fragment into microplastics,
infinitesimal particles capable of contaminating water supplies.
</p>

</section>

<section>

<h2>How To Reduce Plastic Usage</h2>

<ul>
<li>Use reusable bottles.</li>
<li>Carry fabric shopping bags.</li>
<li>Avoid disposable straws.</li>
<li>Recycle conscientiously.</li>
<li>Purchase products with minimal packaging.</li>
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

        "Marine wildlife frequently mistakes plastic for food."

    ];

    let randomFact = facts[Math.floor(Math.random() * facts.length)];

    document.getElementById("fact").innerHTML = randomFact;
}

</script>

</body>

</html>

"""

if __name__ == "__main__":

    app.run(host="0.0.0.0")
