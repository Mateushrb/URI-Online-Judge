let valor
let maior = 0
let posicao

for (let i = 1; i <= 100; i++) {
    valor = parseInt(lines.shift())
    if (valor > maior) {
        maior = valor
        posicao = i
    }
}
console.log(maior)
console.log(posicao)
