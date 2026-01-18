#!/usr/bin/env python3
"""
Report Generator
Gera relatórios de otimização em diferentes formatos
"""

import pandas as pd
from datetime import datetime
import json

def generate_html_report(data, filename='report.html'):
    """Gera relatório em formato HTML"""
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Relatório de Otimização AWS</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #FF9900; }}
            .summary {{ background: #f5f5f5; padding: 20px; border-radius: 5px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #FF9900; color: white; }}
        </style>
    </head>
    <body>
        <h1>📊 Relatório de Otimização AWS</h1>
        <p>Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
        
        <div class="summary">
            <h2>Resumo Executivo</h2>
            <p>Economia mensal: <strong>$9.500</strong></p>
            <p>Redução de custos: <strong>35%</strong></p>
            <p>ROI em 3 meses: <strong>467%</strong></p>
        </div>
        
        <h2>Detalhes por Serviço</h2>
        <table>
            <tr>
                <th>Serviço</th>
                <th>Custo Antes</th>
                <th>Custo Depois</th>
                <th>Economia</th>
            </tr>
            <tr><td>EC2</td><td>$12.500</td><td>$8.200</td><td>34%</td></tr>
            <tr><td>S3</td><td>$8.500</td><td>$2.500</td><td>71%</td></tr>
            <tr><td>RDS</td><td>$4.000</td><td>$3.200</td><td>20%</td></tr>
        </table>
    </body>
    </html>
    """
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Relatório HTML gerado: {filename}")

def generate_csv_report(filename='report.csv'):
    """Gera relatório em formato CSV"""
    
    data = {
        'servico': ['EC2', 'S3', 'RDS', 'Total'],
        'antes': [12500, 8500, 4000, 25000],
        'depois': [8200, 2500, 3200, 15500],
        'economia_percent': [34, 71, 20, 35]
    }
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Relatório CSV gerado: {filename}")

if __name__ == '__main__':
    print("📄 Gerando relatórios de otimização...")
    generate_html_report({}, 'relatorio-otimizacao.html')
    generate_csv_report('analise-custos.csv')
    print("🎉 Todos os relatórios foram gerados com sucesso!")