# ETEC DE SANTA ROSA DE VITERBO
## PROGRAMAÇÃO DE JOGOS DIGITAIS

<br>

# VIKLO PERFUMES: DESENVOLVIMENTO DE UM SISTEMA WEB PARA CATÁLOGO, BUSCA DINÂMICA E GESTÃO DE PRODUTOS DE PERFUMARIA
### Desenvolvimento de uma vitrine digital responsiva utilizando Python, Django e Bootstrap 5

<br>

**Nikolas Marques Menegatti**  
**Pablo Rosê Alves De Moraes**  
**Vitor Hugo de Oliveira**  

**Professor orientador: Daniel Luis Dias da Silva**  
**Professora orientadora: Elisângela Gimenes**

<br>

---

### RESUMO

O presente artigo científico relata o desenvolvimento do sistema VIKLO Perfumes, uma aplicação web concebida para atuar como vitrine digital e gerenciador de catálogo de produtos voltado ao segmento de perfumaria e fragrâncias. O objetivo geral da pesquisa consistiu em projetar, implementar e validar uma plataforma dinâmica, intuitiva e responsiva que ofereça navegação eficiente com busca textual, paginação e visualização de múltiplas imagens em alta definição, associada a um fluxo simplificado de cadastro. A metodologia adotada fundamentou-se em uma abordagem aplicada e experimental de engenharia de software, desenvolvida sob o padrão arquitetural Model-View-Template (MVT) do framework Django (Python), empregando o banco de dados relacional SQLite, a biblioteca Pillow para manipulação e validação de imagens, e estilização front-end com Bootstrap 5 em tema escuro (*Dark Mode*). Como principais resultados, obteve-se um sistema estável que realiza consultas otimizadas por meio de operadores lógicos (*Q objects*), gerencia a paginação em lotes de 12 itens e preserva a integridade referencial dos dados por meio de relacionamentos de cardinalidade 1:N com exclusão em cascata (*CASCADE*) entre perfumes e suas imagens complementares. A discussão dos resultados demonstrou a eficácia do ecossistema Django na redução do tempo de desenvolvimento e no fornecimento de mecanismos nativos de segurança contra vulnerabilidades web. Conclui-se que a solução atende com rigor técnico aos requisitos propostos, destacando-se como uma alternativa viável para pequenos empreendimentos e consolidando competências fundamentais de programação web full-stack no âmbito do ensino técnico profissionalizante.

**Palavras-chave:** Desenvolvimento Web; Django; Python; Catálogo Digital; Banco de Dados Relacional.

---

## 1 INTRODUÇÃO

O mercado global e nacional de perfumaria e cosméticos experimentou uma intensa transformação com a consolidação dos canais digitais de comércio e divulgação. Em um setor no qual a percepção de valor está fortemente vinculada à identidade visual, à sofisticação das embalagens e à detalhada descrição das notas olfativas, a presença na internet deixou de ser apenas um diferencial competitivo e passou a constituir um requisito indispensável de sobrevivência comercial. As vitrines digitais tornaram-se o ponto de contato primordial entre marcas e consumidores, exigindo interfaces interativas, ágeis e esteticamente refinadas, capazes de simular o ambiente sensorial e sofisticado das boutiques físicas de perfumaria.

Apesar da relevância desse mercado, pequenas marcas, revendedores autônomos e empreendimentos regionais enfrentam entraves substanciais para estruturar uma presença digital eficiente e profissional. A utilização de redes sociais como vitrine primária impõe limitações estruturais severas, tais como a ausência de mecanismos eficientes de busca textual, a dificuldade de organização por categorias olfativas e a falta de galerias dedicadas por produto. Em contrapartida, a adesão a plataformas proprietárias de comércio eletrônico frequentemente implica custos de implantação elevados, taxas recorrentes e complexidades operacionais incompatíveis com a necessidade de um catálogo dinâmico e direto. Diante desse cenário, formula-se o problema de pesquisa: como conceber e desenvolver uma aplicação web acessível, responsiva e robusta que atenda com eficácia às necessidades de catalogação, busca e exibição multimídia de produtos de perfumaria?

