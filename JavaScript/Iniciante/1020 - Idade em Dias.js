const idade = parseInt(lines.shift())

let anos = parseInt(idade/365)
let meses = parseInt((idade%365)/30)
let dias = (idade%365)%30

console.log(`${anos} ano(s)`)
console.log(`${meses} mes(es)`)
console.log (`${dias} dia(s)`)
