const N = parseInt(lines.shift())

let valores
let v1
let v2
let v3
let media

for (let i = 0; i < N; i++) {

    valores = lines.shift().split(' ')

    v1 = parseFloat(valores[0])
    v2 = parseFloat(valores[1])
    v3 = parseFloat(valores[2])

    media = ((v1*2) + (v2*3) + (v3*5)) / 10
    media = media.toFixed(1)

    console.log(media)
}
