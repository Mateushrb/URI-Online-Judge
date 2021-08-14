let valores = lines.shift().split(' ')

const A = parseFloat(valores[0])
const B = parseFloat(valores[1])
const C = parseFloat(valores[2])

const pi = 3.14159

let triangulo = (A * C) / 2
triangulo = triangulo.toFixed(3)
console.log(`TRIANGULO: ${triangulo}`)

let circulo = pi * Math.pow(C, 2)
circulo = circulo.toFixed(3)
console.log(`CIRCULO: ${circulo}`)

let trapezio = ((A + B) * C) / 2
trapezio = trapezio.toFixed(3)
console.log(`TRAPEZIO: ${trapezio}`)

let quadrado = B * B
quadrado = quadrado.toFixed(3)
console.log(`QUADRADO: ${quadrado}`)

let retangulo = A * B
retangulo = retangulo.toFixed(3)
console.log(`RETANGULO: ${retangulo}`)
