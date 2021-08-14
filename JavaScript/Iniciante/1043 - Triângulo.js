let valores = lines.shift().split(' ')

const A = parseFloat(valores[0])
const B = parseFloat(valores[1])
const C = parseFloat(valores[2])

if (A < B+C && A > Math.abs(B-C)) {
    let perimetro = A + B + C
    perimetro = perimetro.toFixed(1)
    console.log(`Perimetro = ${perimetro}`)
} else{
    let area = ((A + B) * C) / 2
    area = area.toFixed(1)
    console.log(`Area = ${area}`)
}
