const arr = [5, 3, 8, 4, 2]
const target = 9
/**
 * Perform a binary search on a sorted array to find the index of a target value.
 *
 * @param {number[]} arr - A sorted array of numbers to search.
 * @param {number} target - The value to search for in the array.
 * @returns {number} The index of the target value if found, otherwise -1.
 */

function binarySearch(arr, target) {

  let low = 0;
  let high = arr.length - 1;

  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    if (arr[mid] < target) {
      low = mid + 1;
    } else if (arr[mid] > target) {
      high = mid - 1;
    } else {
      return mid;
    }
  }
  return -1
}

const result = binarySearch(arr, target)
console.log(result)

const outputElement = document.getElementById('output');
outputElement.innerHTML = '';
outputElement.innerHTML = `
  <p>Array: ${arr}</p>
  <p>Target: ${target}</p>
  <p>Find index or -1: ${result}</p>
  <p>For details, check the console.</p>
`;










