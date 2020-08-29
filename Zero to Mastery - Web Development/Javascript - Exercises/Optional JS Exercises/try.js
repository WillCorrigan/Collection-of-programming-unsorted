array = [1,2,4,591,392,391,2,5,10,2,1,1,1,20,20];
array2 = [1, "2", "3", 2];

const reduceSorted = (arr) => {
    let sorted = arr.sort(function(a,b){return a-b});
    let reducedSorted = sorted.reduce((acc, current, index, arrayName) => {
        if(current === arrayName[index-1]) {
            acc[acc.length-1].push(current);
        } else {
            acc.push(current === arrayName[index+1] ? [current] : current);
        }
        return acc;
    }, []);
    console.log(reducedSorted);
}

testArray = [1,2,3,4,5,6,7,8,9];
testArray2 = [1,1,2,3,4,5,6,7,8,9];

const findSum = ((array, target) => {
    returnArray = []
    array.map((number, index) => {
        for (item of array){
            if ((number + item) === target && array.indexOf(item) != index){
                returnArray = [number, item]
            }
        }
    })
    if (returnArray.length === 0) {
        return "No combination of numbers can reach the target!"
    } else {
        return returnArray
    }
});


