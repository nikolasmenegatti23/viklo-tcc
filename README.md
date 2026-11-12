# 🌸 VIKLO Perfumes — Sistema Web de Catálogo e Gestão

> **Trabalho de Conclusão de Curso (TCC) — Ensino Médio Técnico**  
> **ETEC de Santa Rosa de Viterbo — Centro Paula Souza (CPS)**

Aplicação web desenvolvida com **Python**, **Django** e **Bootstrap 5**, projetada para atuar como vitrine digital sofisticada no segmento de perfumaria fina e cosméticos, com suporte a busca dinâmica, paginação e galeria multimídia com múltiplas fotos por produto.

---

## 📸 Funcionalidades Principais

- 🏷️ **Catálogo Dinâmico e Responsivo:** Exibição dos perfumes em grade com layout moderno em *Dark Theme* (`#080b0f`).
- 🔍 **Mecanismo de Busca Textual:** Pesquisa em tempo real por título ou notas olfativas/descrição via operadores lógicos (`Q objects`).
- 📄 **Paginação Otimizada:** Divisão da exibição em lotes de 12 itens por página com a classe `Paginator` do Django.
- 🖼️ **Galeria de Múltiplas Imagens (1:N):** Página de detalhes do perfume com imagem principal e miniaturas complementares interativas.
- 📝 **Formulário de Cadastro com Upload Múltiplo:** Envio simultâneo de dados do perfume e várias fotos adicionais via `multipart/form-data`.
- 🛡️ **Painel Administrativo:** Gestão completa de produtos e fotos via Django Admin.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3.12](https://www.python.org/)
- **Framework Web:** [Django 6.1](https://www.djangoproject.com/)
- **Banco de Dados:** [SQLite 3](https://www.sqlite.org/)
- **Processamento de Imagens:** [Pillow 12.3.0](https://python-pillow.org/)
- **Front-end:** HTML5, CSS3, JavaScript e [Bootstrap 5.3](https://getbootstrap.com/)
- **Controle de Versão:** Git

---

## 🚀 Como Executar o Projeto Localmente

### 1. Clonar o repositório
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd TCC_WEB
```

### 2. Ativar o ambiente virtual (Windows PowerShell)
```powershell
.\ll_web\Scripts\Activate.ps1
```
*(Caso use Prompt de Comando / CMD: `ll_web\Scripts\activate.bat`)*

### 3. Aplicar as migrações do banco de dados
```bash
python manage.py migrate
```

### 4. (Opcional) Criar um superusuário para o painel administrativo
```bash
python manage.py createsuperuser
```

### 5. Iniciar o servidor de desenvolvimento
```bash
python manage.py runserver
```

Acesse no navegador:
- **Catálogo:** [http://127.0.0.1:8000/catalogo/](http://127.0.0.1:8000/catalogo/)
- **Cadastro:** [http://127.0.0.1:8000/formulario/](http://127.0.0.1:8000/formulario/)
- **Painel Administrativo:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📂 Estrutura de Diretórios

```text
TCC_WEB/
├── manage.py                  # CLI do Django
├── db.sqlite3                 # Base de dados relacional SQLite
├── media/                     # Uploads físicos de imagens
│   └── perfumes/
├── TCC_WEB/                   # Configuração global do projeto
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── TCC_WEBS/                  # Aplicação modular de catálogo
│   ├── models.py              # Perfume e ImagemPerfume
│   ├── views.py               # Lógica de controle e consultas
│   ├── templates/             # Templates HTML com Bootstrap
│   └── migrations/
├── ARTIGO_CIENTIFICO_TCC_ETEC.md       # Artigo científico (Markdown)
├── Artigo_Cientifico_TCC_ETEC_SRV.docx # Artigo científico formatado (Word)
└── DOCUMENTO_TECNICO_TCC.md            # Monografia técnica estendida
```

---

## 📄 Documentação Acadêmica

Os documentos técnicos e científicos elaborados para a entrega do TCC encontram-se disponíveis na raiz do projeto:
* `Artigo_Cientifico_TCC_ETEC_SRV.docx`: Artigo científico formatado nas normas da ETEC de Santa Rosa de Viterbo / Centro Paula Souza.
* `ARTIGO_CIENTIFICO_TCC_ETEC.md`: Versão em texto do artigo científico.
* `DOCUMENTO_TECNICO_TCC.md`: Relatório técnico completo estendido.

