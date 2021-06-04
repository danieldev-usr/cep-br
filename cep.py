import requests
import os


def clear(): os.system('clear')
clear()
zz = open('banner.txt','r')
ll = zz.read()
print(ll)
print(' ')

print("")
print("Informe o CEP sem traços! ")
print(' ')

while True:
	x = input('CEP: ')
	if len(x) !=8:
		print(f"Erro in {x}")
	request = requests.get(f'https://viacep.com.br/ws/{x}/json/')
		
	address_data = request.json()
	if 'erro' not in address_data:
		print(' ')
		print('CEP: {}'.format(address_data['cep']))
		print('Logradouro: {}'.format(address_data['logradouro']))
		print('Complemento: {}'.format(address_data['complemento']))
		print('Bairro: {}'.format(address_data['bairro']))
		print('Localidade: {}'.format(address_data['localidade']))
		print('IBGE: {}'.format(address_data['ibge']))
		print('UF: {}'.format(address_data['uf']))
		print('GIA: {}'.format(address_data['gia']))
		print('DDD: {}'.format(address_data['ddd']))
		print('Siafi: {}'.format(address_data['siafi']))
		print(' ')
		
	else:
		print('erro')
