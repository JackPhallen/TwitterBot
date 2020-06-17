from BotModules.txt import txt

# Add reference to module init
init = {
    "txt": txt.init
}

# Add reference to module getter
get = {
    "txt": txt.get
}


def activate(module, config):
    '''
    Initiates module and returns getter to BotConfig
    :param module: module to activate
    :param config: configuration to module
    :return: module getter
    '''
    global init
    global get
    init[module](config)
    return get[module]

