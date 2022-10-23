<h1 align="center"> Anotações sobre as aulas de poo <h1>

## Etapa 1: 
### Classes e objetos:

- __Classe__: Define características e comportamentos de um objeto.
- __Objetos__: São utilizaveis e possuem características/comportamentos definidos dentro da classe.

### Construtores e destrutores:
- __init__: O metodo construtor sempre é executado quando uma nova instância de classe é criada.
- __del__: Sempre executado quando uma instância é destruida, não é tão utilizado em python.

### Herança: 
Capacidade de uma classe filha derivar/herdar características e comportamentos de uma classe pai.

__Benefícios__:
- Fornece reutilização de código.
- Natureza transitiva.

__Herança simples__: Quando uma classe filha herda apenas uma classe pai.
__Herança múltipla__: Quando uma classe filha herda de várias classes pai.

### Encapsulamento: 

__Proteção de acesso__:
O encapsulamento descreve a ideia de agrupar dados e métodos que manipulam dados em uma unidade.
Isso impõe restrições ao acesso direto de variáveis ​e métodos, assim pode evitar a modificação acidental de
dados. Para isso a variável de um objeto só pode ser alterada pelo método desse objeto.

__Modificadores de acesso__:
Em python não existem palavras reservadas para se definir o nível de acesso, pois todos os recursos são públicos, mas se utiliza a convenção de que variaveis e metodos que começam com underline "_" não devem ser manipuladas diretamente.

- __Público__: Pode ser acessado fora da classe.
- __Privado__: Só pode ser acessado pela classe.

__Properties__:
Com "property()" pode-se criar atributos gerenciados em classes, também conhecidos como propriedades, eles podem ser utilizados quando é necessário modificar sua implementação interna sem a alterção da API pública da classe.

### Polimorfismo: 
Mesmo nome de função, com assinaturas diferentes, que são usadas para tipos diferentes.

__Polimorfismo com herança__:
Quando uma classe filha herda métodos de uma classe pai é possivel modificar esses métodos herdades. O que é util quando os métodos de uma classe pai não se encaixam perfeitamente na classe filha.


### Ampliando conceitos:

__Atributos de objeto__:
As Variaveis de classe são compartilhados para todos os objetos, mas os de instância são únicos para cada um dos objetos.

__Metodos__:

- __Método de classe__: Os métodos estão ligados a classe e não ao objeto, possuem acesso ao estado da classe, precisa de acesso ao contexto da classe. Geralmente utilizado para métodos de fábrica (método que retorna instâncias da classe)

- __Método estático__: Não recebe argumento explícito, é ligado à classe e não ao objeto e não pode acessar-la ou modifica-la. Não precisa de acesso ao contexto de classe. Geralmente utilizado para criar funções utilitárias

__Interfaces__:
Interface define o que uma classe deve fazer e não como. Interfaces definem um contrato, onde são declarados métodos e suas assinaturas. Em python as classes abstratas são utilizadas para criar contratos e essas classes não podem ser instanciadas.
Python não fornece classes abstratas por padrão, mas possui o módulo abc que fornece a base para classes abstratas O ABC funciona decorando métodos da classe base como abstratos e registra classes concretas como implementações da base abstrata. Um méto é abstrado quando é decorado com _"@abstractmethod"_.
