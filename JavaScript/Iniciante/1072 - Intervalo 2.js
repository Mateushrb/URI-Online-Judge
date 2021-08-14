const N = parseInt(lines.shift())

let dentro = 0
let fora = 0

let X

for (let i = 0; i < N; i++) {
    X = parseInt(lines.shift())
    if (X >= 10 && X <= 20) {
        dentro += 1
    } else {
        fora += 1
    }
}

console.log(`${dentro} in`)
console.log(`${fora} out`)
