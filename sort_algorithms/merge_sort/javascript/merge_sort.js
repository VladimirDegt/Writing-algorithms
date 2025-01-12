/**
 * Sorts an array using the merge sort algorithm.
 * 
 * @param {number[]} sortedList - The array to be sorted.
 * @returns {number[]} The sorted array.
 */

function merge(left, right) {}
const nonSortedArray = [5, 3, 8, 4, 2]
const inputList = [...nonSortedArray]

function mergeSort(sortedList) {
    if (sortedList.length <= 1) return sortedList;

    const middle = Math.floor(sortedList.length / 2);
    const left = sortedList.slice(0, middle);
    const right = sortedList.slice(middle);

    const sortedLeft = mergeSort(left);
    const sortedRight = mergeSort(right);

    return merge(sortedLeft, sortedRight);
}

/**
 * Merges two sorted arrays into one sorted array.
 * 
 * @param {number[]} left - The left sorted array.
 * @param {number[]} right - The right sorted array.
 * @returns {number[]} The merged and sorted array.
 */

function merge(left, right) {
    let result = [];
    let leftIndex = 0;
    let rightIndex = 0;

    while (leftIndex < left.length && rightIndex < right.length) {
        if (left[leftIndex] < right[rightIndex]) {
            result.push(left[leftIndex]);
            leftIndex++;
        } else {
            result.push(right[rightIndex]);
            rightIndex++;
        }
    }

    while (leftIndex < left.length) {
        result.push(left[leftIndex]);
        leftIndex++;
    }

    while (rightIndex < right.length) {
        result.push(right[rightIndex]);
        rightIndex++;
    }

    return result;
}

const sorted = mergeSort(inputList)

console.log('not sorted array: ', nonSortedArray)
console.log('sorted array: ', sorted)

const outputElement = document.getElementById('output');
outputElement.innerHTML = '';
outputElement.innerHTML = `
  <p>Not sorted array: ${nonSortedArray}</p>
  <p>Sorted array: ${sorted}</p>
  <p>For details, check the console.</p>
`;