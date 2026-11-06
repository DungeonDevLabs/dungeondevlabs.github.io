# Regras Globais do Projeto

## 1. O que Fazer no INÍCIO de Toda Tarefa/Feature (Obrigatório)
Sempre que o usuário solicitar uma nova funcionalidade, alteração ou refatoração:
1. **Ler o Documento de Arquitetura Central:** Antes de abrir ou modificar qualquer código, leia o arquivo de contexto central (`DOCS/ARCHITECTURE_MAP.md` ou equivalente).
2. **Identificar o Escopo:** Use o mapa de arquitetura para localizar exatamente quais pastas, módulos ou schemas serão impactados.
3. **Minimizar Leitura de Arquivos:** Abra e leia APENAS os arquivos diretamente envolvidos no escopo da feature. Não faça varreduras desnecessárias pelo projeto inteiro.

---

## 2. O que Fazer para DEFINIR COMO PRONTO / Definition of Done (Obrigatório)
Uma tarefa SOMENTE pode ser considerada concluída ("Pronta") quando os seguintes passos forem executados:
1. **Execução e Teste:** Garantir que o código da feature está implementado e sem erros de sintaxe ou compilação.
2. **Atualização do Documento Central:** Atualizar o arquivo de mapa de arquitetura (`DOCS/ARCHITECTURE_MAP.md`) refletindo:
   - Novas pastas ou arquivos criados.
   - Novos endpoints, schemas ou contratos alterados.
   - Mudanças nas regras de negócio globais provocadas pela feature.
3. **Resumo das Alterações:** Apresentar ao usuário um resumo conciso do que foi alterado e confirmar que o mapa central de arquitetura foi devidamente atualizado para as próximas tarefas.