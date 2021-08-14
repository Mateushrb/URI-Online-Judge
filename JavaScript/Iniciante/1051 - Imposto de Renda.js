const salario = parseFloat(lines.shift())

let imposto28 = 0
let imposto18 = 0
let imposto8 = 0
let imposto

if (salario <= 2000) {
    console.log('Isento')
} else {
    if (salario <= 3000) {
        imposto8 = (salario - 2000)*0.08
    }else if (salario <= 4500) {
        imposto8 = 80
        imposto18 = (salario - 3000)*0.18
    } else {
        imposto8 = 80
        imposto18 = 270
        imposto28 = (salario - 4500)*0.28
    }
    imposto = (imposto28 + imposto18 + imposto8).toFixed(2)
    console.log(`R$ ${imposto}`)
}
