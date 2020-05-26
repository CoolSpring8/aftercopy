import click
import time
import sys
import pyperclip


class Text:
    def __init__(self, raw, lang):
        self.raw = raw
        self.lang = lang
        self.clean_text()

    def clean_text(self):
        rule_set = {"\r": "", "\n": "", "[ ": "[", "] ": "]"}
        rule_set_cn = {
            "? ": "？",
            "! ": "！",
            ", ": "，",
            ":": "：",
            ";": "；",
            "(": "（",
            ")": "）",
            "… …": "……",
            "`": "‘",
            "' ": "’",
        }

        self.clean = self.raw
        for original, fixed in rule_set.items():
            self.clean = self.clean.replace(original, fixed)
        if self.lang == "cn":
            for original, fixed in rule_set_cn.items():
                self.clean = self.clean.replace(original, fixed)


def copy_echo(text, verbose):
    click.echo(time.strftime("%H:%M:%S ", time.localtime()), nl=False)
    pyperclip.copy(text)
    if verbose:
        click.echo(repr(text))
    else:
        click.echo("Re-copied!")


@click.command()
@click.option(
    "-p",
    "--passive",
    is_flag=True,
    help="Disable active reading from clipboard. Instead you can paste into and copy from terminal. End your input with Ctrl-Z + Enter (Windows) or Ctrl-D + Enter.",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    help="Display the concrete re-copied text and more info.",
)
@click.option(
    "-l",
    "--lang",
    type=click.Choice(["cn", "en"]),
    default="cn",
    help="Switch type of language in text. This will influence the rule set used. (Chinese by default)",
)
def main(passive, verbose, lang):
    click.echo("Ready!\n")

    if passive:
        # paste and re-copy
        s = ""
        for line in sys.stdin:
            s += line
        click.echo(Text(s, lang=lang).clean)

    else:
        # read clipboard and re-copy
        # initial
        tmpText = Text(pyperclip.paste(), lang=lang)
        copy_echo(tmpText.clean, verbose=verbose)
        time.sleep(2)

        # loop
        while True:
            newText = Text(pyperclip.paste(), lang=lang)
            if newText.raw == tmpText.raw or newText.raw == tmpText.clean:
                continue
            copy_echo(newText.clean, verbose=verbose)

            tmpText = newText
            time.sleep(2)


if __name__ == "__main__":
    main()
