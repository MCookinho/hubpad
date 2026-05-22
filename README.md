# Hubpad

O mural público de tudo e de todos.

## Funcionalidades

- 📝 Criar posts com título, texto e anexos
- 🔒 Proteger posts com senha (apenas título visível publicamente)
- 🌐 Suporte a 3 idiomas: Português, English, Español
- 📱 Responsivo (funciona no celular)
- 🔍 Buscar por título, texto, ID ou nome de arquivo
- 🎲 Modo aleatório
- 🌙 Tema claro/escuro
- 📁 Anexar imagens, vídeos, áudios, PDFs, documentos e mais

## Tecnologias

- **Backend**: Python + Flask
- **Frontend**: HTML, CSS, JavaScript
- **Armazenamento**: Arquivos JSON + disco local
- **Segurança**: Senhas hasheadas com Werkzeug

---

## Rodar Localmente

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/hubpad.git
cd hubpad

# 2. Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Rode
python app.py
# ou
./run.sh
```

Acesse: http://localhost:5000

---

## Deploy

### ⭐ MELHOR OPÇÃO: PythonAnywhere (Persistente)

PythonAnywhere mantém os arquivos permanentes (posts e uploads NÃO são deletados).

**Passo a passo:**

1. Acesse https://www.pythonanywhere.com e crie uma conta gratuita
2. Vá em **Dashboard** → **Web** → **Add a new web app**
3. Escolha **Manual configuration** → **Python 3.10+**
4. Vá em **Consoles** → **Start a new console: Bash**
5. Rode no console:
```bash
git clone https://github.com/SEU_USUARIO/hubpad.git
cd hubpad
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. Volte em **Web** e configure:
   - **Source code**: `/home/SEU_USUARIO/hubpad`
   - **Working directory**: `/home/SEU_USUARIO/hubpad`
   - **Virtualenv**: `/home/SEU_USUARIO/hubpad/venv`

7. Clique em **WSGI configuration file** e edite para:
```python
import sys

path = '/home/SEU_USUARIO/hubpad'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

8. Clique em **Reload**: `SEU_USUARIO.pythonanywhere.com`

**Pronto!** Seu app está no ar e os dados são persistentes.

---

### ⚡ Opção Rápida: Render.com (Resetável)

**Aviso**: No plano gratuito do Render, os arquivos são resetados toda vez que o app reinicia (cerca de 1 vez por dia). Use apenas para teste.

**Passo a passo:**

1. Acesse https://render.com e crie uma conta
2. Clique em **New** → **Web Service**
3. Conecte seu repositório GitHub
4. Preencha:
   - **Name**: `hubpad` (ou qualquer nome)
   - **Region**: São Paulo ou mais próxima
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --preload`
   - **Environment**: Python 3
   - **Plan**: Free

5. Clique em **Deploy**

Após ~2 minutos, seu app estará disponível em `https://hubpad-SEU_CODIGO.onrender.com`

---

### 🚂 Railway (Trial)

Similar ao Render, mas com trial de $5 de crédito.

1. https://railway.app
2. New Project → Deploy from GitHub repo
3. Configure as variáveis de ambiente (se precisar)
4. Deploy

---

## Estrutura do Projeto

```
hubpad/
├── app.py                 # Aplicação Flask
├── requirements.txt       # Dependências
├── Procfile               # Deploy em plataformas PaaS
├── runtime.txt            # Versão Python
├── run.sh                 # Script local
├── .gitignore             # Arquivos ignorados pelo git
├── README.md              # Este arquivo
├── data/
│   ├── .gitkeep           # (mantém pasta)
│   └── messages.json      # Dados dos posts (ignorado pelo git)
├── static/
│   └── uploads/
│       └── .gitkeep       # Anexos (aqui ficam as imagens/vídeos)
└── templates/
    └── index.html         # Todo o frontend (HTML + CSS + JS)
```

---

## Considerações sobre Persistência

Este app usa **armazenamento em disco local** (arquivos JSON). Isso significa:

✅ **Funciona perfeitamente** em:
- Seu computador
- PythonAnywhere
- VPS/Dedicados
- Docker com volumes

⚠️ **Dados são RESETADOS** em:
- Render (Free tier)
- Vercel
- Netlify
- Qualquer plataforma "serverless"

**Para produção real**, considere migrar para:
- Banco de dados: PostgreSQL, Supabase, PlanetScale
- Armazenamento de arquivos: Cloudinary, AWS S3, Supabase Storage

---

## Variáveis de Ambiente

| Variável | Padrão | Descrição |
|----------|--------|-----------|
| `PORT` | `5000` | Porta do servidor |
| `FLASK_DEBUG` | `false` | Modo debug |

---

## Licença

MIT - Use como quiser.

---

## Criador

Criado com ❤️ usando opencode
