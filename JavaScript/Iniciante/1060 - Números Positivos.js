let valor
let contador = 0
for (let i = 0; i < 6; i++) {
    valor = parseFloat(lines.shift())
    if (valor > 0) {
        contador++
    } else {

    }
}

console.log(`${contador} valores positivos`)