A justificativa para a execução deste estudo reside na relevância de disponibilizar uma solução tecnológica independente e personalizável, proporcionando uma vitrine moderna sem onerar o lojista com custos abusivos de manutenção. Paralelamente, no âmbito da formação técnica em nível médio no Centro Paula Souza, o projeto reveste-se de profundo valor pedagógico ao congregar conhecimentos interdisciplinares de análise de sistemas, modelagem de bancos de dados relacionais, lógica de programação em linguagem orientada a objetos (Python), segurança da informação e construção de interfaces centradas na experiência do usuário (UX/UI).

Diante do problema delineado, o objetivo geral deste trabalho consiste em projetar, desenvolver e validar a aplicação web VIKLO Perfumes, voltada à exibição de catálogo de fragrâncias, filtragem dinâmica e cadastro de produtos com suporte a múltiplas imagens. Para atingir essa meta, estabeleceram-se os seguintes objetivos específicos: a) estruturar uma base de dados relacional normalizada com integridade referencial 1:N entre produtos e suas imagens; b) programar a camada de controle e negócio em Python utilizando o framework Django sob o padrão MVT; c) implementar um mecanismo de busca textual utilizando operadores de consulta composta e paginação dinâmica; d) conceber formulários web com validação e upload simultâneo de múltiplos arquivos; e e) construir uma interface visual responsiva e elegante baseada em Bootstrap 5 com temática *Dark Mode*.

A metodologia adotada caracterizou-se como uma pesquisa aplicada e exploratória, orientada ao desenvolvimento experimental de software em conformidade com as fases clássicas de engenharia de software. Os procedimentos envolveram o levantamento de requisitos, a modelagem conceitual das entidades no banco de dados SQLite, a codificação orientada a objetos com Django 6.1 e Python 3.12, o tratamento de mídias com a biblioteca Pillow e a composição de interfaces com HTML5, CSS3 e Bootstrap 5. Por fim, realizaram-se testes de caixa-preta, validações de responsividade em diferentes resoluções e análises de integridade relacional.

Este artigo está estruturado em cinco seções principais: após esta introdução, a seção 2 apresenta o referencial teórico que embasa o framework Django, a modelagem de dados relacional e os princípios de design de interface responsiva. A seção 3 detalha a metodologia de desenvolvimento e os recursos tecnológicos aplicados. A seção 4 discute os resultados obtidos, detalhando a arquitetura implementada, os módulos desenvolvidos e os testes de software realizados. Por fim, a seção 5 sintetiza as considerações finais, limitações e propostas de trabalhos futuros, sucedida pelas referências bibliográficas adotadas.

---

## 2 REFERENCIAL TEÓRICO

### 2.1 O Framework Django e a Arquitetura MVT

O desenvolvimento de aplicações web modernas requer a utilização de ferramentas que forneçam alta produtividade, manutenibilidade e proteção contra falhas de segurança recorrentes. Nesse contexto, o framework Django, desenvolvido na linguagem Python, destaca-se por sua filosofia *"batteries-included"* (baterias inclusas), a qual disponibiliza nativamente recursos essenciais como autenticação, camada de persistência, proteção contra ataques de injeção de SQL e falsificação de solicitações entre sites (*Cross-Site Request Forgery* - CSRF) (ALCHIN, 2013). Segundo Pressman e Maxim (2016), o uso de frameworks consolidados minimiza erros conceituais no desenvolvimento e eleva a padronização das soluções de software.

O Django estrutura suas aplicações sobre o padrão arquitetural MVT (*Model-View-Template*), que consiste em uma variação adaptada do clássico modelo MVC (*Model-View-Controller*):
- **Model (Modelo):** atua como a representação e definição lógica das entidades do sistema, encapsulando regras de negócio e mapeando campos para tabelas no banco de dados através do ORM (*Object-Relational Mapping*);
- **View (Visão):** opera como a camada controladora da aplicação. Ela processa as requisições HTTP, executa a lógica de consulta aos modelos e seleciona o template apropriado com seu contexto de dados;
- **Template (Modelo de Apresentação):** constitui a camada de interface gráfica em HTML, combinada à sintaxe de marcação do Django Template Language (DTL), renderizando dinamicamente as respostas visuais ao usuário cliente (DJANGO SOFTWARE FOUNDATION, 2026).

