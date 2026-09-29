# ETL Demo

## 项目简介
从 CSV 抽取数据，用 Python 清洗后入库 MySQL，并用 SQL 做分析。

## 技术栈
- Python 3.10
- pandas
- MySQL 8.0

## 项目结构
- data/         原始数据
- scripts/      清洗脚本
- sql/          分析查询

## 怎么运行
1. 安装依赖：pip install -r requirements.txt
2. 运行清洗脚本：python scripts/clean.py
3. 执行 SQL 查询：source sql/analysis.sql

## 成果
- 清洗了 891 条数据
- 完成 5 条 SQL 分析查询
- 生存率：38.38%
- 女性幸存率远高于男性
- 平均年龄：29.36 岁
- 平均票价：32.2
