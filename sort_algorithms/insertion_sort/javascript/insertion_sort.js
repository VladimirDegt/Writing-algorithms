/**
 * Sorts an array using the insertion sort algorithm.
 *
 * @param {number[]} sortedList - The array to be sorted.
 * @returns {number[]} The sorted array.
 */
const nonSortedArray = [5, 3, 8, 4, 2]
const inputList = [...nonSortedArray]


function insertSort(sortedList) {
    for (let i = 1; i < (sortedList.length); i += 1) {
        const currentElement = sortedList[i];
        let j = i - 1;
        while (j >= 0 && sortedList[j] > currentElement) {
            sortedList[j + 1] = sortedList[j];
            j -= 1; 
        }
        sortedList[j + 1] = currentElement;
    }
  return sortedList;
}

console.log('not sorted array: ', nonSortedArray)
console.log('sorted array: ', insertSort(inputList))


const outputElement = document.getElementById('output');
outputElement.innerHTML = '';
outputElement.innerHTML = `
  <p>Not sorted array: ${nonSortedArray}</p>
  <p>Sorted array: ${inputList}</p>
  <p>For details, check the console.</p>
`;