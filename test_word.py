from docx import Document
import time

def parse_and_print_word_outline(doc_path):
    """
    解析 Word 文档并返回层次结构
    Args:
        doc_path (str): Word文档路径
    Returns:
        dict: 层次结构字典
    """
    def get_heading_level(style_name):
        if style_name and style_name.startswith('Heading'):
            try:
                level = int(style_name.split(' ')[1])
                return level
            except (IndexError, ValueError):
                return None
        return None

    def build_hierarchy(doc_path):
        doc = Document(doc_path)
        hierarchy = {"content": [], "subsections": {}}  # 根节点
        current_path = [hierarchy]  # 栈跟踪当前节点

        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if not text:
                continue
            level = get_heading_level(paragraph.style.name)
            if level:
                while len(current_path) > level:
                    current_path.pop()
                parent = current_path[-1]["subsections"]
                parent[text] = {"content": [], "subsections": {}}
                current_path.append(parent[text])
            else:
                current_path[-1]["content"].append(text)

        def clean_empty_content(node):
            node["content"] = [c for c in node["content"] if c]
            for subsection in node["subsections"].values():
                clean_empty_content(subsection)
        clean_empty_content(hierarchy)
        return hierarchy

    return build_hierarchy(doc_path)

def print_hierarchy(hierarchy, indent=0):
    prefix = "  " * indent
    for content in hierarchy["content"]:
        print(f"{prefix}-  {content}")
    for title, section in hierarchy["subsections"].items():
        print(f"{prefix}- {title}")
        print_hierarchy(section, indent + 1)

if __name__ == "__main__":
    doc_path = "01.docx"
    start_time = time.time()
    result = parse_and_print_word_outline(doc_path)
    end_time = time.time()
    print("文档：")
    print_hierarchy(result)
    print(f"\n处理时间: {end_time - start_time:.2f} 秒")