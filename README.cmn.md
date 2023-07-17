[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.md)
[![fr](https://img.shields.io/badge/lang-fr-beige.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.fr.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.es.md)
[![cmn](https://img.shields.io/badge/lang-cmn-red.svg)](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/README.cmn.md)

# CodeExplorer4CodeInterpreter

CodeExplorer4CodeInterpreter是一个由Python开发的软件，旨在简化向ChatGPT的代码解释器发送多个文档，并方便与之交互。

<div style="display:flex;">
  <img src="https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/assets/1897591/3f675698-96fd-45d3-96fb-b2033411ebd1" alt="Image 1" width="49%">
  <img src="https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/assets/1897591/9444f225-31ed-4b2a-b1ba-d61161a2087a" alt="Image 2" width="49%">
</div>

## 使用案例

- **计算机代码项目分析**：CodeExplorer4CodeInterpreter可用于将整个计算机代码项目发送到ChatGPT的代码解释器。这样开发人员可以向解释器询问他们的代码，获取建议、解释或可能的修正，从而促进开发过程。
- **期刊和出版物分析**：这款软件也可用于将多个期刊和科学出版物发送到ChatGPT的代码解释器。用户可以向解释器询问关于文章的特定问题，请求摘要或附加分析，或获取复杂概念的深入解释。
- **写作和修正的帮助**：CodeExplorer4CodeInterpreter对写作者和学生在发送像论文、报告或学术作品这样的文件到ChatGPT的代码解释器时非常有帮助。他们可以向解释器询问关于结构、语法、改进写作风格的建议，或甚至提出相关关键词的建议。
- **数据分析**：该软件可用于将数据集发送到ChatGPT的代码解释器。用户可以向解释器询问关于数据的问题，获取可视化、统计数据，或关于应用分析方法的推荐。
- **帮助信息搜索**：这款软件可以通过向ChatGPT的代码解释器发送包含特定信息的文件来方便信息搜索。用户可以向解释器询问各种主题的问题，并根据提交文件的内容获取详细答案。

## 特性

- CodeExplorer4CodeInterpreter支持Python 3.7及以后的版本，确保与大多数现代Python环境的兼容性。
- 允许轻松探索项目的代码库。
- 生成一个可以轻松导入并在ChatGPT代码解释器插件中使用的Python脚本。

## 预备条件

在运行CodeExplorer4CodeInterpreter之前，确保你在Python环境中安装了`gitignore_parser`模块。你可以使用pip进行安装：

```bash
pip install gitignore-parser
```

## 入门

要开始使用CodeExplorer4CodeInterpreter，你的系统上必须安装Python 3.7或更高版本。

使用以下命令克隆仓库：
```bash
git clone https://github.com/julienwetzel/CodeExplorer4CodeInterpreter.git
```

访问克隆的目录：
```bash
cd CodeExplorer4CodeInterpreter
```

要生成包含你项目代码的Python脚本，请运行以下命令：
```bash
python ce4ci.py [project_dir] [output_file]
```

其中`[project_dir]`是你的项目目录，`[output_file]`是要生成的文件的名称。

例如：
```bash
python ce4ci.py ./ ../../data/ce4ci_dict.py
```

运行命令后，你将看到操作的摘要：
```bash
----------------------------------------------------
Total files processed: 5
Total directories processed: 0
Total file contents inserted: 3
Total files ignored due to .gitignore rules: 2
Total files skipped because they are not Unicode: 0
----------------------------------------------------
```
## 与ChatGPT代码解释器插件一起使用

一旦生成了Python脚本，你就可以与ChatGPT的代码解释器插件一起使用它。

在ChatGPT的提示中，添加以下文字：

```bash
所有项目文件的内容都在附带的python文件中。
通过/mnt/data/ce4ci_dict.py导入文件，然后简单地运行display_file_content(file_path)
函数，其中file_path是文件的路径。例如，`display_file_content('/your/file.example')`
要显示所有项目文件的列表，使用get_available_file_paths()函数。
```

> 注意：`ce4ci_dict.py`是上传到ChatGPT的代码解释器插件的生成文件的名称。如果不包括`/mnt/data`，文件将无法找到。

## 探索生成的Python字典

要探索生成的Python字典，你可以使用`ce4ci_print.py`脚本。

要显示Python字典的内容，使用以下命令：
```bash
python ce4ci_print.py [--list] <script_path> [<file_path>]
```
例如：
```bash
python ce4ci_print.py ../../data/ce4ci_dict.py '/LICENSE'
```
这将显示LICENSE文件的内容。

要列出字典中包含的所有文件的路径，使用以下命令：
```bash
python ce4ci_print.py ../../data/ce4ci_dict.py --list
```
这将显示所有可用的文件路径。

## 许可

该项目采用MIT许可 - 查看[LICENSE](https://github.com/julienwetzel/CodeExplorer4CodeInterpreter/blob/main/LICENSE)文件以获取更多详情。
