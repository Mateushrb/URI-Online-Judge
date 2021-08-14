let par = 0
let impar = 0
let positivo = 0
let negativo = 0

let valor

for (let i = 0; i < 5; i++) {
    valor = parseInt(lines.shift())
    if (valor % 2 === 0) {
        par += 1
    } else {
        impar += 1
    }
    if (valor > 0) {
        positivo += 1
    } else if (valor < 0) {
        negativo += 1
    }
}

console.log(`${par} valor(es) par(es)`)
console.log(`${impar} valor(es) impar(es)`)
console.log(`${positivo} valor(es) positivo(s)`)
console.log(`${negativo} valor(es) negativo(s)`)
