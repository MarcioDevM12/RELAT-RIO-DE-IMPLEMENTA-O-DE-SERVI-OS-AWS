#!/usr/bin/env python3
"""
EC2 Instance Optimizer
Identifica instâncias EC2 subutilizadas para otimização
"""

import boto3
import pandas as pd

def find_idle_instances(region='us-east-1'):
    """Encontra instâncias EC2 com baixa utilização"""
    
    ec2 = boto3.client('ec2', region_name=region)
    cloudwatch = boto3.client('cloudwatch', region_name=region)
    
    print("🔍 Buscando instâncias EC2 subutilizadas...")
    
    # Listar instâncias em execução
    response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )
    
    recommendations = []
    
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            
            # Verificar métricas de CPU
            try:
                metrics = cloudwatch.get_metric_statistics(
                    Namespace='AWS/EC2',
                    MetricName='CPUUtilization',
                    Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
                    StartTime=pd.Timestamp.now() - pd.Timedelta(days=7),
                    EndTime=pd.Timestamp.now(),
                    Period=3600,
                    Statistics=['Average']
                )
                
                if metrics['Datapoints']:
                    avg_cpu = sum([dp['Average'] for dp in metrics['Datapoints']]) / len(metrics['Datapoints'])
                    
                    if avg_cpu < 10:  # Menos de 10% de utilização
                        recommendations.append({
                            'instance_id': instance_id,
                            'instance_type': instance_type,
                            'avg_cpu': avg_cpu,
                            'recommendation': 'Considerar downsizing ou desligamento'
                        })
            
            except Exception as e:
                print(f"  ⚠️  Erro ao analisar {instance_id}: {e}")
    
    # Exibir recomendações
    if recommendations:
        print("\n✅ RECOMENDAÇÕES DE OTIMIZAÇÃO:")
        print("=" * 60)
        for rec in recommendations:
            print(f"Instância: {rec['instance_id']}")
            print(f"Tipo: {rec['instance_type']}")
            print(f"CPU Média: {rec['avg_cpu']:.1f}%")
            print(f"Ação: {rec['recommendation']}")
            print("-" * 40)
    else:
        print("\n🎉 Todas as instâncias estão bem dimensionadas!")

if __name__ == '__main__':
    find_idle_instances()