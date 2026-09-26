import pandas as pd

# 读取数据
df = pd.read_csv('../data/titanic.csv')

# 查看数据概况
print("数据形状：", df.shape)
print("\n前5行：")
print(df.head())
print("\n列名：")
print(df.columns.tolist())
print("\n缺失值：")
print(df.isnull().sum())

# ========== 数据清洗 ==========

# 1. 处理 Age 缺失值：用中位数填充
df['Age'] = df['Age'].fillna(df['Age'].median())

# 2. 处理 Cabin 缺失值：缺失太多，直接删除这一列
df = df.drop(columns=['Cabin'])

# 3. 处理 Embarked 缺失值：用众数填充
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# 4. 查看清洗后还有没有缺失值
print("\n清洗后缺失值：")
print(df.isnull().sum())

# 5. 保存清洗后的数据
df.to_csv('../data/titanic_clean.csv', index=False)
print("\n清洗后数据已保存到 data/titanic_clean.csv")