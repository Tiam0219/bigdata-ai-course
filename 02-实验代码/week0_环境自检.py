"""环境自检脚本：验证 Python 环境是否可用于本课程"""

import sys


def check_env():
    print("=" * 40)
    print("《大数据与人工智能》课程环境自检")
    print("=" * 40)
    print(f"Python 版本 : {sys.version.split()[0]}")

    if sys.version_info < (3, 12):
        print("⚠️  建议使用 Python 3.12 及以上版本")
    else:
        print("✅ Python 版本满足课程要求")

    # 尝试导入课程常用库（未安装不影响自检，仅提示）
    for lib in ["numpy", "pandas", "matplotlib"]:
        try:
            module = __import__(lib)
            print(f"✅ {lib:<12} 已安装 ({getattr(module, '__version__', '未知版本')})")
        except ImportError:
            print(f"⬜ {lib:<12} 未安装（后续实验课再装）")

    print("=" * 40)
    print("环境自检完成！")


if __name__ == "__main__":
    check_env()
