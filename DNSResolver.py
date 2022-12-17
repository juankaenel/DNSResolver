import argparse
import dns.resolver
import dns.rdatatype
import requests
from colorama import Fore

parser = argparse.ArgumentParser(description="Detector de comandos")
parser.add_argument('-t', '--target', help="set target")
parser = parser.parse_args()

if parser.target:
	# Registros DNS
	print(Fore.GREEN +'\n' + f'---------- Registros DNS ----------'+'\n')
	tipos_registro = ['A', 'NS', 'SOA', 'MX', 'MF', 'MD', 'ANY', 'HINFO', 'AXFR', 'CNAME', 'TXT']
	for registro_dns in tipos_registro:
	    try:
	        consulta = dns.resolver.resolve(parser.target, registro_dns)            
	        for respuesta in consulta:
	            nombre_registro = dns.rdatatype.to_text(respuesta.rdtype)
	            print(Fore.GREEN + f"{nombre_registro}: {respuesta.to_text()}")
	    except Exception as e:
	        print(Fore.RED + f'No se puede resolver el registro {registro_dns}: {e}')

else:
    print(Fore.RED + "[!] Uso: python3 " + sys.argv[0] + " -t google.com")

