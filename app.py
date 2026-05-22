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
    background-color: #d8f3ff;
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

h1{
    margin: 0;
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
    font-size: 16px;
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

ul{
    line-height: 1.8;
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
        Single use plastics are products manufactured to be utilised once 
        before disposal. Examples include disposable bottles, plastic straws, 
        takeaway containers and carrier bags.
    </p>

    <p>
        Although they may appear convenient, these materials persist within 
        the environment for centuries and contribute to extensive pollution.
    </p>

</section>

<section>

    <h2>The Consequences Of Plastic Pollution</h2>

    <p>
        Plastic pollution devastates ecosystems and threatens biodiversity. 
        Marine organisms frequently mistake plastic for nourishment, resulting 
        in severe injury or death.
    </p>

    <p>
        Furthermore, plastics fragment into microplastics, infinitesimal 
        particles capable of contaminating oceans, rivers and food supplies.
    </p>

    <button onclick="showFact()">
        Click For A Fact
    </button>

    <p id="fact"></p>

</section>

<section>

    <h2>How To Reduce Single Use Plastics</h2>

    <ul>
        <li>Carry a reusable water bottle.</li>
        <li>Use fabric shopping bags.</li>
        <li>Avoid disposable cutlery and straws.</li>
        <li>Recycle conscientiously.</li>
        <li>Purchase products with minimal packaging.</li>
    </ul>

    <p>
        Even diminutive lifestyle alterations can culminate in substantial 
        environmental improvement.
    </p>

</section>

<footer>

    <p>
        Protect oceans • Preserve wildlife • Reduce pollution 🌍
    </p>

</footer>

<script>

function showFact(){

    let facts = [

        "A plastic bottle may require 450 years to decompose.",

        "Millions of tonnes of plastic enter oceans annually.",

        "Microplastics have been discovered in drinking water worldwide.",

        "Many marine animals accidentally consume plastic."

    ];

    let randomFact = facts[Math.floor(Math.random() * facts.length)];

    document.getElementById("fact").innerHTML = randomFact;
}

</script>

</body>

</html>

"""

if __name__ == "__main__":
    app.run()
