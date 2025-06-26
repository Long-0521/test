import requests
import time
from PIL import Image
import os

EXTRACTOR_URL = "http://129.28.95.236:20084/pdf/parse"

def imgFile(img_path, pdf_path=None):
    """
    先将图片转为PDF，再上传PDF提取文本内容
    Args:
        img_path (str): 图片路径
        pdf_path (str): 生成的PDF路径，默认为图片同名pdf
    Returns:
        str: 提取的文本内容
    """
    if not pdf_path:
        pdf_path = os.path.splitext(img_path)[0] + '.pdf'
    try:
        # 图片转PDF
        image = Image.open(img_path)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        image.save(pdf_path, "PDF", resolution=100.0)
        print(f"已生成PDF: {pdf_path}")
        # 上传PDF并提取文本
        with open(pdf_path, 'rb') as f:
            response = requests.post(
                EXTRACTOR_URL,
                files={'file': f},
            )
        content = response.json()
        text_content = []
        for item in content.get('content_list', []):
            if item.get('type') == 'text':
                text = item.get('text', '').strip()
                if text:
                    text_content.append(text)
        result = '\n'.join(text_content)
        return result
    except Exception as e:
        print(f"图片转PDF或提取文本失败: {e}")
        return None