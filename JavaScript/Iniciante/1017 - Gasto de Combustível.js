const tempoGasto = parseInt(lines.shift())
const velocidadeMedia = parseInt(lines.shift())

let distancia = tempoGasto * velocidadeMedia
let combustivelNecessario = distancia/12
combustivelNecessario = combustivelNecessario.toFixed(3)

console.log(combustivelNecessario)
