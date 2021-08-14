const x = parseInt(lines.shift())
const y = parseInt(lines.shift())

let soma = 0

let maior
let menor

if (x > y) {
    maior = x
    menor = y
} else {
    maior = y
    menor = x
}

if (menor%2 === 0) {
    menor += 1
} else {
    menor += 2
}

for (let i = menor; i < maior; i += 2) {
    soma += i
}

console.log(soma)