Essa clara separação de responsabilidades viabiliza a manutenção modular do sistema, permitindo que alterações na lógica de persistência ou no estilo visual ocorram de modo desacoplado (SOMMERVILLE, 2018).

### 2.2 Modelagem Relacional de Dados e Processamento de Imagens

Bancos de dados relacionais organizam as informações em entidades e atributos, estruturando vínculos fundamentados na teoria dos conjuntos (SILBERSCHATZ; KORTH; SUDARSHAN, 2020). Em sistemas comerciais e catálogos de produtos, um dos requisitos centrais é a capacidade de associar uma ou mais fotografias complementares a um mesmo produto. Esse cenário exige a implementação de um relacionamento de cardinalidade um-para-muitos (1:N), viabilizado pelo conceito de Chave Estrangeira (*Foreign Key*).

Adicionalmente, a integridade referencial exige que a remoção de um registro principal acarrete a eliminação coerente de seus registros dependentes. No Django, a declaração de atributos como `on_delete=models.CASCADE` garante que, na hipótese de um perfume ser deletado da base de dados, todas as suas fotografias secundárias sejam automaticamente suprimidas, prevenindo a existência de registros órfãos e inconsistências no banco relacional (SILBERSCHATZ; KORTH; SUDARSHAN, 2020).

No que tange ao armazenamento de arquivos multimídia, a integração do Django com a biblioteca **Pillow** capacita a aplicação a validar a autenticidade dos arquivos de imagem no instante do upload. O Pillow inspeciona o cabeçalho binário dos arquivos, assegurando que apenas imagens válidas (JPEG, PNG, WEBP) sejam persistidas em disco sob o diretório `media/`, protegendo a infraestrutura contra o envio indevido de scripts executáveis camuflados (DEITEL; DEITEL, 2017).

### 2.3 Interface do Usuário, Design Responsivo e a Estética Dark Mode

A qualidade da experiência do usuário (*User Experience* - UX) e a usabilidade da interface (*User Interface* - UI) exercem papel decisivo no engajamento dos consumidores em plataformas de comércio virtual. De acordo com Sommerville (2018), uma interface gráfica eficiente deve antecipar necessidades, fornecer retorno claro para ações operacionais e manter coerência visual em múltiplos dispositivos. O conceito de design responsivo orientado a *Mobile-First* preconiza que a estrutura das páginas seja planejada para telas de dimensões reduzidas e expanda-se progressivamente para monitores de alta resolução.

O framework **Bootstrap 5** consolida esse paradigma por meio de um sistema de grade de doze colunas e classes utilitárias fundamentadas em Flexbox (BOOTSTRAP, 2026). No setor de perfumaria fina, a aplicação de uma estética visual fundamentada em tema escuro (*Dark Mode*), utilizando fundos em tons profundos de grafite (`#080b0f`) contrastados com tipografia nítida e elementos de destaque, evoca sofisticação, nobreza e modernidade, ao mesmo tempo em que atenua o cansaço visual do usuário durante a exploração contínua do catálogo.

---

## 3 METODOLOGIA

O presente estudo classifica-se metodologicamente como uma **pesquisa aplicada**, orientada ao desenvolvimento experimental de software (tecnológico), com abordagem qualitativa no levantamento de requisitos e quantitativa na aferição de desempenho das consultas e validação dos testes (PRESSMAN; MAXIM, 2016). A pesquisa não envolveu participantes humanos nem procedimentos laboratoriais clínicos, tendo sido integralmente executada em ambiente virtual de desenvolvimento computacional.

