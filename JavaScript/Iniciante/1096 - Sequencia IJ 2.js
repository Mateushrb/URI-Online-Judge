const J = 7

for (let i = 1; i < 10; i += 2) {
    let j = J
    for (let l = 0; l < 3; l++){
        console.log(`I=${i} J=${j}`)
        j -= 1
    }
}
