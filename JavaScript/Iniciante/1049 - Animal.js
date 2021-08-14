const filo = lines.shift()
const classe = lines.shift()
const ordem = lines.shift()

let animal

if (filo === 'vertebrado') {
    if (classe ==='ave') {
        if (ordem === 'carnivoro') {
            animal = 'aguia'
        } else {
            animal = 'pomba'
        }
    } else {
        if (ordem === 'onivoro') {
            animal = 'homem'
        } else {
            animal = 'vaca'
        }
    }
} else {
    if (classe === 'inseto') {
        if (ordem === 'hematofago') {
            animal = 'pulga'
        } else {
            animal = 'lagarta'
        }
    } else {
        if (ordem === 'hematofago') {
            animal = 'sanguessuga'
        } else {
            animal = 'minhoca'
        }
    }
}

console.log(animal)
