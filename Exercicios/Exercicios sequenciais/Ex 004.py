#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1=float(input('Digite a primeira nota: '))
nota2=float(input('Digite a segunda nota: '))
nota3=float(input('Digite a terceira nota: '))
nota4=float(input('Digite a quarta nota: '))        #Criando VAR do tipo float (Números flutuantes) para receber valores do usuário.

media=(nota1+nota2+nota3+nota4)/4       #Criando uma VAR que irá conter a média total.

print(f'A média é: {media:.2f}')        #Mostrando o resultado ao usuário.