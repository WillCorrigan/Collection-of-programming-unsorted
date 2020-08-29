const fs = require('fs');

// fs.readFile('./santa.txt', "utf8", (err, data) => {
//   console.time('timer');
//   if (err) {
//     console.log('error');
//   }
//   let floor = 0;
//   let result = [...data].map((character, index) => {
//     if (character === '(') {
//       floor +=1;
//     } else {
//       floor -= 1;
//       isBasement(floor, index);
//     }
//     });
//   console.log(floor);
//   console.timeEnd('timer');
//   });

// const isBasement = (floor, index) => {
//   if (floor === -1) {
//     console.log(index + 1, "Santa is in the basement");
//   }
// };


// function question1() {
//   fs.readFile('./santa.txt', (err, data) => {
//     console.time('santa-time');
//     const directions = data.toString();
//     const directionsArray = directions.split('');
//     const answer = directionsArray.reduce((acc, currentValue) => {
//       if (currentValue === '(') {
//         return acc += 1
//       } else if (currentValue === ')') {
//         return acc -=1
//       }
//     }, 0)
//     console.timeEnd('santa-time');
//     console.log('floor', answer);
//   })
// }

// question1()



function question2() {
  fs.readFile('./santa.txt', (err, data) => {
    const directions = data.toString();
    const directionsArray = directions.split('');
    let accumulator = 0;
    let counter = 0;
    const answer = directionsArray.some((currentItem) => {
      if (currentItem === '(') {
        accumulator += 1;
      } else if (currentItem === ')') {
        accumulator -= 1;
      }
      counter ++;
      return accumulator < 0;
    })
    console.log('basement entered at: ', counter);
  })
}

question2()