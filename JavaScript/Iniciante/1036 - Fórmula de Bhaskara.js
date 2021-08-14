let valores = lines.shift().split(' ')

const A = parseFloat(valores[0])
const B = parseFloat(valores[1])
const C = parseFloat(valores[2])

let delta = Math.pow(B, 2) -4*A*C
if (A !== 0) {
    if (delta >= 0) {
        let x1 = (-B + Math.sqrt(delta)) / (2*A)
        let x2 = (-B - Math.sqrt(delta)) / (2*A)
        x1 = x1.toFixed(5)
        x2 = x2.toFixed(5)
        console.log(`R1 = ${x1}`)
        console.log(`R2 = ${x2}`)
    } else {
        console.log('Impossivel calcular')
    }

} else {
    console.log('Impossivel calcular')
}
