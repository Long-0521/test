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