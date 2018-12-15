import re
import os

from colorama import Fore, Style, init

sdict = {
    r"--- ERR: %(asctime)s >>> {%(name)s}: ": Style.BRIGHT + Fore.LIGHTRED_EX + r"--- ERR: %(asctime)s >>> {%(name)s}: " + Style.RESET_ALL,
    r"!!! CRI: %(asctime)s >>> {%(name)s}: ": Style.BRIGHT + Fore.RED + r"!!! CRI: %(asctime)s >>> {%(name)s}: " + Style.RESET_ALL,
    r">>>": Style.BRIGHT + Fore.GREEN + r">>>" + Style.RESET_ALL,
    r"!!!": Style.BRIGHT + Fore.RED + r"!!!" + Style.RESET_ALL,
    r"---": Style.BRIGHT + Fore.CYAN + r"---" + Style.RESET_ALL,
    r"***": Style.BRIGHT + Fore.LIGHTMAGENTA_EX + r"***" + Style.RESET_ALL,
    r"  -": Style.BRIGHT + Fore.YELLOW + r"  -" + Style.RESET_ALL,
    r" [": Style.BRIGHT + Fore.LIGHTGREEN_EX + r" [" + Style.RESET_ALL,
    r"] ": Style.BRIGHT + Fore.LIGHTGREEN_EX + r"] " + Style.RESET_ALL,
    r"{%(name)s}": Style.BRIGHT + Fore.LIGHTBLUE_EX + r"{%(name)s}" + Style.RESET_ALL
}

init()


def multiple_replace(text, adict):
    # type: (str, dict) -> str
    rx = re.compile('|'.join(map(re.escape, adict)))

    def one_xlat(match):
        return adict[match.group(0)]
    return rx.sub(one_xlat, text)


def c_echo(message, debug=False):
    # type (str, bool) -> None
    # if we dont want colors, just print raw message
    if os.environ.get('PYPE_LOG_NO_COLORS', None) is not None:
        print(message)
    message = re.sub(r'\[(.*)\]', '[' + Style.BRIGHT + Fore.WHITE +
                     r'\1' + Style.RESET_ALL + ']', message)
    message = multiple_replace(message + Style.RESET_ALL, sdict)

    print(message)


def c_log(message, debug=False):
    # type (str, bool) -> str
    if os.environ.get('PYPE_LOG_NO_COLORS', None) is not None:
        return message
    message = re.sub(r'\[(.*)\]', '[' + Style.BRIGHT + Fore.WHITE +
                     r'\1' + Style.RESET_ALL + ']', message)
    message = multiple_replace(message + Style.RESET_ALL, sdict)
    return message
