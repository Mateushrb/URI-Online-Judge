let valor
let qtd = 0
for (let i = 0; i < 5; i++) {
    valor = parseInt(lines.shift())
    if (valor%2 === 0) {
        qtd += 1
    }
}

console.log(`${qtd} valores pares`)
