# PHC CS WEB FRAMEWORK SCRIPT MANAGER

> Ferramenta para transformar os scripts da framework web em ficheiros locais, que podem ser editados e importados de volta à base de dados.

## ⚙️ Instalação & Configuração

Para o script **funcionar corretamente** é necessário:

1. Inserir o script dentro de uma sub-pasta na pasta do ambiente de desenvolvimento, exemplo:
```
phcDevelopment/
|
├──scriptManager/
|  ├── scriptManager.py
|  ├── config.cfg
|  └── py/
|      └──(...)

```
2. Ter o [Python3](https://www.python.org) instalado na máquina
3. Instalar a biblioteca pyobdc
```bash
pip install pyodbc
```
4. Alterar o nome do arquivo `config-template.cfg` para `config.cfg`
5. Preencher o `config.cfg` com os dados do servidor e da base de dados

## 👨‍💻 Utilização

Para executar o script, basta abrir a **linha de comandos** dentro da pasta do script e executar: 
```bash
python scriptManager.py
```
Ao que ser-lhe-á apresentado um menu:
```
=== Script Manager PHC Framework 0.1.0

1 - Pull Javascript de Utilizador     

2 - Push Javascript de Utilizador


3 - Pull Scripts Web (VB.NET)

4 - Push Scripts Web (VB.NET)

0 - Quit
```

### Javascript de Utilizador

Em ambas as opções (Pull e Push) do Javascript de Utilizador, existem 2 funções: fazer o pedido **apenas a um** Javascript de Utilizador, ou a **todos** os Javascripts de Utilizador.

>#### Caso selecione o pedido somente a um Javascript de Utilizador...
> ser-lhe-á pedido o título do script que inseriu no campo **Descrição** ao criá-lo diretamente no PHC CS Web
> 
> <img src="https://i.imgur.com/GY976rv.png" style="height: 250px"><br>
> Seguindo o exemplo da imagem, **o título a inserir seria "teste"**

#### 📥 Pull dos Javascripts de Utilizador

Ao receber os Javascripts de Utilizador, os mesmos serão guardados numa pasta fora do diretório do scriptManager, chamada **"jsUtilizador/"**, onde o nome dos sub-diretórios será a descrição do script e o conteúdo será o `{stamp}.js`.
```
phcDevelopment/
|
├──scriptManager/
|  ├── scriptManager.py
|  ├── config.cfg
|  └── py/
|      └──(...)
| 
|──jsUtilizador/
|  ├── teste/
|  |   └──{stampdoteste}.js
|  ├── adicionarObjeto
|  |   └──{stampdoadicionarObjeto}.js
|  └── script/
|      └──{stampdoscript}.js
```

#### 📤 Push dos Javascripts de Utilizador

Para enviar os Javascripts de Utilizador, é bastante similar ao Pull, podemos enviar somente um, colocando a **descrição** do mesmo, ou podemos enviar todos os que temos na pasta `/jsUtilizador`.

### Scripts Web (VB.NET)

Em ambas as opções (Pull e Push) dos Scripts, existem 2 funções: fazer o pedido **apenas a um** Script, ou a **todos**.

>#### Caso selecione o pedido somente a um Script...
> ser-lhe-á pedido o código do Script que inseriu no campo **Código** ao criá-lo diretamente no PHC CS Web
> 
> <img src="https://i.imgur.com/4LQak6V.png" style="height: 275px"><br>
> Seguindo o exemplo da imagem, **o código a inserir seria "teste"**

#### 📥 Pull dos Scripts Web (VB.NET)

Ao receber os Scripts, os mesmos serão guardados numa pasta fora do diretório do scriptManager, chamada **"webScriptsVB/"**, onde o nome dos sub-diretórios será o código do Script e o conteúdo será o `{stamp}.vb`.
```
phcDevelopment/
|
├──scriptManager/
|  ├── scriptManager.py
|  ├── config.cfg
|  └── py/
|      └──(...)
| 
|──webScriptsVB/
|  ├── teste/
|  |   └──{stampdoteste}.vb
|  ├── adicionarObjeto
|  |   └──{stampdoadicionarObjeto}.vb
|  └── script/
|      └──{stampdoscript}.vb
```

#### 📤 Push dos Scripts Web (VB.NET)

Para enviar os Scripts Web, é bastante similar ao Pull, podemos enviar somente um, colocando o **código** do mesmo, ou podemos enviar todos os que temos na pasta `/webScriptsVB`.