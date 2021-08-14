const valores = lines.shift().split(' ')

const V1 = parseFloat(valores[0])
const V2 = parseFloat(valores[1])
const V3 = parseFloat(valores[2])

let A
let B
let C

if (V1 > V2 && V1 > V3) {
    A = V1
    if (V2 > V3) {
        B = V2
        C = V3
    } else {
        B = V3
        C = V2
    }
} else if (V2 > V1 && V2 > V3) {
    A = V2
    if (V1 > V3) {
        B = V1
        C = V3
    } else {
        B = V3
        C = V1
    }
} else {
    A = V3
    if (V1 > V2) {
        B = V1
        C = V2
    } else {
        B = V2
        C = V1
    }
}

if (A >= B+C) {
    console.log('NAO FORMA TRIANGULO')
} else {
    if (Math.pow(A, 2) === Math.pow(B, 2) + Math.pow(C, 2)) {
        console.log('TRIANGULO RETANGULO')
    } if (Math.pow(A, 2) > Math.pow(B, 2) + Math.pow(C, 2)) {
        console.log('TRIANGULO OBTUSANGULO')
    } if (Math.pow(A, 2) < Math.pow(B, 2) + Math.pow(C, 2)) {
        console.log('TRIANGULO ACUTANGULO')
    } if (A === B && B === C) {
        console.log('TRIANGULO EQUILATERO')
    } if (A === B && B != C || A != B && B === C || B != C && C === A) {
        console.log('TRIANGULO ISOSCELES')
    }
}
