const nonSortedArray = [5, 3, 8, 4, 2]
const inputList = [...nonSortedArray]

/**
 * Sorts an array of numbers using the selection sort algorithm.
 *
 * @param {number[]} sortedList - The array of numbers to be sorted.
 * @returns {number[]} The sorted array.
 */

function selection_sort(sortedList) {
    const n = sortedList.length;
    for (let i = 0; i < n - 1; i += 1) {
        let minIdx = i;
        for (let j = i + 1; j < n; j += 1) {
            if (sortedList[j] < sortedList[minIdx]) {
                minIdx = j
            }
        }

        const tempVar = sortedList[i];
        sortedList[i] = sortedList[minIdx];
        sortedList[minIdx] = tempVar;

    }
  return sortedList;
}

console.log('not sorted array: ', nonSortedArray)
console.log('sorted array: ', selection_sort(inputList))


const outputElement = document.getElementById('output');
outputElement.innerHTML = '';
outputElement.innerHTML = `
  <p>Not sorted array: ${nonSortedArray}</p>
  <p>Sorted array: ${inputList}</p>
  <p>For details, check the console.</p>
`;