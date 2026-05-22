from flask import Flask, render_template_string

app = Flask(__name__)

html = """

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Single Use Plastics Awareness</title>

<style>

body{
    font-family: Arial, sans-serif;
    background-color: #d9f3ff;
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
    background: white;
    margin: 20px;
    padding: 20px;
    border-radius: 10px;
}

h2{
    color: #0088aa;
}

button{
    background-color: #0088aa;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover{
    background-color: #005f73;
}

footer{
    background-color: #0088aa;
    color: white;
    text-align: center;
    padding: 15px;
    margin-top: 20px;
}

#factBox{
    margin-top: 15px;
    font-weight: bold;
    color: darkred;
}

</style>
</head>

<body>

<header>
    <h1>Single Use Plastics</h1>
    <p>A basic awareness website for young people</p>
</header>

<section>
    <h2>What Are Single Use Plastics?</h2>

    <p>
        Single use plastics are products manufactured to be utilised once before disposal. 
        Examples include disposable bottles, plastic straws, carrier bags and takeaway packaging.
    </p>

    <p>
        Although these objects may appear convenient, they remain within the environment for centuries, 
        creating extensive pollution across oceans and urban landscapes.
    </p>
</section>

<section>
    <h2>The Consequences Of Plastic Pollution</h2>

    <p>
        Plastic pollution can devastate ecosystems and threaten marine organisms. 
        Sea creatures frequently mistake plastic for nourishment, causing severe injury or death.
    </p>

    <p>
        Furthermore, plastics fragment into microplastics, infinitesimal particles capable of contaminating water supplies and food chains.
    </p>

    <button onclick="showFact()">Press For A Random Fact</button>

    <p id="factBox"></p>
</section>

<section>
    <h2>How To Reduce Single Use Plastics</h2>

    <ul>
        <li>Carry a reusable water bottle.</li>
        <li>Use fabric shopping bags instead of plastic ones.</li>
        <li>Avoid disposable cutlery and straws.</li>
        <li>Recycle conscientiously whenever possible.</li>
        <li>Purchase products with minimal packaging.</li>
    </ul>

    <p>
        Even diminutive alterations to everyday habits can culminate in substantial environmental improvement.
    </p>
</section>

<footer>
    <p>Protecting the planet begins with small decisions 🌍</p>
</footer>

<script>

function showFact(){

    let facts = [
        "A plastic bottle may require 450 years to decompose.",
        "Millions of tonnes of plastic enter oceans annually.",
        "Microplastics have been discovered in drinking water.",
        "Numerous marine animals accidentally consume plastic."
    ];

    let randomFact = facts[Math.floor(Math.random() * facts.length)];

    document.getElementById("factBox").innerHTML = randomFact;
}

</script>

</body>
</html>

"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)