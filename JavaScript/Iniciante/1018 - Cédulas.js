const valorInicial = parseInt(lines.shift())
let valor = valorInicial
console.log(valorInicial)

let notas100 = parseInt(valor/100)
valor %= 100
console.log(`${notas100} nota(s) de R$ 100,00`)

let notas50 = parseInt(valor/50)
valor %= 50
console.log(`${notas50} nota(s) de R$ 50,00`)

let notas20 = parseInt(valor/20)
valor %= 20
console.log(`${notas20} nota(s) de R$ 20,00`)

let notas10 = parseInt(valor/10)
valor %= 10
console.log(`${notas10} nota(s) de R$ 10,00`)

let notas5 = parseInt(valor/5)
valor %= 5
console.log(`${notas5} nota(s) de R$ 5,00`)

let notas2 = parseInt(valor/2)
valor %= 2
console.log(`${notas2} nota(s) de R$ 2,00`)

let notas1 = parseInt(valor)
console.log(`${notas1} nota(s) de R$ 1,00`)
