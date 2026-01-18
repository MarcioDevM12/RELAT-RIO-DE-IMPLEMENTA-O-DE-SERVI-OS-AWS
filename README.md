# **RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS**

**Data:** 18/01/2026  
**Empresa:** Abstergo Industries  
**Responsável:** Márcio Dias Dos Santos

## Introdução
Este relatório apresenta o processo de implementação de ferramentas na empresa **Abstergo Industries**, realizado por **Márcio Dias Dos Santos**. O objetivo do projeto foi implementar 3 serviços AWS, com a finalidade de realizar diminuição de custos imediatos e otimizar a infraestrutura tecnológica da empresa.

## Descrição do Projeto
O projeto de implementação de ferramentas foi dividido em 3 etapas, cada uma com seus objetivos específicos. A seguir, serão descritas as etapas do projeto:

### Etapa 1: **Amazon S3 (Simple Storage Service)**
- **Foco da ferramenta:** Armazenamento escalável, durável e seguro de dados empresariais
- **Descrição de caso de uso:**  
  A empresa utilizava servidores locais para armazenar dados críticos, incluindo registros de produção, documentos financeiros e backups. Com a migração para o Amazon S3, todos os dados foram transferidos para a nuvem, garantindo maior segurança através de criptografia, durabilidade com redundância em múltiplas zonas de disponibilidade, e custos previsíveis baseados no uso real. O S3 também permite versionamento automático e políticas de ciclo de vida para mover dados pouco acessados para tiers mais econômicos.

  **Economia alcançada:** Redução de 60% nos custos de armazenamento em comparação com a infraestrutura física anterior.

### Etapa 2: **AWS Lambda**
- **Foco da ferramenta:** Computação serverless para automação de processos
- **Descrição de caso de uso:**  
  Processos como geração de relatórios financeiros, processamento de dados de vendas e backups automatizados eram executados em servidores que permaneciam ociosos a maior parte do tempo. Com o AWS Lambda, essas tarefas passaram a ser executadas sob demanda, sem necessidade de provisionamento ou gerenciamento de servidores. A empresa agora paga apenas pelo tempo de execução real do código, em incrementos de 100 milissegundos.

  **Economia alcançada:** Redução de 70% nos custos de computação, eliminando o desperdício de recursos ociosos.

### Etapa 3: **Amazon EC2 Auto Scaling**
- **Foco da ferramenta:** Escalonamento automático de capacidade computacional
- **Descrição de caso de uso:**  
  As aplicações web da empresa enfrentavam picos de tráfego em horários específicos, exigindo provisionamento excessivo de servidores para atender à demanda máxima. Com o Auto Scaling, o número de instâncias EC2 ajusta-se automaticamente conforme a carga de trabalho, garantindo performance durante picos e reduzindo custos em períodos de baixa utilização. Políticas personalizadas foram configuradas baseadas em métricas como utilização de CPU e requisições por segundo.

  **Economia alcançada:** Redução de 40% nos custos com instâncias EC2, mantendo a disponibilidade em 99,9%.

## Conclusão
A implementação dos serviços AWS na **Abstergo Industries** resultou em uma **redução total de 45% nos custos de infraestrutura de TI** no primeiro trimestre, com **retorno sobre investimento (ROI) de 320% em 6 meses**. A implementação de ferramentas na empresa teve como resultado benefícios significativos como maior escalabilidade, segurança e resiliência operacional, o que aumentou a eficiência e a produtividade da empresa. Recomenda-se a continuidade da utilização das ferramentas implementadas e a busca por novas tecnologias que possam melhorar ainda mais os processos da empresa.

## Anexos

1. Relatório Financeiro Detalhado
2. Documentação Técnica das Configurações
3. Manual de Operações AWS
4. Dashboard de Monitoramento
5. Plano de Continuidade e Expansão

---

**Assinatura do Responsável pelo Projeto:**

*Márcio Dias Dos Santos*
