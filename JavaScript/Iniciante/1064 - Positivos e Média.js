let valor
let qtd = 0
let soma = 0
let media
for (let i = 0; i < 6; i++) {
    valor = parseFloat(lines.shift())
    if (valor > 0) {
        qtd += 1
        soma += valor
    }
}

media = (soma/qtd).toFixed(1)

console.log(`${qtd} valores positivos`)
console.log(media)
