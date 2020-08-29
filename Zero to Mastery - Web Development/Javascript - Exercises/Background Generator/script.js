var _ = require('lodash');

console.log(_);
var css = document.querySelector("h3");
var color1 = document.querySelector(".color1");
var color2 = document.querySelector(".color2");
var body = document.getElementById("gradient");
var random = document.querySelector('.random')


function setAndDisplayGradient() {
    body.style.background = 
    "linear-gradient(to right, " 
    + color1.value 
    + ", " 
    + color2.value 
    + ")";
    css.textContent = body.style.background + ";";
}

function startColor() {
    setAndDisplayGradient();
}


function setGradient() {
    setAndDisplayGradient();
}

function randomColors() {
    body.style.background = 
    "linear-gradient(to right, #" 
    + Math.floor(Math.random()*16777215).toString(16)
    + ", #" 
    + Math.floor(Math.random()*16777215).toString(16)
    + ")";
    css.textContent = body.style.background + ";";
}

random.addEventListener("click", randomColors);

color1.addEventListener("input", setGradient);

color2.addEventListener("input", setGradient);