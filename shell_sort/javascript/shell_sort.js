const nonSortedArray = [5, 3, 8, 4, 2]
const inputList = [...nonSortedArray]

function shellSort(arr) {
    const n = arr.length;

    // Початковий проміжок (gap) вибирається як половина довжини масиву
    let gap = Math.floor(n / 2);

    // Продовжуємо сортування, поки проміжок більше 0
    while (gap > 0) {
        // Виконуємо сортування вставками для підмасивів з кроком gap
        for (let i = gap; i < n; i++) {
            const temp = arr[i];
            let j = i;

            // Переміщуємо елементи, які більші за temp, на gap позицій вперед
            while (j >= gap && arr[j - gap] > temp) {
                arr[j] = arr[j - gap];
                j -= gap;
            }

            // Вставляємо temp на правильну позицію
            arr[j] = temp;
        }

        // Зменшуємо проміжок
        gap = Math.floor(gap / 2);
    }

    return arr;
}

console.log('not sorted array: ', nonSortedArray)
console.log('sorted array: ', shellSort(inputList))


const outputElement = document.getElementById('output');
outputElement.innerHTML = '';
outputElement.innerHTML = `
  <p>Not sorted array: ${nonSortedArray}</p>
  <p>Sorted array: ${inputList}</p>
  <p>For details, check the console.</p>
`;