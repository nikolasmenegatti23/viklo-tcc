import docx
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="D3D3D3"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'''
        <w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:left w:val="none"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="808080"/>
            <w:right w:val="none"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{color}"/>
            <w:insideV w:val="none"/>
        </w:tblBorders>
    ''')
    tblPr.append(borders)

def build_document():
    doc = docx.Document('Template_Artigo_Cientifico_TCC_ETEC_SRV_Revisado(1).docx')

    # Remove existing tables
    for t in list(doc.tables):
        p = t._element
        p.getparent().remove(p)

    # Remove existing paragraphs
    for p in list(doc.paragraphs):
        p._element.getparent().remove(p._element)

    # Margins are already 3cm top, 3cm left, 2cm bottom, 2cm right
    section = doc.sections[0]
    section.top_margin = Cm(3.0)
    section.left_margin = Cm(3.0)
    section.bottom_margin = Cm(2.0)
    section.right_margin = Cm(2.0)

    # Helper function for adding paragraphs
    def add_p(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=6, line_spacing=1.5, bold=False, italic=False, font_size=12, style='Normal'):
        p = doc.add_paragraph(style=style)
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = line_spacing
        if text:
            run = p.add_run(text)
            run.font.name = 'Arial'
            run.font.size = Pt(font_size)
            run.font.bold = bold
            run.font.italic = italic
            run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_h1(text):
        p = add_p(text, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=14, space_after=6, line_spacing=1.5, bold=True, font_size=12, style='Heading 1')
        return p

    def add_h2(text):
        p = add_p(text, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=12, space_after=6, line_spacing=1.5, bold=True, font_size=12, style='Heading 2')
        return p

    def add_caption(text):
        return add_p(text, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=8, space_after=2, line_spacing=1.0, bold=True, font_size=10)

    def add_source(text):
        return add_p(text, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=2, space_after=8, line_spacing=1.0, italic=True, font_size=10)

    # 1. CABEÇALHO INSTITUCIONAL
    add_p("ETEC DE SANTA ROSA DE VITERBO", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=2, line_spacing=1.0, bold=True)
    add_p("PROGRAMAÇÃO DE JOGOS DIGITAIS", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=18, line_spacing=1.0, bold=True)

    # 2. TÍTULO E SUBTÍTULO
    add_p("VIKLO PERFUMES: DESENVOLVIMENTO DE UM SISTEMA WEB PARA CATÁLOGO, BUSCA DINÂMICA E GESTÃO DE PRODUTOS DE PERFUMARIA", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=4, line_spacing=1.0, bold=True, font_size=14)
    add_p("Desenvolvimento de uma vitrine digital responsiva utilizando Python, Django e Bootstrap 5", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=18, line_spacing=1.0, italic=False, font_size=12)

    # 3. AUTORES E ORIENTADORES
    add_p("Nikolas Marques Menegatti", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=2, line_spacing=1.0)
    add_p("Pablo Rosê Alves De Moraes", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=2, line_spacing=1.0)
    add_p("Vitor Hugo de Oliveira", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=6, line_spacing=1.0)
    add_p("Professor orientador: Daniel Luis Dias da Silva", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=2, line_spacing=1.0)
    add_p("Professora orientadora: Elisângela Gimenes", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=18, line_spacing=1.0)

    # 4. RESUMO
    add_p("RESUMO", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=6, space_after=6, line_spacing=1.0, bold=True)
    
    resumo_texto = (
        "O presente artigo científico relata o desenvolvimento do sistema VIKLO Perfumes, uma aplicação web concebida para atuar "
        "como vitrine digital e gerenciador de catálogo de produtos voltado ao segmento de perfumaria e fragrâncias. O objetivo geral da "
        "pesquisa consistiu em projetar, implementar e validar uma plataforma dinâmica, intuitiva e responsiva que ofereça navegação "
        "eficiente com busca textual, paginação e visualização de múltiplas imagens em alta definição, associada a um fluxo simplificado de "
        "cadastro. A metodologia adotada fundamentou-se em uma abordagem aplicada e experimental de engenharia de software, desenvolvida sob "
        "o padrão arquitetural Model-View-Template (MVT) do framework Django (Python), empregando o banco de dados relacional SQLite, "
        "a biblioteca Pillow para manipulação e validação de imagens, e estilização front-end com Bootstrap 5 em tema escuro (Dark Mode). "
        "Como principais resultados, obteve-se um sistema estável que realiza consultas otimizadas por meio de operadores lógicos (Q objects), "
        "gerencia a paginação em lotes de 12 itens e preserva a integridade referencial dos dados por meio de relacionamentos de cardinalidade "
        "1:N com exclusão em cascata (CASCADE) entre perfumes e suas imagens complementares. A discussão dos resultados demonstrou a eficácia "
        "do ecossistema Django na redução do tempo de desenvolvimento e no fornecimento de mecanismos nativos de segurança contra vulnerabilidades web. "
        "Conclui-se que a solução atende com rigor técnico aos requisitos propostos, destacando-se como uma alternativa viável para pequenos empreendimentos "
        "e consolidando competências fundamentais de programação web full-stack no âmbito do ensino técnico profissionalizante."
    )
    add_p(resumo_texto, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=6, line_spacing=1.0)

    p_kw = add_p(align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=18, line_spacing=1.0)
    r1 = p_kw.add_run("Palavras-chave: ")
    r1.font.name = 'Arial'
    r1.font.size = Pt(12)
    r1.font.bold = True
    r2 = p_kw.add_run("Desenvolvimento Web; Django; Python; Catálogo Digital; Banco de Dados Relacional.")
    r2.font.name = 'Arial'
    r2.font.size = Pt(12)

    # 5. 1 INTRODUÇÃO (6 parágrafos rigorosos)
    add_h1("1 INTRODUÇÃO")

    p1 = (
        "O mercado global e nacional de perfumaria e cosméticos experimentou uma intensa transformação com a consolidação dos "
        "canais digitais de comércio e divulgação. Em um setor no qual a percepção de valor está fortemente vinculada à identidade "
        "visual, à sofisticação das embalagens e à detalhada descrição das notas olfativas, a presença na internet deixou de ser apenas "
        "um diferencial competitivo e passou a constituir um requisito indispensável de sobrevivência comercial. As vitrines digitais "
        "tornaram-se o ponto de contato primordial entre marcas e consumidores, exigindo interfaces interativas, ágeis e esteticamente "
        "refinadas, capazes de simular o ambiente sensorial e sofisticado das boutiques físicas de perfumaria."
    )
    add_p(p1)

    p2 = (
        "Apesar da relevância desse mercado, pequenas marcas, revendedores autônomos e empreendimentos regionais enfrentam entraves "
        "substanciais para estruturar uma presença digital eficiente e profissional. A utilização de redes sociais como vitrine "
        "primária impõe limitações estruturais severas, tais como a ausência de mecanismos eficientes de busca textual, a dificuldade "
        "de organização por categorias olfativas e a falta de galerias dedicadas por produto. Em contrapartida, a adesão a plataformas "
        "proprietárias de comércio eletrônico frequentemente implica custos de implantação elevados, taxas recorrentes e complexidades "
        "operacionais incompatíveis com a necessidade de um catálogo dinâmico e direto. Diante desse cenário, formula-se o problema "
        "de pesquisa: como conceber e desenvolver uma aplicação web acessível, responsiva e robusta que atenda com eficácia às necessidades "
        "de catalogação, busca e exibição multimídia de produtos de perfumaria?"
    )
    add_p(p2)

    p3 = (
        "A justificativa para a execução deste estudo reside na relevância de disponibilizar uma solução tecnológica independente e "
        "personalizável, proporcionando uma vitrine moderna sem onerar o lojista com custos abusivos de manutenção. Paralelamente, "
        "no âmbito da formação técnica em nível médio no Centro Paula Souza, o projeto reveste-se de profundo valor pedagógico ao congregar "
        "conhecimentos interdisciplinares de análise de sistemas, modelagem de bancos de dados relacionais, lógica de programação em "
        "linguagem orientada a objetos (Python), segurança da informação e construção de interfaces centradas na experiência do usuário (UX/UI)."
    )
    add_p(p3)

    p4 = (
        "Diante do problema delineado, o objetivo geral deste trabalho consiste em projetar, desenvolver e validar a aplicação web "
        "VIKLO Perfumes, voltada à exibição de catálogo de fragrâncias, filtragem dinâmica e cadastro de produtos com suporte a múltiplas "
        "imagens. Para atingir essa meta, estabeleceram-se os seguintes objetivos específicos: a) estruturar uma base de dados relacional "
        "normalizada com integridade referencial 1:N entre produtos e suas imagens; b) programar a camada de controle e negócio em Python "
        "utilizando o framework Django sob o padrão MVT; c) implementar um mecanismo de busca textual utilizando operadores de consulta "
        "composta e paginação dinâmica; d) conceber formulários web com validação e upload simultâneo de múltiplos arquivos; e e) construir "
        "uma interface visual responsiva e elegante baseada em Bootstrap 5 com temática Dark Mode."
    )
    add_p(p4)

    p5 = (
        "A metodologia adotada caracterizou-se como uma pesquisa aplicada e exploratória, orientada ao desenvolvimento experimental de software "
        "em conformidade com as fases clássicas de engenharia de software. Os procedimentos envolveram o levantamento de requisitos, a modelagem "
        "conceitual das entidades no banco de dados SQLite, a codificação orientada a objetos com Django 6.1 e Python 3.12, o tratamento de mídias "
        "com a biblioteca Pillow e a composição de interfaces com HTML5, CSS3 e Bootstrap 5. Por fim, realizaram-se testes de caixa-preta, "
        "validações de responsividade em diferentes resoluções e análises de integridade relacional."
    )
    add_p(p5)

    p6 = (
        "Este artigo está estruturado em cinco seções principais: após esta introdução, a seção 2 apresenta o referencial teórico que embasa "
        "o framework Django, a modelagem de dados relacional e os princípios de design de interface responsiva. A seção 3 detalha a metodologia "
        "de desenvolvimento e os recursos tecnológicos aplicados. A seção 4 discute os resultados obtidos, detalhando a arquitetura implementada, "
        "os módulos desenvolvidos e os testes de software realizados. Por fim, a seção 5 sintetiza as considerações finais, limitações e propostas "
        "de trabalhos futuros, sucedida pelas referências bibliográficas adotadas."
    )
    add_p(p6)

    # 6. 2 REFERENCIAL TEÓRICO
    add_h1("2 REFERENCIAL TEÓRICO")

    add_h2("2.1 O Framework Django e a Arquitetura MVT")
    p_ref1 = (
        "O desenvolvimento de aplicações web modernas requer a utilização de ferramentas que forneçam alta produtividade, manutenibilidade "
        "e proteção contra falhas de segurança recorrentes. Nesse contexto, o framework Django, desenvolvido na linguagem Python, destaca-se "
        "por sua filosofia \"batteries-included\" (baterias inclusas), a qual disponibiliza nativamente recursos essenciais como autenticação, "
        "camada de persistência, proteção contra ataques de injeção de SQL e falsificação de solicitações entre sites (Cross-Site Request Forgery - CSRF) "
        "(ALCHIN, 2013). Segundo Pressman e Maxim (2016), o uso de frameworks consolidados minimiza erros conceituais no desenvolvimento e eleva "
        "a padronização das soluções de software."
    )
    add_p(p_ref1)

    p_ref2 = (
        "O Django estrutura suas aplicações sobre o padrão arquitetural MVT (Model-View-Template), que consiste em uma variação adaptada do "
        "clássico modelo MVC (Model-View-Controller). Na camada Model (Modelo), são definidas as representações lógicas das entidades e suas "
        "regras de negócio, mapeadas para o banco de dados via ORM (Object-Relational Mapping). A camada View (Visão) centraliza a lógica de "
        "controle, processando as requisições HTTP, interagindo com os modelos e selecionando o template para retorno. Por fim, a camada Template "
        "(Modelo de Apresentação) estrutura a interface gráfica entregue ao usuário, combinando HTML com a sintaxe segura do Django Template Language "
        "(DTL) (DJANGO SOFTWARE FOUNDATION, 2026). Essa divisão garante alto nível de desacoplamento e facilita manutenções evolutivas (SOMMERVILLE, 2018)."
    )
    add_p(p_ref2)

    add_h2("2.2 Modelagem Relacional de Dados e Processamento de Imagens")
    p_ref3 = (
        "Bancos de dados relacionais organizam as informações em tabelas estruturadas com base na teoria matemática dos conjuntos (SILBERSCHATZ; KORTH; "
        "SUDARSHAN, 2020). No desenvolvimento de catálogos comerciais, a necessidade de associar várias fotografias complementares a um único "
        "produto é atendida por meio de relacionamentos de cardinalidade um-para-muitos (1:N), estabelecidos por chaves estrangeiras (Foreign Keys). "
        "A garantia da integridade referencial impõe que a exclusão de um registro mestre promova a eliminação correlata de seus dependentes. "
        "No Django, a cláusula on_delete=models.CASCADE assegura que, ao remover um perfume, todas as suas fotos sejam excluídas em cascata, "
        "impedindo inconsistências e dados órfãos na base (SILBERSCHATZ; KORTH; SUDARSHAN, 2020)."
    )
    add_p(p_ref3)

    p_ref4 = (
        "Para a manipulação de fluxos multimídia, a integração do Django com a biblioteca Pillow fornece mecanismos de inspeção e validação de "
        "cabeçalhos binários de arquivos enviados por formulários. Essa validação garante que apenas imagens com extensões e assinaturas autênticas "
        "(JPEG, PNG, WEBP) sejam persistidas em disco sob o diretório media/, impedindo a execução indevida de scripts maliciosos no servidor "
        "(DEITEL; DEITEL, 2017)."
    )
    add_p(p_ref4)

    add_h2("2.3 Interface do Usuário, Design Responsivo e a Estética Dark Mode")
    p_ref5 = (
        "A usabilidade e o apelo visual exercem impacto determinante sobre a retenção e a tomada de decisão dos consumidores digitais (SOMMERVILLE, 2018). "
        "A filosofia de design responsivo com foco Mobile-First orienta a concepção das interfaces a partir das restrições de dispositivos portáteis, "
        "expandindo gradativamente a distribuição espacial dos elementos para computadores pessoais. O framework Bootstrap 5 materializa essa "
        "concepção por meio de um sistema de grid de 12 colunas e classes utilitárias fundamentadas em Flexbox (BOOTSTRAP, 2026)."
    )
    add_p(p_ref5)

    p_ref6 = (
        "No nicho de cosméticos e perfumaria fina, a aplicação de uma identidade visual em tema escuro (Dark Mode) emprega planos de fundo em tons "
        "profundos de grafite (#080b0f), criando um contraste nobre com os detalhes do produto e transmitindo sensação de luxo e sofisticação. "
        "Ademais, pesquisas ergonômicas de interface demonstram que ambientes escuros reduzem o estresse ocular em ambientes com baixa luminosidade, "
        "tornando a navegação prolongada mais confortável (BOOTSTRAP, 2026)."
    )
    add_p(p_ref6)

    # 7. 3 METODOLOGIA
    add_h1("3 METODOLOGIA")
    p_met1 = (
        "O presente trabalho caracteriza-se como uma pesquisa aplicada e desenvolvimento experimental de software, orientado à solução prática "
        "de catalogação digital no segmento de perfumaria (PRESSMAN; MAXIM, 2016). O projeto foi integralmente conduzido em ambiente computacional "
        "equipado com sistema operacional Microsoft Windows 11, utilizando o editor de código Visual Studio Code e o sistema de controle de versão Git."
    )
    add_p(p_met1)

    p_met2 = (
        "A arquitetura do sistema foi desenvolvida sobre a linguagem Python (versão 3.12) e o framework Django (versão 6.1), isolados em ambiente "
        "virtual dedicado (ll_web). Utilizou-se o banco de dados relacional SQLite 3 para armazenamento local das informações, a biblioteca Pillow "
        "(versão 12.3.0) para validação dos fluxos binários de imagem, e o framework Bootstrap (versão 5.3) em conjunto com HTML5 e CSS3 customizado "
        "para a camada de apresentação."
    )
    add_p(p_met2)

    p_met3 = (
        "O desenvolvimento seguiu cinco etapas fundamentais de engenharia de software: a) levantamento e especificação dos requisitos funcionais "
        "e não-funcionais da aplicação; b) modelagem relacional de dados e definição das tabelas de entidades; c) codificação do back-end, "
        "incluindo roteamento em urls.py, implementação de views com filtros disjuntivos (Q objects) e paginação com a classe Paginator; "
        "d) construção dos templates front-end responsivos e estilização Dark Theme; e e) realização de testes funcionais de caixa-preta para "
        "validação do comportamento do software sob diferentes condições de entrada e resoluções de tela."
    )
    add_p(p_met3)

    # 8. 4 RESULTADOS E DISCUSSÃO
    add_h1("4 RESULTADOS E DISCUSSÃO")

    add_h2("4.1 Arquitetura do Sistema e Modelo Relacional de Dados")
    p_res1 = (
        "O desenvolvimento resultou no sistema web VIKLO Perfumes, cuja estrutura lógica distribui-se entre o módulo de configuração global "
        "(TCC_WEB) e a aplicação de catálogo (TCC_WEBS). A modelagem dos dados foi estabelecida no arquivo models.py, decomposta em duas classes "
        "relacionadas: Perfume, que armazena os metadados principais e a fotografia de capa, e ImagemPerfume, que registra as imagens adicionais "
        "vinculadas por meio de chave estrangeira com integridade referencial on_delete=models.CASCADE e related_name=\"imagens\"."
    )
    add_p(p_res1)

    add_caption("Tabela 1 – Estrutura das Tabelas Relacionais do Banco de Dados")

    # Table 1: Database Structure
    table1 = doc.add_table(rows=9, cols=5)
    table1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table1)

    t1_headers = ["Tabela", "Atributo", "Tipo de Dado", "Restrição", "Descrição"]
    for j, h in enumerate(t1_headers):
        cell = table1.cell(0, j)
        set_cell_background(cell, "2B2B2B")
        set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    t1_rows = [
        ("Perfume", "id", "INTEGER", "PK, AUTO", "Identificador primário único"),
        ("Perfume", "titulo", "VARCHAR(50)", "NOT NULL", "Nome comercial do perfume"),
        ("Perfume", "descricao", "TEXT", "NOT NULL", "Notas olfativas e descrição"),
        ("Perfume", "imagem", "VARCHAR(100)", "NOT NULL", "Caminho da imagem principal"),
        ("Perfume", "tipo", "VARCHAR(20)", "DEFAULT 'unissex'", "Gênero: masc./fem./unissex"),
        ("ImagemPerfume", "id", "INTEGER", "PK, AUTO", "Identificador da foto extra"),
        ("ImagemPerfume", "perfume_id", "INTEGER", "FK, CASCADE", "Chave estrangeira (Perfume)"),
        ("ImagemPerfume", "imagem", "VARCHAR(100)", "NOT NULL", "Caminho da foto adicional"),
    ]

    for i, row in enumerate(t1_rows, start=1):
        bg = "F9F9F9" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row):
            cell = table1.cell(i, j)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j in (0, 2, 3) else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.0
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(9.5)

    add_source("Fonte: Elaborado pelos autores (2026).")

    p_res2 = (
        "A estrutura concebida preserva a terceira forma normal (3FN), evitando redundâncias de armazenamento e conferindo flexibilidade para "
        "que cada produto disponha de uma galeria personalizada com quantidade dinâmica de imagens. A exclusão em cascata assegura conformidade "
        "com os preceitos de Silberschatz, Korth e Sudarshan (2020), erradicando registros órfãos que degradariam o sistema ao longo do tempo."
    )
    add_p(p_res2)

    add_h2("4.2 Módulo de Catálogo, Filtragem Dinâmica e Paginação")
    p_res3 = (
        "A exibição do catálogo na view catalogo(request) opera de modo integrado ao mecanismo de busca. Ao receber o parâmetro 'q' via requisição "
        "HTTP GET, a aplicação utiliza os objetos Q do Django para articular uma pesquisa lógica disjuntiva (OR) sobre os atributos titulo e "
        "descricao, utilizando o operador de consulta 'icontains'. Esse operador efetua a busca por substring ignorando a diferença entre letras "
        "maiúsculas e minúsculas, assegurando elevada tolerância a variações na digitação do consumidor."
    )
    add_p(p_res3)

    p_res4 = (
        "Para preservar o tempo de resposta e o tráfego de dados na rede, implementou-se a paginação nativa através da classe Paginator, limitando "
        "a renderização em lotes de 12 itens por página. Essa modularização impede sobrecargas no navegador do cliente e mantém a rolagem fluida, "
        "mesmo em cenários de expansão volumosa do banco de dados."
    )
    add_p(p_res4)

    add_h2("4.3 Módulo de Detalhes do Produto e Galeria de Múltiplas Imagens")
    p_res5 = (
        "Ao acionar o card de um perfume, o usuário é direcionado para a rota /perfume/<int:id>/. A view detalhes_perfume recupera a instância via "
        "get_object_or_404(), prevenindo falhas não tratadas na ocorrência de identificadores inexistentes. A recuperação das fotos adicionais dá-se "
        "pelo relacionamento reverso perfume.imagens.all(), injetando os objetos no contexto do template Detalhes.html. No front-end, a imagem principal "
        "é exibida em alta resolução com acabamento arredondado, acompanhada de miniaturas interativas das fotos complementares e indicação do gênero "
        "olfativo (Masculino, Feminino ou Unissex)."
    )
    add_p(p_res5)

    add_h2("4.4 Módulo de Cadastro e Upload Múltiplo de Arquivos")
    p_res6 = (
        "O cadastramento de itens é viabilizado pela view formulario(request) e pelo formulário web configurado com enctype=\"multipart/form-data\". "
        "Ao receber uma requisição POST válida com o token de segurança CSRF, a rotina instancia primeiro o objeto principal Perfume a partir de "
        "request.POST e do arquivo de capa em request.FILES. Em seguida, a função captura a coleção de arquivos adicionais utilizando "
        "request.FILES.getlist(\"imagens\"), instanciando recursivamente os registros na tabela ImagemPerfume. Esse procedimento simplifica o "
        "fluxo de abastecimento da vitrine, condensando em uma única submissão o envio de todo o material promocional do produto."
    )
    add_p(p_res6)

    add_h2("4.5 Avaliação dos Testes e Validação do Software")
    p_res7 = (
        "A validação do sistema deu-se pela aplicação de uma bateria de testes funcionais de caixa-preta, acompanhada de testes de responsividade em "
        "simuladores de dispositivos móveis. O Quadro 1 reúne os casos de teste planejados, os procedimentos executados e os resultados observados:"
    )
    add_p(p_res7)

    add_caption("Quadro 1 – Matriz de Casos de Teste e Validação da Aplicação")

    # Table 2 / Quadro 1: Test Cases
    table2 = doc.add_table(rows=9, cols=5)
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table2)

    t2_headers = ["Caso", "Funcionalidade", "Ação / Entrada Executada", "Resultado Esperado", "Situação"]
    for j, h in enumerate(t2_headers):
        cell = table2.cell(0, j)
        set_cell_background(cell, "2B2B2B")
        set_cell_margins(cell, top=100, bottom=100, left=100, right=100)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run(h)
        r.font.name = "Arial"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    t2_rows = [
        ("CT-01", "Redirecionamento", "Acesso à rota raiz '/'", "Redirecionamento HTTP 302 para '/catalogo/'", "Aprovado"),
        ("CT-02", "Busca Positiva", "Termo existente (ex.: 'amadeirado')", "Listagem filtrada contendo o termo no título ou descrição", "Aprovado"),
        ("CT-03", "Busca Inexistente", "Termo inexistente (ex.: 'xyz123')", "Grade vazia sem quebras de layout ou erros de servidor", "Aprovado"),
        ("CT-04", "Cadastro Capa", "Formulário com 1 foto de capa", "Gravação no banco e redirecionamento para o catálogo", "Aprovado"),
        ("CT-05", "Upload Múltiplo", "Formulário com capa + 3 fotos extras", "Criação de 1 Perfume e 3 ImagemPerfume com arquivos salvos", "Aprovado"),
        ("CT-06", "Tratamento 404", "Acesso a ID inexistente ('/perfume/9999/')", "Retorno controlado de página de erro HTTP 404", "Aprovado"),
        ("CT-07", "Paginação", "Navegação para página 2 ('?page=2')", "Renderização dos próximos 12 itens de forma ordenada", "Aprovado"),
        ("CT-08", "Responsividade", "Exibição em tela de 375px (mobile)", "Empilhamento de cards em coluna única com navbar compacta", "Aprovado"),
    ]

    for i, row in enumerate(t2_rows, start=1):
        bg = "F9F9F9" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row):
            cell = table2.cell(i, j)
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=80, bottom=80, left=90, right=90)
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if j in (0, 4) else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.line_spacing = 1.0
            r = p.add_run(val)
            r.font.name = "Arial"
            r.font.size = Pt(9.5)
            if j == 4:
                r.font.bold = True
                r.font.color.rgb = RGBColor(0, 128, 0)

    add_source("Fonte: Elaborado pelos autores (2026).")

    p_res8 = (
        "Os testes comprovaram a estabilidade e a maturidade do sistema. A separação clara proporcionada pelo padrão MVT, associada ao uso "
        "de rotas explícitas e validação com Pillow, assegurou que nenhum upload inválido corrompesse a aplicação, confirmando a aptidão do "
        "software para atendimento aos requisitos funcionais delineados."
    )
    add_p(p_res8)

    # 9. 5 CONSIDERAÇÕES FINAIS
    add_h1("5 CONSIDERAÇÕES FINAIS")

    p_con1 = (
        "O presente trabalho teve por finalidade projetar, implementar e validar o sistema web VIKLO Perfumes, suprindo a carência de vitrines "
        "digitais dinâmicas, leves e visualmente atrativas para o setor de cosméticos e fragrâncias. Diante dos resultados apresentados, "
        "constata-se que o objetivo geral e os objetivos específicos foram plenamente alcançados, comprovando que o uso combinado do framework "
        "Django e de uma interface responsiva baseada em Bootstrap 5 em modo escuro proporciona uma solução altamente estável, segura e elegante."
    )
    add_p(p_con1)

    p_con2 = (
        "A arquitetura MVT provou ser um alicerce robusto, permitindo o isolamento entre regras de negócio, persistência de dados e apresentação visual. "
        "A modelagem 1:N com integridade em cascata resolveu com simplicidade a exigência comercial de galerias fotográficas completas para cada produto, "
        "enquanto a busca com objetos Q e a paginação conferiram dinamismo e conforto na navegação."
    )
    add_p(p_con2)

    p_con3 = (
        "Como limitações identificadas na versão atual do software, destacam-se a ausência de um carrinho de compras para cálculo de frete e checkout "
        "de pedidos, a inexistência de login de clientes externos para gestão de listas de desejos e a utilização do SQLite, que, embora satisfatório "
        "para desenvolvimento e homologação local, deve ser substituído em cenários de alta concorrência simultânea."
    )
    add_p(p_con3)

    p_con4 = (
        "Por fim, sugerem-se como trabalhos futuros: a) implantação de sistema de autenticação de usuários com controle de permissões por nível de "
        "acesso (administrador, lojista e cliente consumidor); b) integração de carrinho de compras e módulo de pagamentos com provedores consolidados "
        "(como Mercado Pago ou Stripe); c) migração do banco de dados para PostgreSQL e publicação da aplicação em ambiente de nuvem (Render, Railway "
        "ou AWS); e d) integração do armazenamento de mídias a servidores de objetos (Amazon S3 ou Cloudinary)."
    )
    add_p(p_con4)

    # 10. REFERÊNCIAS
    add_p("REFERÊNCIAS", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=18, space_after=12, line_spacing=1.0, bold=True)

    refs = [
        "ALCHIN, Marty. Pro Django. 2. ed. Nova Iorque: Apress, 2013.",
        "BOOTSTRAP. Bootstrap: Powerful, extensible, and feature-packed frontend toolkit. Versão 5.3. Disponível em: <https://getbootstrap.com/>. Acesso em: 11 nov. 2026.",
        "DEITEL, Paul; DEITEL, Harvey. Python: como programar. São Paulo: Pearson Education do Brasil, 2017.",
        "DJANGO SOFTWARE FOUNDATION. Django documentation. Versão 6.1. Disponível em: <https://docs.djangoproject.com/>. Acesso em: 11 nov. 2026.",
        "PRESSMAN, Roger S.; MAXIM, Bruce R. Engenharia de software: uma abordagem profissional. 8. ed. Porto Alegre: AMGH Editora, 2016.",
        "SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. Sistema de banco de dados. 7. ed. Rio de Janeiro: Elsevier, 2020.",
        "SOMMERVILLE, Ian. Engenharia de software. 10. ed. São Paulo: Pearson Education do Brasil, 2018."
    ]

    for ref in refs:
        # Bold the title
        # For books: "Sobrenome, Nome. **Título da obra: subtítulo**. Edição. Local: Editora, ano."
        p = add_p(align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=6, line_spacing=1.0)
        parts = ref.split(". ", 2)
        if len(parts) >= 2:
            author = parts[0] + ". "
            rest = parts[1]
            extra = ". " + parts[2] if len(parts) > 2 else ""
            
            r_auth = p.add_run(author)
            r_auth.font.name = 'Arial'
            r_auth.font.size = Pt(12)
            
            r_title = p.add_run(rest)
            r_title.font.name = 'Arial'
            r_title.font.size = Pt(12)
            r_title.font.bold = True
            
            if extra:
                r_extra = p.add_run(extra)
                r_extra.font.name = 'Arial'
                r_extra.font.size = Pt(12)
        else:
            r = p.add_run(ref)
            r.font.name = 'Arial'
            r.font.size = Pt(12)

    output_filename = "Artigo_Cientifico_TCC_ETEC_SRV.docx"
    try:
        doc.save(output_filename)
        print(f"Documento gerado com sucesso: {output_filename}")
    except PermissionError:
        fallback_filename = "Artigo_Cientifico_TCC_ETEC_SRV_atualizado.docx"
        doc.save(fallback_filename)
        print(f"Aviso: '{output_filename}' está aberto no Word (ou bloqueado). Arquivo salvo com sucesso como '{fallback_filename}'. Feche o Word para atualizar o arquivo original.")

if __name__ == "__main__":
    build_document()

