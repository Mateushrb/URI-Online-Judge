let valores = lines.shift().split(' ')

const A = parseInt(valores[0])
const B = parseInt(valores[1])
const C = parseInt(valores[2])
const D = parseInt(valores[3])

if (B > C && D > A && C + D > A + B && C > 0 && D > 0 && A%2 === 0) {
    console.log("Valores aceitos")
} else {
    console.log("Valores nao aceitos")
}
