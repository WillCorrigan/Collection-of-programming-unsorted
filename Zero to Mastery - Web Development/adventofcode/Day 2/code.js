const fs = require('fs');

fs.readFile('./input.txt', 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }

  let splitData = data.split('\r\n');
  let dataArray = []
  let splitSplitData = splitData.map((data) => {
    dataArray.push(data.split('x'));
  })

  let numberedData = dataArray.map(arr => arr.map(item => Number(item)))

  let total = 0;
  let ribbonTotal = 0;

  for (i = 0; i < dataArray.length-1; i++ ) {
    [l, w, h] = dataArray[i];
    let ribbonBow = l*w*h;
    let storedValue = ((2*l*w)+(2*w*h)+(2*h*l))
    let sortedArray = dataArray[i].sort((a,b)=>a-b);
    let answer = storedValue + (sortedArray[0] * sortedArray[1]);
    console.log(answer);
    total += answer;

    ribbonTotal += ((sortedArray[0] * 2) + (sortedArray[1]*2)) + ribbonBow;
  }
    console.log('the ribbon is', ribbonTotal);
    console.log(`the total is ${total}`)
});