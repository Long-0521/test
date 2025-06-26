import requests
import time
EXTRACTOR_URL = "http://129.28.95.236:20084/pdf/parse"

def pdf_file(filepath):
    """
    上传PDF文件并获取解析结果
    Args:
        filepath (str): PDF文件路径
    Returns:
        str: 文本内容
    """
    try:
        with open(filepath, 'rb') as f:
            response = requests.post(
                EXTRACTOR_URL,
                files={'file': f},
            )

        content = response.json()
        
        # 提取并清理文本内容
        text_content = []
        for item in content.get('content_list', []):
            if item.get('type') == 'text':
                text = item.get('text', '').strip()
                if text:
                    text_content.append(text)
        
        # 合并所有文本，去除多余空行
        result = '\n'.join(text_content)
        return result

    except Exception as e:
        print(f"处理PDF文件出错: {str(e)}")
        return None

if __name__ == "__main__":
    # 记录开始时间
    start_time = time.time()
    
    # 处理PDF文件
    result = pdf_file('data/32.pdf')
    
    # 计算处理时间
    end_time = time.time()
    process_time = end_time - start_time
    
    # 输出结果
    if result:
        print(f"\n处理时间: {process_time:.2f} 秒")
        print(f"内容长度: {len(result)} 字符")
        print("\nPDF文本内容：")
        print(result)