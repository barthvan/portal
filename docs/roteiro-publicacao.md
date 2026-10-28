# Roteiro do GitHub — Portfólio de Jáissom Barth Andrade

Atualizado em 27/10/2026. Este roteiro diferencia **o que já está público**, **o que permanece privado** e **o que depende da liberação de segurança**.

## Repositórios

| Repositório | Situação | Finalidade |
| --- | --- | --- |
| [barthvan/portal](https://github.com/barthvan/portal) | Público | Portfólio profissional, estudos de caso e exemplos independentes |
| `barthvan/terrasentinel` | Privado | Arquivos históricos e documentação do Terra Sentinel; **não abrir diretamente** |
| `barthvan/site` | Privado | Repositório de teste, sem conteúdo significativo na última verificação |
| `JABA-corp/dessulfatador` | Público | Projeto independente; avaliar documentação antes de destacá-lo |

## Terra Sentinel: situação da versão pública

O mantenedor relatou a candidata local `outputs/TERRA_SENTINEL_PUBLIC_V3`, com 235 arquivos, histórico Git novo e testes locais de firmware/API. **Ela ainda não foi publicada nem auditada independentemente aqui**.

Segundo o relatório fornecido, continuam pendentes:
- Confirmação de revogação/rotação de Wi-Fi, tokens Edge/VPS e ingestão, senha de engenharia/WebODM, NASA FIRMS, dashboard e chaves legadas;
- Revisão de autenticação/autorização de todas as rotas da API e das proteções de infraestrutura;
- Autoria, licenças e direitos de componentes de terceiros;
- Testes de integração e validação física dos componentes.

**Não publicar a candidata, alterar visibilidade nem enviar seu histórico enquanto persistirem bloqueadores.**

## Próximos entregáveis do portfólio

- [x] README profissional público
- [x] Estudos de caso: Terra Sentinel, Arquivo Oculto e laboratório de IA
- [x] Exemplo independente em Python com testes
- [x] Apresentação de perfil preparada em `PROFILE_README.md`
- [ ] Criar repositório especial `barthvan/barthvan` para exibir README no perfil do usuário
- [ ] Revisar e documentar o código da candidata Terra Sentinel V3 na máquina local
- [ ] Confirmar rotação das credenciais e auditoria final
- [ ] Revisar direitos de redistribuição e definir licenças
- [ ] Documentar fotos próprias de instalação sem dados sensíveis
- [ ] Vincular demonstração de telemetria somente leitura, quando autenticada e validada
- [ ] Criar evidências de testes verificáveis e instruções reproduzíveis

## Segurança

Nunca copiar tokens, senhas, backups ou artefatos de produção para este repositório. O portfólio é intencionalmente documental e usa exemplos independentes; seu conteúdo público **não certifica** a segurança dos projetos privados.
