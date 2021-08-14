let I = 0
let J = 0

for (let i = 0; i < 11; i++) {
    if (I === 0 || I === 1.0 || I === 2.0) {
        I = parseInt(I)
        J = parseInt(J)
    }
    for (let l = 1; l <= 3; l++) {
        console.log(`I=${I} J=${J+l}`)
    }
    I += 0.2
    J += 0.2
    I = parseFloat(I.toFixed(1))
    J = parseFloat(J.toFixed(1))
}
