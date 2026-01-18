terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "cost_optimization" {
  bucket = "abstergo-cost-data"
  
  tags = {
    Project     = "Cost Optimization"
    Environment = "Production"
    ManagedBy   = "Terraform"
  }
}

resource "aws_lambda_function" "report_generator" {
  filename      = "lambda_function.zip"
  function_name = "cost-report-generator"
  role          = aws_iam_role.lambda_exec.arn
  handler       = "index.handler"
  runtime       = "python3.9"
}