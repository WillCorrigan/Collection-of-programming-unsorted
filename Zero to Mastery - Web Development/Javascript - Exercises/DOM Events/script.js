var button = document.getElementById("enter");
var input = document.getElementById("userinput");
var ul = document.querySelector("ul");
var x = document.querySelectorAll(".listItem");





x.forEach(toggleStrikethrough);


function toggleStrikethrough(item) {
	addButton(item);
	item.addEventListener("click", function(event) {
		if(event.target.classList.contains("listItem")) {
			event.target.classList.toggle("done");
			
		}
	});
}


function addButton(target) {
	var addButton = target.appendChild(document.createElement("button"));
	addButton.setAttribute('class', 'del');
	addButton.innerHTML = "Delete";
	addButton.addEventListener("click", deleteListItem);
}


function inputLength() {
	return input.value.length;
}

function createListElement() {
	var li = document.createElement("li");
	li.appendChild(document.createTextNode(input.value));
	li.setAttribute('class', 'listItem');
	ul.appendChild(li);
	input.value = "";
	toggleStrikethrough(li);
}

function addListAfterClick() {
	if (inputLength() > 0) {
		createListElement();
	}
}

function addListAfterKeypress(event) {
	if (inputLength() > 0 && event.keyCode === 13) {
		createListElement();
	}
}

function deleteListItem(event) {
	fartSound = new Audio("fart-01.mp3");
	fartSound.play();
	event.target.parentElement.remove();

}


button.addEventListener("click", addListAfterClick);

input.addEventListener("keypress", addListAfterKeypress);