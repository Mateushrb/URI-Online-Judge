const number = parseInt(lines.shift())
const hours = parseInt(lines.shift())
const price = parseFloat(lines.shift())

let salary = hours * price
salary = salary.toFixed(2)

console.log(`NUMBER = ${number}`)
console.log(`SALARY = U$ ${salary}`)
