# RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS

**Data:** 18/01/2026  
**Empresa:** Abstergo Industries  
**Responsável:** Márcio Dias Dos Santos

## Introdução
Este relatório apresenta o processo de implementação de ferramentas na empresa **Abstergo Industries**, realizado por **Márcio Dias Dos Santos**. O objetivo do projeto foi elencar 3 serviços AWS, com a finalidade de realizar diminuição de custos imediatos.

## Descrição do Projeto
O projeto de implementação de ferramentas foi dividido em 3 etapas, cada uma com seus objetivos específicos. A seguir, serão descritas as etapas do projeto:

### Etapa 1:  
- **Amazon S3 (Simple Storage Service)**  
- **Foco da ferramenta:** Armazenamento escalável, durável e de baixo custo  
- **Descrição de caso de uso:**  
  A empresa utilizava servidores locais para armazenar arquivos internos e backups, gerando altos custos de manutenção e energia. Com a adoção do Amazon S3, foi possível migrar todo o conteúdo para um ambiente seguro, durável e com pagamento baseado no uso real. O S3 também oferece versionamento e replicação automática para diferentes regiões.

  **🔽 Redução de custos:** Eliminação de infraestrutura física e pagamento apenas pelo armazenamento utilizado.  
  **🔼 Principal ganho:** Armazenamento seguro, escalável e com alta durabilidade, reduzindo riscos e melhorando o acesso aos dados.

---

### Etapa 2:  
- **AWS Lambda**  
- **Foco da ferramenta:** Execução de código sob demanda (computação serverless)  
- **Descrição de caso de uso:**  
  A empresa realizava tarefas automatizadas (como geração de relatórios e processamento de dados) em servidores que ficavam ociosos a maior parte do tempo. Ao migrar essas tarefas para o AWS Lambda, o código passou a ser executado apenas quando necessário, sem a necessidade de manter servidores ativos.

  **🔽 Redução de custos:** Pagamento apenas pelo tempo de execução do código, sem desperdício de recursos computacionais.  
  **🔼 Principal ganho:** Escalabilidade automática, eliminação de manutenção de servidores e maior agilidade na entrega de soluções.

---

### Etapa 3:  
- **Auto Scaling (com Amazon EC2)**  
- **Foco da ferramenta:** Escalabilidade automática de instâncias de computação  
- **Descrição de caso de uso:**  
  A empresa enfrentava picos de acesso em seu sistema web, mantendo diversas instâncias EC2 ativas mesmo durante períodos de baixa demanda. Com o uso do Auto Scaling, as instâncias passaram a ser criadas ou encerradas automaticamente de acordo com a carga de trabalho.

  **🔽 Redução de custos:** Redução do número de instâncias EC2 em momentos de baixa utilização.  
  **🔼 Principal ganho:** Alta disponibilidade e economia simultânea, com uso inteligente de recursos computacionais.

---

## Conclusão
A implementação das ferramentas na empresa **Abstergo Industries** proporcionou uma significativa **redução de custos operacionais** e melhorou a **eficiência dos processos internos**. A adoção de soluções como Amazon S3, AWS Lambda e Auto Scaling resultou em maior segurança, flexibilidade e desempenho. Recomenda-se a continuidade da utilização dos serviços implementados e a constante busca por novas soluções em nuvem que possam aprimorar ainda mais os resultados da empresa.

## Anexos

- Guia de migração de arquivos para o Amazon S3  
- Scripts otimizados para execução no AWS Lambda  
- Estratégia de escalonamento automático configurada no Auto Scaling

---

**Assinatura do Responsável pelo Projeto:**  
*Márcio Dias Doas Santos*
