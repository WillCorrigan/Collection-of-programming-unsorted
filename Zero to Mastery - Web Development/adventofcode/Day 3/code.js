const fs = require('fs');
console.time('hello');
fs.readFile('./input.txt', 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }

  let x = 0;
  let y = 0; 
  let coords = [[0,0]];

  let dataString = data.toString();


  for (i = 0; i < dataString.length; i++) {
    if (dataString[i] === '^' || dataString[i] === 'v') {
      dataString[i] === '^' ? x+=1 : x-=1;
      coords.push([x,y]);
    } else {
      dataString[i] === '>' ? y+=1 : y-=1;
      coords.push([x,y]);
    };
  }

  coordsSorted = coords.slice().sort();

  let answer = coordsSorted.reduce((acc, current, index) => {
    return JSON.stringify(acc).includes(JSON.stringify(current)) ? acc : [...acc, current]
  },[]);

console.log(answer.length);
console.timeEnd('hello');
});