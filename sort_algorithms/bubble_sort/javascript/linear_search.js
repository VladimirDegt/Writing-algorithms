const arr = [5, 3, 8, 4, 2]

function linearSearch(arr, target) {
  for (let i = 0; i < arr.length; i += 1) {
    if ( arr[i] === target) return i
  }
  return -1;
}

const result = linearSearch(arr, 3)
console.log(result)

const outputElement = document.getElementById('output');
outputElement.innerHTML = '';
outputElement.innerHTML = `
  <p>Array: ${arr}</p>
  <p>Target: 3</p>
  <p>Find index or -1: ${result}</p>
  <p>For details, check the console.</p>
`;