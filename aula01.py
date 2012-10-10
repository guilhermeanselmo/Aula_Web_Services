import urllib2
import json
import sys
import Image

try:
  r = urllib2.urlopen('https://api.github.com/users/{0}'.format(sys.argv[1]))
except:
  exit(0)
dados = json.loads(r.read())

#print dados

print 'Nome: {0}'.format(dados['login'])
print 'URL: {0}'.format(dados['url'])
print 'ID: {0}'.format(dados['id'])

#print dados['avatar_url']
img = urllib2.urlopen(dados['avatar_url']).read()
nome = 'img' + dados['avatar_url'][len(dados['avatar_url']) - 4:]
#print nome
arq = open(nome, 'w')
arq.write(img)
arq.close()
Image.open(nome).show()

