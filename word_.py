from docx import Document

def word_file(doc_path):
    """
    解析 Word 文档并打印层次结构
    Args:
        doc_path (str): Word文档路径
    Returns:
        None，直接打印结构
    """
    def get_heading_level(style_name):
        """从样式名称提取标题级别，例如 'Heading 1' -> 1"""
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
            if not text:  # 跳过空段落
                continue
            level = get_heading_level(paragraph.style.name)

            if level:  # 是标题
                # 调整栈到正确级别
                while len(current_path) > level:
                    current_path.pop()
                parent = current_path[-1]["subsections"]
                parent[text] = {"content": [], "subsections": {}}
                current_path.append(parent[text])
            else:  # 普通内容
                current_path[-1]["content"].append(text)

        def clean_empty_content(node):
            node["content"] = [c for c in node["content"] if c]
            for subsection in node["subsections"].values():
                clean_empty_content(subsection)
        clean_empty_content(hierarchy)
        return hierarchy

    def print_hierarchy(hierarchy, indent=0):
        prefix = "  " * indent
        for content in hierarchy["content"]:
            print(f"{prefix}-  {content}")
        for title, section in hierarchy["subsections"].items():
            print(f"{prefix}- {title}")
            print_hierarchy(section, indent + 1)

    result = build_hierarchy(doc_path)
    print("文档：")
    print_hierarchy(result)
