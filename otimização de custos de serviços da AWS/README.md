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

# 🚀 AWS Cost Optimization - Estudo de Caso Completo

<div align="center">

![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Status](https://img.shields.io/badge/Status-Completado-success.svg)

**Implementação real que reduziu custos AWS em 35% com ROI de 467% em 3 meses**

</div>

## 📊 Visão Geral

Este repositório contém o **estudo de caso completo** da implementação de estratégias de otimização de custos AWS na **Abstergo Industries**. 

### 🎯 Principais Resultados
- **✅ 35% redução** nos custos mensais com AWS
- **✅ $9.500 economia** mensal alcançada
- **✅ ROI de 467%** nos primeiros 3 meses
- **✅ Automatização** de 85% das otimizações

## 🛠️ Tecnologias Utilizadas

- **Amazon EC2 Auto Scaling**
- **Amazon S3 Intelligent-Tiering**  
- **AWS Cost Explorer & Budgets**
- **Python** para automação e análise
- **Terraform** para Infra as Code

## 📁 Estrutura do Projeto
aws-cost-optimization/
├── relatorio/ # Documentação completa
├── analise-financeira/ # ROI e análises
├── configs-aws/ # IaC e templates
├── scripts/ # Automação Python
├── docs/ # Guias e tutoriais
└── diagramas/ # Arquitetura

text

## 🚀 Começando

### Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/MarcioDevM12/aws-cost-optimization.git
cd aws-cost-optimization

# Configure ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt
📞 Contato
Márcio Dias Dos Santos
📧 marciodev@gmail.com

📄 Licença
Distribuído sob licença MIT. Veja LICENSE para detalhes.

text

---

## **📄 2. ARQUIVO: `.gitignore`**

```gitignore
# Credenciais
*.pem
*.key
.env
credentials
*.aws/credentials

# Python
__pycache__/
*.pyc
*.pyo

# Sistema
.DS_Store
Thumbs.db
*.log

# Terraform
.terraform/
*.tfstate
*.tfstate.*

# Node.js
node_modules/
package-lock.json

# Temporários
*.tmp
*.temp
~$*
