const nonSortedArray = [5, 3, 8, 4, 2]
const inputList = [...nonSortedArray]

/**
 * Sorts an array using the quick sort algorithm.
 *
 * @param {number[]} sortedList - The array of numbers to be sorted.
 * @returns {number[]} - The sorted array.
 */

function quick_sort(sortedList) {
    if (sortedList.length <= 1) return sortedList;
    const pivotIdx = Math.floor(sortedList.length / 2)
    const pivot = sortedList[pivotIdx]
    
    const leftPart = [];
    const rightPart = [];

    for (let i = 0; i < sortedList.length; i += 1) {
        if (i === pivotIdx) continue;

        if (sortedList[i] < pivot) {
            leftPart.push(sortedList[i])
        } else {
            rightPart.push(sortedList[i])
        }
    }

  return [...quick_sort(leftPart), pivot, ...quick_sort(rightPart)];
}

const sorted = quick_sort(inputList)

console.log('not sorted array: ', nonSortedArray)
console.log('sorted array: ', sorted)

const outputElement = document.getElementById('output');
outputElement.innerHTML = '';
outputElement.innerHTML = `
  <p>Not sorted array: ${nonSortedArray}</p>
  <p>Sorted array: ${sorted}</p>
  <p>For details, check the console.</p>
`;