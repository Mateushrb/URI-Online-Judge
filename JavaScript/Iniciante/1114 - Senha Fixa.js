let senha = 0

while (senha != 2002) {
    senha = parseInt(lines.shift())
    if (senha != 2002) {
        console.log('Senha Invalida')
    } else {
        console.log('Acesso Permitido')
    }
}
