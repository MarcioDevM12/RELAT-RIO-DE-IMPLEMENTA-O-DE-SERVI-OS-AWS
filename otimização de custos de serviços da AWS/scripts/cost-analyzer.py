#!/usr/bin/env python3
"""
AWS Cost Analyzer
Analisa custos AWS e gera recomendações de otimização
"""

import boto3
import pandas as pd
from datetime import datetime, timedelta
import click

@click.command()
@click.option('--profile', default='default', help='Perfil AWS CLI')
@click.option('--months', default=3, help='Número de meses para analisar')
def analyze_costs(profile, months):
    """Analisa custos AWS dos últimos meses"""
    
    session = boto3.Session(profile_name=profile)
    client = session.client('ce')
    
    # Calcular período
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30*months)
    
    print(f"📊 Analisando custos de {start_date.strftime('%Y-%m-%d')} a {end_date.strftime('%Y-%m-%d')}")
    print("=" * 50)
    
    try:
        # Obter dados de custos
        response = client.get_cost_and_usage(
            TimePeriod={
                'Start': start_date.strftime('%Y-%m-%d'),
                'End': end_date.strftime('%Y-%m-%d')
            },
            Granularity='MONTHLY',
            Metrics=['UnblendedCost'],
            GroupBy=[
                {'Type': 'DIMENSION', 'Key': 'SERVICE'}
            ]
        )
        
        # Processar resultados
        for result in response['ResultsByTime']:
            print(f"\n📅 Período: {result['TimePeriod']['Start']} a {result['TimePeriod']['End']}")
            print("-" * 40)
            
            for group in result['Groups']:
                service = group['Keys'][0]
                amount = float(group['Metrics']['UnblendedCost']['Amount'])
                unit = group['Metrics']['UnblendedCost']['Unit']
                
                if amount > 0:
                    print(f"  {service}: ${amount:.2f} {unit}")
    
    except Exception as e:
        print(f"❌ Erro ao analisar custos: {e}")

if __name__ == '__main__':
    analyze_costs()