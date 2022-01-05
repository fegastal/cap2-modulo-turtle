'''

Exercícios Teóricos | Capítulo 02 | Módulo Turtle


1) O QUE ENTENDE POR CONSTRUTOR?

São geralmente usados para instanciar* um objeto.

*Obs: Um objeto é uma instância de uma classe. Ou seja, uma representação da classe. Por exemplo,
Regis é uma instância de uma classe chamada Pessoa, mas a Pessoa é a classe que o representa de uma
forma genérica. Se você criar um outro objeto chamado Fabio, esse objeto também será uma instancia da
classe Pessoa.

A tarefa dos construtores é inicializar (atribuir valores)
aos membros de dados da classe quando um objeto da classe é criado. Em Python, o método __init __() é chamado
de construtor e é sempre chamado quando um objeto é criado.

Sintaxe de declaração de um construtor:

def __init__ (self):
    #corpo do construtor

a) construtor padrão: é um construtor simples que não aceita nenhum argumento. Sua definição tem apenas
um argumento que é uma referência à instância sendo construída (apenas SELF).

class GeekforGeeks:


    def __init__(self):
        self.geek = "GeekforGeeks"


    def print_Geek(self):
        print(self.geek)


obj = GeekforGeeks()
obj.print_Geek()

Resultado: GeekforGeeks

b) construtor com parâmetros (parametrizado) toma seu primeiro argumento como uma referência à instância
que está sendo construída, conhecida como self, e *o resto dos argumentos são fornecidos pelo programador*.

class Addition:
    first = 0
    second = 0
    answer = 0


    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second
obj = Addition(1000, 2000)
obj.calculate()
obj.display()

Resultado:
Primeiro número = 1000
Segundo número = 2.000
Adição de dois números = 3000


2) Quais são as operações básicas sobre tartarugas?

Turtle()	None	Creates and returns a new turtle object
forward()	amount	Moves the turtle forward by the specified amount
backward()	amount	Moves the turtle backward by the specified amount
right()	angle	Turns the turtle clockwise
left()	angle	Turns the turtle counterclockwise
penup()	None	Picks up the turtle’s Pen
pendown()	None	Puts down the turtle’s Pen
up()	None	Picks up the turtle’s Pen
down()	None	Puts down the turtle’s Pen
color()	Color name	Changes the color of the turtle’s pen
fillcolor()	Color name	Changes the color of the turtle will use to fill a polygon
heading()	None	Returns the current heading
position()	None	Returns the current position
goto()	x, y	Move the turtle to position x,y
begin_fill()	None	Remember the starting point for a filled polygon
end_fill()	None	Close the polygon and fill with the current fill color
dot()	None	Leave the dot at the current position
stamp()	None	Leaves an impression of a turtle shape at the current location
shape()	shapename	Should be ‘arrow’, ‘classic’, ‘turtle’ or ‘circle’


3) De que modo se definem novas formas de tartarugas?

import turtle

# Possíveis formatos
# -> arrow (seta)
# -> blank (invisível)
# -> circle (círculo)
# -> classic (clássica)
# -> square (quadrado)
# -> triangle (triângulo)
# -> turtle (tartaruga)

tartaruga = turtle.Turtle()
tartaruga.shape("turtle")

4) Quais são as principais configurações para a tartaruga?

a) ALTERAR COR

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.color("medium aquamarine")

Obs: lista de cores em https://trinket.io/docs/colors

b) FRENTE

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.forward(100)

c) ATRÁS

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.back(100)

d) DIREITA

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.right(90)
tartaruga.fd(100)

e) ESQUERDA

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.left(90)
tartaruga.fd(100)

f) setposition: movimenta a tartaruga para a posição específica em x e y

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.setpos(100, 100)

g) setx(<x>) — movimenta a tartaruga para a posição x (relativa ao eixo x)

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.setx(100)

h) sety(<y>) — movimenta a tartaruga para a posição y (relativa ao eixo y)

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.sety(100)

i) pos() ou position() — retorna uma tupla contendo a posição (x e y) atual da tartaruga

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.forward(100)
tartaruga.left(90)
tartaruga.back(50)
print(tartaruga.pos())

j) home() — movimenta a tartaruga para a origem do sistema de coordenadas (centro do canvas)

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.setx(100)
tartaruga.sety(300)
tartaruga.home()

k) circle (raio)

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.circle(50)

5) Quais são as principais formas de controle da caneta?

a) penup() — desativando a caneta, movimentos com a tartaruga não realizam desenhos

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
# Desativando a caneta
tartaruga.penup()
# Faça 4 vezes
for step in range(0, 4):
    tartaruga.forward(200)
    tartaruga.right(90)

b) pendown() — ativando a caneta, movimentos com a tartaruga realizam desenhos:

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
# Desativando a caneta
tartaruga.penup()
# Faça 4 vezes
for step in range(0, 4):
    tartaruga.forward(200)
    tartaruga.right(90)
# Ativando a caneta
tartaruga.pendown()
# Faça 4 vezes
for step in range(0, 4):
    tartaruga.forward(200)
    tartaruga.left(90)

c) speed(<velocidade>) — indica a velocidade da caneta, sendo um valor entre 1 e 10:

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
# Deixando a tartaruga bem lenta
tartaruga.speed(1)
# Faça 4 vezes
for step in range(0, 4):
    tartaruga.forward(200)
    tartaruga.right(90)

d) pencolor(<cor>) — indica a cor da caneta:

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
# Alterando a cor da caneta
tartaruga.pencolor("blue")
# Faça 4 vezes
for step in range(0, 4):
    tartaruga.forward(200)
    tartaruga.right(90)

e) pensize() — indica o tamanho da caneta:

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
# Alterando o tamanho da caneta
tartaruga.pensize(5)
# Faça 4 vezes
for step in range(0, 4):
    tartaruga.forward(200)
    tartaruga.right(90)

6) Quais são os métodos especiais de desenho?

a) stamp() — realiza um carimbo da tartaruga no canvas

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.fillcolor("aquamarine")
# Desenha um círculo e dá 3 voltas.
for step in range(0, 90):
    tartaruga.forward(10)
    tartaruga.left(4)
    # A cada 20 passos
    if step % 10 == 0:
        tartaruga.stamp()

b) write(<string>, <move>, <alinhamento>, <font>) — Escreve um texto no canvas conforme string passada e demais argumentos.
-> string — string a ser escrita. Caso não seja passada uma string, será feita uma conversão automática para o tipo string;
-> move — True ou False. Indica se a tartaruga deve se mover até o final do texto escrito;
-> alinhamento — “right”, “left” ou “center”;
-> font —Uma tupla contendo o nome da fonte, tamanho e tipo (italic, normal ou bold).

import turtle

tartaruga = turtle.Turtle()

# Apontando pra baixo e removendo a caneta
tartaruga.right(90)
tartaruga.penup()
fonte1 = ("Comic Sans", 20, "italic")
tartaruga.write("Curso", False, "center", fonte1)
tartaruga.forward(40)
fonte2 = ("Comic Sans", 20, "normal")
tartaruga.write("de", False, "center", fonte2)
tartaruga.forward(40)
fonte3 = ("Comic Sans", 30, "bold")
tartaruga.write("Programação", False, "center", fonte3)

c) clear() — limpa todo o canvas, removendo tudo que foi desenhado;

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.fillcolor("aquamarine")
# Desenha um círculo e dá 3 voltas.
for step in range(0, 90):
    tartaruga.forward(10)
    tartaruga.left(4)
# A cada 20 passos
    if step % 10 == 0:
        tartaruga.stamp()
# Limpando tela
tartaruga.clear()

d) fillcolor(<cor>) — indica a cor de preenchimento da tartaruga:

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
# Alterando a cor de preenchimento
tartaruga.fillcolor("blue")

e) begin_fill() — indica que a próxima forma desenhada devem ser preenchidas (deve ser utilizado com end_fill());

f) end_fill() — indica que a forma já terminando de ser desenhada e pode ser preenchida (deve ser utilizado com end_fill());

import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
# Cor para o quadrado
tartaruga.fillcolor("light cyan")
tartaruga.begin_fill()
# Desenhando um quadrado
tartaruga.forward(100)
tartaruga.left(90)
tartaruga.forward(200)
tartaruga.left(90)
tartaruga.forward(200)
tartaruga.left(90)
tartaruga.forward(200)
tartaruga.left(90)
tartaruga.forward(100)
# Terminando de desenhar um quadrado
tartaruga.end_fill()
# cor para o círculo
tartaruga.fillcolor("aquamarine")
tartaruga.begin_fill()
# Desenhando um círculo
tartaruga.circle(50)
# Terminando de desenhar um círculo
tartaruga.end_fill()

7) Quais são os tipos de alterações no canvas (tela)?

import Turtle
tela = turtle.Screen()

a) BACKGROUND (COLOR)

import turtle
tela = turtle.Screen()
tela.bgcolor("pink")

b) BACKGROUND (IMAGE)

import turtle
tela = turtle.Screen()
# Somente imagens do tipo .gif
tela.bgpic("background.gif")

c) register_shape (<imagem>)— cadastra uma forma ou imagem para ser posteriormente utilizado pela tartaruga:

import turtle
tartaruga = turtle.Turtle()
# Imagens
pokemons = ["pikachu.gif", "bulbassaur.gif", "charizard.gif", "squirtle.gif"]
# Posicao de cada imagem
posicoes = [(200, 200), (-200, 200), (-200, -200), (200, -200)]
tartaruga.penup()
# Registrando a imagem, mudando a forma e carimbando
for pokemon, posicao in zip(pokemons, posicoes):
    turtle.register_shape(pokemon)
    tartaruga.shape(pokemon)
    tartaruga.setpos(posicao)
    tartaruga.stamp()

d) screensize(<largura>, <algura>, <cor_de_fundo>) — altera o tamanho da janela e, opcionalmente, a cor de fundo.


8) O que distingue uma função de um método e de um procedimento?

a) funções: todo procedimento que retorna algo. É um pedaço de código que é chamado pelo nome.
Pode ser passado dados para operar (isto é, os parâmetros) e pode opcionalmente retornar dados (o valor de retorno).
Todos os dados que são passados para uma função são explicitamente passados.

b) métodos: todo procedimento que não retorna nada. É um pedaço de código que é chamado por um nome associado a um objeto.
Na maioria dos aspectos, é idêntico a uma função, exceto por duas diferenças principais:

Um método é implicitamente passado o objeto no qual ele foi chamado;
Um método é capaz de operar em dados que estão contidos dentro da classe (lembrando que um objeto é uma
instância de uma classe - a classe é a definição, o objeto é uma instância desses dados).

c) procedimento: seria a base de classificação dos anteriores, algo que executa instruções,
seja com intuito ou não de retornar.

Em geral: métodos são funções que pertencem a uma classe, funções podem estar em qualquer outro
escopo do código, então você poderia afirmar que todos os métodos são funções, mas nem todas as funções são métodos:

Tome o seguinte exemplo de python:

class Door:
  def open(self):
    print 'hello stranger'

def knock_door:
  a_door = Door()
  Door.open(a_door)

knock_door()

O exemplo dado mostra uma classe chamada "Porta" que tem um método ou ação chamada "aberta",
é chamada de método porque foi declarada dentro de uma classe. Existe outra parte do código com "def" logo
abaixo que define uma função, é uma função porque não é declarada dentro de uma classe, essa função chama
o método que definimos dentro de nossa classe como você pode ver e finalmente a função está sendo chamado por si só.

Como você pode ver, você pode chamar uma função em qualquer lugar, mas se você quiser chamar um método,
você tem que passar um novo objeto do mesmo tipo da classe que o método é declarado (Class.method (object)) ou
você deve invocar o método dentro do objeto (object.Method ()), pelo menos em python.

Pense em métodos como coisas que apenas uma entidade pode fazer, portanto, se você tiver uma classe Dog,
faria sentido ter uma função de casca somente dentro dessa classe e isso seria um método, se você também tiver
uma classe Person, poderia fazer sentido escreva uma função "feed" para que não pertença a nenhuma classe,
pois humanos e cães podem ser alimentados e você poderia chamar isso de uma função, já que ela não pertence a
nenhuma classe em particular.


9) Como podemos controlar a escala do nosso desenho?

Página 51: "O uso da operação chamada "setworldcoordinates" é fundamental para a visualização,
pois adapta a janela à escala de valores com que estamos a trabalhar. Se não a usarmos, na prática,
não vemos o gráfico.

Sinceramente, não encontrei uma boa resposta para essa questão. Pendente.

7) Qual é a finalidade de exitonclick()?

Esta função é usada para entrar no loop principal até que o mouse seja clicado. Não requer nenhum argumento.
Método Bind bye () para clicar em TurtleScreen. Se using_IDLE - o valor no dicionário de configuração for False
(valor padrão), insira mainloop. Se IDLE com a opção -n (sem subprocesso) for usado, este valor deve ser definido
como True em turtle.cfg. Neste caso, o mainloop do IDLE está ativo também para o script do cliente.

Syntax : turtle.exitoncick()
Parameters : None
Returns : Nothing

Exemplo:

# import package
import turtle

# loop for motion
for i in range(3):
  turtle.circle(40)
  turtle.right(120)

# exit from the screen
# if and only if
# mouse is clicked
turtle.exitonclick()


8) Porque podemos usar funções como argumentos de funções e que consequências existem desse facto?

"Finalmente,o fato de podermos usar uma função como argumento de uma outra função, mostrando, mais uma vez,
que em Python tudo são objetos." Página 51

Sinceramente, também não encontrei ainda uma boa resposta para essa questão. Pendente.
'''