O ecossistema tecnológico empregado incluiu:
- Sistema Operacional Microsoft Windows 11;
- Ambiente de Desenvolvimento Integrado (IDE) Visual Studio Code;
- Linguagem de programação Python (versão 3.12);
- Framework web Django (versão 6.1) em ambiente virtual isolado (`ll_web`);
- Banco de dados relacional SQLite 3;
- Biblioteca Pillow (versão 12.3.0) para validação e manipulação de fluxos binários de imagem;
- Framework front-end Bootstrap 5.3 com recursos de HTML5 e CSS3;
- Sistema de controle de versão Git.

O processo de engenharia de software foi subdividido em cinco etapas consecutivas:
1. **Elicitação e Análise de Requisitos:** Definição dos requisitos funcionais (RF) — incluindo listagem paginada, busca por termos compostos, detalhamento com galeria e formulário de cadastro com upload múltiplo — e dos requisitos não-funcionais (RNF) — responsividade, segurança CSRF e integridade relacional.
2. **Modelagem de Dados e Arquitetura:** Especificação dos diagramas conceituais e lógicos, modelando as entidades `Perfume` e `ImagemPerfume` com integridade referencial 1:N no SQLite.
3. **Desenvolvimento do Back-end:** Estruturação das rotas em `urls.py` e codificação das funções controladoras em `views.py`, empregando a classe `Paginator` para paginação e a classe `Q` para consultas disjuntivas no banco de dados.
4. **Construção do Front-end:** Elaboração de templates semânticos em HTML5 integrados à linguagem de templates do Django, com componentização de cards, badges e barras de navegação com Bootstrap 5.
5. **Testes de Software e Validação:** Execução de testes de caixa-preta baseados em matriz de casos de teste manuais, abrangendo fluxos de cadastro, validação de tipos de arquivo, filtragens e responsividade de tela.

---

## 4 RESULTADOS E DISCUSSÃO

### 4.1 Arquitetura do Sistema e Modelo Relacional de Dados

A solução desenvolvida resultou em uma aplicação web coesa, organizada no projeto central `TCC_WEB` e na aplicação modular `TCC_WEBS`. A persistência relacional foi concretizada por meio de dois modelos fundamentais no arquivo `models.py`:

```python
class Perfume(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='perfumes/')
    TIPOS_PERFUME = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('unissex', 'Unissex'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS_PERFUME, default='unissex')

class ImagemPerfume(models.Model):
    perfume = models.ForeignKey(Perfume, on_delete=models.CASCADE, related_name="imagens")
    imagem = models.ImageField(upload_to="perfumes/")
```

A estrutura tabular gerada no SQLite expressa a normalização e a preservação da integridade referencial, conforme sumarizado na Tabela 1:

**Tabela 1 – Estrutura das Tabelas Relacionais do Banco de Dados**

| Tabela | Atributo / Coluna | Tipo de Dado | Restrição / Regra | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `Perfume` | `id` | INTEGER | PRIMARY KEY, AUTO | Identificador exclusivo do perfume |
| `Perfume` | `titulo` | VARCHAR(50) | NOT NULL | Nome comercial da fragrância |
| `Perfume` | `descricao` | TEXT | NOT NULL | Detalhamento das notas e composição |
| `Perfume` | `imagem` | VARCHAR(100) | NOT NULL | Caminho da imagem de capa |
| `Perfume` | `tipo` | VARCHAR(20) | DEFAULT 'unissex' | Categoria: masculino, feminino, unissex |
| `ImagemPerfume` | `id` | INTEGER | PRIMARY KEY, AUTO | Identificador da foto complementar |
| `ImagemPerfume` | `perfume_id` | INTEGER | FOREIGN KEY, CASCADE | Chave estrangeira referenciando `Perfume` |
| `ImagemPerfume` | `imagem` | VARCHAR(100) | NOT NULL | Caminho da imagem secundária |

*Fonte: Elaborado pelos autores (2026).*

A configuração `on_delete=models.CASCADE` garante que todas as fotos associadas na tabela `ImagemPerfume` sejam removidas simultaneamente caso o perfume seja excluído, preservando a integridade do banco e eliminando inconsistências apontadas por Silberschatz, Korth e Sudarshan (2020).

