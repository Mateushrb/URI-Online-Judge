let J = 7

for (let i = 1; i < 10; i += 2) {
    for (let l = 0; l < 3; l++) {
        console.log(`I=${i} J=${J}`)
        J -= 1
    }
    J += 5
}
