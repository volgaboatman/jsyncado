SENDER_ADO = 'sender.ado'
SENDER_JIRA = 'sender.jira'

SENDER_BY_SYSTEM = {
    'jira': SENDER_JIRA,
    'ado': SENDER_ADO,
}

ROUTING_ADO = 'routing.ado'
ROUTING_JIRA = 'routing.jira'

MAPPING_ADO_JIRA = 'mapping.ado.jira'
MAPPING_JIRA_ADO = 'mapping.jira.ado'

MAPPING_ADO_JIRA_ROUTING_KEY = 'routing.ado.#.jira.#'
MAPPING_JIRA_ADO_ROUTING_KEY = 'routing.jira.#.ado.#'

MAPPING_EXCHANGE = 'mapping.exchange'

KEY_JIRA = 'jira'
KEY_ADO = 'ado'

MAPPING_QUEUE = 'mapping'


def get_exchange_key_by(routing_key, systems):
    if not systems or not routing_key or '' in systems:
        return 'not_found_systems'
    else:
        return '.'.join([routing_key, '.'.join(systems)])
