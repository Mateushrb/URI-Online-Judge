let valores = lines.shift().split(' ')

const A = parseInt(valores[0])
const B = parseInt(valores[1])
const C = parseInt(valores[2])

let MaiorAB = (A + B + Math.abs(A - B)) / 2
let Maior = (MaiorAB + C + Math.abs(MaiorAB - C)) / 2

console.log(`${Maior} eh o maior`)