### 4.2 Módulo de Catálogo, Filtragem Dinâmica e Paginação

A visualização do catálogo é operada pela view `catalogo(request)`. O usuário dispõe de um campo de pesquisa textual na barra de navegação superior. A requisição processa parâmetros `GET` e efetua consultas que combinam o título e a descrição através de objetos `Q`:

```python
perfumes = Perfume.objects.all().order_by("id")
busca = request.GET.get("q", "")
if busca:
    perfumes = perfumes.filter(
        Q(titulo__icontains=busca) |
        Q(descricao__icontains=busca)
    )
paginator = Paginator(perfumes, 12)
numero = request.GET.get("page")
pagina = paginator.get_page(numero)
```

Essa lógica oferece uma experiência de busca sem distinção entre letras maiúsculas e minúsculas (`icontains`), permitindo que termos parciais (ex.: "amadeirado" ou "floral") localizem rapidamente os perfumes cuja composição contenha tais características. A limitação a 12 registros por página por meio do `Paginator` evita o consumo excessivo de largura de banda e garante fluidez no carregamento das imagens em redes móveis.

### 4.3 Módulo de Detalhes do Produto e Galeria de Múltiplas Imagens

Ao selecionar um produto na grade, o usuário é direcionado à rota `/perfume/<int:id>/`. A view `detalhes_perfume` resgata o objeto garantindo integridade com `get_object_or_404()`, interceptando identificadores inexistentes e devolvendo adequadamente a resposta HTTP 404.

O relacionamento reverso `perfume.imagens.all()` permite carregar todas as fotografias registradas para aquele produto em uma única consulta otimizada. No template `Detalhes.html`, a imagem principal ganha destaque no quadrante esquerdo, acompanhada de miniaturas das fotos adicionais, viabilizando a apreciação detalhada de ângulos do frasco, da caixa e do selo do cosmético.

### 4.4 Módulo de Cadastro e Upload Múltiplo de Arquivos

O gerenciamento de novos produtos ocorre através da view `formulario(request)` e do formulário HTML com codificação `enctype="multipart/form-data"`. Ao enviar a requisição via `POST`, a aplicação extrai os dados textuais, valida a imagem de capa e utiliza o método `request.FILES.getlist("imagens")` para processar um número indeterminado de fotos extras:

```python
perfume = Perfume.objects.create(
    titulo=titulo, descricao=descricao, imagem=imagem, tipo=tipo
)
imagens = request.FILES.getlist("imagens")
for img in imagens:
    ImagemPerfume.objects.create(perfume=perfume, imagem=img)
```

Essa implementação simplifica drasticamente a rotina do operador do sistema, que cadastra todas as mídias do perfume em uma única etapa, dispensando telas intermediárias de upload.

### 4.5 Avaliação dos Testes e Validação do Software

Para verificar a confiabilidade da aplicação, realizou-se uma série de testes funcionais manuais (*black-box testing*). Os cenários avaliados e os respectivos comportamentos observados estão compilados no Quadro 1:

**Quadro 1 – Matriz de Casos de Teste e Validação da Aplicação**

| Caso | Funcionalidade Testada | Entrada / Ação Executada | Resultado Esperado | Situação |
| :---: | :--- | :--- | :--- | :---: |
| **CT-01** | Redirecionamento da Raiz | Acessar rota raiz `/` no navegador | Redirecionar com código HTTP 302 para `/catalogo/` | Aprovado |
| **CT-02** | Busca Textual Positiva | Digitar "masculino" no campo de busca | Exibir apenas produtos com o termo no título ou descrição | Aprovado |
| **CT-03** | Busca Textual Inexistente | Digitar termo inexistente (ex.: "xyz123") | Exibir grade vazia mantendo a integridade da navbar | Aprovado |
| **CT-04** | Cadastro com Mídia Única | Submeter formulário com 1 foto de capa | Salvar perfume e redirecionar para o catálogo | Aprovado |
| **CT-05** | Cadastro com Múltiplas Mídias | Submeter formulário com capa + 3 fotos extras | Criar 1 `Perfume` e 3 `ImagemPerfume` com arquivos salvos em `media/` | Aprovado |
| **CT-06** | Acesso a ID Inválido | Acessar `/perfume/9999/` | Retornar erro HTTP 404 via `get_object_or_404()` | Aprovado |
| **CT-07** | Paginação Dinâmica | Navegar para `/catalogo/?page=2` | Carregar os 12 itens seguintes sem quebra de sessão | Aprovado |
| **CT-08** | Responsividade Mobile | Redimensionar viewport para 375px (smartphone) | Empilhar cards em coluna única com navbar compacta | Aprovado |

