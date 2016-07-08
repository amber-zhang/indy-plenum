
from plenum.cli.constants import \
    UTIL_GRAMS_SIMPLE_CMD_FORMATTED_REG_EX, UTIL_GRAMS_LOAD_CMD_FORMATTED_REG_EX, \
    UTIL_GRAMS_COMMAND_HELP_FORMATTED_REG_EX, UTIL_GRAMS_COMMAND_LIST_FORMATTED_REG_EX, \
    NODE_GRAMS_NODE_COMMAND_FORMATTED_REG_EX, NODE_GRAMS_LOAD_PLUGINS_FORMATTED_REG_EX, \
    CLIENT_GRAMS_CLIENT_COMMAND_FORMATTED_REG_EX, CLIENT_GRAMS_CLIENT_SEND_FORMATTED_REG_EX, \
    CLIENT_GRAMS_CLIENT_SHOW_FORMATTED_REG_EX, CLIENT_GRAMS_ADD_KEY_FORMATTED_REG_EX, \
    CLIENT_GRAMS_NEW_KEYPAIR_FORMATTED_REG_EX, CLIENT_GRAMS_LIST_IDS_FORMATTED_REG_EX, \
    CLIENT_GRAMS_BECOME_FORMATTED_REG_EX, CLIENT_GRAMS_USE_KEYPAIR_FORMATTED_REG_EX

from prompt_toolkit.contrib.regular_languages.compiler import compile


def getGrams():
    utilGrams = [
        UTIL_GRAMS_SIMPLE_CMD_FORMATTED_REG_EX,
        UTIL_GRAMS_LOAD_CMD_FORMATTED_REG_EX,
        UTIL_GRAMS_COMMAND_HELP_FORMATTED_REG_EX,
        UTIL_GRAMS_COMMAND_LIST_FORMATTED_REG_EX
    ]

    nodeGrams = [
        NODE_GRAMS_NODE_COMMAND_FORMATTED_REG_EX,
        NODE_GRAMS_LOAD_PLUGINS_FORMATTED_REG_EX,
    ]

    clientGrams = [
        CLIENT_GRAMS_CLIENT_COMMAND_FORMATTED_REG_EX,
        CLIENT_GRAMS_CLIENT_SEND_FORMATTED_REG_EX,
        CLIENT_GRAMS_CLIENT_SHOW_FORMATTED_REG_EX,
        CLIENT_GRAMS_ADD_KEY_FORMATTED_REG_EX,
        CLIENT_GRAMS_NEW_KEYPAIR_FORMATTED_REG_EX,
        CLIENT_GRAMS_LIST_IDS_FORMATTED_REG_EX,
        CLIENT_GRAMS_BECOME_FORMATTED_REG_EX,
        CLIENT_GRAMS_USE_KEYPAIR_FORMATTED_REG_EX
    ]
    utilGrams[-1] += " |"
    nodeGrams[-1] += " |"

    return utilGrams + nodeGrams + clientGrams


def test_command_reg_ex(cmd):
    grams = getGrams()
    grammar = compile("".join(grams))
    res = grammar.match(cmd)
    assert res

def test_new_keypair_command_reg_ex():
    test_command_reg_ex("new keypair")