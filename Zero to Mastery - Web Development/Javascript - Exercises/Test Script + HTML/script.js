var object = {
    username: "Will",
    password: "Password123",
}

var database = [object];

var newsFeed = [
    {
        username: "1",
        timeline: "t1",
    },
    {
        username: "2",
        timeline: "t2",

    },
    {
        username: "3",
        timeline: "t3",
    }
];



var userNamePrompt = prompt("What is your username?");
var passwordPrompt = prompt("What is your password?");

function signIn(username, password) {
    if (username === database[0].username && 
        password === database[0].password) {
        console.log(newsFeed);
    } else {
        alert("Sorry, wrong username and password!");
    }
};

signIn(userNamePrompt, passwordPrompt);