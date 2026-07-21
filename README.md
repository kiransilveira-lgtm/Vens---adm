# Password Manager 

Um gerenciador de senhas simples com interface gráfica em **Python + Tkinter**, que salva os dados localmente em um banco de dados **SQLite**.

##  Funcionalidades

- Salvar credenciais (website, email/usuário e senha)
- Buscar credenciais salvas por website
- Gerar senhas aleatórias e seguras (letras, números e símbolos)
- Interface gráfica simples e intuitiva
- Armazenamento local em banco de dados SQLite

##  Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — interface gráfica
- [SQLite3](https://docs.python.org/3/library/sqlite3.html) — banco de dados local

##  Estrutura do projeto

```
password-manager/
├── main.py          # ponto de entrada da aplicação
├── frontend.py       # interface gráfica (Tkinter)
├── backend.py         # lógica de banco de dados e geração de senhas
└── vens/
    ├── logo.png       # logo exibida na interface
    └── passwords.db   # banco de dados (criado automaticamente)
```

##  Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/password-manager.git
   cd password-manager
   ```

2. Certifique-se de ter o Python 3 instalado:
   ```bash
   python3 --version
   ```

3. Coloque uma imagem chamada `logo.png` dentro da pasta `vens/` (ela é usada como logo da interface).

4. Execute o programa:
   ```bash
   python3 main.py
   ```

> O banco de dados `passwords.db` é criado automaticamente dentro da pasta `vens/` na primeira execução.

##  Como usar

- **Website / Email / Password**: preencha os campos manualmente ou use o botão **Generate** para criar uma senha aleatória.
- **Add**: salva os dados preenchidos no banco de dados.
- **Search**: busca as credenciais salvas pelo nome do website informado.
- **Clear**: limpa todos os campos da tela.

##  Aviso

Este projeto tem fins educacionais e as senhas são armazenadas **sem criptografia** no banco de dados local. Não recomendado para uso em produção ou para guardar senhas reais sensíveis sem antes implementar criptografia (ex: usando a biblioteca [`cryptography`](https://pypi.org/project/cryptography/)).

##  Possíveis melhorias futuras

- [ ] Criptografar as senhas armazenadas
- [ ] Adicionar autenticação com senha mestra
- [ ] Listar todas as senhas salvas em uma tela
- [ ] Editar/excluir credenciais existentes
- [ ] Copiar senha para a área de transferência com um clique

##  Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.
