let dados = lines.shift().split(' ')

let cod = parseInt(dados[0])
let qtd = parseInt(dados[1])
let valor = 0

if (cod === 1) {
    valor = qtd*4
    valor = valor.toFixed(2)
    console.log(`Total: R$ ${valor}`)
} else if (cod === 2) {
    valor = qtd*4.5
    valor = valor.toFixed(2)
    console.log(`Total: R$ ${valor}`)
} else if (cod === 3) {
    valor = qtd*5
    valor = valor.toFixed(2)
    console.log(`Total: R$ ${valor}`)
} else if (cod === 4) {
    valor = qtd*2
    valor = valor.toFixed(2)
    console.log(`Total: R$ ${valor}`)
} else if (cod === 5) {
    valor = qtd*1.5
    valor = valor.toFixed(2)
    console.log(`Total: R$ ${valor}`)
} else {
    //pass
}
