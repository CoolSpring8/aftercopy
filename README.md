# AfterCopy

有时候需要从 PDF、CAJ 等文件的阅读器窗口中复制出大段文字，但是这样得到的文字粘贴到 Word 里往往不尽人意：原排版的每一行都会被“另起一段”，有些中文标点变成了带有空格的英文标点……手动调整比较烦琐，因此我写了一个简单的脚本来处理这件事。

## Quick Start

```
pip install aftercopy
aftercopy -v
```

然后去阅读器中复制文字，再粘贴时得到的已经是处理好（去掉换行、替换标点）的结果了。由于无法识别分段，段落之间需要使用者手动分开。

使用完毕后请记得关闭，避免影响常规的复制粘贴的使用。

## 用法

```
aftercopy --help
Usage: aftercopy [OPTIONS]

Options:
  -p, --passive       Disable active reading from clipboard. Instead you can
                      paste into and copy from terminal. End your input with
                      Ctrl-Z + Enter (Windows) or Ctrl-D + Enter.

  -v, --verbose       Display the concrete re-copied text and more info.
  -l, --lang [cn|en]  Switch type of language in text. This will influence the
                      rule set used. (Chinese by default)

  --help              Show this message and exit.
```

## 原理

每隔 0.01 秒读一次剪贴板（性能影响可忽略不计），若发生改变则对新读入的文字作相应的处理，将结果重新写入剪贴板。

## TODO

- 替换规则。目前对于标点的替换规则是硬编码的，显然这种做法大大降低了使用的灵活性。但是我还没有想到在每次运行 / 在安装时指定规则文件的较好办法。
- 错别字识别。没找到这方面便捷的库。

## One more thing...

请勿用于抄袭等侵犯他人著作权的用途。