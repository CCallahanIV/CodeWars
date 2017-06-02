/*Find the sum of the odd numbers within an array, after cubing the initial integers. This function will return undefined (NULL in PHP) if any of the values aren't numbers.

Note: There are ONLY integers in the JAVA version of this Kata.*/

function cubeOdd(arr) {
    let sum = 0;
    for(i = 0; i < arr.length; i++){
        if (typeof arr[i] !== 'number'){
            return;
        } else if( arr[i] % 2 !== 0) {
            sum += Math.pow(arr[i], 3);
        }
    }
    return sum;
}


console.log(cubeOdd([1, 2, 3, 4]))   //28
console.log(cubeOdd([-3,-2,2,3]))    //0
console.log(cubeOdd(["a",12,9,"z",42])) //undefined
console.log(cubeOdd([true, 1, 3, 4])) //undefined