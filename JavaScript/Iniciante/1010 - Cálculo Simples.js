let line1 = lines.shift().split(' ')
let line2 = lines.shift().split(' ')

let cod_1 = parseInt(line1[0])
let num_1 = parseInt(line1[1])
let val_1 = parseFloat(line1[2])

let cod_2 = parseInt(line2[0])
let num_2 = parseInt(line2[1])
let val_2 = parseFloat(line2[2])

let preco = (num_1*val_1) + (num_2*val_2)
preco = preco.toFixed(2)

console.log(`VALOR A PAGAR: R$ ${preco}`)
