const fs = require('fs');
console.time('hello');
fs.readFile('./input.txt', 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }

  let santaX = 0;
  let santaY = 0;
  let roboX = 0;
  let roboY = 0; 
  let santaCoords = [[0,0]];
  let roboCoords = [[0,0]];

  let dataString = data.toString();

  let santa = true;

  for (i = 0; i < dataString.length; i++) {
    if(santa){
      if (dataString[i] === '^' || dataString[i] === 'v') {
        dataString[i] === '^' ? santaX+=1 : santaX-=1;
        santaCoords.push([santaX,santaY]);
        santa = !santa;
      } else {
        dataString[i] === '>' ? santaY+=1 : santaY-=1;
        santaCoords.push([santaX,santaY]);
        santa = !santa;
      };
    } else {
      if (dataString[i] === '^' || dataString[i] === 'v') {
        dataString[i] === '^' ? roboX+=1 : roboX-=1;
        roboCoords.push([roboX,roboY]);
        santa = !santa;
      } else {
        dataString[i] === '>' ? roboY+=1 : roboY-=1;
        santaCoords.push([roboX,roboY]);
        santa = !santa;
      };
    }  
  }

  santaCoordsSorted = santaCoords.slice().sort();
  roboCoordsSorted = roboCoords.slice().sort();
  combinedArray = santaCoordsSorted.concat(roboCoordsSorted);

  let finalanswer = combinedArray.reduce((acc, current, index) => {
    return JSON.stringify(acc).includes(JSON.stringify(current)) ? acc : [...acc, current]
  },[]);

console.log(finalanswer.length);
console.timeEnd('hello');
});