PROJETO ANÁLISE DE LOG (MÓDULO 3 CURSO FULL-STACK WEBDEV)
REQUISITOS:
* Sistema Operacional Windows 7 ou superior
* Sistema Vagrant e VirtualBox para acesso a uma MV Linux

INSTRUÇÕES BÁSICAS:
* iniciar a MV em um terminal de sua escolha (preferência Bash) e executar o comando vagrant up para iniciar a MV
* vagrant ssh para iniciar o sistema virtual Linux
* Baixar o banco de dados em https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
* para importar os dados do arquivo SQL, ao banco de dados, se necessário, utilize o comando
"psql -d news -f newsdata.sql"

COMO FUNCIONA:
Este projeto lê os dados de um log e apresenta as seguintes informações:
1) Os três artigos mais populares de todos os tempos.
2) Quem são os autores de artigos mais populares de todos os tempos.
3) Em quais dias mais de 1% das requisições resultaram em erros.

PASSO A PASSO:
1) com a maquina virtual acionada no terminal de sua preferência, acesse a pasta /vagrant
2) Então, execute o arquivo do servidor com o comando python news.py (lembrando que é necessário que todos os arquivos do projeto estejam na pasta /vagrant)
3) É importante executar e criar as views informadas na ultima sessão deste README para que o projeto funcione corretamente.
4) No terminal execute o comando "python news.py", que executará o programa python e automaticamente mostrará as perguntas e os resultados no terminal.

-----------------------------------------
 DETALHES TÉCNICOS:
 1) CREATE VIEW
 foram utilizados dois create view em sql para responder a 3a pergunta, que seguem abaixo:

 create view totalerrors as (
   select time::date as day, count(*) as errors
   from log where status like '4%'
   group by day
 )

 create view totalperday as (
   select time::date as day, count (*) as total
   from log group by day
 )

 2) CÓDIGO DE REFERÊNCIA
 foi utilizado o como base o código da atividade forum do curso. Por isso, serão encontrados métodos ou códigos diversos comentados, como por exemplo o método add_post() que não foi necessário.

 3) o arquivo news.py corresponde ao servidor. O arquivo newsdb.py corresponde aos comandos para acesso ao banco de dados.