*Fonte: Elaborado pelos autores (2026).*

A análise dos resultados atesta que a aplicação atingiu plenamente a estabilidade operacional estipulada nos requisitos de projeto. Os tempos de resposta mantiveram-se reduzidos e a integridade das imagens foi assegurada pela cooperação entre o ORM do Django e o pacote Pillow.

---

## 5 CONSIDERAÇÕES FINAIS

O presente trabalho teve por finalidade projetar, implementar e validar o sistema web **VIKLO Perfumes**, suprindo a carência de vitrines digitais dinâmicas, leves e visualmente atrativas para o setor de cosméticos e fragrâncias. Diante dos resultados apresentados, constata-se que o objetivo geral e os objetivos específicos foram plenamente alcançados, comprovando que o uso combinado do framework Django e de uma interface responsiva baseada em Bootstrap 5 em modo escuro proporciona uma solução altamente estável, segura e elegante.

A arquitetura MVT provou ser um alicerce robusto, permitindo o isolamento entre regras de negócio, persistência de dados e apresentação visual. A modelagem 1:N com integridade em cascata resolveu com simplicidade a exigência comercial de galerias fotográficas completas para cada produto, enquanto a busca com objetos `Q` e a paginação conferiram dinamismo e conforto na navegação.

Como limitações identificadas na versão atual do software, destacam-se a ausência de um carrinho de compras para cálculo de frete e checkout de pedidos, a inexistência de login de clientes externos para gestão de listas de desejos e a utilização do SQLite, que, embora satisfatório para desenvolvimento e homologação local, deve ser substituído em cenários de alta concorrência simultânea.

Por fim, sugerem-se como trabalhos futuros:
1. Implantação de sistema de autenticação de usuários com perfis diferenciados (administrador, lojista e cliente);
2. Integração de carrinho de compras e módulo de pagamentos com provedores como Stripe ou Mercado Pago;
3. Migração do banco de dados para o PostgreSQL e publicação da aplicação em ambiente de computação em nuvem (PaaS como Render, Railway ou AWS);
4. Conexão do armazenamento de arquivos de mídia com servidores externos de armazenamento de objetos (Amazon S3 ou Cloudinary).

---

## REFERÊNCIAS

ALCHIN, Marty. **Pro Django**. 2. ed. Nova Iorque: Apress, 2013.

BOOTSTRAP. **Bootstrap: Powerful, extensible, and feature-packed frontend toolkit**. Versão 5.3. Disponível em: <https://getbootstrap.com/>. Acesso em: 11 nov. 2026.

DEITEL, Paul; DEITEL, Harvey. **Python: como programar**. São Paulo: Pearson Education do Brasil, 2017.

DJANGO SOFTWARE FOUNDATION. **Django documentation**. Versão 6.1. Disponível em: <https://docs.djangoproject.com/>. Acesso em: 11 nov. 2026.

PRESSMAN, Roger S.; MAXIM, Bruce R. **Engenharia de software: uma abordagem profissional**. 8. ed. Porto Alegre: AMGH Editora, 2016.

SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. **Sistema de banco de dados**. 7. ed. Rio de Janeiro: Elsevier, 2020.

SOMMERVILLE, Ian. **Engenharia de software**. 10. ed. São Paulo: Pearson Education do Brasil, 2018.


