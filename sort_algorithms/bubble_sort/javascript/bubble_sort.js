const nonSortedArray = [5, 3, 8, 4, 2]
const inputList = [...nonSortedArray]

/**
 * Sorts a given array using bubble sort algorithm.
 * @param {Array} inputList array of numbers to be sorted
 * @return {Array} sorted array
 */
function bubbleSort(sortedList) {
  for (let i = 0; i < (sortedList.length - 1); i += 1) {
    console.log(`Iteration ${i + 1}:`);
    for (let j = 0; j < (sortedList.length - i - 1); j += 1) {
      console.log(`  Comparing ${sortedList[j]} and ${sortedList[j + 1]}`);
      if (sortedList[j] > sortedList[j + 1]) {
        console.log(`  Swapping ${sortedList[j]} and ${sortedList[j + 1]}`);
        const temp = sortedList[j];
        sortedList[j] = sortedList[j + 1];
        sortedList[j + 1] = temp;
      }
    }
  }
  return sortedList;
}

console.log('not sorted array: ', nonSortedArray)
console.log('sorted array: ', bubbleSort(inputList))


const outputElement = document.getElementById('output');
outputElement.innerHTML = '';
outputElement.innerHTML = `
  <p>Not sorted array: ${nonSortedArray}</p>
  <p>Sorted array: ${inputList}</p>
  <p>For details, check the console.</p>
`;