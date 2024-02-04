function getRandomInt(min, max) {
  min = Math.ceil(min)
  max = Math.floor(max)
  return Math.floor(Math.random() * (max - min + 1)) + min
}

function getTime() {
  return parseFloat((Date.now() / 1000).toFixed(2))
}

function generateNewRoots(roots, equation, x1, x2) {
  temp1 = x1
  temp2 = x2
  while (true) {
    temp1 = getRandomInt(-10, 10)
    temp2 = getRandomInt(-10, 10)
    if (temp1 != 0 && temp2 != 0 && ((temp1 != x1 && temp1 != x2) || (temp2 != x1 && temp2 != x2))) {
      x1 = temp1
      x2 = temp2
      a = 1
      b = -((x1 + x2) / a)
      c = (x1 * x2) / a
      if (b == 0) {
        continue
      }
      roots[0].innerHTML = 'x<sub>1</sub>='
      roots[1].innerHTML = 'x<sub>2</sub>='
      equation.innerHTML = 'x<sup>2</sup>' + (b < 0 ? b : '+' + b) + (c < 0 ? c : '+' + c) + '=0'
      console.log(x1, x2, b, c)
      return [x1, x2]
    }
  }
}
let x1 = 100
let x2 = 100
let equation = document.getElementById('equation')
let roots = document.querySelectorAll('.root') // Select all elements with class 'root'
let item1 = document.querySelector('.item')
let timeElements = document.querySelectorAll('.time-display')

let bestTimeElement = timeElements[0]
let lastTimeElement = timeElements[1]
let bestTime = 10000 // shortest duration to complete the problem in seconds
let lastTime = getTime() // latest duration the problem was completed

newRoots = generateNewRoots(roots, equation, x1, x2)
x1 = newRoots[0]
x2 = newRoots[1]

button.addEventListener('click', (event) => {
  if (roots[0].innerHTML == 'x<sub>1</sub>=') {
    // write out the roots
    roots[0].innerHTML += x1
    roots[1].innerHTML += x2

    // calculate time
    console.log(getTime(), lastTime)
    lastTimeElement.innerHTML = 'Last Time: ' + (getTime() - lastTime).toFixed(2)
    lastTime = (getTime() - lastTime).toFixed(2)
    bestTime = lastTime < bestTime ? lastTime : bestTime
    bestTimeElement.innerHTML = 'Best Time: ' + bestTime
  } else {
    // generate new roots
    newRoots = generateNewRoots(roots, equation, x1, x2)
    x1 = newRoots[0]
    x2 = newRoots[1]

    lastTime = getTime() // reset the time
  }
})
