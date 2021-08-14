const distancia_percorrida = parseInt(lines.shift())
const combustivel_gasto = parseFloat(lines.shift())

let consumo_medio = distancia_percorrida / combustivel_gasto
consumo_medio = consumo_medio.toFixed(3)

console.log(`${consumo_medio} km/l`)
