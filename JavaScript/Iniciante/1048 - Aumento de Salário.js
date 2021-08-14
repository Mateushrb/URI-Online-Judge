const salario = parseFloat(lines.shift())

let novoSalario
let reajuste
let percentual

function reajuste15() {
    percentual = 0.15
    reajuste = salario * percentual
    novoSalario = salario + reajuste
}

function reajuste12() {
    percentual = 0.12
    reajuste = salario * percentual
    novoSalario = salario + reajuste
}

function reajuste10() {
    percentual = 0.10
    reajuste = salario * percentual
    novoSalario = salario + reajuste
}

function reajuste7() {
    percentual = 0.07
    reajuste = salario * percentual
    novoSalario = salario + reajuste
}

function reajuste4() {
    percentual = 0.04
    reajuste = salario * percentual
    novoSalario = salario + reajuste
}

if (salario <= 400) {
    reajuste15()
    percentual = 15
} else if (salario <= 800) {
    reajuste12()
    percentual = 12
} else if (salario <= 1200) {
    reajuste10()
    percentual = 10
} else if (salario <= 2000) {
    reajuste7()
    percentual = 7
} else {
    reajuste4()
    percentual = 4
}

novoSalario = novoSalario.toFixed(2)
reajuste = reajuste.toFixed(2)

console.log(`Novo salario: ${novoSalario}`)
console.log(`Reajuste ganho: ${reajuste}`)
console.log(`Em percentual: ${percentual} %`)
