const N = parseInt(lines.shift())

let produto

for (let i = 1; i <= 10; i++) {
    produto = i*N
    console.log(`${i} x ${N} = ${produto}`)
}
