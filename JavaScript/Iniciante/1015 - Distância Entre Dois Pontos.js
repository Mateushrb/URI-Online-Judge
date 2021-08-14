let p1 = lines.shift().split(' ')
let p2 = lines.shift().split(' ')

const x1 = p1[0]
const y1 = p1[1]

const x2 = p2[0]
const y2 = p2[1]

let distancia = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2))
distancia = distancia.toFixed(4)
console.log(distancia)
