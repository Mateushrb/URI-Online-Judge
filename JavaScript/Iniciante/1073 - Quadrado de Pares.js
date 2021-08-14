const N = parseInt(lines.shift())

let quadrado

for (let i = 2; i <= N; i += 2) {
    quadrado = i**2
    console.log(`${i}^2 = ${quadrado}`)
}
