from PIL import Image
import sys
import os

def img_to_pdf(img_path, pdf_path=None):
    """
    将单张图片转换为PDF文件
    Args:
        img_path (str): 图片路径
        pdf_path (str): 生成的PDF路径，默认为图片同名pdf
    Returns:
        pdf_path (str): 生成的PDF文件路径
    """
    if not pdf_path:
        pdf_path = os.path.splitext(img_path)[0] + '.pdf'
    try:
        image = Image.open(img_path)
        # Pillow要求RGB模式
        if image.mode in ("RGBA", "P"):  # PNG等有透明通道
            image = image.convert("RGB")
        image.save(pdf_path, "PDF", resolution=100.0)
        print(f"已生成PDF: {pdf_path}")
        return pdf_path
    except Exception as e:
        print(f"图片转PDF失败: {e}")
        return None

if __name__ == "__main__":
    # 示例：将图片1.jpg转为1.pdf
    img_path = "data/01.png"  # 可替换为你的图片路径
    img_to_pdf(img_path)
