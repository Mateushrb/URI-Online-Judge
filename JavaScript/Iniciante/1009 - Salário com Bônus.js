const name = toString(lines.shift())
const salary = parseFloat(lines.shift())
const sales = parseFloat(lines.shift())

let commission = 0.15 * sales
let total = salary + commission
total = total.toFixed(2)
console.log(`TOTAL = R$ ${total}`)
