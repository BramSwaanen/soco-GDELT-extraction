import pandas as pd

def truncate_text(text, max_tokens=499):
    # 使用空格分割文本并限制最大令牌数量
    tokens = text.split()
    if len(tokens) > max_tokens:
        return ' '.join(tokens[:max_tokens])
    return text

# 加载数据
file_path = 'extracted_articles.csv'  # 替换成实际文件路径
data = pd.read_csv(file_path)

# 应用截断函数
data['MainText'] = data['MainText'].apply(truncate_text)

# 保存处理后的数据
output_file_path = 'output_cut_data.csv'  # 替换成你想要保存的文件路径
data.to_csv(output_file_path, index=False)
