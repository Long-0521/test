import unittest
import time
from img_02 import OCR_demo

class TestImageOCR(unittest.TestCase):
    """图片OCR测试类"""
    
    def test_image_ocr(self):
        """测试图片OCR识别"""
        # 测试文件列表
        test_files = [
            "data/01.png",

        ]
        
        print("\n=== 图片OCR测试 ===")
        print("=" * 50)
        
        # 测试每个图片
        for file_path in test_files:
            print(f"\n测试文件: {file_path}")
            print("-" * 30)
            
            try:
                # 记录开始时间
                start_time = time.time()
                
                # 处理图片
                result = OCR_demo(file_path)
                
                # 计算处理时间
                end_time = time.time()
                process_time = end_time - start_time
                
                # 输出性能分析
                print("\n性能分析:")
                print(f"处理时间: {process_time:.2f} 秒")
                
                # 验证结果
                self.assertIsNotNone(result, "OCR识别结果不应为空")
                
                if result:
                    print(f"\n内容统计:")
                    print(f"文本长度: {len(result)} 字符")
                    print(f"行数: {len(result.splitlines())} 行")
                
                print("=" * 50)
                
            except Exception as e:
                self.fail(f"处理出错: {str(e)}")

if __name__ == '__main__':
    unittest.main() 