const N = parseInt(lines.shift())

let total = 0
let coelhos = 0
let ratos = 0
let sapos = 0

let testes
let qtd
let animal

for (let i = 0; i < N; i++) {

    testes = lines.shift().split(' ')
    qtd = parseInt(testes[0])
    animal = testes[1]

    if (animal === 'C') {
        coelhos += qtd
    } else if (animal === 'R') {
        ratos += qtd
    } else if (animal === 'S') {
        sapos += qtd
    }

    total += qtd
}

let percentualCoelhos = ((coelhos*100) / total).toFixed(2)
let percentualRatos = ((ratos*100) / total).toFixed(2)
let percentualSapos = ((sapos*100) / total).toFixed(2)

console.log(`Total: ${total} cobaias`)

console.log(`Total de coelhos: ${coelhos}`)
console.log(`Total de ratos: ${ratos}`)
console.log(`Total de sapos: ${sapos}`)

console.log(`Percentual de coelhos: ${percentualCoelhos} %`)
console.log(`Percentual de ratos: ${percentualRatos} %`)
console.log(`Percentual de sapos: ${percentualSapos} %`)
